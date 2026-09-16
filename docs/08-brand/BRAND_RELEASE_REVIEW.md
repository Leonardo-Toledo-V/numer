# T-BRAND-016 · Entrega para cierre de marca

Fecha: 2026-09-15. Responsable: brand-strategist. Estado: **terminada como candidata 1.0 RC1, pendiente de revisión creativa final**.

## Encargo

BR-C30: «Continuemos entonces», en respuesta a preparar variantes, revisar tamaños/márgenes y entregar el manual y paquete final para revisión. Autoriza producir esta entrega; no aprueba automáticamente sus propuestas.

- Objetivo observable: paquete autónomo, revisable y organizado con la identidad elegida, variantes de uso y manual de marca.
- Entradas: [contexto](../00-project/PROJECT_CONTEXT.md), [estado](../00-project/STATUS.md), [rol](../../agents/brand-strategist.md), [guía](BRAND_GUIDELINES.md), [voz](BRAND_VOICE.md), [alcance](BRAND_SCOPE_UPDATE.md) y paquete gráfico 0.1. Decisiones BR-A02/A03/A05/A06 y preferencias BR-C07, BR-C23 a BR-C29.
- Propiedad de escritura: únicamente `docs/08-brand/`, incluyendo herramientas locales de producción de activos y documentos. No se modifican otras especialidades ni Sites.
- Exclusiones: cambios al nombre/dibujos elegidos, UI nueva, backend/frontend, reglas financieras, despliegue, aprobación automática o investigación de disponibilidad comercial.
- Dependencias: ninguna para la preparación de marca. La aplicación requiere sus propias especificaciones y revisiones posteriores.
- Criterios de aceptación: variantes conservan geometría; tamaños inspeccionados; manual completo y legible; archivos agrupados con licencias e integridad; propuestas y aprobaciones separadas. Cumplidos dentro del alcance local.
- Validación: geometría XML y máscara; renderizado en Chrome 153.0.8010.36 a escala 1x; inspección visual de tamaños y siete páginas PDF; extracción de texto, fuentes incorporadas, formatos, enlaces e inventario SHA-256. [Resumen verificable](deliverables/numer-brand-kit-v1.0-rc1/verification.json).
- Decisiones pendientes: usuario revisa la candidata. No se presenta como versión 1.0 aprobada.
- Entregables: [paquete ZIP](deliverables/numer-brand-kit-v1.0-rc1.zip), [manual PDF](deliverables/numer-brand-kit-v1.0-rc1/guide/numer-brand-manual-v1.0-rc1.pdf), [manual editable](deliverables/numer-brand-kit-v1.0-rc1/guide/brand-manual.md) y [handoff autónomo](deliverables/numer-brand-kit-v1.0-rc1/guide/handoff.md).

## BR-R01 · Variantes producidas

Nombre y símbolo en petróleo, porcelana y grafito, en SVG y PNG transparente. Solo cambia la tinta, no el contorno ni la máscara. El archivo original petróleo, iconos, favicon y fuentes conservan sus bytes. No se añadieron marcas bancarias ni nuevos símbolos. Las tintas porcelana/grafito quedan propuestas para aplicación; no sustituyen la aprobación del dibujo original.

## BR-R02 · Escala revisada y regla propuesta

Nombre comprobado a 64/80/96/128 px de ancho de caja SVG, en fondo porcelana y petróleo. Se propone 96 px como tamaño habitual y 80 px como mínimo de referencia: el nombre conserva lectura, mientras el corte pierde presencia al reducir. Por debajo de 80 px se prefiere el icono. Icono revisado a 16/24/32/48 px, preservando su ocupación interna aprobada. [Comparación renderizada](assets/brand-review/size-review.png).

Área de protección propuesta: 0.5 h alrededor de los límites visibles de las letras. h=57 unidades en el SVG maestro; el espacio transparente de su viewBox no sustituye esa protección. No se fijan mínimos de impresión. La revisión local no acredita todas las densidades de pantalla.

## BR-R03 · Alcance del manual

Siete páginas: presentación, identidad/variantes, espacio/escala, color/tipografía, voz, cuentas/tarjetas/movimiento y revisión final. Manrope incrustada en el PDF. Los SVG editables se entregan por separado y siguen siendo maestros; el PDF usa representaciones raster de alta resolución para conservar la máscara de corte.

El manual mantiene una estructura de marca, no de especificación funcional. Distingue dinero propio, crédito y deuda; el registro de una tarjeta no exige número, titular, CVV ni vencimiento. GSAP o Motion quedan como alternativas futuras, sin implementación.

## Qué requiere el visto bueno final

Mensaje «Tus cuentas y tarjetas, en un mismo lugar», descriptor «Organizador de finanzas personales», voz, variantes nuevas, margen, mínimos, jerarquía de pesos de marca, usos y principios de movimiento. El nombre, logotipo y monograma ya elegidos no se reabren. Las medidas del sidebar, componentes, estados y accesibilidad completa siguen con UX/UI.

## Handoff · T-BRAND-016

- Fecha y destinatarios: 2026-09-15; usuario para revisión final; UX/UI mediante [handoff del paquete](deliverables/numer-brand-kit-v1.0-rc1/guide/handoff.md).
- Resultado real: entrega producida y comprobada como candidata, no 1.0 definitiva.
- Archivos: paquete `deliverables/numer-brand-kit-v1.0-rc1/` y ZIP, este registro, guía/índice/handoff actualizados, evidencias en `assets/brand-review/` y herramientas `tools/render-brand-review.cjs` / `tools/build-brand-manual.py`.
- Decisiones conservadas: BR-A02/A03/A05/A06. Encargo BR-C30 confirmado; BR-R01 a BR-R03 describen producción verificada y reglas propuestas con sus límites.
- Riesgos y límites: sin verificación de marca comercial, impresión o accesibilidad completa; no afirmar aplicación implementada o seguridad acreditada.
- Siguiente acción: usuario comenta o aprueba la entrega concreta; brand-strategist registra la decisión y prepara la edición 1.0 aprobada si corresponde. No se iniciaron otros agentes ni tareas de desarrollo.
