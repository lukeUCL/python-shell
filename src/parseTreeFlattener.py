
from antlr4 import InputStream, CommonTokenStream, tree
from PARSER.ShellParser import ShellParser
from PARSER.ShellParserVisitor import ShellParserVisitor
import re

def process_inner_content(content):
    content = content.replace('\\\'', '\'').replace('\\"', '\"')

    return content

class parseTreeFlattener(ShellParserVisitor):

    def visitSeqPipeCommand(self, ctx:ShellParser.SeqPipeCommandContext):
        commands = []
        current_type = None
        current_group = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, tree.Tree.TerminalNodeImpl):
                if child.symbol.type == ShellParser.SEMI or child.symbol.type == ShellParser.PIPE:
                    if current_group:
                        if current_type:
                            commands.append([current_type] + current_group)
                        else:
                            commands.extend(current_group)
                        current_group = []

                    current_type = 'seq' if child.symbol.type == ShellParser.SEMI else 'pipe'
            else:
                command = self.visit(child)
                if command:
                    current_group.append(command)

        if current_group:
            if current_type:
                commands.append([current_type] + current_group)
            else:
                commands.extend(current_group)

        return self.simplify_command_structure(commands)
        

    def simplify_command_structure(self, commands):
        if not isinstance(commands, list) or len(commands) == 0:
            return commands

        if commands[0] in ['seq', 'pipe']:
            command_type = commands[0]
            flattened_commands = [command_type]

            for command in commands[1:]:
                simplified_command = self.simplify_command_structure(command)
                if isinstance(simplified_command, list) and simplified_command[0] == command_type:
                    flattened_commands.extend(simplified_command[1:])
                else:
                    flattened_commands.append(simplified_command)
            
            return flattened_commands

        return commands

    def visitPipeCommand(self, ctx:ShellParser.PipeCommandContext):
        pipe_sequence = ['pipe']
        for i in range(0, ctx.getChildCount(), 2):  
            command = self.visit(ctx.getChild(i))
            #ensure we only have one pipe flag, i.e ['pipe'[command, args]]
            if command:
                if command[0] != 'pipe':
                    pipe_sequence.append(command)
                else:
                    pipe_sequence.extend(command[1:])
        return pipe_sequence

    #same approach as pipe above
    def visitSeqCommand(self, ctx:ShellParser.SeqCommandContext):
        sequence = ['seq']
        for i in range(ctx.getChildCount()):
            command = self.visit(ctx.getChild(i))
            if command:  
                if command[0] != 'seq':
                    sequence.append(command)
                else:
                    sequence.extend(command[1:])
        return sequence

    def visitCallCommand(self, ctx):
        command = None
        arguments = []
        redirection = {'in': None, 'out': None}
        skip_next = False  #Flag to skip for redirection case

        for i in range(ctx.getChildCount()):

            child = ctx.getChild(i)
            text = child.getText()

            #if we have seen a redirection symbol, we skip the next child, as we will have processed redirection, and arg
            if skip_next:
                skip_next = False
                continue

            if isinstance(child, ShellParser.RedirectionContext) or text in ['<', '>']:
                if i + 1 < ctx.getChildCount():
                    redirection_target_node = ctx.getChild(i+1)
                    redirection_target_text = redirection_target_node.getText()
                    if text == '<':
                        redirection['in'] = redirection_target_text
                    elif text == '>':
                        redirection['out'] = redirection_target_text
                    skip_next = True  # Skip the next child since it's part of redirection
                else:
                    #redirection with no target
                    raise ValueError(f"Redirection symbol '{text}' at the end of command without a target")

            elif command is None:
                command = self.processArg(text)
            else:
                if text not in ['<', '>']:
                    argument = self.visit(child)
                    arguments.append(argument)

        if command is None:
            raise ValueError("Command not found in callCommand context")

        full_command = [command] + arguments
        if redirection['in'] or redirection['out']:
            full_command.append(redirection)

        return full_command 
    
    #Args are either quoted (double or single), backquoted, or a mix, where splitting should be taken care off with processArg
    def visitArgument(self, ctx:ShellParser.ArgumentContext):

        if ctx.quoted():
            return self.visit(ctx.quoted())
        
        if ctx.backQuoted():
            return self.visit(ctx.backQuoted())

        arg_text = ctx.getText()
        text = self.processArg(arg_text)
        if '"' in text:  
            return text.replace('"', '')

        return text


    def visitRedirection(self, ctx):
        redirection_type = ctx.getChild(0).getText()  # '<' or '>'
        file_or_command = self.visit(ctx.getChild(1)) # 'dir1/file2.txt' or a command
        return [redirection_type, file_or_command]


    #just visit child- single or double quoted
    def visitQuoted(self, ctx:ShellParser.QuotedContext):
        return self.visit(ctx.getChild(0))

    #just return inner content as is 
    def visitSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        inner_content = ctx.getText()[1:-1]
        return process_inner_content(inner_content)

    #just return inner content as is 
    def visitDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):
        text = ctx.getText()[1:-1] 
        return self.processArg(text)

    def processArg(self, text):
        from shell import run
        # Process the nested command substitutions
        result = ""
        #Check for backquoted to be subbed
        pattern = r'`([^`]*)`'
        while '`' in text:
            match = re.search(pattern, text)
            if match:
                #store text before backquotes
                pre_text = text[:match.start()]
                command_substitution = match.group(1) #extract the command
                #echo is a unique edge case, if we have echo echo we can just skip 5 indexes
                if command_substitution.startswith("echo echo"):
                    return command_substitution[5:] 
                #store text after backquotes
                post_text = text[match.end():]

                #nested shell call, just process the command with run from shell
                #use this output as sub
                substitution_output_deque = run(command_substitution)

                # we will never need any \n in substitution output, replace with spaces
                substitution_output_str = ''.join(substitution_output_deque).replace('\n', ' ').strip()

                result += pre_text + substitution_output_str
                text = post_text
            else:
                break

        return result + text

    def visitBackQuoted(self, ctx):
        backQuotedText = ctx.getText()
        return self.processArg(backQuotedText)

# del ShellParser- cant access 