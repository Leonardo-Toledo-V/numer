# Agentes y propiedad de entregables

Todos leen primero [AGENTS.md](../AGENTS.md), el [contexto](../docs/00-project/PROJECT_CONTEXT.md) y el [estado](../docs/00-project/STATUS.md). Después cargan solo su ficha, el encargo y sus dependencias. Los nombres siguientes son los identificadores canónicos.

Cada rol tiene un perfil nativo del mismo nombre en `.codex/agents/<rol>.toml`, con instrucciones para cargar su ficha y aplicar [SDD](../docs/00-project/SDD_WORKFLOW.md). Ver [formato y uso](../docs/00-project/CODEX_AGENTS.md). El perfil y la ficha cumplen funciones complementarias; el detalle de responsabilidades se mantiene en esta carpeta.

| Rol | Responsabilidad | Salida principal | Revisión / consumidor |
|---|---|---|---|
| [orchestrator](orchestrator.md) | Alcance, secuencia, integración y estado | `docs/00-project/` | Usuario y todos los roles |
| [brand-strategist](brand-strategist.md) | Encargos futuros de marca, aislados | `docs/08-brand/` | Usuario; UX/UI consume decisiones aprobadas |
| [product-analyst](product-analyst.md) | Requisitos y reglas financieras | `docs/01-product/` | Orquestador, arquitectura, UX y QA |
| [architect](architect.md) | Arquitectura, contratos y ADR | `docs/02-architecture/` | Seguridad, frontend y backend |
| [security](security.md) | Amenazas y controles verificables | `docs/03-security/` | Arquitectura, backend y QA |
| [ux-ui](ux-ui.md) | Flujos, interacción y sistema de interfaz | `docs/05-design/` | Producto, frontend y QA |
| [frontend](frontend.md) | Interfaz y su integración | `docs/09-engineering/FRONTEND.md` | Arquitectura, UX, seguridad y QA |
| [backend](backend.md) | Datos, servicios y persistencia | `docs/04-database/`, `docs/09-engineering/BACKEND.md` | Arquitectura, seguridad y QA |
| [qa](qa.md) | Evidencia y trazabilidad de calidad | `docs/06-testing/` | Orquestador y responsables de cambios |

El orquestador mantiene `docs/07-deployment/` integrando procedimientos de backend, frontend, seguridad y QA. El brief pertenece al orquestador; producto propone ajustes. La matriz RLS pertenece a seguridad; backend implementa y QA verifica. El ERD pertenece a backend y lo revisa arquitectura.

En `docs/specs/`, product-analyst mantiene comportamiento y aceptación; architect aporta el plan, especialistas aportan sus contratos y QA registra evidencia. Orchestrator coordina las escrituras y versiones para evitar ediciones simultáneas incompatibles.

## Ejemplo de asignación

> Actúa como `product-analyst`. Lee `AGENTS.md`, `docs/00-project/PROJECT_CONTEXT.md`, `docs/00-project/STATUS.md` y `agents/product-analyst.md`. Para la tarea T-001, concreta el MVP y las preguntas de descubrimiento en `docs/01-product/`. Conserva como propuestas las recomendaciones sin aprobación. Entrega cambios trazables y un handoff para el orquestador.

Los paquetes de trabajo y las revisiones siguen el [protocolo de orquestación](../docs/00-project/ORCHESTRATION.md).
