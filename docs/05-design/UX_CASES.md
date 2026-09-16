# Numer · Casos de experiencia y revisión experta

Versión 0.1 · 2026-09-16 · UX/UI · T-UX-002. Casos preparados, no ejecutados con personas ni backend. Severidad: S3 impide tarea o puede inducir error financiero; S2 genera confusión/recorrido extra; S1 afecta claridad menor. Es estimación experta, no frecuencia observada.

## Mejoras priorizadas

| ID / prioridad | Antes | Después propuesto | Por qué / trazabilidad |
|---|---|---|---|
| UX-I01 · S3 | Pago, compra y transferencia pueden parecer salidas equivalentes | Tipos y efectos explícitos en captura/detalle | Prevención de doble conteo; UX-F04/05/07, RN-05/06 |
| UX-I02 · S3 | Guardado real e incierto sin diseño en maqueta | Pendiente / confirmado / fallo / incierto con recuperación | Visibilidad y control; UX-E05 a E08 |
| UX-I03 · S3 | Dato no informado sin representación propia | «Sin registrar», fecha/fuente y acción de completar | Evitar falsa deuda cero; BR-C28 |
| UX-I04 · S2 | Identificación de una sola tarjeta | Banco + alias en lista, selector y detalle | Reconocimiento sin datos de tarjeta; BR-C26/27 |
| UX-I05 · S2 | Totales de periodo junto a filtro de lista | Ámbitos rotulados y filtro persistente al volver | Correspondencia y orientación; UX-F09 |
| UX-I06 · S2 | Captura genérica repetitiva | Contexto propuesto y visible desde cuenta/tarjeta | Menor esfuerzo sin ocultar origen; UX-F04/07 |
| UX-I07 · S2 | Alta ausente | Inicio breve con primera cuenta o tarjeta y siguiente acción | Llegar a primer valor sin completar todo un cuestionario |
| UX-I08 · S2 | Cuotas/fechas no diseñadas | Previsto frente a registrado, fuentes y detalle de plan | No aparentar pagos ejecutados; UX-F08/12 |
| UX-I09 · S2 | Responsividad acreditada solo en muestras anteriores | Casos de texto amplio, zoom, teclado y altura útil | Accesibilidad y recuperación; UX-Q03/04 |
| UX-I10 · S1 | Activo voluminoso | Selección 38 px, radio 8 px, interacción 44 px | UX-A01 aprobado; nueva implementación aún inexistente |

Método: revisión de evidencia local UX-O01 a UX-O08 y contraste con benchmark. Se cubren visibilidad, correspondencia, control, consistencia, prevención, reconocimiento, eficiencia, jerarquía, recuperación y ayuda como lentes de evaluación. No se certifica una auditoría completa mediante capturas.

## Matriz de escenarios

| Caso | Tarea / variante | Resultado de experiencia esperado | Relación / estado |
|---|---|---|---|
| UX-C01 | Acceso Google cancelado o fallido | Regreso comprensible, sin espacio vacío ni acceso a datos | UX-F01/E09; preparado |
| UX-C02 | Primera entrada sin registros | Primera cuenta o tarjeta identificable; sin total falso | UX-F02/03/E02; preparado |
| UX-C03 | Dos tarjetas del mismo banco | Identificarlas por alias y contexto, sin número/titular | UX-P05; probar alias |
| UX-C04 | Compra desde cuenta | Cuenta visible y editable; importe/fecha claros; detalle tras éxito | UX-F04; preparado |
| UX-C05 | Transferencia A→A | Error asociado y corrección sin borrar importe | RF-05; preparado |
| UX-C06 | Pago a tarjeta | Origen/destino/importe/fecha visibles; se entiende que registra un pago | UX-F07, UX-P01/06; preparado |
| UX-C07 | Doble activación | Una solicitud lógica; pendiente visible; no dos confirmaciones | RN-04; contrato pendiente |
| UX-C08 | Red perdida después de enviar | No asegurar fallo ni éxito; consultar/reintentar misma operación | UX-E08; contrato pendiente |
| UX-C09 | Filtrar y abrir detalle | Entender ámbito de total; volver restaura filtro/posición | UX-F09; preparado |
| UX-C10 | Sin datos frente a cero real | «Sin registrar» distinto de «0»; explicación apropiada | UX-E02/10; preparado |
| UX-C11 | Compra a meses | Separar importe de compra, plan/cuota prevista y hechos | UX-F08; UX-P06/07 pendientes |
| UX-C12 | Fecha inexistente/fin de mes | Validación y explicación según regla; no cambiar silenciosamente | RN-08; UX-P07 pendiente |
| UX-C13 | Ahorro ya incluido en cuenta | Entender ubicación y total sin sumarlo dos veces | RF-08; UX-P08 pendiente |
| UX-C14 | Corrección concurrente/devolución | Revisar datos actuales y consecuencias antes de confirmar | UX-F11; UX-P10 pendiente |
| UX-C15 | Cerrar formulario con cambios | Continuar o descartar explícitamente; regreso a contexto | UX-F04; preparado |
| UX-C16 | Sesión expirada en captura | Retirar información protegida; explicar retorno y límite del borrador | RF-01; contrato seguridad pendiente |
| UX-C17 | Teclado/lector de pantalla | Etiquetas, foco lógico, errores anunciados, retorno de diálogo | RNF-04; prueba pendiente |
| UX-C18 | 320 px, texto 200%, importe largo y teclado móvil | Sin cortar dígitos/acciones; reorganizar o desplazar contenido accesiblemente | UX-Q04; prueba pendiente |
| UX-C19 | Ocultado y movimiento reducido | Sin fugas en detalle/texto accesible; misma información sin desplazamiento | UX-F13/Q07; prueba pendiente |
| UX-C20 | Proyección/alerta incompleta o antigua | Fecha/supuestos/limitación visibles; no aparece como hecho | RF-11/12; fase pendiente |

Casos adicionales al ampliar alcance: importación y conciliación, comisiones, monedas distintas, sobrepagos, saldos negativos, límite cero, archivo de cuenta con movimientos, exportación y eliminación de cuenta. No diseñar resultados financieros para ellos sin producto.

## Condición de entrega a frontend

SPEC versionada y alcance acordado; preguntas críticas resueltas; wireframes con estados; tokens/componentes revisados; textos y ejemplos calculables; comportamiento teclado/móvil; contratos de guardado/error/permisos; casos vinculados a AC. QA marca ejecutado solo con evidencia real. Este paquete satisface preparación UX, no esas validaciones de producto.
