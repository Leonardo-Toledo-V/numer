# Casos de seguridad

Estado: diseño de pruebas; todos no ejecutados. Responsable: qa; revisor: security.

| ID | Intento | Resultado esperado |
|---|---|---|
| TS-01 | Consultar o escribir sin sesión, con sesión inválida o expirada | Rechazo sin filtrar datos |
| TS-02 | Usuario A lee cuentas, movimientos, tarjetas o fondos de B por ID | Sin datos ajenos, incluso al consultar directamente con el rol sujeto a RLS |
| TS-03 | A inserta registro con propietario B | Rechazo y ningún registro persistido |
| TS-04 | A actualiza/elimina registro de B o cambia propietario de uno propio | Rechazo; datos originales intactos |
| TS-05 | A vincula movimiento propio a cuenta, categoría, tarjeta o fondo de B | Rechazo de la relación; sin efectos parciales |
| TS-06 | Manipular tipo, importe, moneda o fecha omitiendo validación cliente | Validación en servidor y/o restricciones rechazan la entrada inválida |
| TS-07 | Manipular callback/redirección o reutilizar flujo de sesión fuera de su contrato | Rechazo conforme al diseño de autenticación acordado |
| TS-08 | Inspeccionar recursos cliente, errores y configuración pública | No aparecen claves privadas, tokens de terceros o privilegios elevados |
| TS-09 | Consultar agregados, vistas y cachés tras alternar A/B | Ninguna reutilización de resultados financieros de otro usuario |

También probar operaciones legítimas equivalentes: una política que deniega todo no acredita una funcionalidad correcta. Anotar rol usado y distinguir pruebas de aplicación de pruebas RLS. Los casos privilegiados y futuras exportaciones, notificaciones o finanzas compartidas requieren escenarios específicos cuando existan.
