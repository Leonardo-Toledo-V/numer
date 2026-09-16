# Wallet · documentación del proyecto

Base documental para planificar una aplicación de finanzas personales y coordinar agentes especializados. **Wallet es un nombre de trabajo.** El proyecto está en definición: todavía no hay aplicación, infraestructura ni pruebas ejecutables.

La documentación recupera la planificación funcional y técnica de la conversación original. Excluye su último bloque de branding. Las propuestas se identifican como tales; no equivalen a decisiones aprobadas.

## Empezar

1. Leer [AGENTS.md](AGENTS.md): reglas compartidas y carga de contexto.
2. Leer [contexto global](docs/00-project/PROJECT_CONTEXT.md): intención, restricciones y estado.
3. Elegir una ficha en [agents/](agents/README.md).
4. Consultar [estado y siguiente trabajo](docs/00-project/STATUS.md), el [flujo SDD](docs/00-project/SDD_WORKFLOW.md) y la especificación de la tarea.
5. Dejar resultados en [docs/](docs/README.md) y preparar un handoff con evidencia.

## Distribución

```text
AGENTS.md                 Reglas para todos los agentes
.codex/agents/*.toml       Perfiles nativos de agentes Codex
agents/                   Fichas de apoyo por especialidad
docs/
  specs/                  Especificaciones que guían las entregas
  00-project/             Contexto, brief, roadmap, decisiones y coordinación
  01-product/             PRD, SRS, glosario, reglas y matriz de funcionalidades
  02-architecture/        Diseño de software y decisiones de arquitectura
  03-security/            Amenazas, requisitos y matriz de acceso
  04-database/            Modelo conceptual y plan de datos
  05-design/              Flujos y criterios de interfaz
  06-testing/             Estrategia de validación y trazabilidad
  07-deployment/          Preparación de despliegue y operación
  08-brand/               Espacio reservado; sin decisiones de marca importadas
  09-engineering/         Entregables de frontend y backend
  templates/             Tareas, handoffs y decisiones
```

Los perfiles TOML definen los agentes nativos y les indican qué contexto y ficha leer. Las fichas Markdown conservan el detalle de responsabilidades. Consultar [configuración de agentes](docs/00-project/CODEX_AGENTS.md). Crear estos archivos no inicia agentes ni tareas automáticamente.

**SDD significa desarrollo guiado por especificaciones:** cada entrega parte de comportamiento y aceptación explícitos, se descompone en plan y tareas, y se verifica contra esa especificación. El [diseño de software](docs/02-architecture/SOFTWARE_DESIGN.md) forma parte del proceso.

El archivo preexistente `BRANDING_AGENT.md` se conserva sin modificaciones y queda fuera de las lecturas comunes y de las fuentes de esta documentación.

**Próximo paso:** resolver las preguntas prioritarias del [PRD](docs/01-product/PRD.md), fijar el alcance inicial y completar las reglas financieras para redactar las primeras especificaciones de producto.

## Repositorio y archivos locales

El remoto del proyecto es [Leonardo-Toledo-V/numer](https://github.com/Leonardo-Toledo-V/numer). Consulta la [política de archivos versionados](docs/07-deployment/GIT_HYGIENE.md) para conocer las exclusiones y los requisitos de las herramientas de diseño.
