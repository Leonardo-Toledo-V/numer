# Configuración nativa de agentes Codex

Fecha: 2026-09-14. Responsable: orchestrator. Decisión: DEC-014.

Los agentes del proyecto usan archivos independientes `.codex/agents/*.toml` con `name`, `description` y `developer_instructions`. El nombre identifica el rol; modelo y razonamiento se heredan cuando se omiten. Fuente: [documentación oficial de agentes personalizados](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Los perfiles de configuración de sesión seleccionados con `--profile` son otro mecanismo. No representan por sí mismos esta colección de especialistas. Fuente: [referencia oficial de configuración](https://learn.chatgpt.com/docs/config-file/config-reference).

## Organización de este repositorio

| Perfil nativo | Detalle de responsabilidades |
|---|---|
| [orchestrator.toml](../../.codex/agents/orchestrator.toml) | [orchestrator](../../agents/orchestrator.md) |
| [brand-strategist.toml](../../.codex/agents/brand-strategist.toml) | [brand-strategist](../../agents/brand-strategist.md) |
| [product-analyst.toml](../../.codex/agents/product-analyst.toml) | [product-analyst](../../agents/product-analyst.md) |
| [architect.toml](../../.codex/agents/architect.toml) | [architect](../../agents/architect.md) |
| [security.toml](../../.codex/agents/security.toml) | [security](../../agents/security.md) |
| [ux-ui.toml](../../.codex/agents/ux-ui.toml) | [ux-ui](../../agents/ux-ui.md) |
| [frontend.toml](../../.codex/agents/frontend.toml) | [frontend](../../agents/frontend.md) |
| [backend.toml](../../.codex/agents/backend.toml) | [backend](../../agents/backend.md) |
| [qa.toml](../../.codex/agents/qa.toml) | [qa](../../agents/qa.md) |

El TOML contiene instrucciones de entrada, especialidad y metodología. La ficha mantiene el detalle del rol; actualizarla cuando cambien sus responsabilidades y revisar que el resumen del TOML siga siendo coherente. Ambos remiten a `AGENTS.md` y al flujo SDD.

La configuración de esta entrega no fija modelos, razonamiento, concurrencia, herramientas ni permisos. Tampoco crea tareas, agentes activos o una orquestación en ejecución.

## Uso y alcance de validación

En una sesión que cargue los perfiles del proyecto se puede pedir, por ejemplo: «Delega a product-analyst la especificación de movimientos; usa la tarea y las reglas de alcance indicadas, y devuelve un handoff». El coordinador mantiene la propiedad de archivos y carga solo el contexto pertinente.

Definir un agente llamado `orchestrator` no transforma automáticamente la sesión principal en ese rol. La sesión principal puede seguir su ficha y coordinar los especialistas según el encargo.

Se comprueba sintaxis y estructura de los archivos, y que sus referencias locales existan. La instalación CLI identificada es `0.154.0-alpha.6.2`. No se ha ejecutado un spawn de prueba ni comprobado una recarga en esta sesión; disponibilidad efectiva y carga deben observarse en la sesión que los utilice.
