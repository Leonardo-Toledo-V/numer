# Estado del proyecto

Actualizado: 2026-09-14. Responsable: orchestrator.

## Completado en esta entrega

- Recuperado el contexto funcional y técnico del chat con procedencia y exclusiones explícitas.
- Creadas instrucciones globales y nueve fichas de rol.
- Definidos propietarios, paquetes de contexto, handoffs y gates de revisión.
- Preparados borradores de producto, dominio, arquitectura, seguridad, datos, diseño, QA, ingeniería y despliegue.

## Corrección del 2026-09-14

- Creados nueve perfiles nativos en `.codex/agents/*.toml`, conservando las fichas Markdown como apoyo.
- Confirmado SDD como desarrollo guiado por especificaciones; añadidos [flujo](SDD_WORKFLOW.md), plantilla e índice de especificaciones.
- Conservado el documento de arquitectura en `SOFTWARE_DESIGN.md` y corregidas sus referencias.
- [T-007](tasks/T-007-perfiles-sdd.md) documenta la corrección; [handoff](handoffs/T-007-perfiles-sdd.md) e [informe](verification/T-007.json) contienen el resultado y sus límites. La carga efectiva de perfiles en una sesión no se ha probado.

## Pendiente

No hay alcance inicial aprobado, diseño de software definitivo, esquema implementado, UI, autenticación configurada, pruebas de aplicación ejecutadas ni despliegue. Los documentos técnicos son propuestas de planificación.

| Tarea | Estado | Responsable | Resultado esperado |
|---|---|---|---|
| T-001 · Concretar alcance | Pendiente | product-analyst | Resolver preguntas prioritarias del PRD y fijar MVP |
| T-002 · Reglas financieras | Pendiente | product-analyst | Cerrar reglas críticas de movimientos, crédito, ahorro y fechas |
| T-003 · Contratos y datos | Pendiente; depende de T-001/T-002 | architect + backend | Diseño de software y ERD revisados, decisiones monetarias |
| T-004 · Seguridad | Pendiente; revisión inicial posible | security | Amenazas y matriz RLS adaptadas a contratos |
| T-005 · Experiencia | Pendiente; exploración posible | ux-ui | Flujos y estados conforme al alcance |
| T-006 · Validación | Pendiente; diseño de casos posible | qa | Casos trazables y datos sintéticos |
| T-007 · Perfiles TOML y SDD | Terminada; carga en ejecución no probada | orchestrator | SPEC-000 y configuración nativa |

Los responsables indicados son roles de trabajo; esta corrección no lanzó agentes ni asignó desarrollo de producto. El estado de trabajo posterior de otras especialidades se conserva en sus entregables y no se reevalúa aquí.

## Verificación de esta entrega documental

Revisión local del 2026-09-13: 44 documentos creados, nueve fichas de rol y 73 enlaces locales comprobados sin rutas rotas. Se comprobaron títulos y cierre de bloques de código. El SHA-256 de `BRANDING_AGENT.md` coincide con el registrado antes de la edición; se conserva intacto.

Esta comprobación valida estructura documental, no renderizado de diagramas, implementación de requisitos ni comportamiento de una aplicación. Los casos de QA siguen sin ejecutar.

## Próxima sesión

Comenzar por T-001 con [PRD](../01-product/PRD.md). Priorizar tipo de producto/usuarios, moneda, entrada de datos, profundidad de tarjetas y ahorro, y qué funcionalidades deben estar desde el primer lanzamiento. Registrar las respuestas en decisiones y propagar sus consecuencias.

## Preparación de GitHub · 2026-09-16

[T-008](tasks/T-008-github.md): Git inicializado en `main` y remoto configurado; exclusiones y limpieza de metadatos personales preparadas. Publicación pendiente de verificar. Consulta el [handoff](handoffs/T-008-github.md) y la [política de archivos](../07-deployment/GIT_HYGIENE.md). No cambia el estado de implementación del producto.
