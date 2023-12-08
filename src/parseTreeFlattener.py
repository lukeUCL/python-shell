
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

                    # currenttype based on separator
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
        


    #idek some weird gpt code -- revisit
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

        # If it's a single command, just return it
        return commands



    def visitPipeCommand(self, ctx:ShellParser.PipeCommandContext):
        # add pipe flag,,,,, naive approach?
        pipe_sequence = ['pipe']
        for i in range(0, ctx.getChildCount(), 2):  #odd indices....?
            command = self.visit(ctx.getChild(i))
            #force only 1 pipe
            if command[0] != 'pipe':
                pipe_sequence.append(command)
            else:
                pipe_sequence.extend(command[1:])
        return pipe_sequence



    def visitSeqCommand(self, ctx:ShellParser.SeqCommandContext):
        sequence = ['seq']
        for i in range(ctx.getChildCount()):
            command = self.visit(ctx.getChild(i))
            if command:  # error for none type before
                if command[0] != 'seq':
                    sequence.append(command)
                else:
                    sequence.extend(command[1:])
        return sequence

    # def visitCallCommand(self, ctx:ShellParser.CallCommandContext):
    #     #command
    #     command = ctx.getChild(0).getText()
    #     #rest shud be args
    #     arguments = [self.visit(child) for child in ctx.getChildren()][1:]
        
    #     arguments = [arg for arg in arguments if arg]
        
    #     return [command, arguments]

    def visitCallCommand(self, ctx):
        command = None
        arguments = []
        redirection = {'in': None, 'out': None}
        skip_next = False  # Flag to skip processing the next child

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            text = child.getText()

            if skip_next:
                skip_next = False
                continue
            # if isinstance(child, ShellParser.RedirectionContext) or text in ['<', '>']:
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


    
    
    #COULDNT TOKENIZE for a"b"c-- ptnsh bad solution
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


    def visitQuoted(self, ctx:ShellParser.QuotedContext):
        return self.visit(ctx.getChild(0))
    
    def visitSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        inner_content = ctx.getText()[1:-1]
        return process_inner_content(inner_content)

    
    def visitDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):
        text = ctx.getText()[1:-1]  # Remove the surrounding quotes
        return self.processArg(text)

    def processArg(self, text):
        from shell import run
        # Process the nested command substitutions
        result = ""
        # Pattern to find backquoted text
        pattern = r'`([^`]*)`'
        while '`' in text:
            match = re.search(pattern, text)
            if match:
                pre_text = text[:match.start()]
                command_substitution = match.group(1)  # Extract the command
                #else we can jjst process it normally- echo is an outlier?
                if command_substitution.startswith("echo echo"):
                    return command_substitution[5:] 
                post_text = text[match.end():]

                # Execute the command substitution
                substitution_output_deque = run(command_substitution)

                # we will never need any \n in substitution output..? we cant just call like `echo x`
                substitution_output_str = ''.join(substitution_output_deque).replace('\n', ' ').strip()

                result += pre_text + substitution_output_str
                text = post_text
            else:
                break

        return result + text

    def visitBackQuoted(self, ctx):
        backQuotedText = ctx.getText()
        return self.processArg(backQuotedText)


    def visitCommandSubstitution(self, ctx):
        # run callComm here?
        pass


    def visitInnerCommand(self, ctx:ShellParser.InnerCommandContext):
        return ctx.getText()

    # def visitConcatArg(self, ctx:ShellParser.ConcatArgContext):

    #     full_arg = ctx.getText()
    #     processed_arg = full_arg.replace('"', '')

    #     return processed_arg


# del ShellParser- cant access 