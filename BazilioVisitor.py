# Generated from Bazilio.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BazilioParser import BazilioParser
else:
    from BazilioParser import BazilioParser

# This class defines a complete generic visitor for a parse tree produced by BazilioParser.

class BazilioVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BazilioParser#programa.
    def visitPrograma(self, ctx:BazilioParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BazilioParser#elemento.
    def visitElemento(self, ctx:BazilioParser.ElementoContext):
        return self.visitChildren(ctx)



del BazilioParser