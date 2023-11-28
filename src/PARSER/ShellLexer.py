# Generated from ShellLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,5,4,5,33,8,5,11,5,12,5,34,1,6,4,6,38,8,6,11,6,12,6,39,1,
        6,1,6,1,7,4,7,45,8,7,11,7,12,7,46,1,7,1,7,1,8,1,8,1,9,1,9,0,0,10,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,1,0,3,9,0,9,10,13,
        13,32,32,34,34,39,39,59,60,62,62,96,96,124,124,2,0,9,9,32,32,2,0,
        10,10,13,13,56,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,
        19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,
        29,1,0,0,0,11,32,1,0,0,0,13,37,1,0,0,0,15,44,1,0,0,0,17,50,1,0,0,
        0,19,52,1,0,0,0,21,22,5,60,0,0,22,2,1,0,0,0,23,24,5,62,0,0,24,4,
        1,0,0,0,25,26,5,39,0,0,26,6,1,0,0,0,27,28,5,34,0,0,28,8,1,0,0,0,
        29,30,5,96,0,0,30,10,1,0,0,0,31,33,8,0,0,0,32,31,1,0,0,0,33,34,1,
        0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,12,1,0,0,0,36,38,7,1,0,0,37,
        36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,
        0,41,42,6,6,0,0,42,14,1,0,0,0,43,45,7,2,0,0,44,43,1,0,0,0,45,46,
        1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,6,7,0,0,
        49,16,1,0,0,0,50,51,5,124,0,0,51,18,1,0,0,0,52,53,5,59,0,0,53,20,
        1,0,0,0,4,0,34,39,46,1,6,0,0
    ]

class ShellLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LT = 1
    GT = 2
    SINGLE_QUOTE = 3
    DOUBLE_QUOTE = 4
    BACK_QUOTE = 5
    UNQUOTED = 6
    WS = 7
    NEWLINE = 8
    PIPE = 9
    SEMI = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'''", "'\"'", "'`'", "'|'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "LT", "GT", "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_QUOTE", "UNQUOTED", 
            "WS", "NEWLINE", "PIPE", "SEMI" ]

    ruleNames = [ "LT", "GT", "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_QUOTE", 
                  "UNQUOTED", "WS", "NEWLINE", "PIPE", "SEMI" ]

    grammarFileName = "ShellLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


