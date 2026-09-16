// Native vector brand exploration. Usage: node build-symbol-exploration.cjs /path/to/opentype.js
const fs=require('fs'),path=require('path');
const ot=require(process.argv[2]);
const base=path.resolve(__dirname,'..'),out=path.join(base,'assets/symbol-exploration');
fs.mkdirSync(out,{recursive:true});
function save(name,title,content){fs.writeFileSync(path.join(out,name),`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="${title}"><title>${title}</title>${content}</svg>\n`);}
save('numer-distribution.svg','Numer — Distribución, símbolo propuesto','<defs><mask id="division" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64"><rect width="64" height="64" fill="white"/><path d="M0 61L61 0H67L0 67Z M0 28H39L33 34H0Z" fill="black"/></mask></defs><rect x="6" y="6" width="52" height="52" rx="15" fill="#185B56" mask="url(#division)"/>');
save('numer-reserve.svg','Numer — Reserva, símbolo propuesto','<g fill="#185B56"><path d="M8 23Q8 18 13 18Q18 18 18 23V36Q18 49 32 49Q46 49 46 36V23Q46 18 51 18Q56 18 56 23V36Q56 59 32 59Q8 59 8 36Z"/><rect x="27" y="5" width="22" height="16" rx="5" transform="rotate(-35 38 13)"/></g>');
const font=ot.loadSync(path.join(base,'assets/typography/Manrope-Semibold.ttf'));
const d=font.charToGlyph('n').getPath(0,72,100).toPathData(3);
// Same lowercase letter and subtle diagonal cut as the selected wordmark.
save('numer-lowercase-n.svg','Numer — n minúscula con corte; alternativa de respaldo','<defs><mask id="n-cut" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="80"><rect width="64" height="80" fill="white"/><path d="M5 49L19 35L19 38L5 52Z" fill="black"/></mask></defs><g transform="translate(5.6 -5.8) scale(.84)"><path fill="#185B56" d="'+d+'" mask="url(#n-cut)"/></g>');
console.log('Two conceptual symbols and lowercase fallback saved; wordmark unchanged.');
