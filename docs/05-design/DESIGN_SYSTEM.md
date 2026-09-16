# Numer · Especificación preliminar de interfaz

**Candidata vigente: UX-DC01 v0.3 / UX-FB03**, detallada en [COMPACT_DESIGN](COMPACT_DESIGN.md). Textos desktop 18 px título, 13 px contenido/cifras, 12 px auxiliares; pesos contenidos y ejes de alineación explícitos. Ocultar importes y Configuración se agrupan en dropdown desde el perfil inferior izquierdo. Son nuevas propuestas tipográficas pendientes de revisión; actualizan las referencias candidatas v0.1/v0.2 inferiores. Sidebar rectangular conservado; ningún cambio de frontend.

Versión 0.3 · 2026-09-16 · Responsable: ux-ui · [T-UX-001](T-UX-001.md), UX-AC-04/05.

Estado: propuesta UX/UI; identidad 1.0 aprobada. Sustituye orientación anterior sin marca; no sustituye el manual ni aprueba todo el sistema. Sin frontend implementado.

**Corrección vigente [UX-FB01](UX-FEEDBACK-001.md):** el usuario rechazó escala, formas y distribución de W01–W10. Las escalas tipográficas, dimensiones de controles/paneles y espaciados propuestos en 0.3 deben revisarse antes de implementarse; no son valores aceptados. Se mantienen identidad y aprobación localizada UX-A01. Próxima dirección: composición compacta, jerarquía clara y patrones coherentes con shadcn/ui. No usar el complemento de Figma.

**Candidata de revisión:** [UX-DC01 v0.1](COMPACT_DESIGN.md) concreta nuevas medidas y composición en C01–C03. Es una propuesta focalizada, no actualización aprobada de todos los tokens. UX-R01 prohíbe permanentemente a este agente modificar frontend; cualquier implementación corresponde al rol frontend.

**UX-FB02 vigente:** el usuario confirma preferencia por sidebar exterior rectangular (radio 0), pegado al borde izquierdo, más estrecho y área derecha blanca. [UX-DC01 v0.2](COMPACT_DESIGN.md) lo muestra a 176 px de ancho propuesto. Sustituye las indicaciones anteriores de conservar radio exterior 24 y márgenes del sidebar. La selección interna UX-A01 continúa con radio 8; la petición distingue el panel exterior del elemento seleccionado. Se mantiene la escala compacta como dirección favorable, no como aceptación global de todos los tokens.

## Base conservada

[Entrega vigente](../08-brand/BRAND_FINAL.md) y [manual 1.0](../08-brand/deliverables/numer-brand-kit-v1.0/guide/brand-manual.md): logo original con corte, símbolo independiente, proporciones/márgenes; Manrope 400/500/600 según función; petróleo `#185B56`, porcelana `#F5F6F7`, grafito `#222629`, niebla `#E1E8E7`. No recomponer logo ni usar RC2. Variante porcelana sobre sidebar oscuro, con protección y tamaño habitual de referencia de 96 px.

BR-A06 acepta base visual del resumen para continuar. Conservar jerarquía, bloques y espacio. Tonos particulares de sidebar/oscuro de BR-UI04 siguen propuestos; faltan escala completa, semántica de estados y densidad general.

## UX-SB01 · Selección compacta recomendada

Origen: BR-C23/25 y encargo actual. Propuesta para revisión; no aplicada al Site ni al frontend.

| Propiedad | Maqueta | Propuesta escritorio |
|---|---|---|
| Bloque | 198 px en columna 214 px, radio exterior 24 px | Conservar ancho, petróleo y radio exterior |
| Superficie activa | Mínimo CSS 46 px, padding vertical 13 px | 38 px visuales con texto en una línea |
| Área accionable | Coincide con botón | Mínimo 44 px; superficie centrada con 3 px arriba/abajo |
| Radio activo | 12/20/12/12 px | 8 px uniforme |
| Separación de áreas | 8 px | 4 px, sin solapamiento |
| Ancho interior | Aproximadamente 166 px | Conservar; padding horizontal 12 px |
| Texto/icono | Manrope 13 px, icono 18 px, separación 12 px | Conservar; texto con línea 20 px, activo Medium 500 |
| Activo claro/oscuro | `#E1E8E7` / `#D1E6E0`; texto `#164E4A` | Conservar combinaciones propuestas |
| Lateral claro/oscuro | `#164E4A` / `#153C39` | Conservar |

Menor superficie reduce peso visual; radio uniforme conserva suavidad. Interacción de 44 px evita reducir el blanco pulsable. No se añade decoración para compensar. Las alturas son referencias mínimas a escala habitual: texto ampliado/multilínea hace crecer fila y superficie; no truncar etiquetas para sostener 38 px ni desplazar iconos al seleccionar.

Alternativa: 40 px visuales y radio 10 px con interacción mínima 44 px. Recomendada primero 38/8 para responder al encargo. La comparación de conversación permite explorar altura 36–42 y radio 6–10; esos ajustes no aprueban tokens ni modifican la maqueta original.

## Estados de navegación

| Estado | Propuesta |
|---|---|
| Normal | Icono/etiqueta `#C4DCD8`, sin fondo activo; alineaciones constantes. |
| Hover | Texto porcelana; sin desplazar tamaño o parecer selección persistente. |
| Actual | Fondo niebla, peso 500, `aria-current="page"`; una sola página actual. |
| Foco | Indicador independiente del activo, sin recorte. Propuesta: contorno porcelana 2 px separado 2 px sobre petróleo, a medir en contexto. |
| Activación | Geometría estable; selección tras cambio de ruta, foco lógico en título principal; volver restaura contexto. |
| No disponible | Omitir módulos fuera de alcance; si hay restricción que deba mostrarse, explicar motivo y semántica. Evitar botones inertes sin explicación. |

Futura implementación: enlaces de navegación y botones de tema/privacidad; shadcn/ui como base adaptable a la SPEC. No se elige librería de animación aquí.

## Móvil

Conservar cabecera petróleo y cuatro destinos etiquetados. Icono sobre texto: proponer superficie activa 48 px, radio 8 px y área mínima 52 px, gap interno 4 px. No trasladar 38 px de escritorio a dos elementos apilados. Referencia actual: mínimo CSS 58 px; contenido/padding pueden excederlo.

A 320 px conservar nombres y blancos de al menos 44 × 44 px. Si texto ampliado/localización impiden cuatro columnas, pasar a dos; nunca esconder etiquetas ni provocar desbordamiento. Punto de cambio se decide por contenido en wireframes. Revisar teclado virtual/altura útil y controles sin hover.

## Criterios de próxima verificación

| ID | Objetivo medible propuesto | Evidencia futura |
|---|---|---|
| UX-Q01 | Texto corriente ≥ 4.5:1; indicadores necesarios/foco ≥ 3:1 contra superficies adyacentes | Medir combinaciones reales, hover/error/deshabilitado incluidos. |
| UX-Q02 | Objetivos principales ≥ 44 × 44 px sin solaparse; selección 38 px dentro de fila ≥ 44 px | Geometría renderizada y puntero táctil. |
| UX-Q03 | Recorridos completos con teclado, foco visible/lógico y retorno | QA y lectura de nombre/estado con lector de pantalla. |
| UX-Q04 | Sin pérdida ni desbordamiento de página a 320/360/390/768/1024 px, texto al 200% y reflow equivalente a 320 px | Nombres largos, importes extensos, teclado móvil. |
| UX-Q05 | Campos etiquetados, errores asociados, pendiente distinguible, éxito solo confirmado | UX-E04/05/06/08 y contrato de servidor. |
| UX-Q06 | Moneda/periodo/fuente; dinero, crédito, deuda, ahorro y proyección separados | Casos aprobados por producto; ausencia de datos distinta de cero. |
| UX-Q07 | Información/acciones equivalentes con movimiento reducido y sin hover | Interacción, sin cifras intermedias ficticias. |

Son objetivos internos, no certificación de accesibilidad. Medición numérica de pares del sidebar en [informe](verification/T-UX-001.json); foco real, lector, reflow general y comportamiento financiero pendientes.

## Por especificar

Escala adaptable de Manrope e importes tabulares; formatos monetarios; botones/campos/selectores de múltiples cuentas y tarjetas; gráficos con alternativa textual; formularios/detalle; errores/avisos/éxito; temas completos y UX-E01 a UX-E10. Importes grandes crecen o se reorganizan sin omitir dígitos. Banco como identidad secundaria y texto equivalente; icono ausente no impide identificar registro.

Versión 0.2 integra identidad BR-A07/A08 y UX-SB01. Resto propuesto, pendiente de diseño y comprobación.

## Versión 0.3 · aprobación y fundamentos ampliados

2026-09-16 · T-UX-002. Este apartado actualiza el estado de UX-SB01 de la versión 0.2.

**UX-A01 · Aprobado por el usuario:** «Sí, me gusta más la recomendación. Qué es lo que sigue? Continuemos.» Evidencia: respuesta a la comparación de sidebar en esta tarea, 2026-09-16. Se adopta la recomendación de escritorio: superficie activa 38 px, radio uniforme 8 px e interacción mínima 44 px, conservando identidad. No extiende aprobación a la variante móvil 48/52, los estados no mostrados, las reglas financieras o el resto del sistema.

### Fundamentos propuestos

Valores CSS de referencia a texto base habitual; en implementación deben crecer con zoom/texto. Los tamaños de marco de wireframe no son breakpoints definitivos.

| Familia | Tokens propuestos | Regla |
|---|---|---|
| Texto | Lectura 16/24; compacto 14/20; metadato 12/18; título 28/34; sección 18/26; importe destacado 36/44 | Manrope 400; controles/títulos 500; 600 excepcional. Importes tabulares, sin animar dígitos. Sidebar aprobado conserva 13/20. |
| Espacio | 4, 8, 12, 16, 24, 32, 48 px | Agrupar por proximidad; 24 px interior escritorio, 16 px móvil como referencia. |
| Formas | Campo/botón 8; panel 16–20; contenedor sidebar 24; selección 8 aprobado | No convertir todo a cápsulas; forma expresa función. |
| Controles | Alto 44 mínimo, icono 18–20; campo móvil texto 16 | El área de interacción no depende de tamaño del glifo. |
| Layout | Contenido fluido, ancho legible máximo propuesto 1200; 24–32 px exterior escritorio, 16 móvil | Tabla pasa a lista cuando la información lo pide; no esconder importes esenciales. |
| Elevación | Paneles normales sin sombra; overlay con separación/scrim | Jerarquía por espacio y borde; no usar vidrio como nuevo lenguaje. |
| Movimiento | Navegación/teclado inmediatos; panel 160–220 ms entrada, 120–160 salida opcionales | Estado real visible de inmediato; reducido estático/fundido breve; sin bloquear acción. |

### Roles de color propuestos

| Rol | Claro | Oscuro |
|---|---|---|
| Fondo | #F5F6F7 | #121819 |
| Superficie | #FFFFFF | #1D2628 |
| Texto | #222629 | #F2F5F4 |
| Secundario | #566265 | #ABB9BA |
| Acento UI | #185B56 | #9ED4CA |
| Texto sobre acento | #FFFFFF | #153C39 |
| Superficie suave | #E1E8E7 | #293F3C |
| Borde de campo | #697A7C | #829395 |
| Error texto / fondo | #B42318 / #FFF1EF | #FFDAD6 / #402523 |
| Aviso texto / fondo | #805600 / #FFF2CF | #F8D98A / #3A311E |

Error, aviso y éxito siempre llevan texto/icono, no solo color. Petróleo no significa rentabilidad. Bordes decorativos pueden ser más suaves; no sustituir borde funcional por uno imperceptible. Foco: petróleo en claro y porcelana en oscuro sobre superficie; dentro de rail usar el contraste específico de UX-SB01. El JSON de [tokens](assets/ux-002/design-tokens.json) conserva estados por grupo, sin configurar una aplicación.

### Catálogo de componentes para diseño

| ID | Componente / variantes | Estados y contrato de experiencia | Base shadcn/ui a evaluar en frontend |
|---|---|---|---|
| UX-CMP01 | Navegación desktop/móvil | Actual, hover, foco, contenido largo; un destino actual | Sidebar + enlaces; adaptación propia |
| UX-CMP02 | Botón primario/secundario/destructivo/texto | Normal, foco, presionado, pendiente, deshabilitado con razón | Button; semántica por acción |
| UX-CMP03 | Campo de importe/fecha/concepto | Etiqueta, ayuda, error, solo lectura; moneda visible | Input/Label; calendario según contrato |
| UX-CMP04 | Selector de cuenta/tarjeta | Banco + alias + tipo, búsqueda si lista lo necesita; vacío | Combobox/Popover/Command |
| UX-CMP05 | Indicador financiero | Importe, unidad, periodo, fuente, desconocido, oculto, desactualizado | Card + texto, enlace de fuente |
| UX-CMP06 | Historial | Tabla/lista, filtros, cero coincidencias, carga, error parcial | Table/lista semántica |
| UX-CMP07 | Filtro/búsqueda | Activo, limpiar, contador y ámbito | Input/Select/Popover |
| UX-CMP08 | Detalle y revisión | Pares etiqueta/valor; origen/destino/efecto; volver | Dialog/Sheet o página según espacio |
| UX-CMP09 | Mensaje de estado | Informativo, error, incierto y éxito confirmado | Alert; toast solo complementa |
| UX-CMP10 | Vacío/carga | Primera acción útil; carga sin ceros ficticios | Skeleton + texto de estado |
| UX-CMP11 | Gráfico/progreso | Unidad/periodo/fuente; alternativa textual; ocultado | Primitiva por elegir tras datos |
| UX-CMP12 | Fechas/plan a meses | Previsto/registrado; evento vinculado; dato faltante | Lista y etiquetas, no calendario por defecto |

Compatibilidad propuesta, no selección de versiones ni implementación. Atributos accesibles, foco y teclado deben comprobarse incluso si se parte de componentes existentes.

### Contenido y reglas de operación

- Usar «Añadir tarjeta», no «Conectar banco» salvo integración confirmada. Banco/alias no acreditan sincronización.
- «Pago registrado» solo con confirmación. «No pudimos confirmar el registro» si no se sabe el resultado. No usar «Error, vuelve a hacerlo» en ese caso.
- Sin dato: «Aún no registras la deuda de esta tarjeta». Cero confirmado: mostrar cero y fecha/fuente pertinentes.
- No mostrar «Pago de este periodo» con una cifra hasta definir si es mínimo, para no generar intereses, cuotas u otro concepto. En wireframe se marca «Concepto por definir».
- Sin PAN, titular, CVV, PIN, vencimiento identificativo o credenciales. Corte y límite de pago son conceptos distintos y sí fueron solicitados.
- Toda etiqueta de total indica su ámbito; no sumar monedas distintas sin regla. Ejemplos de MXN son sintéticos y no deciden soporte monetario.

Referencias verificadas: [benchmark](BENCHMARK.md). Objetivo propuesto: WCAG 2.2 AA, con blancos principales de 44 px como criterio interno más amplio. No se declara conformidad. UX-Q01 a UX-Q07 y [casos](UX_CASES.md) son la base de prueba.
