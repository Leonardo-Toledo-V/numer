# Registro de decisiones

Responsable: orchestrator. Fecha de registro inicial: 2026-09-13. Los orígenes remiten a [SOURCE_NOTES](SOURCE_NOTES.md).

| ID | Estado | Decisión o pregunta | Origen / responsable de resolución |
|---|---|---|---|
| DEC-001 | Confirmado | Next.js + shadcn/ui + Supabase + Vercel | SRC-01, usuario |
| DEC-002 | Confirmado | Acceso con cuenta de Google y seguridad de peticiones | SRC-01, usuario |
| DEC-003 | Confirmado | Roles en `agents/`, entregables en `docs/`, contexto global | SRC-03, usuario |
| DEC-004 | Confirmado | Excluir último bloque de branding | SRC-03, usuario |
| DEC-005 | Propuesto | Gestor de registros sin custodia ni ejecución de pagos | SRC-02; producto y usuario |
| DEC-006 | Propuesto | MVP/V1/V2 según matriz inicial | SRC-02; producto y usuario |
| DEC-007 | Propuesto | App Router, TypeScript, DAL, Auth SSR, RLS | SRC-02; architect y security |
| DEC-008 | Propuesto | Ledger como base del saldo, con posibles snapshots | SRC-02; producto, architect y backend |
| DEC-009 | Propuesto | Motor de proyecciones determinista y explicable | SRC-02; producto y architect |
| DEC-010 | Pendiente | Monedas, zona horaria, idioma y reglas temporales | product-analyst; usuario |
| DEC-011 | Pendiente | Tratamiento de crédito, pagos, ahorro y correcciones | product-analyst; usuario |
| DEC-012 | Propuesto | MFA y operaciones que requerirían segundo factor | SRC-02; security y producto |
| DEC-013 | Pendiente | Usuarios, carga manual/importación y alcance de lanzamiento | product-analyst; usuario |
| DEC-014 | Confirmado | Usar perfiles de agentes TOML; conservar Markdown como documentación de apoyo | SRC-04, usuario, 2026-09-14; formato concretado con documentación oficial |
| DEC-015 | Confirmado | SDD significa desarrollo guiado por especificaciones y se aplica como metodología del proyecto | SRC-04, usuario, 2026-09-14 |

Para resolver: añadir fecha, responsable, evidencia de decisión, alternativas relevantes y documentos afectados. No borrar antecedentes; señalar decisiones sustituidas. Las decisiones técnicas extensas usan ADRs en `docs/02-architecture/adr/` y se enlazan aquí cuando cambian restricciones globales.
