# Fuentes de la exploración Numer

Descargadas el 2026-09-13 desde Google Fonts. Archivos originales sin modificación. No hay fuentes Apple incluidas. Licencias SIL OFL 1.1 conservadas en [Inter-OFL.txt](Inter-OFL.txt) y [Manrope-OFL.txt](Manrope-OFL.txt).

Metadatos de versión y SHA-256 en [font-metadata.json](font-metadata.json).

Fuente de las URLs: [CSS de Google Fonts](https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@400;500;600&display=swap). La primera ronda conservó Regular y Medium; T-BRAND-005 añade Manrope Semibold desde el [CSS de peso 600](https://fonts.googleapis.com/css2?family=Manrope:wght@600&display=swap), consultado el 2026-09-13. Se mantiene su licencia OFL existente y se registra versión y SHA-256.

- [Inter Regular, origen](https://fonts.gstatic.com/s/inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfMZg.ttf).
- [Inter Medium, origen](https://fonts.gstatic.com/s/inter/v20/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuI6fMZg.ttf).
- [Manrope Regular, origen](https://fonts.gstatic.com/s/manrope/v20/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk79FO_F.ttf).
- [Manrope Medium, origen](https://fonts.gstatic.com/s/manrope/v20/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk7PFO_F.ttf).
- [Manrope Semibold, origen](https://fonts.gstatic.com/s/manrope/v20/xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk4jE-_F.ttf).

El refinamiento tiene un generador separado: [build-logo-refinement.cjs](../../tools/build-logo-refinement.cjs), con el mismo argumento opentype.js. Conserva los originales de la primera ronda y genera únicamente los nuevos SVG y metadatos de la fuente adicional.

El generador de contornos es [build-logo-exploration.cjs](../../tools/build-logo-exploration.cjs); requiere como argumento una ruta local a opentype.js 1.3.4. Se utilizó una copia temporal obtenida de [jsDelivr](https://cdn.jsdelivr.net/npm/opentype.js@1.3.4/dist/opentype.js), sin agregar dependencias a una aplicación ni redistribuir esa herramienta en este directorio. Los archivos TTF no fueron modificados; solo se generaron contornos y espaciado de piezas de marca.
