// Brand artwork only. Usage: node build-logo-refinement.cjs /path/to/opentype.js
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const ot = require(process.argv[2]);
const base = path.resolve(__dirname, '..');
const out = path.join(base, 'assets/logo-refinement');
fs.mkdirSync(out, { recursive: true });
const fontFile = path.join(base, 'assets/typography/Manrope-Semibold.ttf');
const font = ot.loadSync(fontFile);
function word(text) {
  let x = 0, d = '';
  const glyphs = font.stringToGlyphs(text);
  glyphs.forEach((g, i) => {
    d += g.getPath(x, 72, 100).toPathData(3) + ' ';
    x += g.advanceWidth * 100 / font.unitsPerEm - 2.5;
    if (i < glyphs.length - 1) x += font.getKerningValue(g, glyphs[i + 1]) * 100 / font.unitsPerEm;
  });
  return d;
}
function save(name, label, defs, body, box) {
  fs.writeFileSync(path.join(out, name), `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${box}" role="img" aria-label="${label}"><title>${label}</title>${defs}<g fill="#222629">${body}</g></svg>\n`);
}
const d = word('numer');
for (const [variant, gap] of [['soft', 3], ['open', 5]]) {
  // A rising diagonal opening crosses only the left stem of the initial n.
  const cut = `M5 ${54-5} L19 ${54-19} L19 ${54-19+gap} L5 ${54-5+gap}Z`;
  const mask = `<defs><mask id="cut-${variant}" maskUnits="userSpaceOnUse" x="0" y="0" width="320" height="90"><rect width="320" height="90" fill="white"/><path d="${cut}" fill="black"/></mask></defs>`;
  save(`numer-b1-${variant}-wordmark.svg`, `numer — Manrope Semibold, corte ${variant === 'soft' ? 'sutil' : 'abierto'}; propuesta`, mask, `<path d="${d}" mask="url(#cut-${variant})"/>`, '0 9 313 70');
}
// Companion uppercase N, drawn independently: rounded joins and diagonal opening.
const mask = '<defs><mask id="split" maskUnits="userSpaceOnUse" x="0" y="0" width="72" height="72"><rect width="72" height="72" fill="white"/><path d="M23 50L47 26L47 20L23 44Z" fill="black"/></mask></defs>';
save('numer-b1-symbol.svg', 'N de Numer, trazos suaves y corte diagonal; propuesta', mask, '<path d="M15 58V14L57 58V14" fill="none" stroke="#222629" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" mask="url(#split)"/>', '0 0 72 72');
const metadataFile = path.join(base, 'assets/typography/font-metadata.json');
const metadata = JSON.parse(fs.readFileSync(metadataFile, 'utf8'));
metadata['Manrope-Semibold'] = { version: font.names.version.en, sha256: crypto.createHash('sha256').update(fs.readFileSync(fontFile)).digest('hex') };
fs.writeFileSync(metadataFile, JSON.stringify(metadata, null, 2) + '\n');
console.log('Saved two wordmark cut treatments and one companion N; original artwork preserved.');
