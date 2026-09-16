# SDD · Desarrollo guiado por especificaciones

Estado: metodología confirmada por el usuario el 2026-09-14; procedimiento operativo definido en esta entrega. Responsable: orchestrator. Decisión: DEC-015.

En este proyecto SDD significa **Spec-Driven Development**: el comportamiento se especifica antes de implementar, las tareas derivan de esa especificación y la entrega se verifica contra sus criterios. Se aplica a cada cambio del producto y durante todo su ciclo de vida.

El [diseño de software](../02-architecture/SOFTWARE_DESIGN.md) sigue siendo un entregable de arquitectura. Una especificación describe qué debe ocurrir; el plan técnico explica cómo construirlo. No son sinónimos de SDD.

## Ciclo por funcionalidad o cambio

1. **Especificar:** producto redacta problema, alcance, exclusiones, requisitos y escenarios verificables en `docs/specs/SPEC-NNN-titulo.md`, usando [SPEC](../templates/SPEC.md). Enlaza RF, RN, SEG y decisiones existentes.
2. **Aclarar:** resolver ambigüedades que alteren comportamiento, especialmente reglas financieras, permisos y datos. Registrar respuestas y evidencias; avanzar en partes independientes mientras se resuelven otras.
3. **Planear:** architect, con los especialistas pertinentes, documenta contratos, datos, controles, UI y estrategia de validación. Un cambio pequeño puede tener el plan dentro de su propia especificación; uno complejo enlaza documentos especializados y ADRs.
4. **Descomponer:** orchestrator crea tareas con responsable único, archivos, dependencias y criterios de aceptación vinculados a la versión de la especificación. Usar [TASK](../templates/TASK.md).
5. **Implementar:** frontend/backend u otro propietario ejecutan el alcance acordado. Si descubren una regla faltante o un cambio de contrato, actualizan primero la especificación y analizan su impacto antes de implementar lo dependiente.
6. **Verificar:** QA y revisores comparan resultados con cada criterio. Registrar prueba, resultado y limitaciones; actualizar especificación y [HANDOFF](../templates/HANDOFF.md).

## Estados de una especificación

`borrador → lista para implementar → en implementación → verificada`.

Una especificación puede pasar a `sustituida`, conservando la referencia a su sucesora. Marcar una versión lista requiere comportamiento comprobable, reglas críticas resueltas, dependencias identificadas y evidencia de las decisiones de alcance necesarias. No es una aprobación automática del usuario ni exige pedirle permiso por cada detalle técnico reversible.

La revisión puede integrarse por el orquestador cuando no requiere otra especialidad; no registrar revisores ficticios. Una especificación de producto no se considera verificada porque se haya revisado su Markdown. Solo se verifica el comportamiento implementado que cubren las evidencias.

## Trazabilidad y cambios

Mantener esta cadena por criterio: `requisito/regla → SPEC + versión + AC → T-XXX → archivo/implementación → caso y resultado`.

Los criterios usan IDs locales `AC-01`, `AC-02`, etc.; citarlos junto al ID de especificación. Si cambia el comportamiento, incrementar la versión, registrar motivo/decisión y revisar tareas, contratos y pruebas afectados. La especificación vigente describe lo que debe entregar el producto; el historial conserva cambios y motivos.

## Papel de los agentes

| Rol | Contribución a SDD |
|---|---|
| orchestrator | Mantiene el ciclo, dependencias y trazabilidad; integra el estado |
| product-analyst | Especifica comportamiento y aceptación; resuelve reglas con el usuario |
| architect | Elabora el plan técnico y contratos necesarios |
| security | Añade amenazas, controles y aceptación de seguridad |
| ux-ui | Especifica recorridos, estados e interacción |
| frontend / backend | Implementan tareas vinculadas a la especificación vigente |
| qa | Diseña y ejecuta casos contra aceptación; documenta desviaciones |
| brand-strategist | Entrega decisiones de marca aplicables cuando el encargo las requiere |

El PRD/SRS dan contexto transversal; cada SPEC concreta una entrega. No duplicar todas las reglas en cada archivo: enlazar su fuente y precisar solo lo necesario. No se instala un framework de SDD ni se adopta una herramienta externa por esta metodología.
