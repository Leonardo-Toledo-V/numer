# UX-FB01 · Corrección de dirección visual

2026-09-16 · Responsable: UX/UI · Seguimiento de T-UX-002.

**UX-R01 · Confirmación posterior del usuario, 2026-09-16:** «Tú jamás vas a modificar frontend. Puedes recomendar, más no modificar. Tu tarea es ser el UX/UI de Numer». Es una restricción permanente de este agente; sustituye cualquier redacción anterior que la tratara solo como ausencia temporal de autorización. El usuario pide continuar la siguiente fase de UX/UI: [T-UX-003](T-UX-003.md).

## Confirmado por el usuario

- No volver a usar el complemento de Figma. El acabado pendiente en esa herramienta deja de ser una acción prevista.
- Las maquetas W01–W10 se rechazan en su composición visual: textos e inputs demasiado grandes; formas y distribución deficientes; interfaz poco intuitiva, moderna y minimalista.
- Los colores y los textos agradan. Conservar identidad y contenido; revisar tamaño, peso, posición y agrupación tipográfica.
- Se solicitan patrones de interfaz coherentes con shadcn/ui.
- La posibilidad de mejorar al generar frontend es una expectativa, no autorización para iniciar su implementación.

## Diagnóstico UX/UI

Se sobredimensionaron campos, botones, paneles y espacios entre grupos. La composición colocó contenido escaso en contenedores grandes, con acciones alejadas de los datos y jerarquía insuficiente entre encabezados, etiquetas, ayuda e importes. La revisión de render y contraste anterior no acreditó calidad de diseño ni aceptación del usuario.

## Criterios para la próxima propuesta

1. Diseñar primero una pantalla representativa y un formulario, con densidad compacta y patrones de shadcn/ui como referencia. Revisarlos antes de extender la composición a todos los recorridos.
2. Controles y tipografía proporcionados a su función; distinguir tamaño visual y superficie de interacción. Definir dimensiones en contexto de escritorio/móvil y comprobar legibilidad, sin reducir todo mediante una escala global.
3. Distribuir por tarea: encabezado breve, acción principal reconocible, datos relacionados próximos, etiquetas estables y acciones junto al formulario. Eliminar columnas auxiliares y espacio vacío sin función.
4. Reservar tarjetas y fondos para grupos que los necesiten; utilizar filas, separadores y alineaciones consistentes. Radios moderados y coherentes, sin trasladar la geometría del sidebar a todos los componentes.
5. Conservar marca, paleta y contenido útil. UX-A01 sigue siendo una aprobación localizada del sidebar; no aprueba las formas y distribución del resto de la aplicación.
6. Evaluar composición y tarea completa en una muestra realista. Los controles de integridad documental y contraste son necesarios, pero no bastan para aprobar UX/UI.

## Handoff y alcance

Destinatarios: UX/UI, orquestador y futuro frontend. W01–W10 y su ZIP/Figma quedan como antecedentes de contenido y escenarios, **no como referencia visual para implementar**. Los flujos, benchmark y casos conservan su estado de propuestas/documentación; el rechazo visual no valida su usabilidad.

Siguiente responsable: UX/UI. Revisar una muestra compacta antes de fijar nuevos tokens y ampliar pantallas. Una futura revisión en navegador puede facilitar el ajuste, pero la estructura debe corregirse deliberadamente: usar shadcn/ui por sí solo no resuelve distribución o jerarquía. No hay frontend autorizado en esta corrección.

Validación de esta actualización: revisión de coherencia documental y enlace desde el índice, wireframes, sistema y handoff. No se generaron nuevas maquetas, no se ejecutaron pruebas de interfaz y no se llamó al complemento de Figma.
