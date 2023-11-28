
from antlr4 import InputStream, CommonTokenStream
from .PARSER.ShellParser import ShellParser
from src.PARSER.ShellParserVisitor import ShellParserVisitor

print(f"The __name__ in ShellParserVisitor.py is: {__name__}")


class parseTreeFlattener(ShellParserVisitor):
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



    def visitCallCommand(self, ctx:ShellParser.CallCommandContext):
        #command
        command = ctx.getChild(0).getText()
        #rest shud be args
        arguments = [self.visit(child) for child in ctx.getChildren()][1:]
        
        arguments = [arg for arg in arguments if arg]
        
        return [command, arguments]
    
    def visitArgument(self, ctx:ShellParser.ArgumentContext):
        return ctx.getText().strip("'\"")

    def visitRedirection(self, ctx:ShellParser.RedirectionContext):
        direction = ctx.getChild(0).getText()
        file_arg = self.visit(ctx.argument())
        return (direction, file_arg)

    def visitQuoted(self, ctx:ShellParser.QuotedContext):
        #wrapper cont
        return self.visit(ctx.getChild(0))

    def visitSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        content = ctx.getText()[1:-1]  #remove single quotes
        return content.split()  
    
    def visitDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):

        return ctx.getText()[1:-1]

    def visitCommandSubstitution(self, ctx):
        # run callComm here?
        pass


    def visitInnerCommand(self, ctx:ShellParser.InnerCommandContext):
        return ctx.getText()


# del ShellParser- cant access 