# Generated from Bazilio.g4 by ANTLR 4.13.2
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
        4,1,6,18,2,0,7,0,2,1,7,1,1,0,1,0,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,1,1,0,4,5,16,0,4,1,0,0,0,2,15,
        1,0,0,0,4,5,5,1,0,0,5,9,5,2,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,11,1,0,
        0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,5,
        3,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,7,0,0,0,16,3,1,0,0,0,1,9
    ]

class BazilioParser ( Parser ):

    grammarFileName = "Bazilio.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Main'", "'{'", "'}'", "<INVALID>", "'R'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "LLAVE_ABRE", "LLAVE_CIERRA", 
                      "NOTA", "SILENCIO", "WS" ]

    RULE_programa = 0
    RULE_elemento = 1

    ruleNames =  [ "programa", "elemento" ]

    EOF = Token.EOF
    MAIN=1
    LLAVE_ABRE=2
    LLAVE_CIERRA=3
    NOTA=4
    SILENCIO=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(BazilioParser.MAIN, 0)

        def LLAVE_ABRE(self):
            return self.getToken(BazilioParser.LLAVE_ABRE, 0)

        def LLAVE_CIERRA(self):
            return self.getToken(BazilioParser.LLAVE_CIERRA, 0)

        def EOF(self):
            return self.getToken(BazilioParser.EOF, 0)

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BazilioParser.ElementoContext)
            else:
                return self.getTypedRuleContext(BazilioParser.ElementoContext,i)


        def getRuleIndex(self):
            return BazilioParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = BazilioParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(BazilioParser.MAIN)
            self.state = 5
            self.match(BazilioParser.LLAVE_ABRE)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 6
                self.elemento()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(BazilioParser.LLAVE_CIERRA)
            self.state = 13
            self.match(BazilioParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTA(self):
            return self.getToken(BazilioParser.NOTA, 0)

        def SILENCIO(self):
            return self.getToken(BazilioParser.SILENCIO, 0)

        def getRuleIndex(self):
            return BazilioParser.RULE_elemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemento" ):
                listener.enterElemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemento" ):
                listener.exitElemento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemento" ):
                return visitor.visitElemento(self)
            else:
                return visitor.visitChildren(self)




    def elemento(self):

        localctx = BazilioParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elemento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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





