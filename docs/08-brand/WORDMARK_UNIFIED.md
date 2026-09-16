# Numer · Inicial del monograma integrada (descartada)

**Actualización BR-C32:** el usuario rechaza esta composición por diferencia de peso. Se aplica la alternativa autorizada de restaurar el nombre anterior. RC2 permanece como historial; usar [entrega 1.0](BRAND_FINAL.md). Los apartados siguientes describen la entrega antes del rechazo.

Fecha: 2026-09-15. Responsable: brand-strategist. Entrega: 1.0 RC2, únicamente para valorar la composición solicitada del nombre.

## Decisiones del usuario

**BR-A07 · Resto de la entrega aceptado.** Evidencia: «Es lo unico que cambiaría, de ahí todo bien», después del manual y paquete 1.0 RC1. Responsable de aprobación: usuario. Se acepta el mensaje, voz, variantes de tinta, reglas de aplicación y dirección de movimiento de la entrega presentada. No se aprueba por extensión una implementación, seguridad, reglas financieras o la maqueta de interfaz completa.

**BR-C31 · Integrar la misma n del icono en el nombre.** Evidencia: «me gustaría que el nombre completo de numer tenga el mismo icono de n dentro del nombre numer». Sustituye la instrucción anterior de conservar separada la n tipográfica con corte. El icono independiente no cambia.

## Cambio producido

Se tomó el contorno exacto del monograma BR-A05, sin su recuadro, y se colocó como inicial del nombre completo. Se aplicó escala uniforme 1.14 y traslación para conservar una altura visible de 57 unidades. Las letras umer conservan su contorno original y reciben solo desplazamiento horizontal de 19.85 unidades. La separación visible entre el remate de la n y la u es de 9.5 unidades. No se deforma el monograma ni se añade otro corte.

Nuevo viewBox del nombre: `0 9 333 70`; su altura y márgenes verticales se conservan. El ancho aumenta para alojar la n personalizada. Los SVG comparten geometría entre petróleo, porcelana y grafito; PNG transparentes a 1332 × 280 px.

La dirección del cambio está confirmada. La composición producida es nueva y se presenta para valoración visual; no se afirma que el usuario ya haya visto y aprobado su espaciado exacto. El resto del cierre no se reabre.

## Entrega y verificación

[Paquete 1.0 RC2](deliverables/numer-brand-kit-v1.0-rc2.zip) · [Manual actualizado](deliverables/numer-brand-kit-v1.0-rc2/guide/numer-brand-manual-v1.0-rc2.pdf) · [Nombre SVG](deliverables/numer-brand-kit-v1.0-rc2/wordmark/numer-wordmark-petroleum.svg).

Comparación de contornos por XML; alfa idéntico entre tintas; revisión local en Chrome a 64/80/96/128 px y símbolos a 16/24/32/48 px. La composición se lee a 80 px y conserva 96 px como referencia habitual. El icono, favicon, fuentes y letras umer permanecen iguales. Manual actualizado y renderizado en siete páginas. Evidencia en `assets/unified-wordmark/` y `verification.json` del paquete.

## T-BRAND-017 · Unificar la inicial del nombre y el símbolo

- Estado: terminada como cambio solicitado; composición nueva presentada para valoración visual.
- Responsable: brand-strategist. Revisor: usuario.
- Objetivo observable: nombre completo Numer con la n del icono, coherente en todas las tintas y en el manual.
- Entradas: BR-A07, BR-C31, [contexto](../00-project/PROJECT_CONTEXT.md), [estado](../00-project/STATUS.md), [rol](../../agents/brand-strategist.md), [entrega anterior](BRAND_RELEASE_REVIEW.md) y SVG maestros RC1.
- Propiedad: `docs/08-brand/`, paquete RC2, documentación, herramientas de exportación y evidencias.
- Exclusiones: cambiar umer o icono, diseñar otro símbolo, repetir naming/voz, modificar Sites, frontend/backend o reglas financieras.
- Dependencias: ninguna para la composición vectorial y actualización editorial.
- Criterios de aceptación: misma silueta de n, resto de letras conservado, variantes coherentes, lectura revisada, PDF y archivos actualizados, aprobación parcial registrada. Cumplidos dentro de la verificación descrita.
- Validación: identidad de trazos, copias conservadas, renderizado y revisión de manual/escala, inventario SHA-256 y archivo ZIP comprobados.
- Pendiente: valoración visual del nombre integrado. BR-A07 conserva el visto bueno al resto.
- Entregables: paquete y PDF RC2, PNG de presentación, registro de cambio y handoff.

## Handoff · T-BRAND-017

- Fecha y destinatario: 2026-09-15; usuario para revisar el resultado, UX/UI mediante documentación local.
- Resultado: inicial del monograma integrada; RC1 y anteriores conservados como historial. BR-A03 describe el nombre antiguo con corte y queda sustituido para uso futuro por la dirección BR-C31.
- Archivos: `WORDMARK_UNIFIED.md`, guías/índice/handoff actuales, `deliverables/numer-brand-kit-v1.0-rc2/`, ZIP, `assets/unified-wordmark/` y herramientas específicas de esta exportación.
- Validación y límites: revisión local, sin pruebas de impresión, auditoría de accesibilidad o implementación. Ningún cambio a Sites.
- Siguiente acción: usuario valora únicamente la composición nueva; brand-strategist registra su decisión. UX/UI deberá usar el archivo integrado cuando se cierre esta revisión, no el nombre histórico con corte.
