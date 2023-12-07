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
        4,1,14,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,3,
        0,29,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,75,8,3,1,4,1,4,1,4,4,4,80,8,4,11,4,12,4,81,1,5,1,5,1,6,1,6,1,6,
        1,6,3,6,90,8,6,1,7,1,7,1,7,3,7,95,8,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,2,3,
        110,0,28,1,0,0,0,2,38,1,0,0,0,4,48,1,0,0,0,6,74,1,0,0,0,8,79,1,0,
        0,0,10,83,1,0,0,0,12,89,1,0,0,0,14,94,1,0,0,0,16,96,1,0,0,0,18,98,
        1,0,0,0,20,100,1,0,0,0,22,102,1,0,0,0,24,29,3,6,3,0,25,29,3,2,1,
        0,26,29,3,4,2,0,27,29,3,8,4,0,28,24,1,0,0,0,28,25,1,0,0,0,28,26,
        1,0,0,0,28,27,1,0,0,0,29,1,1,0,0,0,30,31,3,8,4,0,31,32,5,11,0,0,
        32,33,3,2,1,0,33,39,1,0,0,0,34,35,3,8,4,0,35,36,5,11,0,0,36,37,3,
        8,4,0,37,39,1,0,0,0,38,30,1,0,0,0,38,34,1,0,0,0,39,3,1,0,0,0,40,
        41,3,8,4,0,41,42,5,10,0,0,42,43,3,4,2,0,43,49,1,0,0,0,44,45,3,8,
        4,0,45,46,5,10,0,0,46,47,3,8,4,0,47,49,1,0,0,0,48,40,1,0,0,0,48,
        44,1,0,0,0,49,5,1,0,0,0,50,51,3,2,1,0,51,52,5,10,0,0,52,53,3,2,1,
        0,53,75,1,0,0,0,54,55,3,4,2,0,55,56,5,11,0,0,56,57,3,4,2,0,57,75,
        1,0,0,0,58,59,3,2,1,0,59,60,5,10,0,0,60,61,3,8,4,0,61,75,1,0,0,0,
        62,63,3,8,4,0,63,64,5,10,0,0,64,65,3,2,1,0,65,75,1,0,0,0,66,67,3,
        4,2,0,67,68,5,11,0,0,68,69,3,8,4,0,69,75,1,0,0,0,70,71,3,8,4,0,71,
        72,5,11,0,0,72,73,3,4,2,0,73,75,1,0,0,0,74,50,1,0,0,0,74,54,1,0,
        0,0,74,58,1,0,0,0,74,62,1,0,0,0,74,66,1,0,0,0,74,70,1,0,0,0,75,7,
        1,0,0,0,76,80,3,12,6,0,77,80,3,10,5,0,78,80,3,20,10,0,79,76,1,0,
        0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,
        1,0,0,0,82,9,1,0,0,0,83,84,7,0,0,0,84,11,1,0,0,0,85,90,5,1,0,0,86,
        90,3,14,7,0,87,90,5,7,0,0,88,90,3,20,10,0,89,85,1,0,0,0,89,86,1,
        0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,13,1,0,0,0,91,95,3,16,8,0,92,
        95,3,18,9,0,93,95,3,20,10,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,
        0,0,0,95,15,1,0,0,0,96,97,5,12,0,0,97,17,1,0,0,0,98,99,5,14,0,0,
        99,19,1,0,0,0,100,101,5,13,0,0,101,21,1,0,0,0,102,103,3,8,4,0,103,
        23,1,0,0,0,8,28,38,48,74,79,81,89,94
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
                      "PIPE", "SEMI", "SINGLE_QUOTED_TEXT", "BACK_QUOTED_TEXT", 
                      "DOUBLE_QUOTED_TEXT" ]

    RULE_command = 0
    RULE_seqCommand = 1
    RULE_pipeCommand = 2
    RULE_seqPipeCommand = 3
    RULE_callCommand = 4
    RULE_redirection = 5
    RULE_argument = 6
    RULE_quoted = 7
    RULE_singleQuoted = 8
    RULE_doubleQuoted = 9
    RULE_backQuoted = 10
    RULE_innerCommand = 11

    ruleNames =  [ "command", "seqCommand", "pipeCommand", "seqPipeCommand", 
                   "callCommand", "redirection", "argument", "quoted", "singleQuoted", 
                   "doubleQuoted", "backQuoted", "innerCommand" ]

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
    BACK_QUOTED_TEXT=13
    DOUBLE_QUOTED_TEXT=14

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

        def seqPipeCommand(self):
            return self.getTypedRuleContext(ShellParser.SeqPipeCommandContext,0)


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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.seqPipeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.seqCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.pipeCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.callCommand()
                self.state = 31
                self.match(ShellParser.SEMI)
                self.state = 32
                self.seqCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.callCommand()
                self.state = 35
                self.match(ShellParser.SEMI)
                self.state = 36
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
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.callCommand()
                self.state = 41
                self.match(ShellParser.PIPE)
                self.state = 42
                self.pipeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.callCommand()
                self.state = 45
                self.match(ShellParser.PIPE)
                self.state = 46
                self.callCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqPipeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seqCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.SeqCommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.SeqCommandContext,i)


        def PIPE(self):
            return self.getToken(ShellParser.PIPE, 0)

        def pipeCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.PipeCommandContext)
            else:
                return self.getTypedRuleContext(ShellParser.PipeCommandContext,i)


        def SEMI(self):
            return self.getToken(ShellParser.SEMI, 0)

        def callCommand(self):
            return self.getTypedRuleContext(ShellParser.CallCommandContext,0)


        def getRuleIndex(self):
            return ShellParser.RULE_seqPipeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeqPipeCommand" ):
                listener.enterSeqPipeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeqPipeCommand" ):
                listener.exitSeqPipeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqPipeCommand" ):
                return visitor.visitSeqPipeCommand(self)
            else:
                return visitor.visitChildren(self)




    def seqPipeCommand(self):

        localctx = ShellParser.SeqPipeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_seqPipeCommand)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.seqCommand()
                self.state = 51
                self.match(ShellParser.PIPE)
                self.state = 52
                self.seqCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.pipeCommand()
                self.state = 55
                self.match(ShellParser.SEMI)
                self.state = 56
                self.pipeCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.seqCommand()
                self.state = 59
                self.match(ShellParser.PIPE)
                self.state = 60
                self.callCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.callCommand()
                self.state = 63
                self.match(ShellParser.PIPE)
                self.state = 64
                self.seqCommand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.pipeCommand()
                self.state = 67
                self.match(ShellParser.SEMI)
                self.state = 68
                self.callCommand()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.callCommand()
                self.state = 71
                self.match(ShellParser.SEMI)
                self.state = 72
                self.pipeCommand()
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


        def backQuoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellParser.BackQuotedContext)
            else:
                return self.getTypedRuleContext(ShellParser.BackQuotedContext,i)


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
        self.enterRule(localctx, 8, self.RULE_callCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 76
                    self.argument()
                    pass

                elif la_ == 2:
                    self.state = 77
                    self.redirection()
                    pass

                elif la_ == 3:
                    self.state = 78
                    self.backQuoted()
                    pass


                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28814) != 0)):
                    break

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
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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

        def backQuoted(self):
            return self.getTypedRuleContext(ShellParser.BackQuotedContext,0)


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
        self.enterRule(localctx, 12, self.RULE_argument)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(ShellParser.CONCAT_ARG)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.quoted()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(ShellParser.UNQUOTED)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.backQuoted()
                pass


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


        def backQuoted(self):
            return self.getTypedRuleContext(ShellParser.BackQuotedContext,0)


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
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.singleQuoted()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.doubleQuoted()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.backQuoted()
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
            self.state = 96
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
            self.state = 98
            self.match(ShellParser.DOUBLE_QUOTED_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACK_QUOTED_TEXT(self):
            return self.getToken(ShellParser.BACK_QUOTED_TEXT, 0)

        def getRuleIndex(self):
            return ShellParser.RULE_backQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackQuoted" ):
                listener.enterBackQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackQuoted" ):
                listener.exitBackQuoted(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackQuoted" ):
                return visitor.visitBackQuoted(self)
            else:
                return visitor.visitChildren(self)




    def backQuoted(self):

        localctx = ShellParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_backQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ShellParser.BACK_QUOTED_TEXT)
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
            self.state = 102
            self.callCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





