# Publicar Bazilio en Render

La interfaz index.html funciona completamente en el navegador: audio, PDF y exportación .bzl. El compilador Python de terminal no se ejecuta en este sitio estático.

1. Sube el proyecto a un repositorio de GitHub.
2. En Render selecciona New > Static Site y conecta ese repositorio.
3. Nombre: bazilio. Selecciona la rama que contiene los archivos.
4. Root Directory: dejar vacío.
5. Build Command: `mkdir -p dist && cp index.html dist/index.html`
6. Publish Directory: `dist`
7. Selecciona Create Static Site y espera a que termine el despliegue.

También puedes usar New > Blueprint con el archivo render.yaml incluido.

No se requieren variables de entorno. Solo se publica index.html.
Prueba en la URL de Render reproducir C4 D4 E4 C4 B3 A3, detener el audio, descargar el PDF y exportar el archivo .bzl.
