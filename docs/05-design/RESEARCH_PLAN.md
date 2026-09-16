# Numer · Investigación, hipótesis y pruebas

Versión 0.1 · 2026-09-16 · UX/UI · T-UX-002. Estado: investigación documental realizada; investigación primaria preparada, no ejecutada. No existen entrevistas, personas validadas, citas de usuarios de prueba o resultados de usabilidad en esta entrega.

## Preguntas y método

| Pregunta | Método propuesto | Evidencia que permitiría decidir |
|---|---|---|
| ¿Quién usará la primera versión y en qué contexto? | Conversación de descubrimiento con promotor; 4–6 entrevistas si se abre a otras personas | Contexto real, herramientas actuales, tareas frecuentes y límites de privacidad |
| ¿Se encuentran tarjetas y pagos bajo Cuentas? | Tree test con cinco tareas sobre NAVIGATION | Primer destino y explicación; comparar etiqueta extendida si falla |
| ¿Se distinguen deuda, crédito disponible y pago del periodo? | Prueba moderada con wireframes y preguntas de comprensión | Respuestas en palabras del participante; errores de interpretación |
| ¿El registro contextual reduce errores? | Comparar alta desde historial y desde cuenta | Correcciones de cuenta/tipo, pasos, confianza y finalización |
| ¿Cómo se interpreta un fallo de red? | Escenario simulado sin persistencia | Intención de reintento y comprensión de estado incierto |
| ¿Qué necesita estar al inicio? | Priorizar necesidades observadas + decisiones de producto | Evidencia por problema, frecuencia y consecuencia, no lista de preferencias |

Se planteó al usuario elegir público: uso propio primero / personas independientes / hogares compartidos. Sin respuesta, trabajar provisionalmente con una persona que administra sus finanzas; esto no aprueba uso individual ni descarta acceso compartido. Registrar cualquier respuesta en decisiones antes de cambiar permisos o alcance.

## Perfil de trabajo provisional y JTBD

Hipótesis de perfil, no persona validada: alguien que distribuye dinero entre cuentas y usa varias tarjetas, necesita registrar compras y anticipar pagos. No atribuir edad, ingresos, ocupación o emociones observadas sin investigación.

- UX-J01: al hacer una compra, quiero registrarla en el instrumento correcto para que el historial explique mis cifras.
- UX-J02: al revisar tarjetas, quiero distinguir deuda, crédito y obligaciones del periodo para entender qué información tengo registrada.
- UX-J03: al apartar ahorro, quiero reconocer dónde está incluido para no sumar dinero dos veces.
- UX-J04: al volver después de varios días, quiero identificar datos faltantes o desactualizados para saber qué revisar.

## Journey propuesto, por validar

| Momento | Objetivo | Fricción hipotética | Respuesta de diseño | Señal para observar |
|---|---|---|---|---|
| Preparar | Representar cuentas/tarjetas | No saber qué saldo inicial poner | Fecha de referencia, ayuda contextual, desconocido distinto de cero | Solicitudes de ayuda y errores de referencia |
| Registrar | Capturar un hecho | Confundir cuenta, tarjeta o tipo | Contexto visible, campos por operación | Cambio de origen/tipo antes de confirmar |
| Comprender | Revisar situación | Confundir crédito con dinero propio | Bloques separados, fuentes enlazadas | Explicación de cada indicador |
| Anticipar | Ver próximas obligaciones | Interpretar previsión como pago hecho | Estado previsto/registrado y fecha/fuente | Confusión detectada en relato |
| Corregir | Recuperarse de error | Crear duplicado o perder datos | Estado incierto y corrección trazable | Acción elegida después del fallo |

## Guion de entrevista de 25–35 minutos

Explicar propósito y uso de notas; consentimiento separado si se desea grabar. No solicitar credenciales ni estados de cuenta. Trabajar con ejemplos sintéticos.

1. Describe la última vez que registraste o revisaste tus finanzas. ¿Qué intentabas resolver?
2. ¿Qué herramientas usaste y en qué momento cambiaste de una a otra?
3. ¿Cómo distingues tus tarjetas y cuentas cuando eliges dónde registrar algo?
4. ¿Cómo sabes qué significa lo que toca pagar este mes? ¿De dónde obtienes ese dato?
5. Cuéntame un error o duda reciente al registrar una compra o un pago.
6. ¿Qué revisas antes de confiar en un total? ¿Qué harías si falta un dato?
7. ¿Qué información evitarías registrar o mostrar en una pantalla compartida?
8. ¿Qué tarea te gustaría resolver primero con Numer? Evitar sugerir funciones como respuesta.

## Prueba moderada propuesta de 35–45 minutos

Primera ronda: 5 participantes del segmento elegido como muestra cualitativa, sin pretender representatividad estadística. Si la primera versión es para el promotor, comenzar por su recorrido y luego contrastar con otras personas antes de generalizar. Incluir distintos niveles de familiaridad financiera; agregar sesiones con teclado/tecnología de asistencia según reclutamiento y alcance.

Usar casos UX-C01 a UX-C20, repartidos para no fatigar: una sesión puede cubrir 6–8 tareas prioritarias. Dar una meta, no el nombre del control. Moderador neutral: «¿Qué esperabas que pasara?», no enseñar cómo completar. Separar problema del prototipo de problema de navegación.

Medir por tarea: éxito independiente / con ayuda / no completada; primer clic, retrocesos, errores críticos, tiempo contextual, confianza antes/después y dificultad percibida de 1–7. Tiempos no son metas de rendimiento aprobadas. No recoger importes/conceptos reales en analítica.

## Criterios de iteración propuestos

- Cualquier confusión que pueda duplicar un movimiento o mezclar dinero y crédito se trata como bloqueante de diseño, aunque ocurra una vez.
- Objetivo exploratorio: 4 de 5 completan cada tarea principal sin ayuda. Es señal de iteración, no certificación ni garantía sobre toda la población.
- Si dos personas no encuentran una tarjeta bajo Cuentas, probar etiqueta extendida antes de añadir otro destino.
- Cerrar hallazgo exige evidencia de una nueva prueba o inspección apropiada; cambiar el dibujo no prueba comprensión.

## Registro y backlog de investigación

Plantilla por observación: ID de sesión anónimo, tarea, conducta observada, cita consentida si existe, contexto, severidad, evidencia, hipótesis causal, cambio y siguiente prueba. Distinguir observación de interpretación.

No ejecutado: entrevistas, tree test, pruebas moderadas, card sorting (solo si la organización resulta confusa), comparación A/B (solo con tráfico suficiente), análisis postlanzamiento y validación con tecnologías de asistencia. Diseñar un service blueprint completo no aporta aún mientras custodia/sincronización y soporte no estén definidos; reevaluar después de UX-P01/04. No fabricar mapas de empatía como hechos sin entrevistas.

Base metodológica: [NN/g, heurísticas](https://www.nngroup.com/articles/ten-usability-heuristics/) para evaluación experta; las pruebas con personas son una fuente distinta. Plan y criterios específicos anteriores son elaboración propia para Numer.
