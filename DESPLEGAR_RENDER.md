# Bazilio con ANTLR4 en Render

La página llama a POST /api/compile. Python ejecuta el lexer, parser y visitante semántico de ANTLR4 y devuelve las notas MIDI. El navegador reproduce esas notas y genera el PDF y el archivo .bzl después de una compilación correcta.

## Despliegue

El sitio estático anterior no ejecuta Python. Crea un servicio nuevo:

1. Render > New > Web Service.
2. Conecta mendorlando/brazilio, rama antlr4-web.
3. Nombre: bazilio-antlr4. Language: Python 3. Root Directory: vacío.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `gunicorn --bind 0.0.0.0:$PORT app:app`
6. Selecciona Free y despliega. Health Check Path: `/health`.
7. Usa la nueva URL para reproducir, descargar PDF y exportar .bzl.

También puedes crear un Blueprint con render.yaml.

## Local

`python -m pip install -r requirements.txt`

`python -m flask --app app run`

Abre http://127.0.0.1:5000; no abras index.html directamente.

## Verificación

`python -m unittest discover -s tests -v`

GET /health debe indicar ANTLR4. POST /api/compile acepta JSON con source (por ejemplo `Main { C4 D4 E4 C4 B3 A3 }`) y octave (4). Devuelve árbol sintáctico y notas MIDI; los errores léxicos, sintácticos o semánticos tienen estado 422.
