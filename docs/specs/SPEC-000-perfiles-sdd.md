# SPEC-000 · Perfiles nativos y metodología SDD

- Versión: 1.0.
- Estado: verificada para el alcance de archivos y documentación; carga en ejecución no probada.
- Responsable: orchestrator. Fecha: 2026-09-14.
- Origen: corrección del usuario en esta tarea, SRC-04; DEC-014/015.
- Revisión: integración local por el responsable; sin revisión independiente ni agentes delegados.

## Problema y alcance

La entrega anterior dejó nueve fichas Markdown sin perfiles nativos de Codex e interpretó SDD como documento de diseño de software. Corregir la configuración y establecer desarrollo guiado por especificaciones, conservando las fichas como apoyo y la documentación de arquitectura.

No implementar funcionalidades financieras, cambiar decisiones de marca, instalar herramientas de SDD ni alterar configuración global, permisos, modelos o cuentas del usuario.

## Aceptación

| ID | Dado / cuando | Entonces |
|---|---|---|
| AC-01 | Se inspeccionan los perfiles del proyecto | Existen nueve `.codex/agents/*.toml`, cada uno con nombre único, descripción e instrucciones conforme al formato oficial consultado |
| AC-02 | Se carga el encargo de un rol | Sus instrucciones indican contexto global, ficha especializada, SPEC aplicable, límites y handoff; modelos y permisos no se sobrescriben |
| AC-03 | Un agente prepara trabajo de producto | Encuentra el ciclo especificación → aclaración → plan → tareas → implementación → verificación, con plantilla y trazabilidad |
| AC-04 | Se consulta el antiguo documento SDD | Remite al diseño de software conservado y al significado correcto de SDD; referencias activas de arquitectura usan el nombre corregido |
| AC-05 | Se compara el repositorio con su estado inicial | Branding y recursos ajenos al cambio se conservan; los enlaces documentales y TOML se validan |

## Plan y tareas

T-007, responsable orchestrator: consultar documentación oficial; crear archivos TOML independientes con instrucciones de entrada y especialidad; mantener los detalles de rol en Markdown; separar el diseño de software de la metodología SDD; actualizar guías y estado; validar sintaxis, referencias y preservación de archivos.

Las rutas nativas pertenecen a `.codex/agents/`. `docs/00-project/SDD_WORKFLOW.md` define la metodología; `docs/specs/` guarda las especificaciones; `docs/templates/SPEC.md` normaliza su contenido.

## Verificación

| Criterio | Evidencia prevista | Estado |
|---|---|---|
| AC-01/02 | Nueve TOML válidos, campos y nombres correctos, referencias existentes | Verificado |
| AC-03/04 | Flujo, plantilla y referencias revisados; diseño conservado con enlace de compatibilidad | Verificado |
| AC-05 | 135 enlaces locales comprobados; 123 archivos de branding preservados; ningún archivo eliminado | Verificado |

Evidencia: `docs/00-project/verification/T-007.json` (enlazado desde el handoff de T-007).

La verificación cubre archivos y metodología de esta entrega; no implica que esta sesión haya recargado los perfiles ni que se haya probado un spawn con cada uno.

## Historial

1.0 · 2026-09-14: especificación de la corrección solicitada. No cambia alcance del MVP ni reglas financieras.
