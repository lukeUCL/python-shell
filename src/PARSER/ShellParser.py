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
        4,1,10,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,3,0,26,8,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,46,8,2,1,3,1,3,1,3,4,3,51,8,3,11,3,12,3,52,1,4,1,4,3,4,57,
        8,4,1,5,1,5,1,5,1,6,1,6,3,6,64,8,6,1,7,1,7,5,7,68,8,7,10,7,12,7,
        71,9,7,1,7,1,7,1,8,1,8,5,8,77,8,8,10,8,12,8,80,9,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,2,69,78,0,11,0,2,4,6,8,10,12,14,16,18,20,
        0,1,1,0,1,2,89,0,25,1,0,0,0,2,35,1,0,0,0,4,45,1,0,0,0,6,50,1,0,0,
        0,8,56,1,0,0,0,10,58,1,0,0,0,12,63,1,0,0,0,14,65,1,0,0,0,16,74,1,
        0,0,0,18,83,1,0,0,0,20,87,1,0,0,0,22,26,3,2,1,0,23,26,3,4,2,0,24,
        26,3,6,3,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,1,1,0,0,
        0,27,28,3,6,3,0,28,29,5,10,0,0,29,30,3,2,1,0,30,36,1,0,0,0,31,32,
        3,6,3,0,32,33,5,10,0,0,33,34,3,6,3,0,34,36,1,0,0,0,35,27,1,0,0,0,
        35,31,1,0,0,0,36,3,1,0,0,0,37,38,3,6,3,0,38,39,5,9,0,0,39,40,3,4,
        2,0,40,46,1,0,0,0,41,42,3,6,3,0,42,43,5,9,0,0,43,44,3,6,3,0,44,46,
        1,0,0,0,45,37,1,0,0,0,45,41,1,0,0,0,46,5,1,0,0,0,47,51,3,8,4,0,48,
        51,3,10,5,0,49,51,3,18,9,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,
        0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,7,1,0,0,0,54,57,
        3,12,6,0,55,57,5,6,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,9,1,0,0,0,
        58,59,7,0,0,0,59,60,3,8,4,0,60,11,1,0,0,0,61,64,3,14,7,0,62,64,3,
        16,8,0,63,61,1,0,0,0,63,62,1,0,0,0,64,13,1,0,0,0,65,69,5,3,0,0,66,
        68,9,0,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,70,1,0,0,0,69,67,1,0,0,
        0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,3,0,0,73,15,1,0,0,0,74,78,
        5,4,0,0,75,77,9,0,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,79,1,0,0,0,
        78,76,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,4,0,0,82,17,1,
        0,0,0,83,84,5,5,0,0,84,85,3,20,10,0,85,86,5,5,0,0,86,19,1,0,0,0,
        87,88,3,6,3,0,88,21,1,0,0,0,9,25,35,45,50,52,56,63,69,78
    ]

class ShellParser ( Parser ):

    grammarFileName = "ShellParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'''", "'\"'", "'`'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'|'", "';'" ]

    symbolicNames = [ "<INVALID>", "LT", "GT", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                      "BACK_QUOTE", "UNQUOTED", "WS", "NEWLINE", "PIPE", 
                      "SEMI" ]

    RULE_command = 0
    RULE_seqCommand = 1
    RULE_pipeCommand = 2
    RULE_callCommand = 3
    RULE_argument = 4
    RULE_redirection = 5
    RULE_quoted = 6
    RULE_singleQuoted = 7
    RULE_doubleQuoted = 8
    RULE_commandSubstitution = 9
    RULE_innerCommand = 10

    ruleNames =  [ "command", "seqCommand", "pipeCommand", "callCommand", 
                   "argument", "redirection", "quoted", "singleQuoted", 
                   "doubleQuoted", "commandSubstitution", "innerCommand" ]

    EOF = Token.EOF
    LT=1
    GT=2
    SINGLE_QUOTE=3
    DOUBLE_QUOTE=4
    BACK_QUOTE=5
    UNQUOTED=6
    WS=7
    NEWLINE=8
    PIPE=9
    SEMI=10

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
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.seqCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.pipeCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
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
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.callCommand()
                self.state = 28
                self.match(ShellParser.SEMI)
                self.state = 29
                self.seqCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.callCommand()
                self.state = 32
                self.match(ShellParser.SEMI)
                self.state = 33
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.callCommand()
                self.state = 38
                self.match(ShellParser.PIPE)
                self.state = 39
                self.pipeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.callCommand()
                self.state = 42
                self.match(ShellParser.PIPE)
                self.state = 43
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
            self.state = 50 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 50
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 4, 6]:
                        self.state = 47
                        self.argument()
                        pass
                    elif token in [1, 2]:
                        self.state = 48
                        self.redirection()
                        pass
                    elif token in [5]:
                        self.state = 49
                        self.commandSubstitution()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 52 
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
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.quoted()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
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
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 59
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
        self.enterRule(localctx, 12, self.RULE_quoted)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.singleQuoted()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
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

        def SINGLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.SINGLE_QUOTE)
            else:
                return self.getToken(ShellParser.SINGLE_QUOTE, i)

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
        self.enterRule(localctx, 14, self.RULE_singleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ShellParser.SINGLE_QUOTE)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 66
                    self.matchWildcard() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 72
            self.match(ShellParser.SINGLE_QUOTE)
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

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellParser.DOUBLE_QUOTE)
            else:
                return self.getToken(ShellParser.DOUBLE_QUOTE, i)

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
        self.enterRule(localctx, 16, self.RULE_doubleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ShellParser.DOUBLE_QUOTE)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 75
                    self.matchWildcard() 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 81
            self.match(ShellParser.DOUBLE_QUOTE)
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
        self.enterRule(localctx, 18, self.RULE_commandSubstitution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ShellParser.BACK_QUOTE)
            self.state = 84
            self.innerCommand()
            self.state = 85
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
        self.enterRule(localctx, 20, self.RULE_innerCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.callCommand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





