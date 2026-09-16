"""Static vector design boards only. No application/frontend files are generated."""
from pathlib import Path
from html import escape
import base64, json
from PIL import ImageFont

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'docs/05-design/assets/ux-003'
OUT.mkdir(parents=True,exist_ok=True)
FONTS=ROOT/'docs/08-brand/assets/typography'
LOGO=ROOT/'docs/08-brand/deliverables/numer-brand-kit-v1.0/wordmark/numer-wordmark-porcelain.svg'
LOGOD='data:image/svg+xml;base64,'+base64.b64encode(LOGO.read_bytes()).decode()
C={'bg':'#F5F6F7','ink':'#222629','muted':'#566265','petrol':'#185B56','rail':'#164E4A','soft':'#E1E8E7','line':'#E1E8E7','field':'#85918F','white':'#FFFFFF'}

class Board:
 def __init__(self,w,h,name,background=None):
  self.w=w;self.h=h;self.name=name;self.bounds=[]
  self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(name)}</title><desc id="desc">Propuesta estática de composición Numer. Datos sintéticos. Sin implementación ni acciones funcionales.</desc><style>text{{font-family:Manrope,sans-serif;font-variant-numeric:tabular-nums}}</style>']
  self.rect(0,0,w,h,background or C['bg'],0)
 def rect(self,x,y,w,h,fill,r=8,stroke=None,opacity=None):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+(f' opacity="{opacity}"' if opacity else '')+'/>')
 def text(self,x,y,s,size=14,color=None,weight=400,anchor='start'):
  font=ImageFont.truetype(str(FONTS/('Manrope-Semibold.ttf' if weight>=600 else 'Manrope-Medium.ttf' if weight>=500 else 'Manrope-Regular.ttf')),size)
  width=font.getlength(s)
  left=x-width if anchor=='end' else x-width/2 if anchor=='middle' else x
  assert left>=0 and left+width<=self.w,(self.name,s,left,width)
  assert y<=self.h-4,(self.name,s,y)
  self.bounds.append({'text':s,'left':left,'right':left+width,'baseline':y,'size':size})
  self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color or C["ink"]}" text-anchor="{anchor}">{escape(s)}</text>')
 def path(self,d,color=None,width=1.5):
  self.parts.append(f'<path d="{d}" fill="none" stroke="{color or C["muted"]}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')
 def line(self,x,y,w):self.path(f'M{x} {y}h{w}',C['line'],1)
 def icon(self,x,y,kind,color=None):
  paths={'grid':'M2 2h6v6H2z M12 2h6v6h-6z M2 12h6v6H2z M12 12h6v6h-6z','list':'M3 5h14 M3 10h14 M3 15h14','wallet':'M3 4h13v13H3z M12 8h6v6h-6z','save':'M4 17V9h4v8 M10 17V5h4v12 M16 17V2h2v15','plus':'M10 4v12 M4 10h12','down':'M6 8l4 4 4-4','close':'M5 5l10 10 M15 5 5 15','card':'M2 4h16v12H2z M2 8h16 M5 13h4','chevron':'M8 5l5 5-5 5','gear':'M4 5h12v10H4z M7 2v3 M13 2v3 M7 15v3 M13 15v3 M1 8h3 M16 8h3 M1 12h3 M16 12h3','eye':'M1 10Q10 0 19 10Q10 20 1 10 M7 10a3 3 0 1 0 6 0a3 3 0 1 0 -6 0'}
  self.parts.append(f'<g transform="translate({x} {y})">');self.path(paths[kind],color);self.parts.append('</g>')
 def button(self,x,y,w,label,kind='primary',height=36):
  self.rect(x,y,w,height,C['petrol'] if kind=='primary' else C['white'],6,None if kind=='primary' else C['field'])
  self.text(x+w/2,y+height/2+5,label,12,C['white'] if kind=='primary' else C['ink'],500,'middle')
 def field(self,x,y,w,label,value,select=False,h=36,size=13):
  self.text(x,y,label,12,C['ink'],500);self.rect(x,y+9,w,h,C['white'],6,C['field']);self.text(x+12,y+9+h/2+5,value,size)
  if select:self.icon(x+w-28,y+9+(h-20)/2,'down')
 def logo(self,x,y,w):self.parts.append(f'<image href="{LOGOD}" x="{x}" y="{y}" width="{w}" height="{w*70/313}"/>')
 def save(self,name):
  (OUT/(name+'.svg')).write_text('\n'.join(self.parts+['</svg>']))
  return {'file':name+'.svg','title':self.name,'width':self.w,'height':self.h,'text_count':len(self.bounds),'text_bounds':self.bounds}

def accounts():
 b=Board(1280,800,'C01 · Cuentas y tarjetas / composición compacta',C['white'])
 b.rect(0,0,176,800,C['rail'],0);b.logo(24,38,100)
 b.text(24,126,'TU ESPACIO',10,'#C4DCD8',500)
 for i,(label,icon) in enumerate([('Resumen','grid'),('Movimientos','list'),('Cuentas','wallet'),('Ahorro','save')]):
  y=146+i*46;active=label=='Cuentas'
  if active:b.rect(12,y+3,152,38,C['soft'],8)
  col=C['rail'] if active else '#C4DCD8';b.icon(24,y+12,icon,col);b.text(56,y+27,label,12,col,500 if active else 400)
 b.path('M16 720h144','#41716C',1)
 b.rect(12,732,152,56,'#205B56',6);b.rect(24,744,32,32,C['soft'],16)
 b.text(40,765,'A',12,C['rail'],500,'middle');b.text(64,754,'Alex',12,'#F5F6F7',500);b.text(64,773,'Mi cuenta',12,'#C4DCD8')
 b.path('M144 760l4-4 4 4','#C4DCD8')
 b.text(208,46,'Tu espacio',12,C['muted']);b.text(277,46,'/',12,C['muted']);b.text(292,46,'Cuentas',12)
 b.text(1244,46,'MXN · Saldos registrados',12,C['muted'],anchor='end')
 b.text(208,105,'Cuentas y tarjetas',18,weight=500)
 b.text(208,131,'Tu dinero y tu crédito, en su lugar.',12,C['muted'])
 b.button(1120,88,124,'Añadir',height=34);b.line(208,155,1036)
 b.text(208,195,'Tu dinero',13,weight=500);b.text(280,195,'2 cuentas',12,C['muted'])
 b.text(1244,195,'El ahorro está incluido en estas cuentas.',12,C['muted'],anchor='end')
 b.rect(208,215,1036,168,C['white'],10,C['line'])
 for x,s,anchor in [(276,'Cuenta','start'),(730,'Fecha de referencia','start'),(1114,'Saldo registrado','end')]:b.text(x,239,s,12,C['muted'],500,anchor)
 b.line(208,252,1036)
 for y,name,meta,amount,ic in [(252,'Cuenta diaria','Banco A · Dinero en banco','$8,000.00','wallet'),(317,'Ahorro','Banco A · Cuenta de ahorro','$2,000.00','save')]:
  if y>252:b.line(232,y,988)
  b.rect(232,y+16,32,32,C['bg'],7);b.icon(238,y+22,ic,C['petrol']);b.text(276,y+30,name,13,weight=500);b.text(276,y+49,meta,12,C['muted'])
  b.text(730,y+30,'16 sep 2026',12,C['muted']);b.text(1114,y+30,amount,13,weight=500,anchor='end');b.icon(1194,y+18,'chevron')
 b.text(208,431,'Tus tarjetas',13,weight=500);b.text(294,431,'2 tarjetas',12,C['muted'])
 b.rect(208,451,1036,180,C['white'],10,C['line'])
 for x,s,anchor in [(276,'Tarjeta','start'),(672,'Deuda registrada','end'),(860,'Crédito disponible','end')]:b.text(x,477,s,12,C['muted'],500,anchor)
 b.line(208,491,1036)
 for y,alias,debt,credit in [(491,'Compras','$6,000.00','$14,000.00'),(561,'Viajes','Sin registrar','Sin registrar')]:
  if y>491:b.line(232,y,988)
  b.rect(232,y+19,32,32,C['soft'],7);b.icon(238,y+25,'card',C['petrol']);b.text(276,y+30,alias,13,weight=500);b.text(276,y+49,'Banco A · Crédito',12,C['muted'])
  b.text(672,y+30,debt,13 if alias=='Compras' else 12,C['ink'] if alias=='Compras' else C['muted'],500 if alias=='Compras' else 400,'end');b.text(860,y+30,credit,13 if alias=='Compras' else 12,C['ink'] if alias=='Compras' else C['muted'],500 if alias=='Compras' else 400,'end')
  b.text(958,y+30,'Detalle',12,C['petrol'],500);b.button(1044,y+8,176,'Registrar pago','secondary',34)
 b.text(208,662,'El crédito disponible no forma parte del dinero de tus cuentas.',12,C['muted'])
 b.text(208,760,'C01 · Propuesta de diseño · Datos sintéticos · Sin implementación',10,C['muted'])
 return b

manifest=[]
manifest.append(accounts().save('c01-accounts'))
b=accounts();b.name='C02 · Registro de pago / diálogo compacto'
b.parts[0]=b.parts[0].replace('C01 · Cuentas y tarjetas / composición compacta',b.name)
b.rect(0,0,1280,800,'#102725',0,opacity='.24')
x=410;y=183;w=460
b.rect(x,y+6,w,434,'#102725',12,opacity='.10');b.rect(x,y,w,434,C['white'],12,C['line'])
b.text(x+24,y+37,'Registrar pago',17,weight=500);b.icon(x+w-42,y+20,'close')
b.text(x+24,y+64,'Banco A · Compras',12,C['muted'])
b.line(x+24,y+86,w-48)
b.field(x+24,y+120,w-48,'Cuenta de origen','Cuenta diaria · Banco A',True)
b.field(x+24,y+189,198,'Importe · MXN','1,500.00')
b.field(x+238,y+189,198,'Fecha del pago','16/09/2026')
b.field(x+24,y+258,w-48,'Concepto','Pago de tarjeta')
b.text(x+24,y+326,'Registrar este dato no envía dinero al banco.',12,C['muted'])
b.line(x+24,y+348,w-48)
b.button(x+193,y+374,92,'Cancelar','secondary',36);b.button(x+297,y+374,139,'Revisar pago','primary',36)
manifest.append(b.save('c02-payment-dialog'))

b=Board(390,760,'C03 · Registro de pago / adaptación móvil')
b.rect(0,0,390,760,C['white'],0)
b.text(20,43,'Registrar pago',17,weight=500);b.icon(350,26,'close')
b.text(20,71,'Banco A · Compras',13,C['muted']);b.line(20,94,350)
b.field(20,130,350,'Cuenta de origen','Cuenta diaria · Banco A',True,44,16)
b.field(20,220,350,'Importe · MXN','1,500.00',False,44,16)
b.field(20,310,350,'Fecha del pago','16/09/2026',False,44,16)
b.field(20,400,350,'Concepto','Pago de tarjeta',False,44,16)
b.text(20,492,'Registrar este dato no envía dinero al banco.',12,C['muted'])
b.line(20,521,350);b.button(20,546,106,'Cancelar','secondary',44);b.button(138,546,232,'Revisar pago','primary',44)
b.text(20,722,'C03 · Propuesta · Móvil conserva blancos táctiles.',10,C['muted'])
manifest.append(b.save('c03-payment-mobile'))
b=accounts();b.name='C04 · Menú de perfil / abierto'
b.parts[0]=b.parts[0].replace('C01 · Cuentas y tarjetas / composición compacta',b.name)
b.rect(12,576,220,148,'#102725',8,opacity='.12');b.rect(12,570,220,148,C['white'],8,C['line'])
b.text(28,595,'Mi cuenta',12,C['muted'],500);b.line(20,607,204)
b.icon(28,624,'eye');b.text(58,639,'Ocultar importes',12)
b.rect(202,625,14,14,C['white'],3,C['field'])
b.icon(28,672,'gear');b.text(58,687,'Configuración',12)
manifest.append(b.save('c04-profile-menu'))
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('4 static SVG boards generated; text extents checked')
