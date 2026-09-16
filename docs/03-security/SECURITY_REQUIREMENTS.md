# Requisitos de seguridad

Estado: controles propuestos; no implementados ni verificados. Responsable: security. Relación: RNF-01/03 y RF-01/03. La necesidad de asegurar las peticiones es explícita; el mecanismo detallado requiere revisión técnica.

| ID | Control requerido en el diseño | Evidencia prevista |
|---|---|---|
| SEG-01 | Verificar identidad y sesión en cada operación protegida | Solicitudes sin sesión, inválidas y expiradas rechazadas |
| SEG-02 | Autorizar recursos y sus relaciones por usuario; RLS como control de persistencia | Pruebas A/B para SELECT, INSERT, UPDATE y DELETE |
| SEG-03 | Validar entradas en servidor y proteger invariantes en base de datos cuando corresponda | Entradas alteradas y operaciones parciales no persisten |
| SEG-04 | Minimizar tarjetas y datos financieros | No almacenar PAN completo, CVV, PIN o contraseñas bancarias; muestras sintéticas |
| SEG-05 | Mantener secretos fuera del cliente, repositorio y logs | Revisar configuración, bundles y mensajes; ningún secreto en variables públicas |
| SEG-06 | Restringir privilegios elevados a casos explícitos de servidor | Uso privilegiado inventariado, alcance mínimo y auditoría; no reemplazar acceso ordinario con RLS |
| SEG-07 | Proteger sesión y flujo de autenticación | Revisar redirecciones, callback, cookies, validación del flujo y cierre de sesión |
| SEG-08 | Evitar repetición, abuso y efectos duplicados | Idempotencia financiera y límites de uso definidos según amenaza |
| SEG-09 | Auditar acciones sensibles con datos mínimos | Registrar acción, actor y referencia, sin tokens ni detalle financiero innecesario |
| SEG-10 | Separar entornos y asegurar recuperación | Datos sintéticos fuera de producción, secretos por entorno y ensayo de restauración |
| SEG-11 | Diseñar exportación y borrado cuando entren en alcance | Autorización, confirmación de intención y tratamiento de datos derivados |

## Decisiones abiertas

MFA fue sugerido; no está confirmado. Seguridad y producto deben decidir si se incluye, qué operaciones exigen autenticación reforzada y cómo funciona recuperación. También quedan pendientes retención, eliminación, auditoría, cuotas y canales de notificación.

La implementación de OAuth, cookies, RLS y privilegios debe contrastarse con documentación oficial de las versiones elegidas. Este documento define objetivos de control, no acredita cumplimiento legal ni reemplaza pruebas.
