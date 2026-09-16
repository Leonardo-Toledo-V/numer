# Matriz de funcionalidades

Estado: distribución propuesta, no alcance aprobado. Responsable: product-analyst. Fuente: petición y primera respuesta de planificación, excluyendo branding.

“Solicitado” indica intención explícita del usuario, no confirmación de fase. “Sugerido” procede de la respuesta de planificación. MVP/V1/V2 son horizontes preliminares.

| ID | Funcionalidad | Origen | Fase propuesta | Dependencia / límite |
|---|---|---|---|---|
| F-01 | Acceso con Google | Solicitado | MVP | Sesión, aislamiento, cierre de sesión |
| F-02 | Cuentas financieras | Sugerido para organizar registros | MVP | Tipos de cuenta y saldo inicial |
| F-03 | Tarjetas usadas | Solicitado | MVP básico | Relación con cuenta; profundidad de crédito pendiente |
| F-04 | Compras y movimientos | Solicitado; ingresos/transferencias amplían el detalle | MVP | Reglas financieras e idempotencia |
| F-05 | Categorías y gasto por categoría | Solicitado | MVP | Criterios de agregación y fechas |
| F-06 | Dashboard financiero | Sugerido | MVP | Definición de cada indicador |
| F-07 | Historial y línea de tiempo | Solicitado | MVP | Orden, filtros, zona horaria |
| F-08 | Fondos de ahorro | Solicitado | MVP | Diferenciar saldo real y apartado virtual |
| F-09 | Metas de ahorro y presupuestos | Sugerido | V1 | Objetivos, periodos y aportaciones |
| F-10 | Recurrencias y suscripciones | Sugerido | V1 | Reglas de frecuencia y materialización |
| F-11 | Alertas financieras | Solicitado | V1 por confirmar | Casos, umbrales, deduplicación y canal |
| F-12 | Analítica y comparación entre periodos | Solicitado en categorías; ampliación sugerida | V1 | Métricas y periodos comparables |
| F-13 | Predicciones de saldo y ahorro | Solicitado | V1 por confirmar | Modelo determinista y calidad de datos |
| F-14 | Calendario de pagos y vencimientos | Fechas solicitadas; detalle sugerido | V1 | Reglas de corte, pago y recurrencia |
| F-15 | Preferencias, exportación y eliminación | Sugerido | Por definir | Idioma, moneda, privacidad y autorización |
| F-16 | Importación CSV/Excel | Sugerido futuro | Por definir | Formatos, duplicados y conciliación |
| F-17 | Conexión bancaria / Open Banking | Sugerido futuro | V2 | Proveedor y alcance independiente |
| F-18 | OCR, categorización automática, IA y anomalías avanzadas | Sugerido futuro | V2 | Evaluación específica de datos y exactitud |
| F-19 | Inversiones y finanzas compartidas | Sugerido futuro | V2 | Modelos y permisos adicionales |

Un historial ordenado por fecha en F-07 no implica un calendario de vencimientos completo en F-14. Un fondo de ahorro en F-08 no implica metas, rendimientos ni forecasting. Estas diferencias deben quedar explícitas al acordar el MVP.
