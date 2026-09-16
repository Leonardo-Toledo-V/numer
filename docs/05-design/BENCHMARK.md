# Numer · Benchmark y referencias de experiencia

2026-09-16 · UX/UI · T-UX-002 · Investigación documental, no prueba de los productos con cuentas reales. Selección por problemas compartidos con Numer, no ranking comercial. No se verificó toda la interfaz ni se midió usabilidad de los competidores.

## Matriz de evidencia → aplicación

| ID | Producto / fuente primaria consultada | Hecho documentado | Aplicación propuesta para Numer | Límite / qué no transferir |
|---|---|---|---|---|
| UX-B01 | [Monarch: cuentas manuales](https://help.monarch.com/hc/en-us/articles/360058187072-Manual-Accounts) | Distingue cuentas manuales y permite introducir transacciones desde cuenta o historial. | Captura contextual con cuenta preseleccionada y visible; indicar origen/fecha del dato. | No asumir conexión bancaria ni su política de actualización de saldo. |
| UX-B02 | [Monarch: transacciones manuales](https://help.monarch.com/hc/en-us/articles/360058441811-Creating-Manual-Transactions) | El efecto en saldo depende del tipo de cuenta; el artículo advierte que un registro manual y otro importado pueden coexistir. | Revisión con efecto claro y estados de resultado incierto; si hay importación, diseñar conciliación/duplicados antes de exponerla. | No copiar un interruptor «afectar saldo» sin modelo financiero acordado. |
| UX-B03 | [YNAB: pagos de tarjeta](https://support.ynab.com/en_us/credit-card-payments-a-guide-r1_506Q1j) | Separa registro de pago de tarjeta, dinero reservado para pagarlo y fechas previstas. | Nombrar la acción «Registrar pago»; mostrar dinero propio y crédito con etiquetas distintas; dar a fechas una sección explícita. | Su método de asignación presupuestaria no define las reglas de Numer. |
| UX-B04 | [YNAB: manejo de tarjetas](https://support.ynab.com/en_us/handling-credit-cards-overview-ry7cNub1s) | Explica la relación entre compra, categoría y reserva destinada al pago dentro de su modelo. | En revisión, explicar compra versus pago y enlazar los hechos registrados. | No adoptar reserva automática ni método de sobres sin decisión de producto. |
| UX-B05 | [Lunch Money: recurrentes](https://lunchmoney.app/features/recurring-expenses/) | Documenta periodicidades, inicio/fin, estado, asociación con transacciones y proyección por rango de fechas. | Separar previsto/registrado y permitir consultar el hecho vinculado; explicitar fechas y supuestos. | Marketing de una funcionalidad no acredita precisión ni demuestra la mejor UX; no implica recurrencias en MVP. |
| UX-B06 | [Apple HIG: sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) y [tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) | Recomienda navegación adaptada al espacio y distingue destinos de acciones. | Cuatro destinos estables; Registrar como acción; detalles dentro de cada sección. | HIG es guía para plataformas Apple; Numer es web. No se traslada Liquid Glass ni se cambia Manrope o petróleo. |
| UX-B07 | [W3C: tamaño mínimo](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [ampliado](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced) | WCAG 2.2 AA establece 24 CSS px con excepciones; el criterio ampliado establece 44 CSS px con excepciones. | Mantener 44 × 44 como objetivo interno de controles principales y medir áreas reales. | No afirmar que 44 es el mínimo AA universal ni conformidad por revisar una maqueta. |
| UX-B08 | [W3C: prevención de errores](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data) | Para los casos aplicables ofrece mecanismos de reversión, comprobación o revisión/confirmación. | Revisión estructurada en transferencias/pagos; errores corregibles antes de enviar. | No afirmar que todo clic financiero exige un modal. Reversión depende del contrato. |

Fuentes consultadas el 2026-09-16. Publicación/actualización visible: Monarch manual accounts y transacciones 2026-03-16; YNAB pagos 2026-08-20 y tarjetas 2026-09-02; HIG sidebars/tab bars 2026-06-08. Lunch Money no indica fecha editorial en la página consultada. Las conclusiones para Numer son inferencias del análisis UX, no resultados publicados por esas fuentes.

## Oportunidad de Numer

**Hipótesis UX-H01:** claridad de varias tarjetas y sus obligaciones, con captura breve y trazabilidad del dinero, puede ser más útil para este encargo que añadir más métricas al resumen. Verificar con tareas, no con preferencia estética únicamente.

| Antes, observado en maquetas | Después, propuesto | Motivo / prueba |
|---|---|---|
| Resumen de una sola tarjeta | Lista plural de tarjetas con banco + alias y detalle propio | UX-B03/04; encontrar dos tarjetas del mismo banco sin número |
| Datos de revisión en párrafo | Importe/moneda, origen, destino, fecha y efecto separados | Reducir errores de lectura; UX-C05/06 |
| Totales globales sobre lista filtrada | Etiqueta de ámbito y número de resultados | UX-C09: explicar a qué se refiere cada cifra |
| Formularios genéricos | Campos por operación; cuenta contextual visible | UX-B01/02; comparar errores y esfuerzo de captura |
| Sin estado incierto definido | Mensaje de estado y consultar/reintentar la misma operación | UX-C08; evitar crear un registro nuevo por incertidumbre |
| Cabecera móvil alta | Mantener navegación visible, evaluar compactación sin perder blancos | UX-B06/07; prueba de primer clic y lectura a 320 px |

No se usan puntuaciones inventadas de competidores. Antes de congelar diseño, probar comprensión y finalización con personas del público elegido; el benchmark no sustituye esa evidencia.
