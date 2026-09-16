# Modelo inicial de amenazas

Estado: borrador conceptual. Responsable: security. Dependencias: diseño de software, ERD y requisitos de seguridad.

## Activos y límites

Proteger identidad/sesiones, historial financiero, cuentas/tarjetas, saldos, fondos, agregados y futuros archivos de exportación. Límites a revisar: navegador → servidor, servidor → Auth, servidor → base de datos, tareas programadas → datos de usuario y entornos no productivos → producción.

## Escenarios

| ID | Amenaza / impacto | Control propuesto | Validación |
|---|---|---|---|
| AM-01 | Usuario A adivina ID de B y lee/modifica sus finanzas | SEG-01/02, autorización y RLS | TS-02/03/04 |
| AM-02 | A crea registro propio vinculado a cuenta o categoría de B | Validar propiedad de relaciones y restricciones | TS-05 |
| AM-03 | Una petición altera importe, tipo, fecha o propietario | SEG-03 y reglas de dominio | TS-06 y pruebas financieras |
| AM-04 | Sesión inválida o flujo de acceso manipulado permite operar | SEG-01/07; diseño explícito de callback y sesión | TS-01/07 |
| AM-05 | Reintento o concurrencia crea cargos o transferencias duplicadas | Atomicidad, idempotencia y restricciones | RF-05, RN-03/04 |
| AM-06 | Clave privilegiada filtrada permite acceso amplio | SEG-05/06; evitar exposición y reducir privilegios | TS-08 |
| AM-07 | Logs, errores, caché o agregados revelan datos de otra persona | Minimización y partición por usuario | TS-09 |
| AM-08 | Migración o fallo deja saldos incoherentes o datos perdidos | SEG-10, ensayos, recuperación y reconciliación | Pruebas de migración y restauración |
| AM-09 | Job o alerta futura procesa usuario equivocado o repite avisos | Identidad de ejecución, alcance y deduplicación | Casos al incorporar F-10/11/13 |

Probabilidad, severidad final, superficie concreta y riesgo residual deben revisarse al existir contratos e implementación. No hay un pentest realizado ni un dictamen de seguridad.
