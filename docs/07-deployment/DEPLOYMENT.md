# Despliegue y operación

Estado: plan preliminar; sin entornos configurados ni despliegue autorizado por esta entrega. Responsable: orchestrator; colaboradores: frontend, backend, security y qa.

## Destino y separación

Vercel y Supabase están elegidos por el usuario. La planificación propone desarrollo local, ambiente de desarrollo/preview y producción, evitando compartir datos reales con previews. Nombres de proyectos, regiones, URLs, cuentas y variables concretas están pendientes.

## Preparación antes del lanzamiento

| Entregable | Responsable | Evidencia |
|---|---|---|
| Aplicación construible con configuración documentada | frontend + backend | Comandos y resultado sobre versión identificada |
| Configuración de acceso con Google por entorno | backend + security | Pruebas de callback, sesión, expiración y cierre |
| Variables y secretos separados | backend + security | Inventario sin valores y revisión de exposición |
| Migraciones, restricciones y RLS | backend | Aplicación en entorno aislado y resultados de QA |
| Aceptación, aislamiento y accesibilidad | qa + security | Casos ejecutados y defectos resueltos |
| Recuperación y observabilidad | backend + orchestrator | Ensayo, responsables e indicadores definidos |
| Instrucciones de uso y mantenimiento | Roles por especialidad | Procedimientos correspondientes a la versión real |

## Procedimiento a concretar

Documentar despliegue, comprobaciones posteriores, rollback de aplicación, tratamiento de migraciones y restauración de datos antes de ejecutar sobre producción. Revisar compatibilidad de código/esquema entre versiones. Registrar quién actúa ante incidentes y qué señales requieren intervención.

No se ofrecen comandos ficticios de build o deploy: deben salir de la aplicación y herramientas finalmente elegidas. No se han creado proyectos remotos, configurado OAuth ni publicado ningún recurso.
