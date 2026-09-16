# Diccionario inicial de datos

Estado: conceptual; atributos candidatos, no DDL aprobado. Responsable: backend.

| Entidad | Información candidata | Restricciones a concretar |
|---|---|---|
| Perfil | Identidad, idioma, moneda preferida, zona horaria | Campos mínimos, alta y eliminación |
| Cuenta | Propietario, alias, tipo, moneda, referencia de saldo inicial, estado | Semántica de tipo y saldo; archivo frente a eliminación |
| Tarjeta | Propietario, cuenta, alias, tipo, emisor, últimos cuatro dígitos; crédito si aplica | Datos mínimos; sin PAN completo/CVV/PIN; últimos dígitos como texto |
| Movimiento | Propietario, cuenta, tipo, importe, moneda, fecha efectiva, categoría opcional, nota | Precisión, signos, referencias y corrección |
| Transferencia | Propietario, identificación de operación, origen/destino o movimientos vinculados | Atomicidad, moneda y deduplicación |
| Categoría | Propietario, nombre, estado | Referencias históricas; globales no asumidas |
| Fondo de ahorro | Propietario, nombre, modalidad por decidir | Evitar representar asignación como activo duplicado |

## Convenciones por decidir

Tipos de identificador, representación monetaria, almacenamiento de fechas/instantes, nulos, unicidad, índices, campos de auditoría y acciones de borrado. No fijar `float` para dinero ni convertir fechas financieras en instantes sin definir su significado.

Cada futura tabla debe documentar columnas, tipos, nulabilidad, valor por defecto, restricciones, índices, propiedad y referencia a su política RLS. Cada campo nuevo debe tener propósito funcional; evitar almacenar información sensible por conveniencia.
