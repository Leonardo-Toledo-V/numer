# Roadmap

Estado: propuesta, sin fechas ni estimaciones comprometidas. Responsable: orchestrator.

SDD es la metodología transversal confirmada: cada entrega recorre especificación, aclaración, plan, tareas, implementación y verificación. Las fases siguientes organizan especialidades y dependencias; no sustituyen el [flujo por especificación](SDD_WORKFLOW.md).

| Fase | Responsable | Entregable | Dependencia / salida |
|---|---|---|---|
| 0 · Contexto y brief | orchestrator + producto | Brief, preguntas, registro de decisiones | Base documental creada; falta validar alcance |
| 1 · Requerimientos | product-analyst | PRD, SRS, matriz y aceptación | Responder prioridades del PRD; G1 |
| 2 · Dominio financiero | product-analyst + architect | Reglas, glosario y ejemplos numéricos | Semántica de saldo, deuda, ahorro, fechas |
| 3 · Arquitectura | architect | Diseño de software, diagramas y ADRs | Requisitos y reglas del módulo |
| 4 · Seguridad | security | Amenazas, controles, políticas de sesión | Trabaja desde fase 1 y revisa fase 3 |
| 5 · Datos | backend + architect | ERD, diccionario, migraciones y RLS | Reglas + seguridad; G2 |
| 6 · UX | ux-ui | Navegación, flujos y estados | Puede explorar tras alcance de producto |
| 7 · UI | ux-ui | Sistema de interfaz y especificaciones | Flujos y decisiones visuales aplicables; G3 |
| 8 · Base frontend | frontend | Estructura Next.js y componentes | Contratos y diseño listos para implementar |
| 9 · Base backend | backend | Auth, acceso a datos y persistencia | Datos y controles revisados |
| 10 · Funcionalidades | frontend + backend | Entregas completas por módulo | Cada entrega atraviesa G4 |
| 11 · Forecast y alertas | producto + backend + frontend | Cálculos explicables y notificaciones | Datos fiables y alcance confirmado |
| 12 · Validación | qa + security | Unitarias, integración, E2E y seguridad | QA participa desde fase 1; cierre G4 |
| 13 · Despliegue | orchestrator + ingeniería | Entorno, migraciones y operación | G5 y autorización correspondiente |
| 14 · Mantenimiento | Todos por área | Documentación técnica, de usuario y operación | Se actualiza durante todas las fases |

La numeración organiza entregables; no obliga a terminar todo el producto antes de diseñar o probar un módulo. Las foundations desembocan en entregas completas, por ejemplo: movimiento → formulario → validación → caso de uso → persistencia → aislamiento → prueba.

La separación inicial MVP/V1/V2 se conserva en [FEATURE_MATRIX](../01-product/FEATURE_MATRIX.md) como propuesta. Forecast y alertas fueron pedidos por el usuario: su aplazamiento requiere resolver alcance, no asumir que dejaron de ser necesarios.
