# Handoff · T-007 · orchestrator

- Fecha: 2026-09-14. Responsable: orchestrator. Destinatario: usuario y siguiente coordinador de producto.
- Resultado: nueve perfiles nativos TOML guardados en `.codex/agents/`; metodología SDD incorporada al contexto, las fichas, las tareas y las plantillas.
- Especificación: [SPEC-000](../../specs/SPEC-000-perfiles-sdd.md), versión 1.0, AC-01 a AC-05.
- Decisiones: DEC-014/015, basadas en la corrección explícita del usuario, SRC-04. El alcance del MVP sigue pendiente.
- Archivos: perfiles `.codex/agents/*.toml`, guías globales, ocho fichas de rol, referencias de arquitectura, `SDD_WORKFLOW.md`, `CODEX_AGENTS.md`, `docs/specs/`, plantilla SPEC y plantillas TASK/HANDOFF. El informe registra los archivos cambiados.
- Conservación: el diseño anterior se mantiene en `SOFTWARE_DESIGN.md`; `SDD.md` remite a él y a la metodología. El contenido de branding queda fuera del cambio.
- Validación: parseo con `tomllib`, nombres/campos requeridos, lecturas de contexto, enlaces Markdown y hashes de archivos previos. Resultado detallado en [verification/T-007.json](../verification/T-007.json).
- Limitaciones: no se ha comprobado carga o spawn de estos perfiles dentro de una nueva sesión. Tampoco se han ejecutado pruebas de producto ni cambiado configuración global, modelos o permisos.
- Revisión: integración local del responsable, sin revisión independiente ni agentes delegados.
- Siguiente acción: product-analyst resuelve T-001/T-002 y redacta las primeras especificaciones funcionales con aceptación explícita; orchestrator deriva el plan y las tareas según SDD.
