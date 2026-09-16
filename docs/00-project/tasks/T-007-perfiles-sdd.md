# T-007 · Perfiles TOML y desarrollo guiado por especificaciones

- Estado: terminada; alcance y limitaciones en el handoff.
- Responsable: orchestrator; integración local, sin delegación.
- Objetivo: corregir la organización de agentes y el significado de SDD.
- Especificación: [SPEC-000](../../specs/SPEC-000-perfiles-sdd.md), versión 1.0, AC-01 a AC-05.
- Entradas: contexto, estado, ficha orchestrator, corrección del usuario y documentación oficial de Codex.
- Archivos: `.codex/agents/*.toml`, fichas afectadas de `agents/`, guías globales, referencias de arquitectura y documentos/plantillas SDD.
- Exclusiones: contenido de branding, funcionalidad financiera, configuración global, modelos y permisos.
- Dependencias: formato oficial comprobado; escritura de perfiles sujeta a protección de `.codex/` del entorno.
- Validación: parseo TOML, campos, enlaces, terminología y comparación de hashes.
- Handoff: [T-007](../handoffs/T-007-perfiles-sdd.md).
