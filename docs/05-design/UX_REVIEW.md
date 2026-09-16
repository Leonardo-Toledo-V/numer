# Numer · Revisión UX/UI de maquetas

Versión 0.1 · 2026-09-16 · Responsable: ux-ui · [T-UX-001](T-UX-001.md).

Actualización T-UX-002: la recomendación de selección de escritorio fue aprobada como UX-A01 el 2026-09-16; ver DESIGN_SYSTEM. Los hallazgos inferiores conservan el contexto de la revisión inicial.

Estado: análisis realizado; resto de recomendaciones de experiencia propuestas. Identidad Numer 1.0 aprobada; esa decisión no aprueba todos los recorridos y tokens de interfaz.

## Vigencia de las fuentes

Aplicar [BR-A08/entrega final](../08-brand/BRAND_FINAL.md), maestros del [paquete 1.0](../08-brand/deliverables/numer-brand-kit-v1.0/README.md) y [manual editable](../08-brand/deliverables/numer-brand-kit-v1.0/guide/brand-manual.md). Conservar logo original con corte, símbolo independiente, Manrope, petróleo/porcelana/grafito/niebla y voz clara, calmada y cercana. El encargo actual confirma ajustar altura y radio de selección, manteniendo redondeado moderado según BR-C23/25.

Los apartados históricos que dicen «voz pendiente» o «variantes pendientes» no reabren BR-A07/A08. El contexto global del 14 de septiembre tampoco revoca el cierre especializado del día 15. Se informa al orquestador sin modificar sus fuentes ni los documentos de marca.

BR-C26/27/28 en [alcance confirmado](../08-brand/BRAND_SCOPE_UPDATE.md) incluyen varias cuentas/tarjetas, exclusión de datos identificativos y seguimiento de deuda, meses, crédito, corte y pago. F-03, Q-05 y RF-03 aún reflejan un alcance anterior: producto debe actualizar esas fuentes antes de propagarlas a una SPEC. La profundidad financiera está solicitada; su fase y reglas siguen pendientes. «Conjunta» no confirma acceso compartido. MXN y las fechas de septiembre son datos sintéticos.

## Inventario inspeccionado

| Muestra | Evidencia leída visualmente | Cobertura real |
|---|---|---|
| Resumen T-BRAND-011 | [Escritorio claro](../08-brand/assets/financial-overview/desktop-light.png), [oscuro](../08-brand/assets/financial-overview/desktop-dark.png), [móvil claro](../08-brand/assets/financial-overview/mobile-light.png), [oscuro](../08-brand/assets/financial-overview/mobile-dark.png) | Cuentas, gastos, ahorro, deuda y movimientos. Sidebar anterior excluido de BR-A06. |
| Movimientos T-BRAND-012 | [Escritorio claro](../08-brand/assets/movements/desktop-light.png), [oscuro](../08-brand/assets/movements/desktop-dark.png), [móvil claro](../08-brand/assets/movements/mobile-light.png), [oscuro](../08-brand/assets/movements/mobile-dark.png) | Sidebar petróleo, historial, tipos, tema y ocultado. |
| Captura/revisión | [Formulario móvil](../08-brand/assets/movements/mobile-form.png), [revisión](../08-brand/assets/movements/capture-preview.png) | Captura de transferencia y revisión sin guardado; no prueban recuperación/persistencia. |
| Fuente conservada | [HTML de la maqueta](../08-brand/sites/numer-movements/dist/index.html), `.navigation button` y `navigate` | Valores CSS y reutilización del resumen en cuentas/ahorro. Leído, sin modificaciones. |

Las interacciones descritas en [Navegación y movimientos](../08-brand/NAVIGATION_MOVEMENTS.md) y [Resumen](../08-brand/UI_EXPLORATION.md) son evidencia previa de marca; esta revisión no vuelve a acreditar esas pruebas de navegador.

## Hallazgos

| ID | Observación | Acción propuesta |
|---|---|---|
| UX-O01 | Jerarquía del resumen y sidebar petróleo aportan continuidad visual. | Conservar composición, tipografía e iconos de línea; ajustar solo selección. No recuperar sidebar gris descartado. |
| UX-O02 | Activo: mínimo CSS 46 px, padding vertical 13 px, radios 12/20/12/12. | Reducir superficie a 38 px y radio uniforme 8 px, dentro de interacción de 44 px. El mínimo CSS no equivale a una medición en todo navegador. |
| UX-O03 | Deuda y ahorro incluido en cuentas ya están diferenciados, pero solo aparece una tarjeta. | Ampliar a varias tarjetas con banco/alias propuesto; faltan crédito total/usado/disponible, meses y pago del periodo. |
| UX-O04 | Cuentas y Ahorro reutilizan partes del resumen. | Diseñar listas, alta, detalle y estados propios. La meta ilustrativa no confirma metas en lanzamiento. |
| UX-O05 | Totales del periodo no cambian al filtrar historial. | Rótulo persistente «Totales del periodo · sin filtros» y «N movimientos filtrados». Periodo común a ambos ámbitos. Confirmar UX-P09. |
| UX-O06 | Registrar acaba en vista previa; revisión concatena datos en un párrafo. | Revisión por etiqueta/valor y estados pendiente/confirmado/incierto. Compra a crédito necesita rama propia. |
| UX-O07 | Cabecera móvil ocupa aproximadamente 185 px en captura de 392 px de ancho. | Probar selección móvil de 48 px dentro de fila de 52 px; conservar etiquetas, revisar 320 px/zoom/teclado virtual. |
| UX-O08 | Sin evidencia de acceso, onboarding, error de servidor, sesión vencida o deuda desconocida. | Diferenciar ausencia de datos de cero. Capturas no prueban foco, lector de pantalla o altura móvil reducida. |

## Decisiones pendientes de producto

P0 bloquea la SPEC del recorrido afectado; P1 debe resolverse antes de su diseño definitivo. Se registran preguntas para producto, no solicitudes de autorización para esta entrega.

| ID / prioridad | Pregunta y recomendación | Fuente | Responsable / efecto |
|---|---|---|---|
| UX-P01 · P0 | ¿Solo registro, sin custodia o ejecución de pagos? Recomendación: confirmar ese límite. | Q-01, DEC-005 | Producto + usuario; alcance y lenguaje «Registrar pago». |
| UX-P02 · P0 | ¿Uso propio o abierto a usuarios independientes? ¿Compartir datos? No inferirlo de «conjunta». | Q-02, DEC-013, BR-C26 | Producto + usuario; acceso y permisos. |
| UX-P03 · P0 | ¿Moneda(s), idioma, zona horaria, fecha efectiva y agregados multimoneda? | Q-03, DEC-010, RN-01/08 | Producto; formatos/campos/totales. No fijar MXN por la muestra. |
| UX-P04 · P0 | ¿Registro manual, importación o ambos? ¿Saldo/deuda inicial con qué fecha y fuente? Manual primero es recomendación. | Q-04, RF-02/04, RN-02 | Producto; onboarding, historial y conciliación. |
| UX-P05 · P0 | ¿Tipos y relación cuenta/tarjeta? ¿Alias obligatorio cuando hay varias del mismo banco? Recomendación: banco + alias y recurso neutro si falta icono. | BR-C26/27, RF-02/03 | Producto; identificación sin número/titular/vencimiento. |
| UX-P06 · P0 | ¿Definición de deuda total/utilizada/al corte y pago del periodo? ¿Qué se captura/calcula? ¿Parciales, sobrepagos, comisiones/intereses y meses? | BR-C28, Q-05, RN-06 | Producto; efectos/cuotas. No volver a preguntar si se quiere deuda: precisar reglas y fase. |
| UX-P07 · P0 | ¿Corte/pago como fechas o periodos? ¿Fin de mes, compra cercana al corte y pago tardío? | BR-C28, RN-08 | Producto; calendario y alertas. |
| UX-P08 · P1 | ¿Ahorro como cuenta, apartado o ambos? ¿Metas desde lanzamiento? | Q-06, RN-07 | Producto; aportación, retiro, disponibilidad y doble conteo. |
| UX-P09 · P1 | ¿Filtros afectan filas o también totales? ¿Agregados/orden? Recomendar ámbitos explícitos de periodo y resultados. | RF-06/07, RN-05, BR-UI05 | Producto + UX; historial y fuentes del resumen. |
| UX-P10 · P0 para correcciones | ¿Edición, archivo, borrado, devolución y retroactividad? ¿Efectos sobre cuotas/periodos? | Q-08, RN-02/05/06 | Producto; bloquea esas acciones, no consulta. |
| UX-P11 · P1 | ¿Alertas/proyecciones al lanzamiento? ¿Canales, horizontes, supuestos, datos mínimos? ¿Recurrencias, metas y presupuestos? | Q-07/09, RF-09/10/11/12 | Producto + usuario; fase y navegación. Intención confirmada no fija todas las variantes. |
| UX-P12 · P1 | ¿Preferencias persistentes, ocultado entre sesiones, exportación, eliminación de cuenta y MFA? | Q-10, F-15, DEC-012 | Producto + seguridad; ajustes/sesión. |

## Secuencia recomendada

1. Producto integra BR-C26/27/28 en PRD/SRS y resuelve P0; orquestador fija primera entrega y SPEC.
2. UX/UI dibuja acceso → primera cuenta/tarjeta → primer movimiento con estados UX-E01 a UX-E10.
3. UX/UI desarrolla tarjeta → deuda/meses/corte → registrar pago y después resumen/historial con fuentes coherentes.
4. Ahorro, alertas y proyecciones se detallan en la fase confirmada. Permanecen en el inventario sin crear destinos vacíos en el sidebar.

La propuesta de selección puede revisarse ahora sin resolver fórmulas. Próximo responsable del alcance: product-analyst. Siguiente entrega UX: wireframes de recorridos priorizados.
