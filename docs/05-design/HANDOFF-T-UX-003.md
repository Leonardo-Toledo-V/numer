# Handoff · T-UX-003 · UX/UI

**Revisión vigente: UX-DC01 v0.3 / UX-FB03.** Sidebar valorado favorablemente; textos/columnas revisados y privacidad/configuración trasladados al menú del perfil inferior izquierdo. C04 añade estado abierto. Fuentes de la nueva interacción: documentación oficial de Dropdown Menu referenciada en COMPACT_DESIGN. No hay aceptación tipográfica nueva ni pruebas de comportamiento. Ver [entrega por etapas a frontend](UX_TO_FRONTEND.md); exclusivamente otro responsable implementa.

Se conservó v0.2 en `assets/ux-003/revisions/0.2/` y su informe histórico. Generador/render estáticos actualizados; cuatro láminas vigentes y registro de revisión actualizado. Informe vigente verifica tipografía y líneas base, además de geometría. Las notas siguientes documentan la entrega inicial y v0.2; la instrucción v0.3 prevalece.

2026-09-16 · Responsable UX/UI · Destinatarios: usuario, producto y orquestador; posteriormente frontend/QA. No se enviaron mensajes ni se asignaron tareas a otros agentes.

## Resultado

Propuesta UX-DC01 v0.2 lista para revisión de diseño: cuentas en listas comparables, captura contextual en diálogo compacto y adaptación móvil. **No aprobada globalmente ni implementada.** Identidad conservada; no se usó Figma.

Actualización UX-FB02: comentario favorable parcial del usuario a la densidad; instrucción expresa de sidebar rectangular, al borde izquierdo, más estrecho y área derecha blanca. C01/C02 actualizados con ancho propuesto 176 px, radio exterior 0, sin márgenes y fondo blanco. Selección interna 38/8 conservada. C03 no cambia. Los archivos previos de C01/C02 y vista conjunta están en `assets/ux-003/revisions/0.1/`; informe original conservado como `verification/T-UX-003-v0.1.json`. El informe vigente verifica geometría y color de v0.2; sigue sin acreditar comprensión o aceptación global.

UX-R01 confirma un límite permanente: este agente **nunca modifica frontend**. Diseña, investiga, especifica, recomienda y revisa. No interpretar la aceptación de sus documentos como autorización para ejecutar frontend.

## Artefactos y aceptación documental

| Criterio | Evidencia / estado |
|---|---|
| UX3-AC01 | UX-R01 en README, UX-FEEDBACK-001 y tarea. Registrado. |
| UX3-AC02 | COMPACT_DESIGN: fuentes primarias Table/Field/Input/Dialog/Sheet y tabla antes/después. Realizado. |
| UX3-AC03 | C01/C02 desktop y C03 móvil, SVG/PNG en assets/ux-003. Dibujados e inspeccionados. |
| UX3-AC04 | COMPACT_DESIGN: ocho contratos de interacción, estados/adaptación y dependencias de producto. Propuestos. |
| UX3-AC05 | verification/T-UX-003.json: integridad, contraste y alcance visual. No acredita usabilidad. |
| UX3-AC06 | REVIEW-UX-003 contiene guion/registro sin resultados inventados; este handoff. Preparado. |

Archivos nuevos: COMPACT_DESIGN.md, T-UX-003.md, REVIEW-UX-003.md, este handoff, assets/ux-003 con tres SVG/tres PNG/vista conjunta/manifiesto, herramientas de generación/render estáticos e informe de verificación. Archivos actualizados: README, UX-FEEDBACK-001 y DESIGN_SYSTEM para estado y límites. No se modificaron fichas de otros roles ni fuentes de producto/marca/estado global.

## Cambios de dirección

W01–W10 siguen rechazados en composición. C01–C03 los suceden únicamente como nueva propuesta focalizada. Títulos/campos/controles reducen peso visual; listas sustituyen tarjetas grandes; destino contextual visible evita un selector redundante. La aprobación de sidebar UX-A01 se mantiene. El resto de dimensiones sigue propuesto y no se incorpora a tokens globales como decisión aprobada.

Fuentes: [contrato y láminas](COMPACT_DESIGN.md), [restricciones](UX-FEEDBACK-001.md), [pendientes financieros](UX_REVIEW.md). Las medidas de Numer no se presentan como defaults universales de shadcn/ui. No se eligieron nuevas librerías.

## Verificación y límites

Tres láminas renderizadas con Sharp del runtime e inspeccionadas a tamaño de referencia. Se refinó la separación de grupos del diálogo para evitar tanto espacio vacío como etiquetas amontonadas. Wordmark original incrustado sin cambios. Manrope local. Comprobación de límites de texto, dimensiones, enlaces y pares de contraste en el informe.

Los scripts de `tools/` generan exclusivamente documentos visuales SVG/PNG dentro de `docs/05-design/assets/ux-003`; no son componentes, páginas ni prototipo web. Rutas de runtime en el render corresponden a esta máquina, no a dependencias del producto.

No verificado: aceptación del usuario, comprensión con participantes, teclado/lector real, zoom/reflow, móvil con teclado, funcionamiento de controles, autenticación, seguridad o cálculos. C03 es formulario móvil; no cubre todavía la adaptación de C01. El estado de revisión está documentado pero no dibujado en una nueva lámina completa.

## Siguiente responsable y acción

1. **Usuario + UX/UI:** evaluar densidad/jerarquía y tareas de REVIEW-UX-003. Registrar respuestas; corregir esta muestra antes de ampliar.
2. **Producto:** cerrar UX-P01–08 y reglas relevantes antes de completar alta financiera, deuda/corte/meses y ahorro. La muestra no resuelve esos pendientes.
3. **UX/UI:** tras esa evidencia, extender el patrón a detalle de tarjeta, revisión de pago y movimientos, manteniendo estados y adaptación.
4. **Orquestador/frontend:** cuando corresponda, convertir especificaciones aceptadas en tareas de implementación a cargo de frontend. UX/UI solo recomienda y revisa. QA verifica comportamiento en la implementación del responsable.
