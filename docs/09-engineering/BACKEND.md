# Plan de backend

Estado: preparación documental; sin servicios ni base configurada. Responsable: backend. Entradas: SRS, reglas del dominio, diseño de software, ERD y matriz RLS.

## Primera entrega técnica propuesta

Cuando se asigne desarrollo, establecer acceso con Google mediante el diseño de Auth elegido, acceso a datos en servidor, esquema mínimo versionado, validación, autorización y pruebas con usuarios sintéticos. La forma concreta de comandos, consultas y transacciones depende de decisiones monetarias y de ledger aún pendientes.

## Contratos pendientes por módulo

| Módulo | Definir antes de implementar |
|---|---|
| Identidad | Alta de perfil, sesión, callback, cierre y recuperación |
| Cuentas/tarjetas | Tipos, moneda, saldo inicial, asociación y ciclo de vida |
| Movimientos | Tipos, signos, corrección, validación y efecto sobre saldo |
| Transferencias | Atomicidad, moneda, referencias e identidad del reintento |
| Ahorro | Cuenta real frente a apartado y relación con disponibilidad |
| Consultas | Agregados, filtros, paginación, caché y aislamiento |

## Forecast y trabajos futuros

Incorporarlos solo cuando producto establezca alcance, supuestos y aceptación. Separar proyecciones de hechos, definir repetición segura y comprobar propiedad de datos en cada ejecución. Los accesos privilegiados requieren un caso explícito y controles revisados por security.

## Evidencia futura de entrega

Migraciones, contratos, pruebas de invariantes y RLS, recuperación, variables requeridas sin valores y resultados de revisión. Los procedimientos de datos se mantienen en `docs/04-database/` para evitar copias divergentes.
