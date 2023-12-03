
from antlr4 import InputStream, CommonTokenStream, tree
from PARSER.ShellParser import ShellParser
from PARSER.ShellParserVisitor import ShellParserVisitor

# print(f"The __name__ in ShellParserVisitor.py is: {__name__}")
# def process_inner_content(content):
#     content = content.replace('\\\'', '\'').replace('\\"', '\"')

#     return content


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
        redirections = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            print("Child type:", type(child).__name__, "Text:", child.getText())

            if isinstance(child, ShellParser.RedirectionContext):
                redirection_symbol = child.getChild(0).getText()  # '<' or '>'
                redirection_target = self.visit(child.getChild(1))  # e.g., 'dir1/file2.txt'
                redirections.append(redirection_symbol)
                redirections.append(redirection_target)
            elif command is None:
                command = child.getText()
            else:
                argument = self.visit(child)
                arguments.append(argument)

        if command is None:
            raise ValueError("Command not found in callCommand context")

        # Combine command, arguments, and redirections
        full_command = [command] + arguments + redirections
        return full_command


            
    # def visitArgument(self, ctx:ShellParser.ArgumentContext):
    #     print("In visitArgument: ", ctx.getText())

    #     if ctx.quoted():
    #         return self.visit(ctx.quoted())
    #     # Otherwise, return the text directly
    #     return ctx.getText().strip("'\"")

    #COULDNT TOKENIZE for a"b"c-- ptnsh bad solution
    def visitArgument(self, ctx:ShellParser.ArgumentContext):
        print("In visitArgument: ", ctx.getText())

        if ctx.quoted():
            return self.visit(ctx.quoted())

        arg_text = ctx.getText()
        if '"' in arg_text:  
            return arg_text.replace('"', '')

        return arg_text


    def visitRedirection(self, ctx):
        redirection_type = ctx.getChild(0).getText()  # '<' or '>'
        file_or_command = self.visit(ctx.getChild(1)) # 'dir1/file2.txt' or a command

        print("Redirection type:", redirection_type)
        print("File or command:", file_or_command)

        return [redirection_type, file_or_command]


    def visitQuoted(self, ctx:ShellParser.QuotedContext):
        print("In visitQuoted")
        return self.visit(ctx.getChild(0))
    
    def visitSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        print("In visitSingleQuoted")
        inner_content = ctx.getText()[1:-1]
        return process_inner_content(inner_content)

    
    def visitDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):

        return ctx.getText()[1:-1]

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