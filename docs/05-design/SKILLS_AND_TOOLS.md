# Numer · Skills y herramientas de UX/UI

2026-09-16 · T-UX-002. Origen: solicitud explícita de descargar skills desde skills.sh; Apple, Impeccable y Emil como sugerencias opcionales.

## Selección instalada

| Skill | Procedencia | Uso en Numer |
|---|---|---|
| apple-design | [skills.sh](https://www.skills.sh/emilkowalski/skills/apple-design), [repositorio del autor](https://github.com/emilkowalski/skills) | Orientación, respuesta, claridad, escala adaptable y movimiento reducido. |
| emil-design-eng | [skills.sh](https://www.skills.sh/emilkowalski/skills/emil-design-eng), mismo repositorio | Detalle de componentes, criterio de cuándo no animar y revisión antes/después. |

Instalación mediante el instalador de skills de Codex, revisión fija `85e8e2363b713506e1d5b6e07a0eb2da66be1bc3`; directorios personales `~/.codex/skills/apple-design` y `~/.codex/skills/emil-design-eng`. Cada carpeta upstream contiene un SKILL.md; sin scripts auxiliares ejecutados. Disponibles automáticamente a partir del siguiente turno; leídas explícitamente para este análisis.

Impeccable fue evaluada en [skills.sh](https://www.skills.sh/pbakaus/impeccable/impeccable) y su [repositorio](https://github.com/pbakaus/impeccable). La edición actual integra flujo de producción y un launcher/binario; no se instala en esta entrega documental porque las dos skills elegidas y revisión experta cubren la necesidad actual. No se descarta para trabajo futuro ni se atribuye un problema de seguridad sin evidencia.

## Aplicación delimitada

Las instrucciones del usuario y la identidad aprobada prevalecen. No trasladar por defecto materiales translúcidos, fuente de sistema, rebotes, sonido, haptics, hold-to-delete o bibliotecas de una skill a Numer. Mantener Manrope, paleta y sidebar sólido. La feedback visual al presionar no ejecuta una operación antes de completarse el clic. Guardados financieros siguen dependiendo de confirmación real.

Movimiento propuesto: navegación y teclado inmediatos; entrada de panel opcional de 160–220 ms y salida 120–160 ms, sin bloquear acciones ni animar importes; en reducción de movimiento, cambio estático o fundido breve. Valores de diseño propios, pendientes de comprobar; no son especificaciones oficiales de Apple. Motion/GSAP siguen alternativas futuras sin dependencia instalada.

## Figma

**Instrucción vigente UX-FB01:** el usuario indicó «ya no uses más el complemento de figma». No volver a llamar sus herramientas. Las notas inferiores documentan acciones pasadas; no autorizan continuar el acabado ni implican aceptación visual. Ver [corrección de dirección](UX-FEEDBACK-001.md).

Durante la entrega se habilitó Figma y se confirmó conexión. Se aplicaron las guías `figma-create-new-file`, `figma-use`, `figma-generate-design` y `figma-generate-diagram` del complemento 2.0.21. Se creó un [archivo de diseño](https://www.figma.com/design/tTqlU8S1gc4AvW9BdPOuI6) con diez wireframes importados y un [mapa en FigJam](https://www.figma.com/board/iFDAZcS4HOnjp4O13nlnDt). Solo se trasladaron diseños sintéticos, no datos personales ni documentos del proyecto completos.

El archivo nuevo estaba vacío; no había Code Connect en el repositorio. Las bibliotecas disponibles eran kits comunitarios; las búsquedas de NavItem/Button, petróleo y Manrope de Numer no encontraron activos propios. No se adoptó un kit ajeno a la marca. Esta entrega importa los wireframes existentes como geometría y texto editables; no constituye biblioteca nativa con auto layout, variables o componentes ni prototipo conectado.

Manrope se comprobó disponible y se inspeccionaron las diez capturas importadas. El importador normalizó pesos a Regular: se corrigieron 41 textos a Medium. El límite MCP del plan Starter impidió terminar otros 66 y separar W04 de W05 en el lienzo. El archivo local SVG/PNG conserva los pesos y disposición revisados. [Manifiesto de Figma](assets/ux-002/figma-manifest.json) registra nodos, enlaces y el ajuste pendiente de W04: X=100, Y=1100. No se ha contratado un plan ni publicado un sitio.
