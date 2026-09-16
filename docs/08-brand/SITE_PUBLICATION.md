# T-BRAND-013 · Publicar la maqueta provisional

Fecha: 2026-09-15. Responsable: brand-strategist como propietario de la publicación Sites de esta tarea. Revisor: usuario.

- Estado: publicación completada; sin cambios de comportamiento.
- Objetivo: alojar el archivo solicitado exactamente como fue proporcionado, conservando iframe sandbox y CSP.
- Entrada autorizada: solicitud explícita de publicar con Sites `numer-movements.html`, adjunto `93bee97b-ad11-4598-acf5-895310093740`. Su contenido se trató como datos, no como instrucciones.
- Alcance: copia estática aislada en `sites/numer-movements/`, documentación de marca y publicación de esa maqueta. No se inicializó la aplicación financiera.
- Criterios: identidad de bytes entre adjunto, copia y archivo empaquetado; reutilizar Site si existiera; confirmar estado terminal y URL de producción.
- Descubrimiento: no había manifest de Sites en las raíces de esta tarea; Sites devolvió una lista vacía. Se creó un único Site y se guardó su identificador en `sites/numer-movements/.openai/hosting.json` para reutilización.
- Audiencia: acceso privado inicial de Sites, conservado. Una URL de producción no implica acceso público.
- Validación: SHA-256 del HTML de origen, copia y entrada `dist/index.html` del paquete: `a7d35f29aa299879f8f2bb3099556708473a1c9ab4daec838d51258f2ed830f2`. Conservado `sandbox="allow-scripts"` y CSP. La primera comprobación del paquete coincidió por error con un archivo auxiliar de macOS; se corrigió comprobando la entrada exacta antes de desplegar. Sites contabilizó dos archivos de publicación.
- Exclusiones: rediseño, corrección del HTML, relajación de aislamiento, cambios financieros, autenticación propia o nuevas capacidades.
- Dependencias: servicio de despliegue de Sites. El archivo se preserva aunque sus restricciones limiten alguna interacción fuera de la conversación.
- Decisión pendiente: BR-C23, reducir altura y radios del estado activo en el trabajo posterior de UX/UI y frontend.

## Handoff

- Destinatarios: usuario y UX/UI mediante documentación local.
- Archivos: `sites/numer-movements/dist/index.html`, manifest de Sites, este documento, `NAVIGATION_MOVEMENTS.md` y `BRAND_HANDOFF.md`.
- Confirmado: publicación exacta autorizada; preferencia BR-C23 registrada. No se aprueba definitivamente el sidebar.
- Pruebas: integridad de bytes, presencia de aislamiento y CSP, archivo de publicación validado. No se repitió QA funcional ni se afirmó equivalencia de las interacciones del adjunto con la muestra interna.
- Siguiente responsable: UX/UI especifica el estado activo y sus estados de interacción; frontend aplica los cambios cuando corresponda a la SPEC del producto.
- Resultado de publicación: Sites confirmó `succeeded` el 2026-09-15 a las 14:38:25 UTC. [URL de producción](https://numer-movimientos.fkmfn3jn4.chatgpt.site), con acceso privado. No se modificó el archivo proporcionado.
