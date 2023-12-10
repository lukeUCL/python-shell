# Generated from ShellParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ShellParser import ShellParser
else:
    from ShellParser import ShellParser

# This class defines a complete generic visitor for a parse tree produced by ShellParser.

class ShellParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellParser#command.
    def visitCommand(self, ctx:ShellParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#seqCommand.
    def visitSeqCommand(self, ctx:ShellParser.SeqCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#pipeCommand.
    def visitPipeCommand(self, ctx:ShellParser.PipeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#seqPipeCommand.
    def visitSeqPipeCommand(self, ctx:ShellParser.SeqPipeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#callCommand.
    def visitCallCommand(self, ctx:ShellParser.CallCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#redirection.
    def visitRedirection(self, ctx:ShellParser.RedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#argument.
    def visitArgument(self, ctx:ShellParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#quoted.
    def visitQuoted(self, ctx:ShellParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#singleQuoted.
    def visitSingleQuoted(self, ctx:ShellParser.SingleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#doubleQuoted.
    def visitDoubleQuoted(self, ctx:ShellParser.DoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellParser#backQuoted.
    def visitBackQuoted(self, ctx:ShellParser.BackQuotedContext):
        return self.visitChildren(ctx)



del ShellParser