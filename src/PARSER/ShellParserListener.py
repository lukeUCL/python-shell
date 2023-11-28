# Generated from ShellParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete listener for a parse tree produced by ShellParser.
class ShellParserListener(ParseTreeListener):

    # Enter a parse tree produced by ShellParser#command.
    def enterCommand(self, ctx:ShellParser.CommandContext):
        pass

    # Exit a parse tree produced by ShellParser#command.
    def exitCommand(self, ctx:ShellParser.CommandContext):
        pass


    # Enter a parse tree produced by ShellParser#seqCommand.
    def enterSeqCommand(self, ctx:ShellParser.SeqCommandContext):
        pass

    # Exit a parse tree produced by ShellParser#seqCommand.
    def exitSeqCommand(self, ctx:ShellParser.SeqCommandContext):
        pass


    # Enter a parse tree produced by ShellParser#pipeCommand.
    def enterPipeCommand(self, ctx:ShellParser.PipeCommandContext):
        pass

    # Exit a parse tree produced by ShellParser#pipeCommand.
    def exitPipeCommand(self, ctx:ShellParser.PipeCommandContext):
        pass


    # Enter a parse tree produced by ShellParser#callCommand.
    def enterCallCommand(self, ctx:ShellParser.CallCommandContext):
        pass

    # Exit a parse tree produced by ShellParser#callCommand.
    def exitCallCommand(self, ctx:ShellParser.CallCommandContext):
        pass


    # Enter a parse tree produced by ShellParser#argument.
    def enterArgument(self, ctx:ShellParser.ArgumentContext):
        pass

    # Exit a parse tree produced by ShellParser#argument.
    def exitArgument(self, ctx:ShellParser.ArgumentContext):
        pass


    # Enter a parse tree produced by ShellParser#redirection.
    def enterRedirection(self, ctx:ShellParser.RedirectionContext):
        pass

    # Exit a parse tree produced by ShellParser#redirection.
    def exitRedirection(self, ctx:ShellParser.RedirectionContext):
        pass


    # Enter a parse tree produced by ShellParser#quoted.
    def enterQuoted(self, ctx:ShellParser.QuotedContext):
        pass

    # Exit a parse tree produced by ShellParser#quoted.
    def exitQuoted(self, ctx:ShellParser.QuotedContext):
        pass


    # Enter a parse tree produced by ShellParser#singleQuoted.
    def enterSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        pass

    # Exit a parse tree produced by ShellParser#singleQuoted.
    def exitSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        pass


    # Enter a parse tree produced by ShellParser#doubleQuoted.
    def enterDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):
        pass

    # Exit a parse tree produced by ShellParser#doubleQuoted.
    def exitDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):
        pass


    # Enter a parse tree produced by ShellParser#commandSubstitution.
    def enterCommandSubstitution(self, ctx:ShellParser.CommandSubstitutionContext):
        pass

    # Exit a parse tree produced by ShellParser#commandSubstitution.
    def exitCommandSubstitution(self, ctx:ShellParser.CommandSubstitutionContext):
        pass


    # Enter a parse tree produced by ShellParser#innerCommand.
    def enterInnerCommand(self, ctx:ShellParser.InnerCommandContext):
        pass

    # Exit a parse tree produced by ShellParser#innerCommand.
    def exitInnerCommand(self, ctx:ShellParser.InnerCommandContext):
        pass



del ShellParser