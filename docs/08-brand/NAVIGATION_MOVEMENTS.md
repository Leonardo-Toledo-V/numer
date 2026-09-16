# Numer · Navegación y movimientos

Fecha: 2026-09-14. Responsable: brand-strategist. Estado: muestra visual propuesta, pendiente de revisión del usuario.

### Actualización del 2026-09-15 · BR-C23

El usuario considera que el sidebar se acerca más a la personalidad buscada, pero pide una selección menos redonda y posiblemente menos alta: «no me gusta que sea muy redondo el selected […] quizás menos alto». Propone considerar esta versión una maqueta provisional y ajustar durante UX/UI y frontend. Se registra como orientación confirmada, no como aprobación definitiva de la navegación. Recomendación: conservar la muestra y concretar altura, radios, foco y área táctil al especificar el componente, antes de implementarlo. No se modificó la maqueta en esta entrega.

### BR-C25 · Aclaración sobre redondeado

El 2026-09-15 el usuario condiciona quitar redondez a la referencia de Apple: «Si lo usa no lo quites, si no lo usa entonces hay que reducirle». La fuente oficial [Build a SwiftUI app with the new design, WWDC25](https://developer.apple.com/videos/play/wwdc2025/323/) describe botones de cápsula y controles pequeños/medianos de macOS con rectángulos redondeados. Apple sí utiliza redondeado y adapta la forma al contexto.

Aplicación de la instrucción: conservar las esquinas redondeadas; no realizar una reducción general ni editar la maqueta publicada por esta duda. BR-C23 permanece como observación localizada sobre altura y forma del estado activo, para evaluar con UX/UI. No se interpreta la referencia a Apple como aprobación de los radios actuales ni como un valor universal de radio. Consulta de la fuente: 2026-09-15.

## Decisiones y encargo

**BR-A06 · Base visual del resumen aceptada.** Responsable de aprobación: usuario. Fecha: 2026-09-14. Evidencia: «Excelente, me gustó el diseño. Aunque el sidebar no me gustó tanto, se me hace muy simple y muy genérico». Se conserva la dirección visual de T-BRAND-011 para continuar. El sidebar anterior queda expresamente excluido; esta aceptación no cierra todos los componentes, estados, reglas financieras o requisitos de accesibilidad.

**BR-C22 · Continuar navegación y movimientos.** Confirmado por el usuario: «Excelente, continuemos con lo que siga», tras la propuesta de trabajar la navegación y la pantalla de movimientos. Se desarrolla una muestra reversible, sin aplicación, persistencia o despliegue.

## BR-UI04 · Navegación propuesta

Bloque independiente en petróleo, con esquinas de 24 px, logotipo claro y monograma aprobado. Selección con superficie niebla y una esquina superior derecha más abierta; iconos de línea acompañados por texto. Los accesos de apariencia y privacidad se sitúan en la parte inferior, separados de las secciones financieras.

En escritorio el bloque lateral ocupa 198 px dentro de una columna de 214 px. En móvil se transforma en cabecera con cuatro accesos etiquetados. La selección tiene texto, icono y fondo: no depende únicamente de color. Conserva el orden Resumen, Movimientos, Cuentas y Ahorro. Cuentas y Ahorro reutilizan secciones de la muestra anterior para evaluar navegación; no son módulos completos.

Color principal del bloque: `#164E4A` en claro y `#153C39` en oscuro; texto `#F5F6F7`, secundario `#C4DCD8`, selección `#E1E8E7` / `#D1E6E0` con texto `#164E4A`. Se ofrece una alternativa grafito mineral y dos densidades de filas mediante los controles de diseño del entorno. Ninguna variante está aprobada todavía.

## BR-UI05 · Historial propuesto

El resumen superior conserva totales del periodo completo, rotulados como tales; el filtro solo cambia las filas del historial. Se agrupan por intervalos de fecha, en orden descendente. Cada fila muestra concepto, fecha, cuenta, importe y tipo; el detalle añade categoría, destino cuando corresponde y explicación del efecto financiero.

Se completa el conjunto sintético de T-BRAND-011 con diez movimientos: siete gastos por $6,380.50, un ingreso de $18,000.00, una transferencia interna de $2,000.00 y un pago de deuda de $300.00. El dinero ahorrado y los saldos del resumen se conservan. Todo el ejemplo usa MXN y fechas de septiembre de 2026; no son decisiones definitivas de moneda o calendario.

El filtro de devoluciones presenta un estado vacío. No añade operaciones de devolución ni fija su tratamiento contable. Ocultar importes enmascara resumen, filas y detalles; las barras de las vistas de resumen también se ocultan. La navegación, el tema y los filtros son locales a la muestra.

## BR-UI06 · Captura y revisión propuestas

Registrar abre un diálogo con tipo, concepto, importe en MXN, fecha y cuenta. Gasto e ingreso muestran categoría; transferencia y pago de deuda muestran origen y destino. Los destinos del pago son tarjetas, no cuentas de efectivo. Campos con etiquetas visibles, orden natural de foco y controles nativos.

Revisar presenta los datos capturados y permite volver conservándolos. En esta exploración se valida presencia de campos obligatorios, importe positivo con hasta dos decimales y cuentas distintas para una transferencia. El máximo de importe de $999,999.99 es una restricción local de la muestra, no una regla aprobada del producto. El botón final cierra la vista previa; no guarda ni altera historial o saldos. La muestra declara este límite antes de revisar.

La definición de guardado, errores de servidor, reintentos, edición, borrado, devoluciones, comisiones y fechas requiere producto y UX/UI. Los textos de efecto usan las distinciones propuestas en RN-03, RN-05, RN-06 y RN-07; no promueven esas reglas a aprobación.

## Evidencia

- [Escritorio claro](assets/movements/desktop-light.png) y [oscuro](assets/movements/desktop-dark.png).
- [Móvil claro](assets/movements/mobile-light.png), [oscuro](assets/movements/mobile-dark.png) y [captura móvil](assets/movements/mobile-form.png).
- [Revisión de captura](assets/movements/capture-preview.png) y [verificación](assets/movements/verification.json).

Chrome 153.0.8010.36: sin errores de JavaScript ni desbordamiento horizontal a 1024, 360 y 320 px. Se verificaron navegación entre las cuatro vistas, filtro de transferencias, estado vacío, detalle, Escape, privacidad en filas y detalle, error por origen/destino iguales, revisión y conservación de campos. El historial continúa con diez filas tras la vista previa. Cuatro iconos de navegación renderizados. Revisión visual de escritorio, móvil y formulario; se apiló importe/fecha en móvil para evitar truncar la fecha.

No verificado: auditoría completa de accesibilidad, lectores de pantalla, otros navegadores, guardado, seguridad o reglas de producción. Los controles opcionales del entorno no se probaron dentro de la aplicación anfitriona. No se declara conformidad WCAG ni aplicación implementada.

## T-BRAND-012 · Nueva navegación y pantalla de movimientos

- Estado: terminada como entrega de muestra; revisión de diseño pendiente.
- Responsable: brand-strategist. Revisor de dirección: usuario. Destinatario posterior: UX/UI.
- Objetivo observable: evaluar una navegación con mayor presencia de marca y aplicar la base visual aceptada al historial y una primera captura.
- Entradas: BR-A06, BR-C22, [guía](BRAND_GUIDELINES.md), [muestra anterior](UI_EXPLORATION.md), [contexto](../00-project/PROJECT_CONTEXT.md), [estado](../00-project/STATUS.md), [rol de marca](../../agents/brand-strategist.md), [rol UX/UI](../../agents/ux-ui.md), [reglas financieras](../01-product/BUSINESS_RULES.md), [glosario](../01-product/DOMAIN_GLOSSARY.md), [flujos](../05-design/USER_FLOWS.md), [decisiones](../00-project/DECISIONS.md). Referencias: RF-03/04/05/06/07/08 y RN-03/05/06/07, conservando su estado de propuesta.
- Alcance y propiedad: documentación y capturas en `docs/08-brand/`; muestra interactiva en la conversación. Sin escrituras en archivos de otros roles.
- Exclusiones: módulos completos, motor financiero, autenticación, persistencia, edición/eliminación, cambios al logotipo y despliegue.
- Dependencias: identidad elegida disponible. Reglas de producto sin cerrar permiten la exploración pero bloquean una especificación lista para implementar.
- Criterios de aceptación: conservar dirección elegida; diferenciar sidebar; historial coherente; navegación y captura local revisables; adaptación móvil. Cumplidos como muestra.
- Validación: navegador, capturas y comprobaciones descritas arriba, con alcance limitado.
- Decisiones pendientes: usuario revisa BR-UI04 a BR-UI06; producto y UX/UI definen comportamiento final.
- Entregables: muestra en la conversación, este documento, capturas, verificación y actualizaciones de índice/guía/handoff.

## Handoff · T-BRAND-012

- Fecha, responsable y destinatarios: 2026-09-14; brand-strategist; usuario, UX/UI y orquestador mediante documento local.
- Resultado real: nueva propuesta de navegación e historial con captura de revisión, comprobada en navegador. Sin aplicación implementada.
- Archivos: `NAVIGATION_MOVEMENTS.md`, `assets/movements/`, `UI_EXPLORATION.md`, `BRAND_GUIDELINES.md`, `BRAND_HANDOFF.md` y `README.md`; muestra en la conversación.
- Aprobado: BR-A06, con alcance y evidencia arriba. Confirmado: BR-C22. Propuesto: BR-UI04, BR-UI05 y BR-UI06.
- Validación y limitaciones: sección Evidencia. Las capturas de datos son ficticias y no acreditan seguridad o reglas financieras.
- Revisión requerida: personalidad y peso visual del sidebar; claridad del historial y campos de captura.
- Siguiente acción: usuario revisa esta muestra; brand-strategist ajusta la dirección y entrega las decisiones seleccionadas a UX/UI para especificación de componentes y estados.
