# Handoff · T-UX-001 · ux-ui

Continuación: [T-UX-002](HANDOFF-T-UX-002.md) registra la aprobación posterior UX-A01 y los nuevos entregables. Este handoff conserva el estado de su entrega original.

- Fecha: 2026-09-16. Responsable: ux-ui. Destinatarios: usuario, product-analyst y orchestrator mediante archivos locales; sin iniciar otros agentes.
- Resultado: diez capturas y fuente de maqueta revisadas; trece flujos, diez estados, doce decisiones pendientes y selección compacta propuesta. Investigación terminada; diseño pendiente de revisión. Sin frontend ni cambios de Sites.
- Creados: [tarea](T-UX-001.md), [revisión](UX_REVIEW.md), este handoff e [informe](verification/T-UX-001.json). Actualizados: [flujos](USER_FLOWS.md) y [sistema](DESIGN_SYSTEM.md).
- Artefacto adicional: comparación del sidebar dentro de la conversación y su directorio de visualizaciones; no forma parte del frontend del proyecto.
- Requisitos: RF-01 a RF-12 y reglas relacionadas según flujos; BR-C26/27/28 deben integrarse por producto. Fuentes de otros roles intactas.
- SPEC: investigación previa de T-005 sin SPEC funcional asignada; UX-AC-01 a UX-AC-05 son criterios documentales. Ninguna SPEC de producto se declara lista/verificada.

## Confirmado y propuesto

Identidad aprobada por [BR-A08](../08-brand/BRAND_FINAL.md); varias cuentas/tarjetas y crédito por [BR-C26/27/28](../08-brand/BRAND_SCOPE_UPDATE.md); encargo actual sin frontend y con ajuste localizado.

Propuesto: selección de escritorio 38 px, radio 8 px, interacción mínima 44 px; móvil 48 px dentro de 52 px; tarjetas dentro de Cuentas; alias por tarjeta; ámbitos de totales/filtros explícitos. No se promueven estas propuestas a aprobación.

## Validación y límites

Inspección visual de cuatro capturas de resumen, cuatro de movimientos y dos de captura/revisión; lectura de CSS y navegación. Enlaces, IDs y pares de contraste comprobados mediante script local, con método/resultado en el informe. La comparación nueva solo muestra navegación.

Resultado: 52 enlaces sin rutas rotas; seis pares de contraste entre 6.56:1 y 11.17:1; sintaxis JavaScript válida y cuatro activos incorporados sin alterar bytes. La comparación nueva solo se revisó en fuente: el servidor local no pudo abrir un socket en el sandbox y la vista de archivo local fue rechazada por la política de URL del navegador. No se intentó eludirla; inspección visual de esa comparación, interacción y controles del host pendientes.

No se repiten ni atribuyen las pruebas de Chrome previas de marca. Sin pruebas de guardado, cálculos, lector de pantalla, accesibilidad completa, RLS, autorización, autenticación o persistencia.

## Riesgos y siguiente acción

PRD Q-05/F-03 están desfasados respecto a BR-C28. Los textos históricos de marca no deben reabrir BR-A07/A08. Datos desconocidos no equivalen a cero; la apariencia no acredita integridad financiera ni seguridad.

1. **Producto:** actualizar PRD/SRS con BR-C26/27/28, resolver UX-P01 a UX-P07 y UX-P10 para sus recorridos, acordar fase del resto y crear/versionar SPEC con casos financieros comprobables.
2. **Usuario y UX/UI:** revisar UX-SB01 y continuar wireframes de acceso, alta y captura; identidad cerrada.
3. **Orchestrator:** integrar resultado parcial de T-005 al estado global, conservando T-001/T-002 pendientes. No está terminada toda la experiencia.
4. **Frontend y QA, futuros:** implementar con alcance autorizado y SPEC aplicable; verificar UX-Q01 a UX-Q07 y los AC de producto. No iniciados por este handoff.
