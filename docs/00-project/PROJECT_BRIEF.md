# Project Brief

Estado: borrador basado en la solicitud. Responsable: orchestrator; colaborador: product-analyst.

## Problema y objetivo

El usuario quiere centralizar sus finanzas y registros de compras para entender dónde gasta, qué tiene ahorrado y qué puede esperar en fechas futuras. La aplicación deberá hacer accesible ese panorama y proteger las peticiones y los datos.

## Usuario inicial

La necesidad de partida es el uso personal del solicitante. Público adicional, disponibilidad pública, cuentas compartidas y modelo de negocio permanecen pendientes; no asumirlos al diseñar el MVP.

## Resultados buscados

- Capturar y consultar movimientos sin confundir gasto, transferencia, deuda y ahorro.
- Conocer el estado de cuentas, tarjetas y fondos con cifras explicables.
- Identificar categorías de gasto y eventos financieros por fecha.
- Consultar estimaciones de ahorro y alertas útiles cuando esas funciones entren en alcance.
- Acceder con Google y mantener privada la información de cada usuario.

## Alcance y restricciones

El conjunto deseado y su reparto preliminar están en [FEATURE_MATRIX](../01-product/FEATURE_MATRIX.md). La selección Next.js, shadcn/ui, Supabase, Vercel y Google está confirmada. No hay versiones elegidas ni cuentas de proveedores verificadas.

La carga manual, uso individual y ausencia de pagos/custodia constituyen una propuesta inicial. Conexión bancaria, OCR, asistente de IA, inversiones y finanzas compartidas fueron sugerencias futuras; no forman parte de un compromiso de entrega.

## Éxito propuesto para la primera versión

Un usuario puede iniciar sesión, configurar cuentas, registrar movimientos, comprender saldos y consultar historial y categorías. Las operaciones financieras satisfacen sus invariantes y las pruebas entre usuarios impiden acceso ajeno. QA debe poder reproducir estos resultados con datos sintéticos.

Las métricas cuantitativas de rendimiento, usabilidad, adopción y disponibilidad se fijarán durante el levantamiento; no existen objetivos numéricos acordados.

## Riesgos de definición

1. Modelar tarjetas y pagos como gastos duplicados.
2. Confundir fondos apartados con dinero adicional al saldo de las cuentas.
3. Presentar predicciones sin explicitar supuestos o calidad de datos.
4. Dar por aprobado un MVP que posterga capacidades solicitadas.
5. Empezar implementación antes de precisar propiedad de datos y reglas críticas.
