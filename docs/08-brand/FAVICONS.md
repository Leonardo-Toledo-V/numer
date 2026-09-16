# Numer · Favicon y exploraciones

Estado vigente: monograma n continuo, escala y tratamiento del icono aprobados por BR-A05. T-BRAND-009 cerrado como selección visual; activos consolidados en la guía 0.1 (T-BRAND-010). Fecha: 2026-09-13. Responsable: brand-strategist.

## Aprobación del monograma · BR-A05

El usuario responde a la muestra de T-BRAND-009: «Es perfecto. Me encantó. Ahora que procede?». Responsable de aprobación: usuario. Fecha: 2026-09-13. Se acepta la n continua redibujada, con remate extendido, 60% de ancho y 50% de alto sobre el recuadro petróleo mostrado. No se retoman los símbolos ni tamaños descartados. Identidad básica y paquete en [BRAND_GUIDELINES](BRAND_GUIDELINES.md).

## Selección de inicial · BR-A04 / tamaño histórico BR-C19

Actualización BR-C20: el 80% resultó excesivo para el usuario. La nueva petición sustituye ese tamaño y requiere rediseñar el símbolo; T-BRAND-009 contiene el estado vigente.

Evidencia del usuario: «No, yo creo que mejor si con la letra. Que abarque un 80% del recuadro, que no sea chiquita». Responsable: usuario. Fecha: 2026-09-13.

BR-A04 elige la letra para el símbolo; se usa la **n minúscula** por BR-C16 y el nombre aceptado en BR-A03. BR-C19 pide una ocupación aproximada del 80% del recuadro. Criterio aplicado por el especialista: altura visible del glifo = 80% del lado; escala uniforme, ancho resultante 70.045% y márgenes verticales del 10%. No se interpreta como 80% de superficie pintada ni se estira la letra para llenar ambos ejes.

Los conceptos Ábaco, Pliegue, Conciliar e Hitos quedan descartados en esta selección. No continuar la exploración conceptual salvo nueva petición.

## Encargo confirmado · BR-C18

«No, pero mejora otros, dame 4 propuestas de favicons». El usuario corrige la conclusión del asistente de retomar automáticamente la n. El símbolo sigue abierto: entregar cuatro alternativas nuevas. BR-C17 mantiene descartados Distribución y Reserva; BR-A03 conserva el nombre dibujado en Manrope Semibold y su corte. La n es únicamente un respaldo condicional, sin selección actual.

## T-BRAND-007 · Cuatro favicons nuevos

- Estado: completada como comparación; ninguna de las cuatro propuestas seleccionada. Continúa en T-BRAND-008 con BR-A04.
- Responsable: brand-strategist. Revisor: usuario.
- Objetivo: comparar cuatro siluetas relacionadas con cuentas, registros, relaciones entre movimientos y planificación, a escala de marca y favicon.
- Entradas: BR-C18, BR-C17, BR-A03 y BR-C07; [VISUAL_IDENTITY](VISUAL_IDENTITY.md).
- Alcance: documentos de `docs/08-brand/`, `assets/favicon-round2/`, `tools/build-favicon-round2.cjs` y muestra de conversación.
- Exclusiones: seleccionar símbolo unilateralmente, reutilizar A/B descartados, modificar el nombre elegido, implementar la app o publicar favicon.
- Dependencias: elección creativa del usuario; no impide exploración reversible.
- Criterios de aceptación: exactamente cuatro propuestas nuevas; siluetas diferentes; aplicación junto al nombre; reducción a 16/32 px; SVG y exportaciones de favicon identificadas como propuestas; corregir el cierre prematuro hacia la n.
- Validación: Chrome temporal, temas claro/oscuro, 748/328 px, fuente real y ausencia de desbordamiento; rasterización a 16/32/48 px; estructura de archivos ICO.
- Decisión pendiente: BR-Q07, qué alternativa merece refinamiento; responsable usuario.
- Entregables y destinatario: cuatro SVG, doce PNG y cuatro ICO de exploración; comparación y evidencias para el usuario.

## Propuestas

Los nombres siguientes son etiquetas de conceptos; el producto se sigue llamando Numer. Las interpretaciones son intenciones creativas, no significados universales ni funcionalidades nuevas aprobadas.

| ID | Concepto | Relación con Numer | Ventaja | Límite a evaluar |
|---|---|---|---|---|
| BR-V09 | **01 · Ábaco** | Dos varillas con cuentas a diferente altura evocan cálculo y control de cifras. | Trazos suaves y referencia numérica concreta. | Puede recordar controles de ajuste; las varillas son más finas que las otras siluetas a 16 px. |
| BR-V10 | **02 · Pliegue** | Dos hojas plegadas evocan un registro de movimientos; una separación diagonal conecta con el nombre dibujado. | Silueta sólida y detalle compartido con el logotipo. | También puede sugerir libro o documentación; no es exclusivamente financiero. |
| BR-V11 | **03 · Conciliar** | Dos piezas curvas enfrentadas sugieren relacionar cuentas y movimientos. | Forma compacta y ritmo suave junto a Manrope. | Puede leerse como enlace o una S; no implica conciliación bancaria implementada. |
| BR-V12 | **04 · Hitos** | Recorrido entre dos hitos distintos alude a fechas, movimientos y planes. | Asimetría y extremos diferenciados. | Puede sugerir navegación o retorno; el recorrido no representa rentabilidad ni una tendencia financiera. |

Recomendación exploratoria: comparar primero Ábaco y Pliegue por sus referencias concretas y diferentes. Ninguna alternativa está aprobada y no se ha acreditado singularidad marcaria.

## Archivos

| Concepto | Vector | Favicon de propuesta |
|---|---|---|
| Ábaco | [SVG](assets/favicon-round2/01-abaco.svg) | [ICO](assets/favicon-round2/01-abaco.ico) |
| Pliegue | [SVG](assets/favicon-round2/02-pliegue.svg) | [ICO](assets/favicon-round2/02-pliegue.ico) |
| Conciliar | [SVG](assets/favicon-round2/03-conciliar.svg) | [ICO](assets/favicon-round2/03-conciliar.ico) |
| Hitos | [SVG](assets/favicon-round2/04-hitos.svg) | [ICO](assets/favicon-round2/04-hitos.ico) |

Los PNG transparentes con sufijos `-16`, `-32` y `-48` están en la misma carpeta. Los ICO contienen esas tres resoluciones en PNG. Se usa petróleo `#185B56` en los archivos; la muestra adapta el tono al modo oscuro y permite comparar grafito. Un favicon definitivo aún debe definir su tratamiento de color en pestañas claras y oscuras.

## Handoff · T-BRAND-007

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario para revisión.
- Resultado real: cuatro favicons propuestos; nombre conservado y elección de símbolo abierta.
- Archivos: este documento, VISUAL_IDENTITY, BRAND_BRIEF, README y BRAND_HANDOFF actualizados; SVG/PNG/ICO/capturas en `assets/favicon-round2/`; generador en `tools/`.
- Confirmado: BR-C18 corrige la interpretación de cerrar en n. BR-A03 se conserva. BR-V09 a BR-V12 propuestos; no son un handoff de identidad aprobada.
- Validación: Chrome 153.0.8010.36 con perfil temporal, Manrope cargada y sin desbordamiento a 748/328 px; revisión de [tema claro](assets/favicon-round2/review-light.png) y [oscuro móvil](assets/favicon-round2/review-dark-mobile.png). Callback Petróleo/Grafito probado con helper simulado; panel nativo no verificado. [Evidencia](assets/favicon-round2/verification.json).
- Exportación: Sharp para PNG y contenedor ICO de tres tamaños; dimensiones y estructura comprobadas. La muestra usa SVG a tamaño CSS real. No se probó instalación en pestañas reales ni compatibilidad completa entre navegadores.
- No verificado: singularidad, reconocimiento de terceros, impresión, mínimos finales y sistema de contraste completo. No hay pruebas ni implementación de aplicación.
- Siguiente responsable: usuario señala la propuesta que desea refinar; brand-strategist ajusta forma, peso y reducción de esa propuesta. La n no sustituye esta exploración sin nueva indicación del usuario.

## T-BRAND-008 · n protagonista al 80%

- Estado: ajuste realizado y entregado para revisión visual; letra elegida, aplicación exacta recién dibujada.
- Responsable: brand-strategist. Revisor: usuario.
- Objetivo: usar la inicial minúscula del nombre, grande y centrada en el recuadro, manteniendo su corte diagonal.
- Entradas: BR-A04, BR-C19, BR-A03, BR-C16 y BR-C07.
- Alcance: documentación de marca, `assets/n-favicon/`, `tools/build-n-favicon.cjs` y muestra en conversación.
- Exclusiones: nuevas alternativas conceptuales, deformación de Manrope, cambio al nombre dibujado, aplicación o despliegue.
- Dependencias: ninguna para realizar el ajuste; aplicación visual exacta sujeta a la revisión del usuario.
- Criterios de aceptación: n minúscula, altura visible 80%, centrado geométrico y proporciones conservadas; muestra a 16/32/64 px; archivos SVG, PNG e ICO; corte visible en reducción.
- Validación: cálculo sobre límites reales del contorno; rasterización e inspección en Chrome claro/oscuro; archivos locales y exportaciones comprobados.
- Decisiones pendientes: valoración de esta aplicación concreta; no implica repetir la selección de letra ya realizada.
- Entregables y destinatario: favicon y comparación de tamaños para el usuario; BR-A04 y BR-C19 comunicados en BRAND_HANDOFF.

### Construcción aplicada

- Fondo petróleo `#185B56`, letra porcelana `#F5F6F7`; esquinas de radio 14 sobre un lienzo de 64 unidades. Tratamiento gráfico aplicado por el especialista, no un nuevo sistema cromático completo.
- n de Manrope Semibold derivada del mismo contorno que el nombre. Altura visible 51.2 sobre 64; centrada con escala uniforme. [Geometría](assets/n-favicon/geometry.json).
- Versión estándar conserva el corte de 3 unidades en coordenadas originales; versión de 16 px amplía solo esa abertura a 6 unidades para dar aproximadamente un píxel de separación perpendicular. El peso y contorno exterior de la letra permanecen iguales.
- [SVG estándar](assets/n-favicon/numer-n-standard.svg) · [SVG para reducción](assets/n-favicon/numer-n-small.svg) · [ICO de 16/32/48 px](assets/n-favicon/favicon.ico) · [PNG 256 px](assets/n-favicon/numer-n-256.png).

### Handoff · T-BRAND-008

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario para revisión del ajuste. Orquestador/UX reciben elección y requisito confirmados.
- Resultado: n minúscula aplicada al 80% de altura sobre recuadro petróleo, con exportaciones y versión óptica de 16 px. No hay implementación en la app.
- Archivos: FAVICONS, VISUAL_IDENTITY, BRAND_BRIEF, README y BRAND_HANDOFF actualizados; generador, dos SVG, cinco PNG, un ICO, geometría y evidencia en las rutas indicadas.
- Aprobado/confirmado: BR-A04 elige la letra; BR-C19 pide tamaño dominante cercano al 80%. La convención de medir la altura, el fondo, radio y ajuste del corte son elaboración del especialista para esta entrega.
- Validación: Chrome 153.0.8010.36 temporal; fuente e imágenes cargadas; sin errores JavaScript ni desbordamiento a 748/328 px. Inspección de [claro](assets/n-favicon/review-light.png) y [oscuro móvil](assets/n-favicon/review-dark-mobile.png); [evidencia](assets/n-favicon/verification.json). PNG de 16 px usa la variante óptica, resto la estándar; ICO contiene 16/32/48 px.
- Límites: no se probó instalación real en pestaña ni compatibilidad completa entre navegadores. La revisión acredita artefactos y geometría, no un sistema visual completo ni reconocimiento con usuarios.
- Siguiente responsable: usuario revisa presencia de la n en el recuadro; brand-strategist consolida la aplicación en la guía de marca cuando quede aceptada.

## T-BRAND-009 · Escala de referencia y n dibujada

- Estado: terminada como selección visual; propuesta BR-V13 aprobada mediante BR-A05.
- Responsable: brand-strategist. Revisor: usuario.
- Objetivo: reducir la ocupación del icono y diseñar una inicial con personalidad en su silueta.
- BR-C20 confirmado: «Quedó muy grande. Mejor más chico. Toma de referencia el logo de nu o el de revolut. Y hazlo de ese tamaño. Y dale diseño. Porque eso de poner solo la letra con una cortada se me hace algo básico y vacío». Fuente: petición del usuario y las dos imágenes adjuntas de Nu/Revolut, 2026-09-13.
- Entradas: BR-C20, BR-A04, BR-A03, BR-C07; referencias visuales aportadas por el usuario. No se extraen instrucciones de las imágenes ni se investigan normas de marca externas.
- Alcance: documentación de marca, `assets/n-monogram/`, `tools/build-n-monogram.cjs` y muestra de conversación.
- Exclusiones: aprobación unilateral de la nueva silueta, cambio al nombre dibujado elegido, rediseño de las marcas de referencia, aplicación o despliegue.
- Dependencias: revisión creativa del usuario; ninguna impide producir la propuesta.
- Criterios de aceptación: menor ocupación que el 80%; comparación con referencias a igual tamaño de recuadro; monograma redibujado que no dependa de una separación diagonal; reducción 16/32 px y exportaciones.
- Validación: medición de referencias, límites geométricos, rasterización, Chrome claro/oscuro, móvil y carga de imágenes.
- Decisión pendiente: aceptar o refinar la nueva silueta y su escala. No registrar su aprobación por herencia de BR-A04.
- Entregables: SVG de icono y símbolo transparente, cinco PNG, ICO de tres tamaños y muestra comparativa para el usuario.

### BR-V13 · n continua, aprobada mediante BR-A05

Monograma dibujado directamente como contorno, sin importar un glifo. Presenta hombro asimétrico, curva interior ascendente, variación de grosor y un remate inferior derecho que continúa hacia afuera. Se elimina la separación diagonal en el símbolo. La inicial n sigue siendo legible; el remate le da una silueta diferente de Manrope. El nombre dibujado BR-A03 se muestra como referencia de convivencia, sin alterarlo automáticamente.

- Ocupación: **60% de ancho y 50% de alto**, centrado geométrico; márgenes laterales 20% y verticales 25%. [Geometría](assets/n-monogram/geometry.json).
- Referencias medidas en los archivos aportados: Nu 61% de ancho / 33.5% de alto; Revolut 50.5% / 63.5%. Son cajas delimitadoras aproximadas de píxeles claros, no normas oficiales de marca. Nu contiene dos letras y Revolut una inicial: no se equiparan sus proporciones. [Mediciones](assets/n-monogram/reference-measurements.json).
- El ancho de Nu sirve de referencia para escala horizontal, con altura intermedia entre ambos ejemplos. No se calcan contornos de Nu o Revolut.
- Intención: una presencia más contenida, con carácter aportado por la construcción de la letra. No se añade una metáfora financiera ficticia a cada curva.
- Ventaja: contorno continuo, sin detalle fino que se cierre al reducirlo. Límite: el remate puede recordar lettering o una ligadura; falta revisar percepción de terceros y singularidad. Su coherencia con el nombre exige valoración del usuario.
- Archivos: [icono SVG](assets/n-monogram/numer-n-icon.svg), [símbolo transparente](assets/n-monogram/numer-n-symbol.svg), [ICO](assets/n-monogram/favicon.ico), [PNG 256](assets/n-monogram/numer-n-256.png). Los originales conservan metadatos históricos de propuesta. Usar la edición consolidada de BRAND_GUIDELINES para la entrega vigente.

### Handoff · T-BRAND-009

- Fecha, responsable y destinatario: 2026-09-13; brand-strategist; usuario para revisión.
- Resultado real: n redibujada, con escala menor comparada con las dos imágenes del usuario; exportaciones generadas. BR-C20 confirmado; BR-V13 propuesto.
- Archivos: este documento, VISUAL_IDENTITY, BRAND_BRIEF, README y BRAND_HANDOFF; generador y artefactos en las rutas del alcance. Las entregas anteriores se conservan como historial.
- Validación: Chrome 153.0.8010.36 con perfil temporal; Manrope e imágenes cargadas, sin desbordamiento a 748/328 px ni errores JavaScript. Inspección de [claro](assets/n-monogram/review-light.png) y [oscuro móvil](assets/n-monogram/review-dark-mobile.png); [evidencia](assets/n-monogram/verification.json). PNG 16/32/48/64/256 y estructura ICO 16/32/48 comprobados.
- Referencias: únicamente los archivos proporcionados, medidos sin modificarlos. Sus marcas se muestran etiquetadas para comparar escala, no como propuestas para Numer.
- Límites: favicon mostrado en pestaña simulada, sin instalación real ni comprobación completa entre navegadores. No se acredita singularidad marcaria, reconocimiento con usuarios ni identidad definitiva.
- Siguiente responsable: usuario valora tamaño y carácter del monograma; brand-strategist ajusta la silueta elegida antes de consolidar la guía.
