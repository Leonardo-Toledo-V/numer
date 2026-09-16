# Numer · Preparación de entrega a frontend

2026-09-16 · UX/UI · UX-DC01 v0.3. Recomendación de secuencia, no autorización ni tarea de implementación. **Este agente nunca modifica frontend.**

## Qué sigue

Cerrar la revisión de tipografía, alineaciones y menú de perfil con C01/C02/C04. El sidebar recibió valoración favorable del usuario; la nueva revisión tipográfica aún no. Después puede entregarse una primera base visual al agente frontend sin esperar que todas las capacidades futuras estén diseñadas. Producto/orquestación deben delimitar la entrega y su SPEC antes de implementar comportamiento.

| Parte | Preparación UX actual | Falta antes del trabajo dependiente |
|---|---|---|
| Estructura desktop, sidebar, navegación y perfil | Geometría, tipografía candidata, menú abierto/cerrado y recomendaciones de interacción | Revisión visual v0.3; definir adaptación de navegación móvil y comprobar foco/zoom en implementación |
| Listas de cuentas y tarjetas | Jerarquía, columnas, acciones, desconocido frente a cero; vacíos/carga/error especificados | Contrato de datos y reglas del producto para obtener cifras; no inferir fórmulas del ejemplo |
| Formulario contextual | Desktop/móvil, destino visible, validación, cierre con cambios y revisión en el mismo diálogo especificados | Revisión final y estados visuales de validación/revisión; reglas de pago y contrato de servidor para guardar |
| Ocultar importes | Menú con estado; respuesta inmediata propuesta | Alcance exacto y persistencia UX-P12; QA con lector de pantalla y refresco |
| Deuda, meses, corte, ahorro y correcciones | Flujos y preguntas documentados | Decisiones UX-P01–08/P10 y SPEC funcional de producto |

## Entrega mínima a otro responsable

Usar [COMPACT_DESIGN v0.3](COMPACT_DESIGN.md) como propuesta vigente y [REVIEW-UX-003](REVIEW-UX-003.md) como evidencia de qué se aceptó y qué falta. Entregar activos de marca aprobados, medidas/tipos/estados, comportamiento adaptable y escenarios QA. Las maquetas W01–W10 rechazadas no son referencia de composición.

La primera entrega visual propuesta puede centrarse en sidebar/perfil, tabla/lista, campo y botón con datos sintéticos, si el usuario/orquestador la autoriza al agente frontend y la especificación la delimita. No requiere fingir pagos, autenticación o datos guardados. UX revisa capturas y recorridos y devuelve observaciones; frontend realiza cada cambio de aplicación.

## Responsabilidades

- UX/UI: completar muestra/estados y evaluar fidelidad visual, jerarquía e interacción; documentar recomendaciones.
- Producto: cerrar reglas y alcance funcional; no delegar decisiones monetarias a una maqueta.
- Orquestador: secuenciar SPEC y asignar propietarios; este documento no lanza agentes ni tareas.
- Frontend: implementar el alcance autorizado en sus archivos; validar composición con UX.
- QA: comprobar casos de teclado, ampliación, pantallas pequeñas, privacidad visual y resultados reales junto con las demás especialidades.

Recomendación: pasar por etapas a frontend después de cerrar esta revisión focalizada; continuar definición UX en paralelo a las siguientes entregas cuando sus dependencias estén resueltas. No afirmar que toda Numer está lista para implementación.
