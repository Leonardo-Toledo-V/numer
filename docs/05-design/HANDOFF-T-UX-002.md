# Handoff · T-UX-002 · UX/UI

**Actualización posterior — [UX-FB01](UX-FEEDBACK-001.md):** composición de las diez maquetas rechazada por el usuario. No usar estos marcos como referencia visual para frontend ni continuar el acabado en Figma; queda prohibido volver a usar el complemento. Conservar colores y contenido; replantear escala, formas y distribución con patrones de shadcn/ui. Esta actualización sustituye las acciones siguientes que propongan terminar Figma. El resto del documento conserva evidencia histórica, no aceptación.

2026-09-16 · Responsable: UX/UI · Destinatarios: producto y orquestación; después UX, arquitectura, seguridad y frontend según su alcance.

## Resultado y estado real

Base de experiencia 0.3 entregada: mapa, benchmark documental, hipótesis e investigación preparada, flujos, sistema de diseño, mejoras priorizadas, casos y diez wireframes locales revisados. Dos skills instaladas. Diez marcos trasladados a Figma y navegación creada en FigJam. Acabado Figma parcial por límite de herramientas Starter: no presentar el archivo como prototipo conectado o biblioteca terminada. No hay frontend, aplicación, despliegue ni prueba con usuarios.

Entradas mínimas: [hub](README.md), [pendientes](UX_REVIEW.md), [sistema](DESIGN_SYSTEM.md), [marca aprobada](../08-brand/BRAND_HANDOFF.md). No es necesario cargar exploraciones de marca.

## Archivos y aceptación

Contrato documental T-UX-002 v0.1, previo a SPEC funcional. La aprobación del diseño no resuelve reglas financieras.

| Criterio | Resultado y evidencia |
|---|---|
| UX2-AC01 | UX-A01: selección desktop 38 px / radio 8 px / blanco 44 px. Evidencia textual del usuario en DESIGN_SYSTEM 0.3. |
| UX2-AC02 | apple-design y emil-design-eng instaladas desde la revisión fija de Emil Kowalski; [procedencia y límites](SKILLS_AND_TOOLS.md). |
| UX2-AC03 | [NAVIGATION](NAVIGATION.md): quince pantallas, cuatro destinos, retorno, accesos contextuales y diagrama FigJam. Propuesto. |
| UX2-AC04 | [BENCHMARK](BENCHMARK.md): fuentes primarias de Monarch, YNAB, Lunch Money, Apple y W3C; hechos separados de inferencias. |
| UX2-AC05 | [USER_FLOWS](USER_FLOWS.md) 0.3: trece flujos, diez estados y tres diagramas de prioridad; [UX_CASES](UX_CASES.md) enlaza escenarios. |
| UX2-AC06 | [DESIGN_SYSTEM](DESIGN_SYSTEM.md) 0.3 y [tokens](assets/ux-002/design-tokens.json): doce contratos de componentes, fundamentos, contenido y criterios de accesibilidad. Propuestos salvo marca/sidebar. |
| UX2-AC07 | [WIREFRAMES](WIREFRAMES.md): ocho desktop + dos móvil, SVG/PNG inspeccionados. Figma importado, con dos tipos de acabado pendientes descritos abajo. |
| UX2-AC08 | [RESEARCH_PLAN](RESEARCH_PLAN.md): público provisional, JTBD/journey hipotéticos, entrevista, tree testing y prueba moderada. Veinte casos preparados; cero sesiones ejecutadas. |
| UX2-AC09 | Este handoff, [informe](verification/T-UX-002.json) y [manifiesto Figma](assets/ux-002/figma-manifest.json). |

También se actualizaron README, T-UX-002, aviso de evolución en UX_REVIEW y HANDOFF-T-UX-001. Herramientas reproducibles en `tools/build_ux002_wireframes.py`, `tools/render_ux002.cjs`, `tools/prepare_figma_import.py` y `tools/verify_ux002.py`. No se editaron fuentes de producto, marca o estado global.

## Decisiones y propuestas

- **Aprobado UX-A01:** usuario acepta la recomendación anterior; aplica a selección de escritorio, no a toda la propuesta visual o de producto. Marca BR-A07/A08 permanece aprobada.
- **Confirmado:** continuar definición UX; descargar skills pertinentes; usar Figma si es posible. Varias cuentas/tarjetas y datos excluidos siguen BR-C26/27/28.
- **Propuesto:** IA, jerarquías de deuda/crédito, captura contextual, revisión con efecto, recuperación de resultado incierto, tokens complementarios y geometría móvil.
- **Pendiente:** público objetivo consultado sin respuesta al cerrar la entrega. Se usa provisionalmente gestión financiera individual; no se infiere acceso compartido.

## Validación realizada

Render de diez SVG con Manrope local y Sharp del runtime, revisión visual de las diez imágenes y vista conjunta; se corrigieron solapamiento en W01 y falsa apariencia de campo en W10. Se comprobaron enlaces locales, IDs, dimensiones y contraste de pares de tokens. Los hashes de skills se comparan con la revisión descargada y el wordmark incrustado con el maestro original. Método y resultados en el informe JSON.

En Figma: archivo vacío inspeccionado, búsqueda de activos propios, fuentes disponibles comprobadas, diez importaciones y diez capturas revisadas. Se detectó normalización de Medium a Regular; se corrigieron 41 textos antes del límite. No hay revisión final de todas las correcciones. El mapa FigJam se generó con la herramienta y conserva edición; no se realizó una prueba de usabilidad del mapa.

## Límite concreto de Figma

[Diseño](https://www.figma.com/design/tTqlU8S1gc4AvW9BdPOuI6) · [FigJam](https://www.figma.com/board/iFDAZcS4HOnjp4O13nlnDt).

El plan Starter agotó su cuota MCP. Permanecen 66 textos por restituir a Manrope Medium y el marco W04 superpuesto con W05: mover nodo `2:2` a X=100, Y=1100. IDs exactos en el manifiesto. Los SVG/PNG locales son la referencia visual revisada. No se exige una compra para utilizar la entrega. Continuar ese acabado cuando haya capacidad, o editar esos valores en Figma; después verificar capturas. Auto layout, biblioteca nativa y conexiones de prototipo son una entrega posterior, no trabajo ya realizado.

## No verificado y dependencias

No se verificaron teclado, lector de pantalla, zoom/reflow, dispositivos reales, persistencia, cálculos, autorización o RLS. Los pares de contraste no acreditan conformidad WCAG de un producto. Los diez marcos no cubren cada pantalla del mapa: meses/deuda completos, transferencias, detalle de movimiento, ahorro y demás recorridos mantienen cobertura documental; requieren reglas y marcos posteriores. Datos sintéticos independientes, sin conciliación contable global.

El benchmark es documental, no estudio comparativo con usuarios. Journey, hipótesis y umbrales de prueba son propuestas. No se inventaron entrevistas, métricas, personas validadas ni resultados.

## Siguiente trabajo concreto

1. **Producto + usuario:** cerrar público y alcance de registro (UX-P01/02), manualidad/moneda/instrumentos (P03–05), deuda/meses/pago/corte (P06/07) y modelo de ahorro (P08). Corregir PRD/SRS que aún contradicen BR-C26/27/28 y redactar SPEC versionada del primer recorrido.
2. **UX/UI:** usar esa SPEC para completar alta financiera y estados, resolver acabado Figma y conectar el prototipo. Conservar las cuatro secciones como hipótesis de navegación hasta la prueba.
3. **UX + participantes del público elegido:** ejecutar el guion, medir comprensión y errores, priorizar hallazgos y revisar. La invitación/contacto a participantes necesita autorización explícita; no se envió ninguna.
4. **Orquestador:** integrar estado global y asignar arquitectura/seguridad. Frontend comienza únicamente cuando se autorice y existan contratos/criterios suficientes.

Primera revisión recomendada: W02 → W03 → W04 → W05; luego W08. Pregunta de evaluación: ¿se entiende qué dinero cambia y por qué un pago de deuda no aparece como otra compra? La respuesta aún debe obtenerse de personas, no deducirse del dibujo.
