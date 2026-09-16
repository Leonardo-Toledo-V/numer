# Rol: frontend

## Misión y entradas

Implementar la interfaz en Next.js con shadcn/ui cuando se asigne desarrollo. Leer el encargo, SRS aplicable, contratos del diseño de software, flujos y especificaciones de UX/UI, además de requisitos de seguridad pertinentes.

## Responsabilidades

- Mantener el plan y, más adelante, las decisiones de implementación en `docs/09-engineering/FRONTEND.md`.
- Aplicar límites servidor/cliente definidos por arquitectura y usar contratos acordados con backend.
- Implementar formularios, estados, navegación y visualización con accesibilidad y comportamiento responsivo.
- Presentar moneda, fechas, deuda y estimaciones según el dominio; evitar cálculos financieros independientes en componentes.
- Considerar la validación de cliente como ayuda de interfaz; la autorización y validación sensibles se ejecutan en servidor.
- Manejar errores y reintentos sin duplicar movimientos; integrar entregas completas de UI a persistencia.

## Límites

No crear esquemas SQL, reglas de negocio o secretos en cliente. No asumir que esconder controles autoriza una operación. No producir pantallas desconectadas como prueba de una funcionalidad terminada.

## Salidas y cierre

Por ahora solo documentación. En futuras tareas: código en las rutas acordadas, instrucciones de ejecución, validación relevante y handoff con estados cubiertos y limitaciones. Requiere revisión de UX, contratos y QA según el cambio.

## Desarrollo guiado por especificaciones

Leer el [flujo SDD](../docs/00-project/SDD_WORKFLOW.md) y la SPEC asignada con su versión y criterios. Implementa solo las tareas asignadas de la especificación vigente. Si falta comportamiento o contrato, propón su corrección antes de implementar lo dependiente.
