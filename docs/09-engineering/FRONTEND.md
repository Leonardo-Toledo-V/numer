# Plan de frontend

Estado: preparación documental; sin código. Responsable: frontend. Entradas: ficha de rol, SRS del módulo, contratos del diseño de software y entregables de UX/UI.

## Primera entrega técnica propuesta

Cuando se asigne desarrollo y estén resueltos los contratos, establecer Next.js y shadcn/ui, convenciones de componentes, límites servidor/cliente, formularios y manejo de errores. TypeScript, librerías de validación, gráficos, iconos y movimiento son decisiones técnicas pendientes de concreción.

La primera funcionalidad completa debe conectar captura y consulta con validación de servidor y persistencia real. Dashboard e historial deben derivar cifras de contratos de dominio; no mantener fórmulas financieras paralelas en la interfaz.

## Información que necesita el rol

- Campos, tipos, validaciones y errores de los comandos.
- Datos de consulta, paginación, representación monetaria y zona horaria.
- Comportamiento de sesión y acceso no autorizado.
- Estados, navegación y criterios de accesibilidad de UX.
- Contrato de reintento/idempotencia y frescura de datos tras escritura.

## Evidencia futura de entrega

Registrar rutas implementadas, contratos consumidos, estados cubiertos, pruebas de interacción y limitaciones. Enlazar revisión de UX, integración y resultados de QA. Añadir comandos de ejecución solo cuando existan y hayan sido comprobados.
