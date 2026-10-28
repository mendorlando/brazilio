# Generated from Bazilio.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,38,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,3,3,25,8,3,1,3,3,3,28,
        8,3,1,4,1,4,1,5,4,5,33,8,5,11,5,12,5,34,1,5,1,5,0,0,6,1,1,3,2,5,
        3,7,4,9,5,11,6,1,0,4,1,0,65,71,2,0,35,35,98,98,1,0,48,56,3,0,9,10,
        13,13,32,32,40,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,18,1,0,0,0,5,20,1,0,0,0,7,
        22,1,0,0,0,9,29,1,0,0,0,11,32,1,0,0,0,13,14,5,77,0,0,14,15,5,97,
        0,0,15,16,5,105,0,0,16,17,5,110,0,0,17,2,1,0,0,0,18,19,5,123,0,0,
        19,4,1,0,0,0,20,21,5,125,0,0,21,6,1,0,0,0,22,24,7,0,0,0,23,25,7,
        1,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,28,7,2,0,0,27,
        26,1,0,0,0,27,28,1,0,0,0,28,8,1,0,0,0,29,30,5,82,0,0,30,10,1,0,0,
        0,31,33,7,3,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,
        1,0,0,0,35,36,1,0,0,0,36,37,6,5,0,0,37,12,1,0,0,0,4,0,24,27,34,1,
        6,0,0
    ]

class BazilioLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN = 1
    LLAVE_ABRE = 2
    LLAVE_CIERRA = 3
    NOTA = 4
    SILENCIO = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Main'", "'{'", "'}'", "'R'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN", "LLAVE_ABRE", "LLAVE_CIERRA", "NOTA", "SILENCIO", "WS" ]

    ruleNames = [ "MAIN", "LLAVE_ABRE", "LLAVE_CIERRA", "NOTA", "SILENCIO", 
                  "WS" ]

    grammarFileName = "Bazilio.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


