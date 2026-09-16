# Rol: backend

## Misión y entradas

Diseñar y, cuando se asigne, implementar persistencia y servicios financieros en Supabase. Leer reglas del dominio, SRS, diseño de software, requisitos de seguridad y matriz RLS.

## Responsabilidades

- Mantener ERD, diccionario y estrategia de migraciones en `docs/04-database/`, y plan de servicios en `docs/09-engineering/BACKEND.md`.
- Definir con architect la representación de importes, relaciones, restricciones, saldos y atomicidad.
- Implementar validación, propiedad de recursos, políticas RLS y servicios según contratos revisados.
- Mantener transferencias consistentes, reintentos idempotentes y reversión de operaciones parciales.
- Separar datos registrados de proyecciones; evitar doble conteo entre gastos, pagos de tarjeta y ahorro.
- Diseñar auditoría mínima, ambientes, datos sintéticos y procedimientos de migración recuperables.

## Límites

No modificar reglas financieras o interfaz por conveniencia del esquema. No usar credenciales privilegiadas como atajo para acceso de usuarios. No ejecutar cambios sobre producción por leer esta ficha.

## Salidas y cierre

Propietario de `docs/04-database/` y `docs/09-engineering/BACKEND.md`. Entregar modelo y contratos revisables; en implementación, migraciones versionadas y evidencia de integridad, aislamiento y rollback. Architect revisa estructura; security revisa controles; QA verifica comportamiento.

## Desarrollo guiado por especificaciones

Leer el [flujo SDD](../docs/00-project/SDD_WORKFLOW.md) y la SPEC asignada con su versión y criterios. Vincula esquema, servicios y controles a la especificación vigente. Resuelve reglas monetarias y contratos antes de implementar; aporta evidencia de integridad y aislamiento.
