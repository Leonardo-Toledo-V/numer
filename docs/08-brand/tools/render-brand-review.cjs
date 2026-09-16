const fs=require('fs'),path=require('path');
const r=require;
const root=path.resolve(__dirname,'..'),kit=path.join(root,'deliverables/numer-brand-kit-v1.0-rc1'),out=path.join(root,'assets/brand-review');
(async()=>{
 const browser=await r('playwright').chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const page=await browser.newPage({viewport:{width:1300,height:800},deviceScaleFactor:1});
 const source=fs.readFileSync(path.join(kit,'wordmark/numer-wordmark-petroleum.svg'),'utf8');
 await page.setContent(source);const box=await page.locator('svg > g').evaluate(e=>{const b=e.getBBox();return{x:b.x,y:b.y,width:b.width,height:b.height};});
 const files=['wordmark/numer-wordmark-petroleum.svg','wordmark/numer-wordmark-porcelain.svg','wordmark/numer-wordmark-graphite.svg','symbol/numer-symbol-petroleum.svg','symbol/numer-symbol-porcelain.svg','symbol/numer-symbol-graphite.svg','icon/numer-icon.svg'];
 for(const file of files){const width=file.startsWith('wordmark')?1252:400,height=file.startsWith('wordmark')?280:400;await page.setViewportSize({width,height});await page.setContent('<style>html,body{margin:0;padding:0;background:transparent}svg{display:block;width:100%;height:100%}</style>'+fs.readFileSync(path.join(kit,file),'utf8'));await page.screenshot({path:path.join(out,path.basename(file,'.svg')+'.png'),omitBackground:true});}
 const rows=[];
 for(const bg of ['#F5F6F7','#185B56']){const ink=bg==='#F5F6F7'?'petroleum':'porcelain';rows.push('<section style="background:'+bg+';color:'+(ink==='petroleum'?'#222629':'#F5F6F7')+'"><h2>'+ink+'</h2><div class="samples">'+[64,80,96,128].map(w=>'<figure><img style="width:'+w+'px" src="data:image/svg+xml;base64,'+fs.readFileSync(path.join(kit,'wordmark/numer-wordmark-'+ink+'.svg')).toString('base64')+'"><figcaption>'+w+' px de caja</figcaption></figure>').join('')+'</div></section>');}
 rows.push('<section><h2>Icono aprobado</h2><div class="samples">'+[16,24,32,48].map(w=>'<figure><img width="'+w+'" height="'+w+'" src="data:image/svg+xml;base64,'+fs.readFileSync(path.join(kit,'icon/numer-icon.svg')).toString('base64')+'"><figcaption>'+w+' px</figcaption></figure>').join('')+'</div></section>');
 const html='<!doctype html><html lang="es"><meta charset="utf-8"><style>body{margin:0;background:#F5F6F7;font:14px Arial;color:#222629}section{padding:30px 36px}h2{font-size:14px;font-weight:400;margin:0 0 24px}.samples{display:flex;align-items:center;gap:40px}figure{margin:0;min-width:110px}img{display:block}figcaption{font-size:12px;margin-top:18px}</style>'+rows.join('')+'</html>';
 fs.writeFileSync(path.join(out,'size-review.html'),html);await page.setViewportSize({width:800,height:500});await page.setContent(html);await page.screenshot({path:path.join(out,'size-review.png'),fullPage:true});
 fs.writeFileSync(path.join(out,'render-verification.json'),JSON.stringify({browser:await browser.version(),wordmark_visible_bounds:box,assets_rendered:files,wordmark_widths:[64,80,96,128],icon_sizes:[16,24,32,48],deviceScaleFactor:1},null,2)+'\n');
 await browser.close();console.log(JSON.stringify({box,rendered:files.length}));
})().catch(e=>{console.error(e);process.exit(1)});
