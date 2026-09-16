# Publicación del repositorio

Fecha: 2026-09-16. Responsable: orchestrator, preparación de Git solicitada por el usuario.

Repositorio confirmado: https://github.com/Leonardo-Toledo-V/numer.git. Rama inicial: `main`.

## Qué se conserva

Documentación, especificaciones, fichas y perfiles compartidos de agentes, diseños, herramientas de generación, recursos gráficos y licencias de tipografías. Los borradores y versiones históricas conservan su estado documental; publicarlos no los aprueba.

## Qué se excluye

[.gitignore](../../.gitignore) omite credenciales y archivos `.env` (salvo plantillas sin secretos), claves privadas, dependencias, compilaciones, cachés, logs, configuración de editores, bases locales y copias de respaldo. También omite:

- `BRANDING_AGENT.md`: instrucciones locales preexistentes; se conserva intacto en disco.
- ZIP generados en `docs/`: sus recursos descomprimidos siguen disponibles. Las referencias históricas a ZIP describen entregables locales, no archivos incluidos en el clon.
- `docs/08-brand/sites/`: copia local de un sitio publicado, con repositorio anidado y metadatos de hosting. El clon no incluye ese sitio ejecutable; conserva documentación y recursos de diseño.
- Estado local de `.codex/`, excepto los perfiles compartidos `agents/*.toml`.

Se retiraron identificadores de conversaciones privadas y rutas personales de seis herramientas. Estas herramientas ahora resuelven `sharp` y `playwright` mediante el mecanismo normal de Node.js; puede usarse `NODE_PATH` para dependencias externas. No se instalaron dependencias ni se volvieron a generar los diseños. Otros requisitos locales, como Chrome, siguen siendo responsabilidad del entorno de ejecución.

## Revisión antes de cada subida

Revisar `git status`, `git diff --cached` y los archivos que se van a publicar. `.gitignore` no protege secretos dentro de archivos admitidos ni deja de versionar archivos ya añadidos. Mantener datos financieros reales fuera del repositorio; utilizar datos sintéticos en ejemplos.

La identidad de commit usa el alias del repositorio y un correo `noreply` de GitHub configurados únicamente para este proyecto. No se modifica la configuración global de Git.
