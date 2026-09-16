// Render static design documents. Does not create or modify application code.
const fs=require('fs');
const path=require('path');
const sharp=require('sharp');
const dir=path.resolve(__dirname,'../assets/ux-003');
(async()=>{
 const items=JSON.parse(fs.readFileSync(path.join(dir,'manifest.json'),'utf8'));
 await Promise.all(items.map(i=>sharp(path.join(dir,i.file)).png().toFile(path.join(dir,i.file.replace('.svg','.png')))));
 const main=await sharp(path.join(dir,'c01-accounts.png')).resize({width:960}).toBuffer();
 const dialog=await sharp(path.join(dir,'c02-payment-dialog.png')).extract({left:398,top:171,width:484,height:458}).resize({width:400}).toBuffer();
 await sharp({create:{width:1392,height:632,channels:4,background:'#E9EDED'}}).composite([{input:main,left:16,top:16},{input:dialog,left:984,top:88}]).png().toFile(path.join(dir,'review-overview.png'));
 console.log(items.length+' PNG boards and overview rendered');
})();
