# T-008 · Preparar y publicar el repositorio GitHub

- Estado: en curso; preparación local terminada, publicación pendiente de verificar.
- Responsable: orchestrator, mantenimiento de Git; destinatario: usuario.
- Objetivo: subir el proyecto a `Leonardo-Toledo-V/numer` omitiendo información privada y artefactos locales innecesarios.
- Especificación: mantenimiento de repositorio sin comportamiento nuevo de producto; no requiere SPEC funcional.
- Entradas: solicitud explícita del usuario del 2026-09-16, contexto global, estado y ficha de orchestrator.
- Archivos: `.gitignore`, README, notas de procedencia, seis herramientas con rutas personales, documentación de publicación y estado. Configuración local de Git y selección de archivos a versionar.
- Exclusiones: inicializar aplicación, despliegues, modificar reglas de producto, eliminar archivos locales o sobrescribir historial remoto.
- Dependencias: acceso de escritura al repositorio indicado. Consulta inicial del remoto completada sin referencias existentes.
- AC-01: remoto exacto y rama `main` configurados.
- AC-02: exclusiones verificadas y selección revisada sin indicios de credenciales.
- AC-03: commit local publicado y hash remoto igual al local.
- Validación: reglas de ignore, revisión de archivos, patrones de secretos, sintaxis de herramientas modificadas y comprobación de referencias Git.
- Decisiones: conservar los entregables útiles, omitir ZIP duplicados y copia local de hosting; usar noreply local.
- Handoff: [T-008](../handoffs/T-008-github.md).
