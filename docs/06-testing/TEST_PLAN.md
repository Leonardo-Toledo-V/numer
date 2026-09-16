# Plan de pruebas

Estado: estrategia propuesta; pruebas de aplicación no ejecutadas. Responsable: qa.

En el [flujo SDD](../00-project/SDD_WORKFLOW.md), cada ejecución debe vincular caso → SPEC y versión → criterio AC → requisito/regla. Los casos transversales siguientes se concretan para la especificación de cada entrega; su existencia no sustituye esa aceptación.

## Capas y herramientas candidatas

- Unitarias para reglas financieras y proyecciones; Vitest fue sugerido.
- Componentes e interacción; Testing Library fue sugerido.
- Integración para contratos, validación y persistencia, incluyendo fallos y reintentos.
- Base de datos para restricciones, atomicidad, funciones y RLS con identidades representativas.
- E2E para recorridos completos; Playwright fue sugerido.
- Revisión de seguridad, accesibilidad y procedimientos de migración/recuperación según riesgo.

No hay herramientas instaladas ni comandos del proyecto todavía. Elegir versiones y configuración al implementar, sin presentar estos nombres como dependencias existentes.

## Trazabilidad inicial

| Caso | Requisitos / reglas | Resultado esperado | Estado |
|---|---|---|---|
| TP-01 · Acceso y cierre | RF-01, SEG-01/07 | Identidad correcta; cancelación y sesión inválida no permiten operar | No ejecutado |
| TP-02 · Compra registrada | RF-04/06/07, RN-01/02/05 | Un registro modifica una vez saldo/deuda, historial y categoría correspondientes | No ejecutado |
| TP-03 · Transferencia | RF-05, RN-03 | A=1,000/B=200 → A=900/B=300; total=1,200; gasto sin cambio | No ejecutado |
| TP-04 · Reintento y fallo parcial | RF-05, RN-03/04 | Doble petición conserva un efecto; fallo deja ambas cuentas sin cambio | No ejecutado |
| TP-05 · Dinero y redondeo | RNF-02, RN-01 | Operaciones repetidas y límites respetan precisión elegida | Pendiente representación monetaria |
| TP-06 · Compra y pago de tarjeta | RN-06 | Compra 100 + pago 100 no produce gasto 200 | Pendiente modelo de crédito |
| TP-07 · Ahorro apartado | RF-08, RN-07 | Apartar 200 de 1,000 no produce total 1,200 | Pendiente modalidad de fondo |
| TP-08 · Aislamiento | RNF-01, RN-11, SEG-02 | A no opera recursos de B por API ni base de datos | No ejecutado; ver casos TS |
| TP-09 · Fechas y recurrencias | RF-10, RN-08 | Fin de mes, zona horaria y repetición siguen reglas acordadas | Pendiente alcance y reglas |
| TP-10 · Proyecciones y alertas | RF-11/12, RN-09/10 | Estimaciones reproducibles, datos insuficientes explícitos y avisos sin duplicar | Fase pendiente |
| TP-11 · UX y accesibilidad | RNF-04, RF-04/07 | Captura/consulta por teclado, errores comprensibles y estados completos | No ejecutado |
| TP-12 · Recuperación | RNF-06, SEG-10 | Migración y recuperación preservan integridad y aislamiento | No ejecutado |

## Datos y ejecución

Usar usuarios sintéticos A y B, al menos dos cuentas de A, una de B y datos de categorías/tarjetas de ambos. Incorporar movimientos con y sin categoría, montos límite, fechas limítrofes y solicitudes repetidas. Completar resultados numéricos esperados tras resolver reglas pendientes.

Cada ejecución registra tarea, versión, entorno, comando o procedimiento, resultado y evidencia. Los defectos incluyen pasos, esperado/observado, impacto y responsable. No registrar tokens, claves ni finanzas personales.

## Criterio de salida

Casos de aceptación del alcance implementado ejecutados; invariantes financieros y acceso cruzado comprobados; defectos críticos resueltos; limitaciones y áreas sin cobertura visibles. La validación documental de esta entrega no equivale a pasar estas pruebas de aplicación.
