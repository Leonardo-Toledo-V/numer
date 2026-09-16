# Handoff · T-008 · orchestrator

- Fecha: 2026-09-16. Responsable: orchestrator. Destinatario: usuario.
- Resultado: preparación de Git y exclusiones completada; publicación pendiente de verificar.
- Archivos: `.gitignore`, `.gitattributes`, README, `SOURCE_NOTES.md`, `STATUS.md`, `GIT_HYGIENE.md`, tarea T-008 y este handoff; seis scripts de renderizado ahora resuelven dependencias sin rutas personales.
- Requisitos: solicitud directa de publicación en el remoto proporcionado. Sin cambio de alcance de producto ni SPEC funcional.
- AC-01: repositorio local inicializado en `main`; remoto `https://github.com/Leonardo-Toledo-V/numer.git`.
- AC-02: revisión de patrones de tokens, claves, asignaciones de credenciales, correos y rutas personales. Coincidencias numéricas revisadas: decimales de geometría y contraste, sin números de tarjeta identificados. Exclusiones comprobadas: 437 archivos preparados antes de añadir `.gitattributes`, aproximadamente 10 MB, nueve perfiles compartidos y cero gitlinks. Los seis scripts modificados pasan `node --check`. La comprobación de espacios detectó avisos preexistentes en documentos y licencias; se conservan intactos. PDF y otros recursos declarados binarios en `.gitattributes`.
- AC-03: pendiente de commit y comparación de `HEAD` con `refs/heads/main` remoto.
- Límites: revisión por patrones, sin garantía absoluta de ausencia de datos sensibles. No se ejecutó la aplicación ni se regeneraron imágenes. No se modificó la visibilidad del repositorio remoto.
- Riesgos: archivos nuevos deben revisarse antes de futuros commits; `.gitignore` no inspecciona contenidos.
- Siguiente responsable: orchestrator, finalizar commit, push y verificación; después usuario, continuar planificación.
