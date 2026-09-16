# PRD · Requisitos de producto

Estado: borrador para levantamiento. Responsable: product-analyst. Entradas: [brief](../00-project/PROJECT_BRIEF.md) y [fuentes](../00-project/SOURCE_NOTES.md).

## Necesidad

Centralizar el registro financiero personal para entender gastos, cuentas, tarjetas y ahorro, y anticipar eventos y resultados mediante alertas y proyecciones. La descripción del producto está confirmada como intención; alcance por versión y criterios detallados siguen propuestos.

## Escenarios principales

| Escenario | Resultado deseado | Funcionalidades |
|---|---|---|
| Registrar una compra | Consultar importe, fecha, categoría y efecto en saldo/deuda | F-04, F-05 |
| Revisar situación financiera | Distinguir efectivo, deuda y ahorro sin duplicar cantidades | F-02, F-03, F-06, F-08 |
| Entender hábitos | Identificar categorías de mayor gasto y evolución temporal | F-05, F-07, F-12 |
| Preparar próximas fechas | Ver pagos, recurrencias y avisos relevantes | F-10, F-11, F-14 |
| Planificar ahorro | Ver fondo actual y estimaciones con supuestos explícitos | F-08, F-09, F-13 |

## Primera versión propuesta

Acceso con Google, cuentas, tarjetas básicas, ingresos/gastos/transferencias, categorías, dashboard, historial y fondos de ahorro. Véase [matriz](FEATURE_MATRIX.md). Esta división procede de una recomendación del chat; el usuario pidió también alertas y predicciones, por lo que debe decidirse si entran desde el lanzamiento.

Entrada manual y uso individual son hipótesis de planificación. Integración bancaria, custodia, ejecución de pagos, OCR, finanzas compartidas y asistente de IA carecen de alcance autorizado o especificación para esta versión.

## Preguntas prioritarias

| ID | Pregunta a resolver | Impacto |
|---|---|---|
| Q-01 | ¿Se confirma gestión de registros sin custodiar dinero ni ejecutar pagos? | Límites del producto y arquitectura |
| Q-02 | ¿Primera versión para uso propio o abierta a otros usuarios? ¿Datos compartidos? | Alta, aislamiento y operación |
| Q-03 | ¿Qué moneda o monedas, idioma y zona horaria deben soportarse? | Importes, fechas y reportes; no asumir MXN por ejemplos |
| Q-04 | ¿Registro manual inicialmente o importación necesaria desde el lanzamiento? | Captura, conciliación e idempotencia |
| Q-05 | ¿Tarjetas solo informativas o con deuda, cortes, pagos y mensualidades? | Modelo de crédito y calendario |
| Q-06 | ¿Fondo como cuenta separada, apartado virtual o ambos? ¿Metas en MVP? | Evitar duplicar ahorro y patrimonio |
| Q-07 | ¿Alertas y predicciones son requisito del primer lanzamiento? ¿Qué casos? | Aceptación del MVP |
| Q-08 | ¿Qué edición, eliminación, devoluciones y ajustes se permiten? | Trazabilidad e integridad financiera |
| Q-09 | ¿Avisos dentro de la app o también correo/push? | Permisos, proveedores y operación |
| Q-10 | ¿Se necesitan exportación, eliminación de cuenta y MFA desde el inicio? | Privacidad, seguridad y alcance |

Resolver Q-01 a Q-07 primero. No hace falta resolver todo el roadmap para especificar una entrega inicial coherente.

## Aceptación de producto propuesta

- Un movimiento registrado aparece en historial y afecta una sola vez los indicadores pertinentes.
- Una transferencia interna mueve saldo entre cuentas sin convertirse en gasto ni ingreso global.
- Deuda, dinero disponible y ahorro apartado tienen definiciones visibles y consistentes.
- La información se aísla por usuario en cada operación, incluyendo relaciones y agregados.
- Si hay proyecciones, la interfaz identifica fecha de cálculo, supuestos y limitaciones; no las presenta como saldos registrados.

El SRS descompone estos resultados en requisitos verificables. Las métricas de velocidad de captura, rendimiento y satisfacción requieren objetivos acordados; todavía no hay valores comprometidos.
