// Four native vector studies. No app or runtime dependency added.
const fs=require('fs'),path=require('path');
const dir=path.resolve(__dirname,'../assets/favicon-round2');fs.mkdirSync(dir,{recursive:true});
const proposals=[
 ['01-abaco','Ábaco','<g fill="none" stroke="#185B56" stroke-width="6" stroke-linecap="round"><path d="M22 9V55M42 9V55"/></g><g fill="#185B56"><rect x="10" y="17" width="24" height="13" rx="6.5"/><rect x="30" y="35" width="24" height="13" rx="6.5"/></g>'],
 ['02-pliegue','Pliegue','<g fill="#185B56"><path d="M8 13Q8 8 13 10L29 18V55L13 47Q8 45 8 40Z"/><path d="M35 18L50 10Q55 7 55 13V24L35 35Z"/><path d="M35 42L55 31V42Q55 47 50 49L35 57Z"/></g>'],
 ['03-conciliar','Conciliar','<g fill="none" stroke="#185B56" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"><path d="M36 10H24Q10 10 10 24V32Q10 40 18 40H28"/><path d="M28 54H40Q54 54 54 40V32Q54 24 46 24H36"/></g>'],
 ['04-hitos','Hitos','<path d="M13 14H40Q54 14 54 28Q54 42 40 42H24" fill="none" stroke="#185B56" stroke-width="10" stroke-linecap="round"/><circle cx="13" cy="14" r="8" fill="#185B56"/><rect x="16" y="34" width="16" height="16" rx="3" transform="rotate(45 24 42)" fill="#185B56"/>']
];
for(const [name,title,body]of proposals)fs.writeFileSync(path.join(dir,name+'.svg'),`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Numer, ${title}; propuesta de favicon"><title>Numer · ${title} · Propuesta</title>${body}</svg>\n`);
console.log('Four new vector proposals saved.');
