# Contexto global

Estado: base de planificación; sin implementación de la aplicación. Responsable: orchestrator. Fuente: [SRC-01 a SRC-04](SOURCE_NOTES.md).

## Producto

Aplicación de finanzas personales para registrar compras y movimientos, organizar cuentas y tarjetas, consultar ahorro y categorías de gasto, recorrer fechas e historial y recibir proyecciones y alertas. Wallet es el identificador provisional del proyecto.

La interpretación inicial es un gestor de registros financieros personales. La ausencia de custodia de dinero y ejecución de pagos es una **propuesta de límite**, pendiente de confirmar en producto; no hay autorización ni diseño para prestar esos servicios.

## Confirmado por el usuario

- Next.js para la aplicación, componentes de shadcn/ui, Supabase como base de datos y despliegue en Vercel.
- Acceso mediante cuenta de Google y seguridad de las peticiones por la sensibilidad de la información financiera.
- Registro de finanzas y compras, tarjetas usadas, fondo de ahorro, predicciones de ahorro, categorías de mayor gasto, fechas, líneas de tiempo y alertas.
- Referencia de diseño al estilo Apple en la petición inicial; no constituye un sistema visual ni una identidad aprobada.
- Desarrollo guiado por especificaciones (SDD) como metodología transversal a requerimientos, arquitectura, UX/UI, frontend, backend, datos, documentación y pruebas.
- Instrucciones separadas por rol en `agents/` y entregables en `docs/`; excluir la última parte de branding del contexto importado.
- Perfiles nativos de agentes en TOML; las fichas Markdown se mantienen como apoyo. Corrección del usuario del 2026-09-14.

## Propuesto en la planificación

- Sprint 0 antes de código; definir PRD, SRS y reglas financieras.
- Next.js App Router y TypeScript, acceso sensible centralizado en servidor, Supabase Auth y aislamiento RLS.
- Historial de movimientos como base para saldos; cálculos consistentes, transferencias atómicas e idempotencia.
- Entregas completas por funcionalidad, conectando interfaz, validación, servidor, persistencia y pruebas.
- Forecast determinista explicable, sin IA generativa inicial; horizontes y escenarios pendientes.
- MVP centrado en registro y consulta; ampliar después con presupuestos, metas, recurrencias, alertas y forecast. La fase de cada capacidad aún debe confirmarse.

## Situación y siguiente paso

Existe una base documental con nueve fichas de rol y configuración nativa TOML. La metodología está en [SDD_WORKFLOW](SDD_WORKFLOW.md) y las especificaciones en [docs/specs](../specs/README.md). No existe implementación de la aplicación acreditada por esta entrega. El siguiente trabajo de producto es resolver las preguntas y establecer el alcance inicial. Consultar [STATUS](STATUS.md). Los entregables posteriores de especialidades conservan su estado en sus documentos; esta corrección no evalúa decisiones de marca.

## Cómo compartir contexto

Los hechos y restricciones anteriores son la base común. Reglas y requisitos detallados viven en `docs/01-product/`; contratos técnicos en arquitectura, seguridad y datos. Cada agente devuelve un handoff con decisiones y enlaces. El orquestador integra solo cambios relevantes para todos, sin copiar exploraciones, logs ni conversaciones de marca.
