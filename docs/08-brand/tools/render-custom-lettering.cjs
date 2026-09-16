const fs = require('fs');
const path = require('path');
const req = require;
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'assets/custom-lettering-provisional');
// The n is the exact approved BR-A05 outline. The other four letters are
// an original provisional drawing, not a font with a substituted initial.
const letters = [
  ['n', 0, 'M8 56V24Q8 17 15 17H22V24C26 16 33 12 41 12C53 12 59 20 59 33V43C59 49 62 52 68 52V62C52 62 44 57 44 44V33C44 26 41 23 36 23C28 23 23 30 23 40V56Z'],
  ['u', 66, 'M8 17H23V40C23 48 26 51 31 51C39 51 44 44 44 34V17H59V43C59 49 62 52 68 52V62C58 62 51 59 48 54C43 60 37 62 29 62C15 62 8 54 8 41Z'],
  ['m', 132, 'M8 56V24Q8 17 15 17H22V24C26 16 32 12 39 12C47 12 53 16 55 23C59 16 65 12 73 12C86 12 92 20 92 33V43C92 49 95 52 101 52V62C85 62 77 57 77 44V33C77 26 75 23 70 23C63 23 59 30 59 40V56H44V33C44 26 42 23 37 23C28 23 23 30 23 40V56Z'],
  ['e', 235, 'M64 40H23C24 48 29 52 37 52C43 52 47 50 51 46L62 52C56 59 48 62 37 62C19 62 8 52 8 37C8 22 19 12 36 12C54 12 64 23 64 38ZM23 31H49C48 25 44 22 36 22C29 22 25 25 23 31Z'],
  ['r', 301, 'M8 56V24Q8 17 15 17H22V24C26 16 33 12 41 12C46 12 50 13 54 16L48 29C45 26 42 25 38 25C29 25 23 32 23 42V56Z']
];
const svg = ink => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 4 364 66" role="img" aria-label="Numer · lettering personalizado provisional"><title>Numer · lettering personalizado provisional</title><g fill="${ink}" fill-rule="evenodd">${letters.map(([name,x,d])=>`<path data-letter="${name}" transform="translate(${x} 0)" d="${d}"/>`).join('')}</g></svg>`;
for (const [name, ink] of [['petroleum','#185B56'],['porcelain','#F5F6F7']]) fs.writeFileSync(path.join(out,`numer-custom-${name}.svg`),svg(ink));
const data = source => 'data:image/svg+xml;base64,'+Buffer.from(source).toString('base64');
const font = path.join(root,'assets/typography/Manrope-Regular.ttf');
const fontData = 'data:font/ttf;base64,'+fs.readFileSync(font).toString('base64');
const icon = fs.readFileSync(path.join(root,'deliverables/numer-brand-kit-v1.0/icon/numer-icon.svg'),'utf8');
const html = `<!doctype html><html lang="es"><meta charset="utf-8"><style>
@font-face{font-family:Manrope;src:url('${fontData}')}*{box-sizing:border-box}body{margin:0;background:#F5F6F7;color:#222629;font-family:Manrope,Arial}main{width:1400px}.hero{height:610px;padding:58px 72px}.head{display:flex;justify-content:space-between;font-size:16px;letter-spacing:1.5px;color:#55716e}.word{height:385px;display:flex;align-items:center;justify-content:center}.word img{width:1120px}.caption{font-size:22px;line-height:1.6;color:#526461}.bottom{display:flex;height:290px}.reverse{background:#185B56;width:850px;display:flex;align-items:center;justify-content:center}.reverse img{width:620px}.symbol{background:#E1E8E7;flex:1;display:flex;gap:35px;align-items:center;padding:48px}.symbol img{width:115px}.symbol p{font-size:18px;line-height:1.7}.symbol small{display:block;font-size:14px;color:#526461}</style><main><section class="hero"><div class="head"><span>NUMER / EXPLORACIÓN TIPOGRÁFICA</span><span>01 · PROVISIONAL</span></div><div class="word"><img alt="numer personalizado" src="${data(svg('#185B56'))}"></div><div class="caption">La misma n. Un trazo propio para cada letra.</div></section><section class="bottom"><div class="reverse"><img alt="Numer en porcelana" src="${data(svg('#F5F6F7'))}"></div><div class="symbol"><img alt="Icono de referencia" src="${data(icon)}"><p>Origen del trazo<small>La n del icono aprobado.</small></p></div></section></main></html>`;
fs.writeFileSync(path.join(out,'preview.html'),html);
(async()=>{
 const browser = await req('playwright').chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const page = await browser.newPage({viewport:{width:1400,height:900},deviceScaleFactor:1});
 await page.setContent(html);await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
 await page.screenshot({path:path.join(out,'numer-custom-preview.png')});
 await page.setViewportSize({width:1456,height:264});
 await page.setContent('<style>body{margin:0;background:transparent}svg{display:block;width:100%;height:100%}</style>'+svg('#185B56'));
 await page.screenshot({path:path.join(out,'numer-custom-transparent.png'),omitBackground:true});
 const bounds=await page.locator('path').evaluateAll(ps=>ps.map(p=>{const b=p.getBBox();return{letter:p.dataset.letter,x:b.x,y:b.y,width:b.width,height:b.height};}));
 fs.writeFileSync(path.join(out,'geometry.json'),JSON.stringify({status:'provisional',browser:await browser.version(),letters:bounds,nMatchesApproved:icon.includes(letters[0][2])},null,2)+'\n');
 await browser.close();console.log(JSON.stringify({out,letters:bounds}));
})().catch(e=>{console.error(e);process.exit(1)});
