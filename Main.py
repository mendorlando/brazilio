
import sys

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from BazilioLexer import BazilioLexer
from BazilioParser import BazilioParser
from BazilioSemanticVisitor import BazilioSemanticVisitor


class ContadorErrores(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = 0

    def syntaxError(
        self, recognizer, offendingSymbol,
        line, column, msg, e
    ):
        self.errores += 1
        print(f"Error en línea {line}: {msg}")


def main():

    if len(sys.argv) < 2:
        print("Uso: python Main.py mis_notas.bzl")
        sys.exit(1)

    archivo = sys.argv[1]

    entrada = FileStream(archivo, encoding="utf-8")

    # Análisis léxico
    lexer = BazilioLexer(entrada)
    errores_lexicos = ContadorErrores()

    lexer.removeErrorListeners()
    lexer.addErrorListener(errores_lexicos)

    tokens = CommonTokenStream(lexer)

    # Análisis sintáctico
    parser = BazilioParser(tokens)
    errores_sintacticos = ContadorErrores()

    parser.removeErrorListeners()
    parser.addErrorListener(errores_sintacticos)

    arbol = parser.programa()

    if errores_lexicos.errores or errores_sintacticos.errores:
        print("Compilación detenida por errores.")
        sys.exit(1)

    print("=" * 35)
    print("       COMPILADOR BAZILIO")
    print("=" * 35)

    print("Archivo:", archivo)
    print("Análisis léxico: CORRECTO")
    print("Análisis sintáctico: CORRECTO")

    print("\nÁrbol sintáctico:")
    print(arbol.toStringTree(recog=parser))

    # Análisis semántico
    print("\nANÁLISIS SEMÁNTICO")
    print("-" * 35)

    semantic = BazilioSemanticVisitor()
    semantic.visit(arbol)

    if semantic.errores > 0:
        print("Análisis semántico: INCORRECTO")
        sys.exit(1)

    print("\nAnálisis semántico: CORRECTO")
    print(
        "Eventos musicales reconocidos:",
        len(semantic.notas_midi)
    )

    print("\nCOMPILACIÓN FINALIZADA CORRECTAMENTE")


if __name__ == "__main__":
    main()
