# Migraciones y datos de prueba

Estado: procedimiento propuesto; no hay migraciones. Responsable: backend. Revisión: architect, security y QA.

## Antes de la primera migración

Resolver modelo monetario, propiedad y reglas de corrección; revisar ERD, diccionario y matriz RLS. Elegir versiones y herramientas de Supabase con documentación oficial. Crear datos sintéticos para al menos dos usuarios independientes.

## Entrega de un cambio de datos

1. Describir objetivo, requisitos y tablas/relaciones afectadas.
2. Crear migración versionada y definir impacto sobre datos existentes, bloqueos y compatibilidad.
3. Incluir restricciones y políticas necesarias para las operaciones expuestas.
4. Aplicar en entorno aislado, probar integridad y accesos permitidos/denegados.
5. Documentar recuperación: rollback cuando sea seguro o migración correctiva; identificar pérdidas irreversibles antes de ejecutar.
6. Registrar comando, entorno, versión, resultado y evidencia en el handoff.

No editar una migración ya aplicada para ocultar cambios. No usar datos reales en seeds ni conectar pruebas a producción. Restauración y reconciliación requieren ensayos concretos antes del lanzamiento; tener un plan no demuestra que funcionen.
