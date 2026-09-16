# Numer · Primera muestra del resumen financiero

Fecha de muestra: 2026-09-13. Responsable: brand-strategist. Actualización 2026-09-14: **base visual aceptada para continuar, excepto el sidebar** (BR-A06). Evidencia, alcance y continuación en [Navegación y movimientos](NAVIGATION_MOVEMENTS.md). No equivale a aprobación de un sistema de interfaz completo. Los apartados de tarea/handoff inferiores conservan el estado de la entrega inicial.

## BR-C21 · Encargo confirmado

Origen: usuario, «Me gustaría ver un sistema visual sobre una primera muestra del resumen financiero. Así podremos evaluar cómo se siente Numer como producto».

Se aplican nombre BR-A02, logotipo BR-A03, monograma BR-A05 y dirección Petróleo mineral BR-C07. La muestra conserva las geometrías elegidas. El resto de las decisiones de esta página son propuestas.

## BR-UI01 · Composición y tipografía propuestas

La jerarquía comienza con saldo y cuentas, continúa con distribución de gastos, ahorro y deuda, y termina en movimientos recientes. El petróleo identifica selección y acentos; no comunica rentabilidad ni seguridad técnica. La inspiración en Apple se expresa mediante espacio, alineación y jerarquía tranquila.

Manrope Regular 400 y Medium 500 para interfaz; el logotipo conserva su dibujo aprobado basado en Semibold. Importes con cifras tabulares. Título principal 28 px; saldo hasta 42 px en escritorio, adaptado en móvil; títulos de sección 15 px; texto y controles entre 11 y 14 px, con selector móvil de 16 px. Radios de panel de 20 px; separación interior principal de 24 px y variante compacta de 18 px. Estos tamaños son una exploración, no una escala aprobada para todas las pantallas.

Navegación lateral en escritorio y horizontal en móvil. Los enlaces llevan a secciones de esta misma muestra. No representan otras pantallas implementadas.

## BR-UI02 · Colores de interfaz propuestos

| Uso | Claro | Oscuro |
|---|---|---|
| Fondo | `#F5F6F7` | `#121819` |
| Panel | `#FFFFFF` | `#1D2628` |
| Navegación | `#EEF1F1` | `#172022` |
| Texto principal | `#222629` | `#F2F5F4` |
| Texto secundario | `#566265` | `#ABB9BA` |
| Acento de interfaz | `#185B56` | `#9ED4CA` |
| Superficie de acento | `#E1E8E7` | `#293F3C` |
| Separadores | `#DCE2E1` | `#39484A` |
| Fondo de barras | `#E9EEED` | `#344344` |

La variante clara del acento en modo oscuro es adaptación de interfaz; no cambia el archivo maestro del logotipo. Los estados de error, éxito, advertencia, formularios y carga siguen pendientes.

## BR-UI03 · Contenido sintético e interacciones

Ejemplo en MXN al 13 de septiembre de 2026. La moneda es una elección para la muestra, no una decisión sobre soporte monetario del producto.

- Cuentas: diaria $14,680.50, ahorro $8,000.00 y efectivo $2,000.00; total $24,680.50. El saldo no se etiqueta como dinero libre para gastar ni como patrimonio neto.
- Ahorro: los mismos $8,000.00 de la cuenta, incluidos en el total; meta ilustrativa $20,000.00, progreso 40%. No se suman dos veces ni se define el modelo definitivo de metas.
- Gastos: vivienda $3,500.00, alimentación $1,750.50, transporte $680.00 y suscripciones $450.00; total $6,380.50. Barras proporcionales al total de gastos.
- Ingresos: $18,000.00. Deuda de tarjeta: $3,420.00, presentada por separado.
- Los cinco movimientos son una selección reciente, no todo el mes. La transferencia entre cuentas no cambia el total; el pago de deuda no se cuenta como gasto nuevo.

Conciliación sintética posible: saldo inicial $13,361.00 + ingresos $18,000.00 − gastos $6,380.50 − pago de deuda $300.00 = saldo final $24,680.50. Una transferencia interna de $2,000.00 tiene efecto agregado cero. El ejemplo supone gastos pagados con saldo existente y deuda previa de $3,720.00. No introduce reglas financieras nuevas.

Se puede cambiar tema, ocultar importes y barras de categorías, filtrar movimientos y abrir su detalle. El diálogo respeta el ocultado de importes. Son interacciones locales sin persistencia, datos reales o conexión bancaria. Las alternativas de apariencia y espaciado están conectadas al control de diseño del entorno cuando está disponible.

## Evidencia y límites

Muestra interactiva entregada en la conversación. Capturas: [escritorio claro](assets/financial-overview/desktop-light.png), [escritorio oscuro](assets/financial-overview/desktop-dark.png), [móvil claro](assets/financial-overview/mobile-light.png), [móvil oscuro](assets/financial-overview/mobile-dark.png).

[Verificación](assets/financial-overview/verification.json): Chrome 153.0.8010.36; sin desbordamiento horizontal a 1024, 360 y 320 px; fuentes cargadas; tema oscuro con fondo calculado correcto; filtros, apertura/cierre de detalle y Escape; ocultado de importes y barras; sin errores de JavaScript. Contrastes de los siete pares de texto comprobados superiores a 4.5:1. Capturas clara/oscura y móvil inspeccionadas visualmente.

Esta revisión no es una auditoría completa de accesibilidad ni una prueba del producto. Pendientes: lector de pantalla, navegación completa por teclado, otros navegadores, contenido extremo, estados vacíos/error/carga y control de diseño dentro del host real. No hay aplicación inicializada, motor financiero ni integración.

## T-BRAND-011 · Sistema visual aplicado al resumen

- Estado: terminada como primera muestra; propuesta en revisión por el usuario.
- Responsable: brand-strategist. Revisor de dirección: usuario; destinatario posterior: UX/UI.
- Objetivo observable: evaluar cómo se siente Numer mediante un resumen financiero interactivo en claro/oscuro y móvil.
- Entradas: BR-C21; [guía vigente](BRAND_GUIDELINES.md); [contexto](../00-project/PROJECT_CONTEXT.md); [estado](../00-project/STATUS.md); [rol de marca](../../agents/brand-strategist.md); [rol UX/UI](../../agents/ux-ui.md); [reglas](../01-product/BUSINESS_RULES.md); [glosario](../01-product/DOMAIN_GLOSSARY.md); [PRD](../01-product/PRD.md); [SRS](../01-product/SRS.md); [sistema de diseño](../05-design/DESIGN_SYSTEM.md).
- Alcance y propiedad: exploración de marca en `docs/08-brand/` y muestra en la conversación. Sin escrituras en el dominio UX/UI o contexto global.
- Exclusiones: aplicación, reglas nuevas, datos reales, despliegue y cambios a los símbolos aprobados.
- Dependencias: activos aprobados disponibles; definición completa de producto no bloquea la muestra sintética.
- Criterios de aceptación: aplicar identidad elegida, mostrar jerarquía financiera legible, mantener cifras coherentes y revisar adaptación y controles locales. Cumplidos como prototipo.
- Validación proporcional: navegador, capturas, controles, contraste y conciliación del ejemplo; evidencia arriba.
- Decisiones pendientes: aprobación o ajuste de BR-UI01 a BR-UI03 por el usuario. UX/UI deberá especificar estados y comportamiento antes de implementación.
- Entregables: muestra, este documento, capturas, verificación e índice/handoff actualizados.

## Handoff · T-BRAND-011 · brand-strategist

- Fecha y destinatario: 2026-09-13; usuario para revisión, UX/UI y orquestador mediante este documento local.
- Resultado real: primera muestra interactiva completa y verificada dentro del alcance descrito. El sistema propuesto sigue sin aprobación.
- Archivos: `UI_EXPLORATION.md`, `assets/financial-overview/`, `README.md`, `BRAND_HANDOFF.md`, `BRAND_GUIDELINES.md`; muestra en la conversación.
- Confirmado: encargo BR-C21; decisiones existentes BR-A02, BR-A03, BR-A05 y BR-C07 conservadas. Propuesto: BR-UI01 a BR-UI03.
- Validación y limitaciones: sección de evidencia anterior. No se acredita funcionalidad de producto ni accesibilidad completa.
- Revisión requerida: percepción, jerarquía, densidad y protagonismo del petróleo.
- Siguiente acción: usuario comenta la muestra; brand-strategist ajusta la dirección. UX/UI recibe las decisiones seleccionadas para especificar componentes y estados.
