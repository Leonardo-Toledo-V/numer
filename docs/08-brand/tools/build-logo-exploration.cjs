// Tooling for brand artwork only; no application code or project dependencies.
// Usage: node build-logo-exploration.cjs /absolute/path/to/opentype.js
const fs = require('fs');
const path = require('path');
const ot = require(process.argv[2]);
const base = path.resolve(__dirname, '..');
const out = path.join(base, 'assets/logo-exploration');
const inter = ot.loadSync(path.join(base, 'assets/typography/Inter-Medium.ttf'));
const manrope = ot.loadSync(path.join(base, 'assets/typography/Manrope-Medium.ttf'));
const N = 'M0 72V0H10L35 34H23L10 17V72Z M56 0V72H46L21 38H33L46 55V0Z';
function textPath(font, text, start, baseline, size, tracking) {
  let x = start;
  const glyphs = font.stringToGlyphs(text);
  let d = '';
  glyphs.forEach((g, i) => {
    d += g.getPath(x, baseline, size).toPathData(3) + ' ';
    x += g.advanceWidth * size / font.unitsPerEm + tracking;
    if (i < glyphs.length - 1) x += font.getKerningValue(g, glyphs[i+1]) * size / font.unitsPerEm;
  });
  return d;
}
function save(name, title, body, width, height) {
  fs.writeFileSync(path.join(out, name), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" role="img" aria-label="${title}"><title>${title}</title><g fill="#222629">${body}</g></svg>\n`);
}
// Route A: authored split-diagonal N, paired with optically spaced Inter letters.
const aRest = textPath(inter, 'umer', 62, 72, 100, -2.0);
save('numer-a-wordmark.svg', 'Numer — A, precisión; propuesta', `<g transform="translate(4 4)"><path d="${N}"/><path d="${aRest}"/></g>`, 315, 82);
save('numer-a-monogram.svg', 'N de Numer — A; propuesta', `<g transform="translate(8 0)"><path d="${N}"/></g>`, 72, 72);
// Route B: lowercase wordmark; original Manrope glyph contours, optical spacing only.
const b = textPath(manrope, 'numer', 0, 72, 100, -2.5);
save('numer-b-wordmark.svg', 'numer — B, cercanía; propuesta', `<path d="${b}"/>`, 309, 82);
const nGlyph = manrope.charToGlyph('n');
const nBounds = nGlyph.getPath(0, 0, 100).getBoundingBox();
const nScale = 57 / (nBounds.y2 - nBounds.y1);
const nSize = 100 * nScale;
const nWidth = (nBounds.x2 - nBounds.x1) * nScale;
const nX = (72 - nWidth)/2 - nBounds.x1*nScale;
save('numer-b-monogram.svg', 'n de numer — B; propuesta', `<path d="${nGlyph.getPath(nX, 64, nSize).toPathData(3)}"/>`,72,72);
console.log('Four outlined SVG proposals saved. Fonts remain unmodified.');
