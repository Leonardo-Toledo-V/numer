const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const out = path.resolve(__dirname, '../assets/ux-002');
(async () => {
 const items = JSON.parse(fs.readFileSync(path.join(out, 'wireframe-manifest.json'), 'utf8'));
 await Promise.all(items.map(item => sharp(path.join(out,item.file)).png().toFile(path.join(out,item.file.replace('.svg','.png')))));
 const chosen=['w02-accounts','w03-card','w04-payment','w05-review'];
 const layers=await Promise.all(chosen.map(async (name,i)=>({input:await sharp(path.join(out,name+'.png')).resize({width:700}).toBuffer(),left:(i%2)*732+16,top:Math.floor(i/2)*590+16})));
 await sharp({create:{width:1464,height:1180,channels:4,background:'#FFFFFF'}}).composite(layers).png().toFile(path.join(out,'wireframes-overview.png'));
 console.log('Rendered '+items.length+' wireframes and overview.');
})();
