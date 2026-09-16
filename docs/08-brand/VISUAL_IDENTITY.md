# Numer · logotipo y tipografía

Estado: logotipo BR-A03 y monograma BR-A05 aprobados; identidad básica consolidada en BRAND_GUIDELINES 0.1. Sistema de interfaz pendiente. Fecha: 2026-09-13. Responsable: brand-strategist.

## Confirmado

- BR-A05: el usuario aprueba el monograma mostrado en T-BRAND-009: «Es perfecto. Me encantó. Ahora que procede?». Fecha: 2026-09-13. Abarca silueta continua, remate extendido y escala/tratamiento del icono presentado. Detalle en [FAVICONS](FAVICONS.md) y entrega en [BRAND_GUIDELINES](BRAND_GUIDELINES.md).

- BR-C20: el usuario pide reducir la escala según las imágenes de Nu/Revolut que aporta y diseñar una inicial con más carácter; considera la letra con corte básica y vacía. Sustituye el tamaño BR-C19 y el tratamiento anterior del icono, sin retirar explícitamente el nombre dibujado BR-A03. Evidencia y propuesta BR-V13 en [FAVICONS](FAVICONS.md), T-BRAND-009.

- BR-A04 / BR-C19: el usuario elige la letra y pide que abarque aproximadamente el 80% del recuadro. Evidencia: «No, yo creo que mejor si con la letra. Que abarque un 80% del recuadro, que no sea chiquita». Se usa n minúscula por BR-C16. Fecha: 2026-09-13; responsable de elección: usuario. Aplicación, convención de medida y validación en [FAVICONS](FAVICONS.md), T-BRAND-008. Supera la exploración de cuatro símbolos de BR-C18.

- BR-C18: «No, pero mejora otros, dame 4 propuestas de favicons». Corrige la conclusión del asistente de retomar automáticamente la n tras BR-C17. Se mantiene abierta la exploración de símbolo y se entregan cuatro alternativas en [FAVICONS](FAVICONS.md), T-BRAND-007. Toda mención anterior a consolidar la n se conserva como interpretación histórica superada, no como decisión del usuario.

- BR-C17: el usuario descarta ambos símbolos conceptuales. Evidencia del 2026-09-13: «Ninguno me gustó. El A se ve genérico, y el B me figura al logo de DiDi». A/Distribución se percibe genérico y B/Reserva evoca DiDi para el usuario; no se presenta esta asociación como estudio de similitud ni conclusión marcaria. Se retoma el respaldo n minúscula indicado en BR-C16; no se infiere aprobación de nuevas variantes ni de un paquete final de favicon.
- BR-A03: el usuario acepta el nombre dibujado B refinado: Manrope Semibold, minúsculas y corte diagonal. Evidencia del 2026-09-13: «Me encanta, se ve excelente. Ahora para el símbolo tiene que ser en minúscula igual. Aunque de logo preferiría algun diseño y no solo la letra». Responsable de aprobación: usuario. Se conserva la [versión mostrada con corte sutil](assets/logo-refinement/numer-b1-soft-wordmark.svg); no se infiere una elección de la variante abierta ni un sistema tipográfico completo.
- BR-C16: explorar un símbolo relacionado con la propuesta financiera, apto para futuro favicon. La N mayúscula queda retirada; si se utiliza una inicial, debe ser n minúscula. Evidencia de la misma respuesta: «Algo referente a mi propuesta. Eso para que funcione de favicon a futuro igual, si no me gusta nada entonces dejamos la "n" pero en minúscula». El fallback es condicional; no se lo selecciona automáticamente.
- BR-A02: Numer es el nombre elegido. Evidencia en [NAMING](NAMING.md).
- BR-C07: Petróleo mineral es la dirección cromática preferida: porcelana `#F5F6F7`, grafito `#222629`, petróleo `#185B56` y niebla `#E1E8E7`. No equivale a un sistema completo de color.
- BR-C14: el usuario solicita continuar con logotipo y tipografía y reitera la referencia Apple: «Recuerda que el diseño de Apple me gusta, por consecuente su tipografía». En ese momento no seleccionaba una familia concreta.
- BR-C15: preferencia explícita por la suavidad de B y Manrope; rechazo del icono n minúscula anterior y solicitud de explorar mayor peso y un corte. Evidencia del 2026-09-13: «Me gusta la suavidad de B, manrope. Pero no me gusta el icono de la n en minuscula, quizás si se hace un poco más grueso el nombre y si se añade algun detalle como el corte diagonal de A me gustaría más». Confirma la dirección a refinar, no los dibujos nuevos ni los pesos de toda la interfaz.

## T-BRAND-004 · Dos rutas de logo y tipografía

- Estado: comparación completada; dirección B/Manrope preferida mediante BR-C15. Continúa en T-BRAND-005.
- Responsable: brand-strategist. Revisor de dirección: usuario. Futuro consumidor: UX/UI.
- Objetivo: comparar dos rutas de logotipo, monograma y tipografía aplicadas a importes y texto.
- Entradas: BR-A02, BR-C07, BR-C14, brief de marca y [handoff](BRAND_HANDOFF.md).
- Alcance: `docs/08-brand/`, fuentes abiertas para la exploración y muestra en la conversación. No se inicializa aplicación.
- Exclusiones: logo final aprobado, registro de marca, despliegue, código de aplicación y selección de reglas financieras.
- Dependencias: selección visual del usuario; disponibilidad comercial del nombre pendiente, sin impedir esta exploración reversible.
- Criterios de aceptación: dos rutas visualmente distintas; archivos vectoriales; fuentes reales identificadas y licencias conservadas; prueba de reducción, temas claro/oscuro e importes; no confundir inspiración Apple con uso irrestricto de sus fuentes descargables.
- Validación: inspección en Chrome temporal, carga de fuentes, límites de SVG, desbordamiento, cifras tabulares y cambio de color. Detalle abajo.
- BR-Q04 resuelta como dirección a profundizar: B/Manrope mediante BR-C15; el símbolo n anterior fue rechazado. Logo final pendiente.
- Entregables: este documento, cuatro SVG, capturas, evidencia de revisión y muestra interactiva. Siguiente responsable: usuario revisa; brand-strategist refina.

## Referencia Apple y elección de fuentes

Apple identifica San Francisco como su fuente de sistema. Su licencia de descarga limita usos y no concede un permiso general para incrustarla y redistribuirla en una web o usarla en cualquier pieza de marca. No se descargó, modificó ni distribuyó San Francisco. Referencia consultada: [Apple Fonts](https://developer.apple.com/fonts/), apartados 2A–2C de la licencia publicada.

Propuesta: estudiar sus cualidades de legibilidad, jerarquía y contención mediante fuentes abiertas, manteniendo identidad propia. La semejanza visual es un criterio del especialista; no implica equivalencia métrica con San Francisco.

- **Inter:** fuente orientada a lectura en pantalla, con variantes ópticas y cifras tabulares documentadas por su autor. En la muestra se usa Regular para texto y Medium como base del logo A. [Inter](https://rsms.me/inter/) · [Licencia conservada](assets/typography/Inter-OFL.txt).
- **Manrope:** alternativa de formas más geométricas; aquí se usa Regular para texto y Medium para el logo B. La lectura más amable es una valoración creativa. [Licencia publicada](https://github.com/google/fonts/blob/main/ofl/manrope/OFL.txt) · [Copia conservada](assets/typography/Manrope-OFL.txt).

Las dos familias se distribuyen con SIL OFL 1.1. Se conservaron las fuentes descargadas y sus licencias; no se modificaron archivos tipográficos. Los logos se entregan como contornos SVG, sin requerir instalación de fuentes para visualizarlos.

## BR-V01 · Ruta A: precisión

Propuesto: **Numer** con N mayúscula dibujada para esta exploración, corte horizontal en el centro de la diagonal y resto del nombre basado en Inter Medium con espaciado ajustado. La misma N sirve de monograma.

- Intención: claridad y una presencia sobria, con un detalle reconocible en la inicial.
- Ventaja: el monograma y el nombre comparten la misma construcción; funciona en un solo color.
- Riesgo: la separación diagonal puede perderse en tamaños muy pequeños o percibirse como una N fragmentada. Su reconocimiento debe revisarse con usuarios; no hay prueba de singularidad marcaria.
- Aplicación: logotipo en acceso y encabezados; N aislada en icono o espacio reducido. Inter Regular para lectura y cifras tabulares en columnas monetarias; pesos y escala definitiva pendientes.
- Archivos: [Logotipo A](assets/logo-exploration/numer-a-wordmark.svg) · [Monograma A](assets/logo-exploration/numer-a-monogram.svg).

La N es una interpretación gráfica de la inicial del nombre. No se le atribuye una garantía de seguridad, rentabilidad ni una metáfora financiera artificial. Las letras restantes conservan los contornos originales de Inter; el logo no es una nueva familia tipográfica.

## BR-V02 · Ruta B: cercanía

Propuesto: **numer** en minúsculas, basado en Manrope Medium con espaciado ajustado; n minúscula como monograma derivado del mismo tipo.

- Intención: una presencia más suave y cotidiana.
- Ventaja: ritmo visual continuo y formas simples; fácil de aplicar a encabezados y mensajes.
- Riesgo: el monograma n es convencional y menos distintivo que la inicial de la ruta A. No se presenta como símbolo original terminado.
- Aplicación: nombre en minúsculas en piezas gráficas; Numer sigue siendo la escritura del nombre en texto. Manrope Regular en la muestra de interfaz, con cifras tabulares activadas.
- Archivos: [Logotipo B](assets/logo-exploration/numer-b-wordmark.svg) · [Monograma B](assets/logo-exploration/numer-b-monogram.svg).

## BR-V03 · Recomendación inicial

Recomendación histórica, superada por BR-C15: el especialista propuso profundizar la ruta A con Inter. La dirección vigente es B/Manrope por preferencia del usuario.

El color de marca es un acento. La muestra usa una variante más clara del petróleo en tema oscuro para conservar legibilidad; esta adaptación no es una paleta oscura aprobada. Se incluyó cambio local a grafito para revisar lectura monocroma. Las cifras y movimientos son sintéticos y no definen fórmulas financieras.

## Verificación realizada

- Chrome `153.0.8010.36`, sesión temporal de Playwright, sin perfil personal. La muestra es autónoma: fuentes y vectores incrustados; no depende de red para verse.
- Fuentes Inter y Manrope cargadas correctamente. Los cuatro SVG contienen sus trazados dentro de su viewBox, sin recortes geométricos.
- Sin desbordamiento horizontal a 748 px y 328 px de ancho interior en la revisión de escritorio/móvil.
- Inspección visual de tema claro y oscuro; pruebas de wordmark a 104 px de ancho y monograma a 16 px, además del icono de muestra a 48 px. No equivalen a tamaños mínimos aprobados ni estudio de reconocimiento.
- Cifras tabulares comprobadas a 40 px: `1111` y `8888` miden ambos 103.75 px en Inter y 99.203125 px en Manrope.
- Cambio de color Petróleo/Grafito comprobado con el callback del helper simulado en el navegador. No se verificó el panel nativo del anfitrión; su ausencia deja la primera vista operativa.
- Sin errores JavaScript en la revisión. No se ejecutaron pruebas de aplicación porque no hay implementación.
- Evidencia: [datos de verificación](assets/logo-exploration/verification.json), [captura clara](assets/logo-exploration/review-light.png), [captura oscura móvil](assets/logo-exploration/review-dark-mobile.png). Esta última registra el cambio a grafito.

## Handoff · T-BRAND-004

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario para revisión.
- Resultado: primera exploración de logo y tipografía, con artefactos verificados. BR-V01 a BR-V03 siguen propuestos.
- Archivos: este documento, SVG/capturas/verificación en `assets/logo-exploration/`, fuentes/licencias en `assets/typography/`, generador en `tools/`, brief e índice actualizados y muestra en la conversación.
- Confirmado: BR-A02, BR-C07 y BR-C14. No se transfiere ninguna nueva elección visual como aprobada.
- Riesgos y límites: disponibilidad del nombre, singularidad del símbolo, percepción de usuarios, licencia de fuentes de Apple para otros usos y sistema de accesibilidad completo no quedan acreditados por estas pruebas.
- Siguiente responsable: usuario compara rutas; brand-strategist refina el logo elegido, espaciado y tipografía antes de preparar versiones finales. Orquestador y UX/UI reciben el handoff visual solo cuando exista selección aprobada.

## T-BRAND-005 · Manrope con más cuerpo y un detalle propio

- Estado: cerrado como refinamiento del nombre mediante BR-A03. Símbolo mayúsculo retirado por BR-C16; continúa exploración en T-BRAND-006.
- Responsable: brand-strategist. Revisor: usuario.
- Objetivo y resultado observable: mantener la suavidad de B, aumentar moderadamente el peso del nombre y explorar un corte diagonal junto con un símbolo alternativo al n minúsculo rechazado.
- Entradas: BR-C15, BR-A02, BR-C07 y vectores de T-BRAND-004.
- Alcance de archivos: este documento, brief, índice y handoff de marca; `assets/logo-refinement/`, `assets/typography/`, `tools/build-logo-refinement.cjs`; muestra de conversación.
- Exclusiones: aprobación unilateral, logo de producción, implementación de aplicación y propagación de exploraciones al contexto global.
- Dependencias: preferencias del usuario para consolidar logo y símbolo; ninguna impide la exploración reversible.
- Criterios de aceptación: Manrope real con mayor peso; corte visible en el nombre; símbolo alternativo; comparación con el original a la misma escala; revisión de reducción y temas; conservación del historial.
- Validación: Chrome temporal, carga de Manrope, escritorio/móvil, inspección visual y control local del corte. Evidencia abajo.
- BR-Q05 resuelta parcialmente: nombre dibujado elegido en BR-A03; N mayúscula retirada por BR-C16. Nuevo símbolo pendiente en BR-Q06.
- Entregables y destinatario: dos tratamientos del corte, una N complementaria y comparación para el usuario.

### BR-V04 · B refinada, propuesta

Actualización: el nombre dibujado queda elegido mediante BR-A03. Los tratamientos alternativos y especificaciones de uso definitivo continúan sujetos a consolidación.

Nombre en minúsculas basado en **Manrope Semibold (600)**, frente a Medium (500) de B. Espaciado ajustado; corte diagonal ascendente de 45° en el trazo izquierdo de la n. El resto de las letras conserva sus curvas y contornos. La fuente permanece intacta: las modificaciones pertenecen únicamente a la pieza vectorial.

- Intención: dar más presencia al nombre manteniendo el carácter suave elegido.
- Ventaja: una sola intervención permite conservar un ritmo de lectura uniforme; el corte aporta un detalle para explorar identidad.
- Riesgo: la abertura se hace muy fina en encabezados pequeños; las muestras a 86 y 104 px no fijan tamaños mínimos de producción. No se acredita singularidad marcaria.
- Tratamientos comparables: [corte sutil](assets/logo-refinement/numer-b1-soft-wordmark.svg), abertura de 3 unidades; [corte abierto](assets/logo-refinement/numer-b1-open-wordmark.svg), 5 unidades. La muestra permite alternarlos localmente. Recomendación del especialista: sutil para continuar, pendiente de aprobación.
- Aplicación tipográfica: Semibold se explora para el logo; Manrope Regular permanece en el ejemplo de texto e importe. No se impone Semibold a toda la interfaz.

### BR-V05 · N complementaria, propuesta

Estado vigente: retirada por BR-C16. Se conserva exclusivamente como historial.

[Símbolo N](assets/logo-refinement/numer-b1-symbol.svg): mayúscula dibujada con extremos y uniones redondeados, trazo más robusto y separación diagonal ascendente. Es una alternativa al icono n minúsculo rechazado; no es un glifo de Manrope. Comparte con el nombre las curvas suaves y el ángulo del corte, pero requiere revisión de coherencia por tratarse de una forma distinta de la inicial del logotipo.

La N se muestra en contenedores de 64 y 32 px, y aislada a 16 px. El corte pierde protagonismo al reducirse; se conserva la lectura de la inicial como criterio de exploración, sin declarar reconocimiento probado con usuarios.

### Handoff · T-BRAND-005

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario para revisión visual.
- Resultado real: refinamiento B en vectores y muestra comparativa. BR-C15 confirmado; BR-V04 y BR-V05 son propuestas. No hay logo final aprobado.
- Archivos creados/modificados: los descritos en el alcance, tres SVG nuevos, fuente original Manrope Semibold y metadatos; dos capturas y [verificación](assets/logo-refinement/verification.json). Las rutas A/B originales se conservan.
- Validación realizada: Chrome 153.0.8010.36 en perfil temporal; carga de Manrope y ausencia de desbordamiento a 748/328 px; inspección de [tema claro](assets/logo-refinement/review-light.png) y [oscuro móvil](assets/logo-refinement/review-dark-mobile.png); cambio Sutil/Abierto mediante callback con helper simulado; sin errores JavaScript. No se comprobó el panel nativo del anfitrión.
- No verificado: estudio de reconocimiento, singularidad, tamaños mínimos definitivos, impresión y accesibilidad de un sistema completo. No hay pruebas de aplicación ni implementación.
- Revisión requerida: usuario valora el peso y corte del nombre, y la N complementaria por separado.
- Siguiente acción y responsable: brand-strategist ajusta la propuesta según BR-Q05 y prepara versiones finales solo tras selección. Orquestador y UX/UI no reciben estos vectores como identidad aprobada.

## T-BRAND-006 · Símbolo financiero y reducción a favicon

- Estado: comparación cerrada con descarte de ambos conceptos mediante BR-C17. Se retoma n minúscula como respaldo conforme a BR-C16; ajustes finales de reducción pendientes.
- Responsable: brand-strategist. Revisor: usuario.
- Objetivo: explorar dos símbolos conceptuales relacionados con organizar el dinero y apartar ahorro, junto con la n minúscula solicitada como respaldo.
- Entradas: BR-A03, BR-C16, BR-A02, BR-C07 y brief funcional de finanzas personales.
- Alcance y propiedad: documentos de `docs/08-brand/`, `assets/symbol-exploration/`, `tools/build-symbol-exploration.cjs` y muestra en conversación.
- Exclusiones: modificar el nombre dibujado elegido, implementar favicon en una app, seleccionar símbolo unilateralmente o publicar la identidad.
- Dependencias: valoración del usuario; disponibilidad marcaria no verificada, sin impedir esta exploración reversible.
- Criterios de aceptación: símbolos asociados a capacidades del producto; alternativas diferenciadas; coherencia con la suavidad de Manrope; n minúscula de respaldo; vistas a 16/32 px y junto al nombre; conservar propuestas como tales.
- Validación: revisión visual en Chrome temporal, claro/oscuro y móvil; PNG a 16 y 32 px; carga tipográfica y desbordamiento; comparación monocroma local.
- BR-Q06: A y B descartados por BR-C17. Se retoma la alternativa de respaldo n minúscula que el usuario había indicado en BR-C16.
- Entregables y destinatario: tres SVG, seis PNG de reducción, muestra y evidencia para el usuario.

### BR-V06 · Distribución, propuesta

Estado vigente: descartado por BR-C17; el usuario lo percibe genérico. Descripción conservada como historial.

[Vector Distribución](assets/symbol-exploration/numer-distribution.svg). Una silueta cuadrada de esquinas redondeadas se divide en tres superficies. La separación diagonal repite el gesto del nombre; el conjunto propone representar el dinero organizado entre diferentes destinos, como gasto, ahorro y planes. Las superficies no codifican porcentajes ni categorías fijas.

- Emoción buscada: orden y claridad sin rigidez; valoración creativa, no resultado de estudio.
- Ventaja: conexión con el alcance general del gestor y con el corte del logotipo; silueta compacta para reducción.
- Límite: su significado requiere contexto inicial y puede recordar un gráfico segmentado. No se afirma originalidad marcaria ni reconocimiento probado.
- Aplicación: símbolo aislado en favicon y junto al nombre; motivo de división disponible para futuras piezas, todavía no aprobado.

### BR-V07 · Reserva, propuesta

Estado vigente: descartado por BR-C17; el usuario lo asocia con DiDi. Descripción conservada como historial.

[Vector Reserva](assets/symbol-exploration/numer-reserve.svg). Una pieza inclinada y una base abierta de curvas amplias sugieren separar una parte para un propósito. Conecta con fondos de ahorro y planes personales; no representa custodia real, depósito bancario ni ejecución de pagos.

- Emoción buscada: cuidado y previsión.
- Ventaja: lectura gestual simple y trazos robustos. La pieza se inclinó y desplazó para reducir la semejanza con un botón de encendido observada durante revisión.
- Límite: enfatiza ahorro sobre el resto del producto y puede recordar una hucha o depósito. La separación de la pieza pierde espacio al reducirse; requiere ajuste óptico si se elige.
- Aplicación: símbolo de marca en comparación; no asignarlo como botón funcional de ingreso o ahorro sin especificación UX.

### BR-V08 · n minúscula, respaldo propuesto

[Vector n minúscula](assets/symbol-exploration/numer-lowercase-n.svg). Derivado de la misma Manrope Semibold y el mismo corte sutil del nombre. Ventaja: continuidad literal con el logotipo; límite: menor diferenciación conceptual y corte apenas perceptible a 16 px. No se trata de la n Medium sin detalle rechazada en la primera ronda.

Recomendación histórica retirada por BR-C17: profundizar Distribución. Los nombres Distribución y Reserva identificaban conceptos de símbolo; el producto sigue llamándose Numer. Dirección vigente: cuatro propuestas nuevas mediante BR-C18, documentadas en FAVICONS; la n sigue como respaldo condicional sin selección.

### Handoff · T-BRAND-006

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario para elección de símbolo. Orquestador/UX reciben únicamente BR-A03 y restricciones confirmadas a través de BRAND_HANDOFF.
- Resultado real: dos símbolos conceptuales y n de respaldo dibujados; ninguna de estas tres alternativas está aprobada.
- Archivos: este documento, brief, índice y handoff actualizados; SVG/PNG/capturas/evidencia en `assets/symbol-exploration/`; generador de vectores en `tools/`. Se conserva sin modificar el nombre dibujado de BR-A03.
- Confirmado/aprobado: BR-A03 y BR-C16, con evidencia arriba. BR-V06 a BR-V08 propuestos.
- Validación realizada: Chrome 153.0.8010.36 en perfil temporal, fuente Manrope cargada y sin desbordamiento a 748/328 px; inspección de [vista clara](assets/symbol-exploration/review-light.png) y [oscura móvil](assets/symbol-exploration/review-dark-mobile.png); cambio a grafito con helper simulado; sin errores JavaScript. [Evidencia](assets/symbol-exploration/verification.json).
- Reducción: PNG transparentes a 16/32 px generados desde SVG mediante Sharp; comparación del símbolo a tamaño CSS real en pestañas simuladas. No se instaló un favicon en navegador ni aplicación; no se acredita reconocimiento con usuarios o mínimo de producción.
- Limitaciones: singularidad marcaria, interpretación de terceros, impresión y compatibilidad completa de favicons pendientes. Las variantes oscuras de color continúan como adaptación de muestra.
- Siguiente responsable: usuario responde BR-Q06; brand-strategist refina el símbolo seleccionado y sus versiones pequeñas antes de preparar una entrega final.

### Actualización histórica del handoff · T-BRAND-006 tras BR-C17

Corrección vigente BR-C18: la conclusión del asistente de consolidar la n fue prematura. El usuario solicita cuatro propuestas nuevas; continuar en T-BRAND-007 de [FAVICONS](FAVICONS.md).

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario.
- Resultado: A/Distribución y B/Reserva descartados, recomendación de A retirada y motivos registrados. Se retoma BR-V08 conforme al respaldo solicitado en BR-C16.
- Archivos modificados: VISUAL_IDENTITY, BRAND_BRIEF, README y BRAND_HANDOFF. Los vectores y muestras anteriores se conservan como historial.
- Confirmado: BR-C17. Se conservan BR-A03 y BR-C16. No se registra aprobación de nuevos dibujos ni especificaciones finales de favicon.
- Validación: consistencia de estado y referencias locales; no hubo cambios gráficos ni nuevas pruebas de aplicación.
- Limitaciones: el corte de la n es muy discreto a 16 px; ajustes ópticos y paquete de favicon definitivo pendientes. La asociación con DiDi se registra como percepción del usuario.
- Siguiente responsable: brand-strategist consolida la n minúscula con el nombre elegido, siguiendo el respaldo indicado; cualquier nueva ronda conceptual requeriría una nueva dirección creativa.
