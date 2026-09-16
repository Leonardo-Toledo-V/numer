# Numer · Cuentas, tarjetas y dirección de marca

Fecha: 2026-09-15. Responsable: brand-strategist. Registro de instrucciones del usuario y elaboración de marca; no es una especificación funcional ni técnica.

## Instrucciones confirmadas

Origen de BR-C26 a BR-C29: mensaje del usuario del 2026-09-15 que comienza «Okey. Recuerda que al ser una wallet conjunta puedes tener varias tarjetas».

| ID | Confirmado por el usuario | Consecuencia para branding |
|---|---|---|
| BR-C26 | Numer reúne dinero distribuido entre varias cuentas y tarjetas, y deuda de varias tarjetas. | Hablar de una visión conjunta de las finanzas y permitir plural en mensajes. No presentar una sola tarjeta como límite del producto. |
| BR-C27 | Alta de tarjeta con icono del banco, sin número de tarjeta, nombre del titular, CVV ni fecha de la tarjeta. | Explicar el registro de forma transparente; no dibujar numeración ficticia, titular, vencimiento, chip o campos de identificación como parte de la marca. |
| BR-C28 | Registrar deuda, importes a meses, lo que corresponde pagar este mes, corte, periodo de pago, porcentaje de uso y crédito total, libre y usado. | Dar a cada concepto una etiqueta específica; evitar que «saldo» o «disponible» mezclen dinero propio y crédito. |
| BR-C29 | Animaciones con GSAP o Motion en el futuro frontend; no en Sites. Este responsable trabaja únicamente en branding. | Registrar ambas alternativas sin seleccionar ni instalar una. Definir intención expresiva; transferir elección y comportamiento a UX/UI/frontend. |

«Wallet conjunta» describe aquí la visión que reúne cuentas y tarjetas. No confirma cotitularidad, acceso compartido ni múltiples usuarios; esa interpretación queda fuera de esta elaboración de marca. La exclusión de «fecha» se entiende por contexto como fecha identificativa de la tarjeta, por ejemplo vencimiento; no suprime corte y pago, solicitados expresamente. Producto debe conservar esta distinción en su especificación.

## BR-P11 · Posicionamiento propuesto

**Descriptor:** Organizador de finanzas personales.

**Mensaje principal:** Tus cuentas y tarjetas, en un mismo lugar.

**Explicación:** Organiza tu dinero, tu crédito y tus pagos con claridad.

El mensaje expresa reunión de información; no implica que Numer custodie fondos, conceda crédito, sincronice bancos o ejecute pagos. Evitar llamar «tu dinero» a una suma que incluya crédito disponible. La voz mantiene claridad, calma y cercanía, ahora aplicada a varios bancos, cuentas y tarjetas.

## BR-P12 · Confianza desde la identidad

La confianza se expresa con lenguaje preciso, estados reconocibles e información comprensible sobre lo que se pide. Texto propuesto para el alta:

> Añade una tarjeta y elige su banco. No te pediremos el número de tarjeta, el nombre del titular, el CVV ni la fecha de vencimiento.

Usar ese mensaje cuando el flujo real cumpla la exclusión. Los importes de deuda y movimientos también son información financiera sensible: no describir Numer como una aplicación que «no pide datos sensibles» ni afirmar «100% seguro», certificaciones o protección bancaria no verificadas.

Propuesta visual: banco e icono como identificadores secundarios; Numer mantiene tipografía, estructura y acento. Conservar forma y colores originales de los iconos bancarios que se autoricen, sin dar a entender asociación o conexión automática. Prever un identificador textual equivalente para accesibilidad y un recurso neutro si falta el icono. Para varias tarjetas del mismo banco, UX/UI deberá resolver su distinción sin recurrir a números de tarjeta; un alias elegido por el usuario es una propuesta, no un requisito confirmado.

## BR-P13 · Vocabulario de cuentas y crédito

Estas son etiquetas editoriales propuestas; no definen cómo se calculan las cifras.

| Concepto del usuario | Etiqueta propuesta | Precisión necesaria |
|---|---|---|
| Dinero distribuido entre cuentas | Dinero en tus cuentas | Una tarjeta asociada no representa otro saldo que deba sumarse. |
| Deuda de varias tarjetas | Deuda de tus tarjetas | Mostrar deuda separada de dinero propio; agregación requiere reglas de producto. |
| Crédito total | Límite de crédito | Contexto de una tarjeta concreta. |
| Crédito usado | Crédito utilizado | No equiparar automáticamente con deuda al corte. |
| Crédito libre | Crédito disponible | No etiquetar como dinero disponible. |
| Porcentaje de uso | Uso de crédito | Acompañar de contexto de tarjeta; no presentarlo como puntuación de salud financiera. |
| Cuánto debes a meses | Pendiente en compras a meses | No asumir meses sin intereses ni cálculo de intereses. |
| Cuánto toca pagar este mes | Pago de este periodo | Producto debe distinguir mínimo, pago para no generar intereses, mensualidades y monto registrado; no elegirlos silenciosamente. |
| Periodo de corte | Periodo de corte | Distinguir el periodo de su fecha de cierre. |
| Periodo de pago | Periodo de pago / Fecha límite de pago | No intercambiarlos si los datos describen cosas distintas. |

## BR-M01 · Movimiento de marca propuesto

**Intención:** Numer responde con suavidad y continuidad; los cambios ayudan a entender dónde está el usuario y qué acaba de ocurrir.

- Transiciones discretas al navegar y abrir detalles, sin bloquear lectura o acciones.
- Realce breve y contenido al confirmar un registro; sin confeti, rebotes ni celebraciones por usar crédito.
- Conservar legibilidad y estabilidad de los importes; evitar contadores que pasen por valores falsos para decorar la carga.
- Ofrecer una experiencia equivalente con movimiento reducido; ninguna información dependerá de una animación.

GSAP o Motion son alternativas mencionadas por el usuario para el futuro frontend. Duraciones, curvas, librería y ejecución pertenecen a la especificación de UX/UI y frontend. No se modifica Sites ni se instalan dependencias.

## Handoff de las instrucciones fuera de branding

Se conservan aquí para no perder el encargo; no se escribieron requisitos en archivos de otros roles ni se iniciaron agentes.

- Producto/orquestación: incorporar BR-C26 a BR-C28 a la SPEC de cuentas/tarjetas y resolver tipo de tarjeta, relación con cuentas, conceptos de deuda/pago, compras a meses y calendarios. No inferir un modelo de acceso compartido a partir de «conjunta».
- Seguridad/backend: traducir la exclusión de datos identificativos de tarjeta y la petición de seguridad a controles verificables. Este documento no diseña almacenamiento, autorización o cálculos ni acredita seguridad.
- UX/UI: usar vocabulario inequívoco, distinguir tarjetas del mismo banco, retomar BR-C23/BR-C25 sobre la selección del sidebar y definir estados antes de implementación.
- Frontend: considerar GSAP o Motion cuando comience su alcance; no ambas por defecto. Aplicar la dirección BR-M01 conforme a especificación.

