from pathlib import Path

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from flask import Flask, jsonify, request, send_file
from werkzeug.exceptions import HTTPException

from BazilioLexer import BazilioLexer
from BazilioParser import BazilioParser
from BazilioSemanticVisitor import BazilioSemanticVisitor

app = Flask(__name__, static_folder=None)
app.config["MAX_CONTENT_LENGTH"] = 32768


class Diagnostics(ErrorListener):
    def __init__(self, stage, errors):
        self.stage, self.errors = stage, errors

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({"stage": self.stage, "line": line,
                            "column": column + 1, "message": msg})


@app.errorhandler(HTTPException)
def http_error(error):
    return jsonify(ok=False, errors=[{"message": error.description}]), error.code


@app.get("/")
def index():
    return send_file(Path(__file__).with_name("index.html"))


@app.get("/health")
def health():
    return jsonify(ok=True, compiler="ANTLR4", runtime="4.13.2")


@app.post("/api/compile")
def compile_source():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(ok=False, errors=[{"message": "Se requiere un objeto JSON."}]), 400
    source = data.get("source")
    octave = data.get("octave", 4)
    if not isinstance(source, str) or not source.strip() or len(source) > 16000:
        return jsonify(ok=False, errors=[{"message": "Programa vacío o demasiado largo (máximo 16000 caracteres)."}]), 400
    if type(octave) is not int or not 2 <= octave <= 6:
        return jsonify(ok=False, errors=[{"message": "La octava base debe ser un entero entre 2 y 6."}]), 400
    errors = []
    lexer = BazilioLexer(InputStream(source))
    lexer.removeErrorListeners()
    lexer.addErrorListener(Diagnostics("léxico", errors))
    tokens = CommonTokenStream(lexer)
    parser = BazilioParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(Diagnostics("sintáctico", errors))
    tree = parser.programa()
    if errors:
        return jsonify(ok=False, errors=errors), 422
    messages = []
    visitor = BazilioSemanticVisitor(emit=messages.append)
    visitor.octava_base = octave
    visitor.visit(tree)
    if visitor.errores:
        return jsonify(ok=False, errors=[{"stage": "semántico", "message": m}
                       for m in messages if m.startswith("Error")]), 422
    notes = []
    for element, midi in zip(tree.elemento(), visitor.notas_midi):
        token = element.getText()
        if midi == -1:
            notes.append({"token": token, "rest": True})
        else:
            explicit = token[-1].isdigit()
            notes.append({"token": token, "rest": False, "midi": midi,
                          "name": token[:-1] if explicit else token,
                          "octave": int(token[-1]) if explicit else octave})
    return jsonify(ok=True, compiler="ANTLR4", notes=notes,
                   tree=tree.toStringTree(recog=parser), diagnostics=messages)
