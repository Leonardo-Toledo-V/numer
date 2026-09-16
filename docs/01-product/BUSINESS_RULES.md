# Reglas financieras

Estado: propuestas para validación; no motor implementado. Responsable: product-analyst. Revisión: architect, backend y QA.

| ID | Regla propuesta | Ejemplo / decisión pendiente |
|---|---|---|
| RN-01 | Todo importe tiene moneda y representación exacta, con redondeo explícito | Elegir unidades menores enteras o decimal; no usar coma flotante binaria como base del cálculo monetario |
| RN-02 | Saldo inicial y movimientos explican el saldo registrado; una corrección conserva trazabilidad | Decidir saldo inicial como asiento o base separada; política de edición/reversión pendiente |
| RN-03 | Transferencia propia en igual moneda tiene dos efectos atómicos y total neto cero | A=1,000, B=200; transferir 100 deja A=900, B=300, total=1,200 |
| RN-04 | Reintentar una operación identificada no la duplica | Doble envío de RN-03 conserva total y una sola transferencia; definir alcance/vida de la clave |
| RN-05 | Agregados distinguen gasto, ingreso, transferencia y devolución | Transferencia no suma gasto; decidir imputación de devoluciones y comisiones |
| RN-06 | Compra a crédito y pago de tarjeta no duplican el gasto | Compra de 100 crea gasto/deuda; pago de 100 liquida deuda y reduce efectivo, sin otro gasto por la compra |
| RN-07 | Apartar ahorro no aumenta patrimonio | De 1,000 se apartan 200: total sigue 1,000; disponibilidad de 800 solo si ese modelo se acuerda |
| RN-08 | Fechas previstas y efectivas son distintas; ocurrencias recurrentes tienen identidad estable | Decidir zona horaria, fin de mes, días de corte/pago y confirmación de cobros |
| RN-09 | Proyección usa entradas y supuestos versionados y no modifica movimientos registrados | Saldo base + entradas previstas − salidas previstas; evitar contar compra y pago dos veces |
| RN-10 | Alerta identifica evento, regla, destinatario y periodo | Recalcular no emite repetidamente el mismo aviso; decidir caducidad y lectura |
| RN-11 | Relaciones financieras pertenecen al mismo usuario salvo futuro modelo compartido explícito | No vincular movimiento propio a cuenta, tarjeta, categoría o meta de otra persona |

## Límites por resolver

- Multimoneda: no sumar monedas diferentes sin regla explícita de conversión, fuente y fecha de tipo de cambio. Hasta resolverlo, los ejemplos son de una única moneda genérica.
- Transferencias con comisiones, intereses, mensualidades, pagos parciales y sobrepagos no tienen tratamiento definido.
- La política de eliminación, reversión, conciliación y retroactividad debe acordarse antes de exponer esas operaciones.
- Fondos y metas requieren distinguir propiedad real del dinero y asignaciones virtuales.

## Proyecciones propuestas en el chat

Se sugirió un motor determinista con saldo base, ingresos/gastos recurrentes, obligaciones y estimación de gasto variable; horizontes de 30/60/90 días, 6 y 12 meses y escenarios conservador, esperado y optimista. Son alternativas pendientes de alcance y calibración, no fórmulas aceptadas ni garantías.

Producto debe definir qué mide cada proyección (efectivo o patrimonio), cómo evita doble conteo de crédito, cómo trata datos insuficientes y cómo se explican sus supuestos. QA necesitará ejemplos calculables y resultados esperados antes de validar el motor.
