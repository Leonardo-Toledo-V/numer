# Matriz de acceso y RLS

Estado: política conceptual propuesta; no SQL ni políticas instaladas. Responsable: security. Backend implementa; QA prueba. Identidad de trabajo: usuario autenticado propietario del recurso.

| Recurso conceptual | SELECT | INSERT | UPDATE | DELETE | Relaciones a comprobar |
|---|---|---|---|---|---|
| Perfil | Propio | Propio, mediante alta controlada | Propio, campos permitidos | Por flujo de eliminación aún pendiente | Identidad autenticada |
| Cuenta | Propia | Propietario autenticado | Propia, sin transferir propietario | Política financiera pendiente | Movimientos, tarjetas y saldo |
| Tarjeta | Propia | Propia y cuenta propia | Propia y cuenta propia | Política pendiente si tiene historial | Cuenta |
| Movimiento | Propio | Propio y referencias propias | Según política de corrección pendiente | Según política de reversión pendiente | Cuenta, tarjeta, categoría, transferencia |
| Categoría | Propia | Propia | Propia | Política de referencias pendiente | Movimientos y presupuestos |
| Fondo / meta | Propio | Propio | Propio y referencias propias | Política pendiente | Cuenta y aportaciones |
| Presupuesto / recurrencia | Propio | Propio | Propio | Propio según ciclo de vida | Categoría y cuenta propias |
| Alertas / forecast / snapshots | Propios | Solo flujo autorizado de generación | Solo flujo permitido | Según ciclo de vida | Usuario y datos fuente |
| Auditoría | Acceso mínimo definido por caso | Solo flujo controlado | No para usuario ordinario | No para usuario ordinario | Actor y recurso |

## Reglas de revisión

- Denegar acceso anónimo a datos financieros. No conceder una operación cuyo ciclo de vida no esté definido todavía.
- En inserciones, comprobar el propietario del registro nuevo; en actualizaciones, comprobar tanto la fila existente como el resultado. Impedir cambiar el propietario.
- Comprobar relaciones de propiedad, además de un campo `user_id`; una FK por ID aislado no expresa necesariamente esa condición.
- Revisar agregados, vistas, funciones, exportaciones y cachés: también deben respetar el aislamiento.
- Probar acceso directo a la base con identidades representativas, además de rutas de aplicación. Una prueba con privilegios elevados no demuestra RLS.
- Si se introducen categorías globales, finanzas compartidas, Storage o trabajos privilegiados, ampliar la matriz antes de implementarlos.

Las condiciones SQL, roles de ejecución, privilegios y restricciones concretas dependen del ERD final y se verificarán con documentación oficial y pruebas. No copiar esta matriz como una política universal sin revisar cada operación.
