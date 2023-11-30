# Generated from ShellParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,3,0,28,
        8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,4,3,53,8,3,11,3,12,3,54,1,4,
        1,4,1,4,3,4,60,8,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,3,7,69,8,7,1,8,1,
        8,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,1,1,0,2,3,78,0,27,1,0,0,0,2,37,1,0,0,0,4,47,
        1,0,0,0,6,52,1,0,0,0,8,59,1,0,0,0,10,61,1,0,0,0,12,63,1,0,0,0,14,
        68,1,0,0,0,16,70,1,0,0,0,18,72,1,0,0,0,20,74,1,0,0,0,22,78,1,0,0,
        0,24,28,3,2,1,0,25,28,3,4,2,0,26,28,3,6,3,0,27,24,1,0,0,0,27,25,
        1,0,0,0,27,26,1,0,0,0,28,1,1,0,0,0,29,30,3,6,3,0,30,31,5,11,0,0,
        31,32,3,2,1,0,32,38,1,0,0,0,33,34,3,6,3,0,34,35,5,11,0,0,35,36,3,
        6,3,0,36,38,1,0,0,0,37,29,1,0,0,0,37,33,1,0,0,0,38,3,1,0,0,0,39,
        40,3,6,3,0,40,41,5,10,0,0,41,42,3,4,2,0,42,48,1,0,0,0,43,44,3,6,
        3,0,44,45,5,10,0,0,45,46,3,6,3,0,46,48,1,0,0,0,47,39,1,0,0,0,47,
        43,1,0,0,0,48,5,1,0,0,0,49,53,3,8,4,0,50,53,3,12,6,0,51,53,3,20,
        10,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,
        52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,60,5,1,0,0,57,60,3,14,7,
        0,58,60,5,7,0,0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,9,1,
        0,0,0,61,62,5,1,0,0,62,11,1,0,0,0,63,64,7,0,0,0,64,65,3,8,4,0,65,
        13,1,0,0,0,66,69,3,16,8,0,67,69,3,18,9,0,68,66,1,0,0,0,68,67,1,0,
        0,0,69,15,1,0,0,0,70,71,5,12,0,0,71,17,1,0,0,0,72,73,5,13,0,0,73,
        19,1,0,0,0,74,75,5,6,0,0,75,76,3,22,11,0,76,77,5,6,0,0,77,21,1,0,
        0,0,78,79,3,6,3,0,79,23,1,0,0,0,7,27,37,47,52,54,59,68
    ]

class ShellParser ( Parser ):

    grammarFileName = "ShellParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'<'", "'>'", "'''", "'\"'", 
                     "'`'", "<INVALID>", "<INVALID>", "<INVALID>", "'|'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "CONCAT_ARG", "LT", "GT", "SINGLE_QUOTE", 
                      "DOUBLE_QUOTE", "BACK_QUOTE", "UNQUOTED", "WS", "NEWLINE", 
                      "PIPE", "SEMI", "SINGLE_QUOTED_TEXT", "DOUBLE_QUOTED_TEXT" ]

    RULE_command = 0
    RULE_seqCommand = 1
    RULE_pipeCommand = 2
    RULE_callCommand = 3
    RULE_argument = 4
    RULE_concatArg = 5
    RULE_redirection = 6
    RULE_quoted = 7
    RULE_singleQuoted = 8
    RULE_doubleQuoted = 9
    RULE_commandSubstitution = 10
    RULE_innerCommand = 11

    ruleNames =  [ "command", "seqCommand", "pipeCommand", "callCommand", 
                   "argument", "concatArg", "redirection", "quoted", "singleQuoted", 
                   "doubleQuoted", "commandSubstitution", "innerCommand" ]

    EOF = Token.EOF
    CONCAT_ARG=1
    LT=2
    GT=3
    SINGLE_QUOTE=4
    DOUBLE_QUOTE=5
    BACK_QUOTE=6
    UNQUOTED=7
    WS=8
    NEWLINE=9
    PIPE=10
    SEMI=11
    SINGLE_QUOTED_TEXT=12
    DOUBLE_QUOTED_TEXT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seqCommand(self):
            return self.getTypedRuleContext(ShellParser.SeqCommandContext,0)


        def pipeCommand(self):
            return self.getTypedRuleContext(ShellParser.PipeCommandContext,0)


        def callCommand(self):
            return self.getTypedRuleContext(ShellParser.CallCommandContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = ShellParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.seqCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.pipeCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.callCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.CallCommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.CallCommandContext,i)


        def SEMI(self):
            return self.getToken(ShellParser.SEMI, 0)

        def seqCommand(self):
            return self.getTypedRuleContext(ShellParser.SeqCommandContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_seqCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeqCommand" ):
                listener.enterSeqCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeqCommand" ):
                listener.exitSeqCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqCommand" ):
                return visitor.visitSeqCommand(self)
            else:
                return visitor.visitChildren(self)




    def seqCommand(self):

        localctx = ShellParser.SeqCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_seqCommand)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.callCommand()
                self.state = 30
                self.match(ShellParser.SEMI)
                self.state = 31
                self.seqCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.callCommand()
                self.state = 34
                self.match(ShellParser.SEMI)
                self.state = 35
                self.callCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.CallCommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.CallCommandContext,i)


        def PIPE(self):
            return self.getToken(ShellParser.PIPE, 0)

        def pipeCommand(self):
            return self.getTypedRuleContext(ShellParser.PipeCommandContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_pipeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipeCommand" ):
                listener.enterPipeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipeCommand" ):
                listener.exitPipeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipeCommand" ):
                return visitor.visitPipeCommand(self)
            else:
                return visitor.visitChildren(self)




    def pipeCommand(self):

        localctx = ShellParser.PipeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pipeCommand)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.callCommand()
                self.state = 40
                self.match(ShellParser.PIPE)
                self.state = 41
                self.pipeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.callCommand()
                self.state = 44
                self.match(ShellParser.PIPE)
                self.state = 45
                self.callCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(ShellParser.ArgumentContext,i)


        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellParser.RedirectionContext,i)


        def commandSubstitution(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.CommandSubstitutionContext)
            else:
                return self.getTypedRuleContext(ShellParser.CommandSubstitutionContext,i)


        def getRuleIndex(self):
            return ShellParser.RULE_callCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallCommand" ):
                listener.enterCallCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallCommand" ):
                listener.exitCallCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallCommand" ):
                return visitor.visitCallCommand(self)
            else:
                return visitor.visitChildren(self)




    def callCommand(self):

        localctx = ShellParser.CallCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_callCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 52
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 7, 12, 13]:
                        self.state = 49
                        self.argument()
                        pass
                    elif token in [2, 3]:
                        self.state = 50
                        self.redirection()
                        pass
                    elif token in [6]:
                        self.state = 51
                        self.commandSubstitution()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCAT_ARG(self):
            return self.getToken(ShellParser.CONCAT_ARG, 0)

        def quoted(self):
            return self.getTypedRuleContext(ShellParser.QuotedContext,0)


        def UNQUOTED(self):
            return self.getToken(ShellParser.UNQUOTED, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ShellParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(ShellParser.CONCAT_ARG)
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.quoted()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(ShellParser.UNQUOTED)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCAT_ARG(self):
            return self.getToken(ShellParser.CONCAT_ARG, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_concatArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatArg" ):
                listener.enterConcatArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatArg" ):
                listener.exitConcatArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatArg" ):
                return visitor.visitConcatArg(self)
            else:
                return visitor.visitChildren(self)




    def concatArg(self):

        localctx = ShellParser.ConcatArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concatArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ShellParser.CONCAT_ARG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(ShellParser.ArgumentContext,0)


        def LT(self):
            return self.getToken(ShellParser.LT, 0)

        def GT(self):
            return self.getToken(ShellParser.GT, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = ShellParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(ShellParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(ShellParser.DoubleQuotedContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = ShellParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quoted)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.singleQuoted()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.doubleQuoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTED_TEXT(self):
            return self.getToken(ShellParser.SINGLE_QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_singleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleQuoted" ):
                listener.enterSingleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleQuoted" ):
                listener.exitSingleQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleQuoted" ):
                return visitor.visitSingleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def singleQuoted(self):

        localctx = ShellParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_singleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ShellParser.SINGLE_QUOTED_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTED_TEXT(self):
            return self.getToken(ShellParser.DOUBLE_QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_doubleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleQuoted" ):
                listener.enterDoubleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleQuoted" ):
                listener.exitDoubleQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoubleQuoted" ):
                return visitor.visitDoubleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def doubleQuoted(self):

        localctx = ShellParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doubleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ShellParser.DOUBLE_QUOTED_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandSubstitutionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACK_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.BACK_QUOTE)
            else:
                return self.getToken(ShellParser.BACK_QUOTE, i)

        def innerCommand(self):
            return self.getTypedRuleContext(ShellParser.InnerCommandContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_commandSubstitution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandSubstitution" ):
                listener.enterCommandSubstitution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandSubstitution" ):
                listener.exitCommandSubstitution(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandSubstitution" ):
                return visitor.visitCommandSubstitution(self)
            else:
                return visitor.visitChildren(self)




    def commandSubstitution(self):

        localctx = ShellParser.CommandSubstitutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_commandSubstitution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ShellParser.BACK_QUOTE)
            self.state = 75
            self.innerCommand()
            self.state = 76
            self.match(ShellParser.BACK_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callCommand(self):
            return self.getTypedRuleContext(ShellParser.CallCommandContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_innerCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInnerCommand" ):
                listener.enterInnerCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInnerCommand" ):
                listener.exitInnerCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerCommand" ):
                return visitor.visitInnerCommand(self)
            else:
                return visitor.visitChildren(self)




    def innerCommand(self):

        localctx = ShellParser.InnerCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_innerCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.callCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





