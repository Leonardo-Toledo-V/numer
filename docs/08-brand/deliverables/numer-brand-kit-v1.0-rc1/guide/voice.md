# Numer · Voz y tono 0.2

Fecha: 2026-09-15. Responsable: brand-strategist. Estado: **propuesta editorial para revisión del usuario**, no aplicada al sitio ni a una aplicación.

## Encargo y alcance

BR-C24 confirma continuar con la voz: «Continuemos con voz». La referencia creativa conserva la claridad y el cuidado de Apple, con una expresión propia para Numer. Los principios y mensajes de este documento se proponen; todavía no están aprobados. Desarrollan el antecedente BR-P09 sin aprobar automáticamente su eslogan.

La edición 0.2 incorpora la instrucción de varias cuentas/tarjetas y registro sin datos identificativos de tarjeta, BR-C26 a BR-C29, con procedencia y límites en [alcance de marca](context.md). La respuesta «Okey» permite continuar; no se convierte en aprobación de todos los mensajes ni de funciones todavía sin especificar.

## BR-V01 · Personalidad verbal

**Numer habla con claridad, calma y cercanía.** Ayuda a entender lo registrado y a elegir el siguiente paso. Su personalidad se reconoce en la precisión y en la ausencia de presión.

- Claridad: nombrar qué ocurrió, a qué afecta y qué se puede hacer. Preferir «Gasto registrado» a «Operación procesada satisfactoriamente».
- Calma: presentar cambios y errores con la intensidad que requieren. Evitar dramatizar deudas, gastos o periodos sin ahorro.
- Cercanía: tratar de tú, con español natural y sin familiaridad forzada. Preferir «Revisa el importe» a «El usuario deberá validar el campo monetario».
- Respeto: describir hechos sin juzgar hábitos ni capacidad económica. No calificar al usuario de buen o mal ahorrador.

No usar por defecto emojis, exclamaciones, diminutivos, humor sobre dinero, felicitaciones automáticas, cuenta regresiva persuasiva o expresiones como «toma el control de tu futuro financiero». Una confirmación cotidiana no necesita una celebración.

## BR-V02 · Tono según el momento

| Momento | Tratamiento propuesto |
|---|---|
| Bienvenida y primera configuración | Cercano y orientador; una acción concreta por mensaje. |
| Consulta habitual | Breve y factual; conceptos e importes por delante del texto decorativo. |
| Confirmación | Directa; nombrar la acción realmente completada. |
| Error de campo | Específico y útil; explicar cómo corregirlo sin culpar. |
| Fallo o resultado incierto | Preciso sobre lo que se sabe; no afirmar pérdida o éxito sin evidencia. |
| Aviso de deuda o gasto | Sereno; importe, fecha y contexto verificados. |
| Meta alcanzada | Cálido y contenido; reconocer el hecho sin comparar con otras personas. |
| Estimación | Explicitar que es una estimación, sus supuestos y el periodo. |

## BR-V03 · Primera biblioteca de mensajes

Textos propuestos; su condición de uso forma parte de la propuesta. Los importes y fechas de ejemplo son sintéticos.

| ID | Situación | Mensaje | Acción / condición |
|---|---|---|---|
| VC-01 | Bienvenida inicial | «Tus cuentas y tarjetas, en un mismo lugar.» «Organiza tu dinero, tu crédito y tus pagos con claridad.» | Acciones propuestas «Añadir cuenta» y «Añadir tarjeta», solo cuando existan ambos recorridos. Mensaje de marca propuesto, no eslogan aprobado. |
| VC-02 | Historial sin registros | «Aún no tienes movimientos.» «Registra el primero para empezar tu historial.» | «Registrar movimiento». Solo cuando el conjunto completo está vacío. |
| VC-03 | Filtro sin coincidencias | «No hay movimientos con estos filtros.» | «Cambiar filtros», si existe esa acción. No afirmar que no hay datos fuera del filtro. |
| VC-04 | Gasto guardado | «Gasto registrado.» | Solo después de confirmación de persistencia. |
| VC-05 | Importe inválido | «Introduce un importe mayor que cero.» | Junto al campo; no sustituye las otras validaciones que defina producto. |
| VC-06 | Transferencia a la misma cuenta | «Elige una cuenta de destino distinta del origen.» | Mantener los datos introducidos. |
| VC-07 | Fallo de guardado confirmado | «No se guardó el movimiento. Inténtalo de nuevo.» | Solo si se sabe que no hubo escritura y el reintento está protegido contra duplicados. |
| VC-08 | Resultado de guardado incierto | «No pudimos confirmar si se guardó el movimiento.» | UX/UI debe ofrecer comprobación del historial o del estado antes de un nuevo envío. No mostrar VC-07 por un simple timeout. |
| VC-09 | Transferencia propia registrada | «Transferencia registrada.» «Cambió el saldo de tus cuentas, pero el total se mantiene.» | Solo transferencia interna de igual moneda y sin comisión, bajo RN-03 propuesta. No implica ejecución de una transferencia bancaria. |
| VC-10 | Pago de deuda registrado | «Pago de tarjeta registrado.» «La deuda se redujo en $300.00.» | Solo si el modelo y resultado confirmado acreditan esa reducción exacta. El registro no ejecuta un pago bancario. |
| VC-11 | Progreso de ahorro | «Llevas $8,000.00 de tu meta de $20,000.00.» | Vincular a datos comprobados; no llamar rentabilidad a aportaciones. |
| VC-12 | Meta alcanzada | «Alcanzaste tu meta de ahorro.» | Solo al cumplirse la condición de la meta; sin prometer que el dinero seguirá creciendo. |
| VC-13 | Vencimiento conocido | «El pago registrado vence el 20 de septiembre.» | Solo si existe una fecha válida y el aviso corresponde a la obligación. No inventar vencimientos ni órdenes de pago. |
| VC-14 | Proyección | «Ahorro estimado al cierre del mes: $2,400.00.» | Acompañar de acceso a supuestos y fecha de cálculo; capacidad todavía dependiente de producto. |
| VC-15 | Carga | «Cargando movimientos…» | Durante carga real; no reemplazar cifras con cero ni anunciar saldo cero. |
| VC-16 | Sesión finalizada | «Tu sesión terminó. Inicia sesión para continuar.» | Solo si el estado está confirmado. No asegurar conservación de datos sin comprobarla. |

VC-09 a VC-14 son ejemplos condicionados para evaluar la voz, no aprobación de capacidades, fórmulas, fechas o reglas financieras.

### Mensajes para cuentas y tarjetas · edición 0.2

| ID | Situación | Mensaje propuesto | Condición |
|---|---|---|---|
| VC-17 | Alta de tarjeta | «Añade una tarjeta y elige su banco.» | Usar «añadir», sin sugerir vinculación o sincronización bancaria. |
| VC-18 | Explicación de datos | «No te pediremos el número de tarjeta, el nombre del titular, el CVV ni la fecha de vencimiento.» | Debe cumplirse en el flujo completo, no solo en un formulario. |
| VC-19 | Alta completada | «Tarjeta añadida.» | Después de persistencia confirmada; no implica activación bancaria. |
| VC-20 | Elección de banco | «Elige el banco para identificar tu tarjeta.» | El icono identifica; no acredita conexión, validación o asociación comercial. |
| VC-21 | Tarjeta sin deuda registrada | «Aún no has registrado la deuda de esta tarjeta.» | No sustituir ausencia de datos por «No tienes deuda». |
| VC-22 | Datos de deuda | «Registra cuánto debes y los datos de corte y pago.» | Los campos y sus definiciones dependen de producto. |
| VC-23 | Compras a meses | «Consulta lo pendiente de tus compras a meses.» | No añadir «sin intereses» salvo que corresponda a los datos. |
| VC-24 | Crédito de tarjeta | «Crédito disponible» | Mantener separado de «Dinero en tus cuentas». |
| VC-25 | Pago confirmado en el registro | «Pago de tarjeta registrado.» | Registra un hecho; no afirmar «Pagamos tu tarjeta». |
| VC-26 | Periodo de pago | «Pago de este periodo» | Explicitar el concepto real antes de mostrar cifras: mínimo, mensualidades u otro importe. No tratarlos como equivalentes. |

La marca expresa seguridad mediante precisión y transparencia. Evitar «sin datos sensibles», porque deudas y movimientos también lo son. La exclusión confirmada se refiere a datos identificativos de tarjeta, sin limitar los controles de privacidad y seguridad que necesitará el producto.

## BR-V04 · Convenciones editoriales

- Usar Numer con mayúscula inicial en texto; reservar «numer» para el logotipo.
- Usar «tú» en orientación y omitir el pronombre cuando no haga falta. Evitar mezclar «tú», «usted» y «vos».
- Botones con verbos concretos: «Registrar gasto», «Revisar movimiento», «Guardar cambios», «Volver». Nombrar la acción final; evitar «Aceptar» cuando no explica su efecto.
- Títulos en estilo oración. Etiquetas y botones sin punto final; mensajes completos con punto. No usar MAYÚSCULAS para dar urgencia.
- Identificar la moneda cuando pueda haber ambigüedad; formato, zona horaria y moneda definitivos los determina producto.
- Distinguir «saldo en cuentas», «deuda», «ahorro» y «estimación». No sustituir saldo registrado por «dinero disponible» sin definición aprobada.
- Distinguir «Registrar pago» de «Pagar» y «Registrar transferencia» de «Transferir dinero» mientras no haya servicios de ejecución confirmados.
- Preferir fechas explícitas en información que pueda consultarse después. Reservar «hoy» o «mañana» para contextos con zona horaria y actualización fiables.
- En errores, ordenar el texto como hecho conocido → siguiente paso. Detalles técnicos solo cuando ayuden a resolver el problema.
- En notificaciones externas, proponer un texto discreto como «Tienes un aviso en Numer»; la exposición de importes necesita preferencias de privacidad y especificación propias.

## BR-V05 · Criterios de revisión

Un mensaje debe permitir entender qué ocurrió, si es un hecho o una estimación y cuál es la siguiente acción disponible. No debe prometer capacidades que no existen, atribuir un fallo al usuario sin evidencia, duplicar información cercana ni emitir juicios sobre su dinero. La longitud se decide según claridad y espacio, no mediante un máximo arbitrario de caracteres.

Antes de incorporar un mensaje al producto, UX/UI enlaza el ID VC con su estado y criterio de aceptación en la SPEC correspondiente. Producto valida su semántica financiera; frontend lo aplica y QA comprueba que se muestra en el estado correcto. Esta biblioteca no inicia esa implementación.

