# Índice de documentación

Cada documento tiene un propietario. Los borradores contienen información útil para trabajar, pero no prueban implementación ni aprobación. Las fuentes y límites de esta entrega están en [SOURCE_NOTES](00-project/SOURCE_NOTES.md).

| Área | Documentos | Propietario |
|---|---|---|
| Contexto común | [Contexto](00-project/PROJECT_CONTEXT.md), [brief](00-project/PROJECT_BRIEF.md), [estado](00-project/STATUS.md) | orchestrator |
| Coordinación | [Orquestación](00-project/ORCHESTRATION.md), [roadmap](00-project/ROADMAP.md), [decisiones](00-project/DECISIONS.md) | orchestrator |
| Agentes nativos | [Configuración TOML](00-project/CODEX_AGENTS.md) | orchestrator |
| SDD | [Metodología](00-project/SDD_WORKFLOW.md), [especificaciones](specs/README.md) | orchestrator + especialistas |
| Producto | [PRD](01-product/PRD.md), [SRS](01-product/SRS.md), [funcionalidades](01-product/FEATURE_MATRIX.md) | product-analyst |
| Dominio | [Glosario](01-product/DOMAIN_GLOSSARY.md), [reglas financieras](01-product/BUSINESS_RULES.md) | product-analyst |
| Arquitectura | [Diseño de software](02-architecture/SOFTWARE_DESIGN.md), [ADRs](02-architecture/adr/README.md) | architect |
| Seguridad | [Amenazas](03-security/THREAT_MODEL.md), [requisitos](03-security/SECURITY_REQUIREMENTS.md), [RLS](03-security/RLS_MATRIX.md) | security |
| Datos | [ERD](04-database/ERD.md), [diccionario](04-database/DATA_DICTIONARY.md), [migraciones](04-database/MIGRATIONS.md) | backend |
| Diseño | [Flujos](05-design/USER_FLOWS.md), [sistema de interfaz](05-design/DESIGN_SYSTEM.md) | ux-ui |
| QA | [Plan](06-testing/TEST_PLAN.md), [casos de seguridad](06-testing/SECURITY_TESTS.md) | qa |
| Operación | [Despliegue](07-deployment/DEPLOYMENT.md) | orchestrator, con especialistas |
| Marca | [Espacio reservado](08-brand/README.md) | brand-strategist |
| Desarrollo | [Frontend](09-engineering/FRONTEND.md), [backend](09-engineering/BACKEND.md) | frontend / backend |
| Plantillas | [Especificación](templates/SPEC.md), [tarea](templates/TASK.md), [handoff](templates/HANDOFF.md), [decisión](templates/DECISION.md) | orchestrator |

## Convenciones

- Documentar en español; mantener identificadores técnicos consistentes.
- Conservar IDs de requisitos, reglas, decisiones y tareas cuando cambie su redacción.
- Indicar estado, responsable y dependencias; añadir fecha y evidencia al aprobar o verificar.
- Enlazar la fuente de una regla en lugar de mantener varias copias divergentes.
- Añadir documentos cuando haya entregables reales: no es necesario crear todos los archivos de una fase por adelantado.
- Los futuros handoffs pueden guardarse en `00-project/handoffs/T-XXX-rol.md`; las evidencias técnicas permanecen junto a la especialidad correspondiente. Estas rutas se crearán al usarse.
