# SRS · Especificación inicial

Estado: requisitos detallados propuestos, pendientes de validación y diseño. Responsable: product-analyst.

El stack y la intención funcional proceden del usuario; los criterios siguientes son una elaboración para discusión. Los requisitos de fases futuras solo aplican al incorporarse su funcionalidad. No describen capacidades implementadas.

## Funcionales

| ID | Función | Criterio de aceptación propuesto | Relación |
|---|---|---|---|
| RF-01 | Acceso con Google | Tras acceso válido se consulta solo el espacio propio; cancelación/fallo permiten reintentar; sesión cerrada impide operaciones protegidas | F-01 |
| RF-02 | Cuentas | Crear y consultar cuenta con moneda y saldo inicial definidos; su representación no duplica movimientos ni agregados | F-02, RN-01 |
| RF-03 | Tarjetas | Registrar alias, tipo y datos mínimos; rechazar vínculo con cuenta ajena; no solicitar secretos bancarios | F-03, SEG-04 |
| RF-04 | Movimientos | Registrar importe, moneda, fecha, cuenta y tipo; gasto puede asociar categoría; entrada inválida no persiste cambios parciales | F-04, RN-01/02 |
| RF-05 | Transferencias | Mover 100 unidades de A a B reduce A en 100 y aumenta B en 100; no altera el patrimonio total ni el gasto; reintento no duplica | F-04, RN-03/04 |
| RF-06 | Categorías y análisis básico | Filtrar por periodo y categoría produce totales explicables por los movimientos elegibles; transferencias no inflan gasto | F-05, RN-05 |
| RF-07 | Dashboard e historial | Indicadores concuerdan con reglas de saldo; historial permite entender su origen y presenta estados vacíos y errores | F-06/07 |
| RF-08 | Ahorro | Registrar fondos según el modelo decidido; apartar dinero no crea patrimonio adicional; saldo disponible y apartado se distinguen | F-08, RN-07 |
| RF-09 | Presupuestos y metas | Periodo, categoría u objetivo y progreso tienen fórmula explícita y tratamiento definido de ajustes | F-09, fase posterior |
| RF-10 | Recurrencias y fechas | Una ocurrencia conserva fecha prevista y estado; regenerar el mismo periodo no duplica movimientos reales | F-10/14, RN-08 |
| RF-11 | Forecast | Mostrar proyección con fecha de cálculo, horizonte y supuestos; datos insuficientes producen estado explícito | F-13, RN-09 |
| RF-12 | Alertas | Una regla identifica condición, periodo y destinatario; repetir evaluación no genera avisos duplicados del mismo evento | F-11, RN-10 |

Edición, eliminación, devolución, conciliación, crédito avanzado e importación requieren criterios adicionales tras resolver las preguntas del PRD.

## No funcionales

| ID | Requisito propuesto | Evidencia requerida |
|---|---|---|
| RNF-01 | Aislamiento por usuario en lectura y escritura | Pruebas negativas de servidor y RLS, también en relaciones y agregados |
| RNF-02 | Cálculos monetarios exactos y repetibles | Casos de redondeo, acumulación y atomicidad con representación acordada |
| RNF-03 | Secretos protegidos y datos minimizados | Revisión de cliente, configuración, errores y logs |
| RNF-04 | Interfaz usable con teclado y tecnologías de asistencia | Criterios y pruebas de accesibilidad definidos por UX/QA |
| RNF-05 | Mantenibilidad y trazabilidad | Requisito → regla → contrato → implementación → prueba |
| RNF-06 | Recuperación y observabilidad | Procedimientos y evidencia de restauración en entorno no productivo |
| RNF-07 | Rendimiento adecuado al volumen previsto | Pendiente fijar volumen, percentil, latencia y medición; no tiene umbral aprobado |

## Restricciones y dependencias

Respetar DEC-001/002. No se fija versión de librerías. Moneda, fechas, modelo de saldo, eliminación y representación de deuda dependen de DEC-010/011. El [plan de pruebas](../06-testing/TEST_PLAN.md) enlaza escenarios con estos IDs; sus resultados actuales son no ejecutados.
