# Instrucciones globales

Aplican a todo el repositorio. Las instrucciones explícitas del usuario y las reglas del entorno prevalecen. Estas reglas distribuyen el trabajo; no otorgan autorización adicional para acciones externas.

## Contexto mínimo obligatorio

1. [Contexto global](docs/00-project/PROJECT_CONTEXT.md).
2. [Estado](docs/00-project/STATUS.md).
3. Ficha del rol asignado en [agents/](agents/README.md).
4. Encargo, criterios de aceptación y documentos relevantes para esa tarea.

Los perfiles nativos están en `.codex/agents/*.toml`; las fichas de `agents/` detallan responsabilidades. Para tareas de producto, leer también [SDD_WORKFLOW](docs/00-project/SDD_WORKFLOW.md) y la especificación asignada con su versión.

Consultar [decisiones](docs/00-project/DECISIONS.md) cuando una tarea dependa de alcance o restricciones. No cargar todo `docs/` por defecto. Compartir referencias y resúmenes de decisiones, no conversaciones completas. No cargar `BRANDING_AGENT.md` ni exploraciones de marca como contexto común.

## Estado de la información

- **Confirmado:** requisito explícito del usuario, con origen identificado.
- **Propuesto:** recomendación o elaboración inicial pendiente de validación.
- **Pendiente:** pregunta o decisión aún sin respuesta.
- **Aprobado:** decisión con responsable, fecha y evidencia de aceptación.
- **Implementado / verificado:** cambio existente / comportamiento comprobado con evidencia. Nunca deducirlos de una especificación.

No promover propuestas a decisiones por repetición. El contexto global resume decisiones; los documentos especializados conservan su detalle. Las discrepancias se registran y se resuelven en la fuente correspondiente antes de propagarlas.

## Forma de trabajar

- Una tarea tiene un responsable, entradas, alcance de archivos, dependencias y criterios de aceptación. Usar [TASK](docs/templates/TASK.md).
- Cargar la ficha del especialista. No asumir que el nombre de una carpeta activa un agente ni que esta documentación exige lanzarlos todos.
- Coordinar escrituras sobre archivos compartidos; evitar dos propietarios editando el mismo archivo a la vez. Proponer cambios de otro dominio mediante handoff.
- Avanzar de forma autónoma en trabajo autorizado y reversible. Consultar solo decisiones que alteren materialmente el producto o acciones que requieran autorización aún no otorgada.
- No sobrescribir trabajo existente, secretos, datos reales ni migraciones aplicadas. Documentar dependencias o impedimentos concretos.
- Al terminar, entregar [HANDOFF](docs/templates/HANDOFF.md) con archivos, decisiones, riesgos, pruebas realizadas y siguiente responsable. El orquestador integra el estado global.
- Actualizar documentación junto con los cambios. Usar IDs estables para requisitos, reglas, decisiones y tareas.

## Desarrollo guiado por especificaciones

SDD significa **Spec-Driven Development**, confirmado por el usuario. Seguir el ciclo especificación → aclaración → plan → tareas → implementación → verificación. El diseño de software es un entregable técnico dentro de ese proceso.

- Escribir o actualizar la SPEC de la entrega en `docs/specs/` antes de implementar comportamiento nuevo. Usar [SPEC](docs/templates/SPEC.md), con detalle proporcional al cambio.
- Cada tarea de implementación referencia SPEC, versión y criterios de aceptación; los resultados enlazan esos criterios con archivos y pruebas.
- Resolver ambigüedades críticas antes del trabajo dependiente. Si cambia el comportamiento, actualizar la especificación y revisar contratos y pruebas afectados.
- La autorización existente permite avanzar en detalles reversibles; la metodología no exige nuevas aprobaciones para cada documento o tarea.

## Límites del proyecto

- El alcance actual es documentación y definición. No inicializar la aplicación ni desplegar como consecuencia de leer estas instrucciones.
- Next.js, shadcn/ui, Supabase, Vercel y acceso con Google son elecciones explícitas. Versiones, librerías complementarias y diseño de datos requieren especificación técnica.
- Priorizar exactitud de importes, transferencias, deuda y ahorro. No inventar reglas financieras silenciosamente; registrar la decisión antes de implementar su comportamiento.
- Diseñar aislamiento por usuario, autorización y validación en servidor, RLS y pruebas de acceso entre usuarios. La revisión visual no acredita seguridad.
- Minimizar datos de tarjetas: no almacenar PAN completo, CVV, PIN ni contraseñas bancarias. No exponer secretos en código cliente, ejemplos, logs o documentación.
- Utilizar datos sintéticos en ejemplos y pruebas. Separar transacciones reales de proyecciones y distinguir gastos, transferencias y pagos de deuda.
- Verificar documentación oficial y versiones antes de implementar integraciones. Las referencias del chat son antecedentes, no una comprobación actual de APIs.
- No añadir dependencias o skills por disponibilidad. Justificar necesidad y respetar las capacidades y permisos de la sesión.

## Criterio de entrega

Un documento puede entregarse como borrador si señala qué está propuesto, qué falta y quién debe resolverlo. Una funcionalidad requiere requisitos trazables, revisión pertinente, pruebas apropiadas, documentación actualizada y limitaciones visibles. Nunca afirmar que algo está aprobado, probado o desplegado sin evidencia.
