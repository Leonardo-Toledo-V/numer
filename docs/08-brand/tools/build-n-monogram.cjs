// Bespoke lowercase n for the icon. No font glyph is imported or cut.
const fs=require('fs'),path=require('path');
const out=path.resolve(__dirname,'../assets/n-monogram');fs.mkdirSync(out,{recursive:true});
// A compact shoulder with a rising inner curve flows into an outward return.
const d='M8 56V24Q8 17 15 17H22V24C26 16 33 12 41 12C53 12 59 20 59 33V43C59 49 62 52 68 52V62C52 62 44 57 44 44V33C44 26 41 23 36 23C28 23 23 30 23 40V56Z';
// Artwork bounds: x8..68, y12..62. Uniform scale 1, then translate to center.
const mark=`<path d="${d}" transform="translate(12 13)"/>`;
const title='Numer · monograma n continuo · propuesta';
fs.writeFileSync(path.join(out,'numer-n-icon.svg'),`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="${title}"><title>${title}</title><rect width="100" height="100" rx="22" fill="#185B56"/><g fill="#F5F6F7">${mark}</g></svg>\n`);
fs.writeFileSync(path.join(out,'numer-n-symbol.svg'),`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="${title}"><title>${title}</title><g fill="#185B56">${mark}</g></svg>\n`);
fs.writeFileSync(path.join(out,'geometry.json'),JSON.stringify({canvas:100,visibleBounds:{x:20,y:25,width:60,height:50},widthPercent:60,heightPercent:50,design:'Single continuous outline; asymmetrical shoulder, variable stroke and curved outward terminal. No diagonal separation.',status:'proposed'},null,2)+'\n');
console.log('Custom n icon and transparent symbol saved.');
