// Selected lowercase n; normalize visible glyph bounds to 80% of square height.
// Usage: node build-n-favicon.cjs /path/to/opentype.js
const fs=require('fs'),path=require('path');
const ot=require(process.argv[2]);
const base=path.resolve(__dirname,'..'),out=path.join(base,'assets/n-favicon');fs.mkdirSync(out,{recursive:true});
const font=ot.loadSync(path.join(base,'assets/typography/Manrope-Semibold.ttf'));
const glyph=font.charToGlyph('n').getPath(0,72,100),b=glyph.getBoundingBox();
const scale=51.2/(b.y2-b.y1),width=(b.x2-b.x1)*scale;
const x=(64-width)/2-b.x1*scale,y=6.4-b.y1*scale;
for(const [variant,gap] of [['standard',3],['small',6]]){
 const defs=`<defs><mask id="cut" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="80"><rect width="64" height="80" fill="white"/><path d="M5 49L19 35L19 ${35+gap}L5 ${49+gap}Z" fill="black"/></mask></defs>`;
 const mark=`<g transform="translate(${x.toFixed(6)} ${y.toFixed(6)}) scale(${scale.toFixed(6)})"><path fill="#F5F6F7" d="${glyph.toPathData(4)}" mask="url(#cut)"/></g>`;
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Numer, n minúscula al 80 por ciento de altura"><title>Numer · n al 80% · ${variant}</title>${defs}<rect width="64" height="64" rx="14" fill="#185B56"/>${mark}</svg>\n`;
 fs.writeFileSync(path.join(out,`numer-n-${variant}.svg`),svg);
}
fs.writeFileSync(path.join(out,'geometry.json'),JSON.stringify({canvas:64,glyphHeight:51.2,heightPercent:80,glyphWidth:width,widthPercent:width/64*100,marginTop:6.4,marginBottom:6.4,marginLeft:(64-width)/2,marginRight:(64-width)/2,scale,translation:{x,y},gapStandard:3,gap16px:6,note:'80% means visible glyph height, with uniform scaling. The small variant widens only the diagonal opening.'},null,2)+'\n');
console.log(JSON.stringify({heightPercent:80,widthPercent:width/64*100}));
