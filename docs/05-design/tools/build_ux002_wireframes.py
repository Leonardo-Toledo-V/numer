from pathlib import Path
from html import escape
import base64, json
from PIL import ImageFont
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'docs/05-design/assets/ux-002'
FONT=ROOT/'docs/08-brand/assets/typography'
LOGO=ROOT/'docs/08-brand/deliverables/numer-brand-kit-v1.0/wordmark/numer-wordmark-porcelain.svg'
LOGOD='data:image/svg+xml;base64,'+base64.b64encode(LOGO.read_bytes()).decode()
PALETTE=dict(bg='#F5F6F7',paper='#FFFFFF',ink='#222629',muted='#566265',accent='#185B56',rail='#164E4A',soft='#E1E8E7',line='#DCE2E1',field='#697A7C')
class Canvas:
 def __init__(self,w,h,name):
  self.w=w;self.h=h;self.parts=[];self.name=name;self.bounds=[]
  self.parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(name)}</title><desc id="desc">Wireframe de Numer. Datos sintéticos. Propuesta de experiencia sin persistencia.</desc>')
  self.parts.append('<style>text{font-family:Manrope,Arial,sans-serif}</style>')
  self.rect(0,0,w,h,PALETTE['bg'],0)
 def rect(self,x,y,w,h,fill='#FFFFFF',r=12,stroke=None):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+'/>')
 def text(self,x,y,s,size=14,color=None,weight=400,maxw=None):
  font=ImageFont.truetype(str(FONT/('Manrope-Medium.ttf' if weight>=500 else 'Manrope-Regular.ttf')),size)
  if maxw:
   words=s.split();lines=[];line=''
   for word in words:
    candidate=(line+' '+word).strip()
    if font.getlength(candidate)>maxw and line: lines.append(line);line=word
    else: line=candidate
   if line: lines.append(line)
  else:lines=[s]
  for i,line in enumerate(lines):
   yy=y+i*(size*1.5)
   width=font.getlength(line)
   self.bounds.append(dict(text=line,x=x,y=yy,width=width,size=size))
   self.parts.append(f'<text x="{x}" y="{yy}" font-size="{size}" font-weight="{weight}" fill="{color or PALETTE["ink"]}">{escape(line)}</text>')
  return len(lines)*size*1.5
 def line(self,x,y,w): self.parts.append(f'<path d="M{x} {y}h{w}" stroke="{PALETTE["line"]}"/>')
 def button(self,x,y,w,label,primary=True):
  self.rect(x,y,w,44,PALETTE['accent'] if primary else PALETTE['paper'],8,None if primary else PALETTE['field'])
  self.text(x+14,y+28,label,14,'#FFFFFF' if primary else PALETTE['ink'],500,maxw=w-24)
 def field(self,x,y,w,label,value):
  self.text(x,y,label,13,PALETTE['muted'],500)
  self.rect(x,y+10,w,46,PALETTE['paper'],8,PALETTE['field'])
  self.text(x+12,y+39,value,16,maxw=w-24)
 def shell(self,title,active='Cuentas',sub='Datos sintéticos · MXN solo para esta muestra'):
  self.rect(24,24,198,self.h-80,PALETTE['rail'],24)
  self.parts.append(f'<image href="{LOGOD}" x="62" y="56" width="116" height="38"/>')
  self.text(48,137,'TU ESPACIO',11,'#C4DCD8',500)
  for i,label in enumerate(['Resumen','Movimientos','Cuentas','Ahorro']):
   y=158+i*48
   if label==active:self.rect(40,y+3,166,38,PALETTE['soft'],8)
   self.text(54,y+28,label,13,PALETTE['rail'] if label==active else '#C4DCD8',500 if label==active else 400)
  self.line(48,self.h-205,150)
  self.text(48,self.h-172,'Ocultar importes',12,'#C4DCD8')
  self.text(48,self.h-132,'Ajustes y sesión',12,'#C4DCD8')
  self.text(254,64,title,28,weight=500)
  self.text(254,94,sub,13,PALETTE['muted'])
 def footer(self,label): self.text(24,self.h-20,label,11,PALETTE['muted'],maxw=self.w-48)
 def save(self,filename):
  for t in self.bounds:
   assert t['x']+t['width']<=self.w-8,(filename,t)
   assert t['y']<=self.h-8,(filename,t)
  (OUT/filename).write_text('\n'.join(self.parts+['</svg>']))
  return dict(file=filename,title=self.name,width=self.w,height=self.h,text_items=len(self.bounds))
manifest=[]
# W01
c=Canvas(1100,760,'W01 · Acceso e inicio guiado')
c.rect(32,32,360,676,PALETTE['rail'],24)
c.parts.append(f'<image href="{LOGOD}" x="66" y="70" width="160" height="52"/>')
c.text(66,220,'Tus cuentas',28,'#F5F6F7',500)
c.text(66,262,'y tarjetas, en',28,'#F5F6F7',500)
c.text(66,304,'un mismo lugar.',28,'#F5F6F7',500)
c.text(66,372,'Organiza tu dinero, tu crédito y tus pagos con claridad.',18,'#C4DCD8',maxw=285)
c.rect(456,96,568,538,'#FFFFFF',20,PALETTE['line'])
c.text(492,156,'Empieza con lo esencial',28,weight=500)
c.text(492,202,'Accede a tu espacio con tu cuenta de Google.',16,maxw=450)
c.button(492,234,440,'Continuar con Google')
c.line(492,316,440)
c.text(492,354,'Después, añade tu primera cuenta o tarjeta.',16,weight=500,maxw=450)
c.text(492,399,'Puedes completar el resto de tus registros después.',14,PALETTE['muted'],maxw=430)
c.text(492,458,'Para identificar tarjetas usaremos banco y alias.',14,maxw=430)
c.text(492,498,'No te pediremos número, titular, CVV ni vencimiento.',14,PALETTE['muted'],maxw=430)
c.footer('W01 · Propuesta · Acceso y explicación del primer paso; el alta se abre después de autenticar.')
manifest.append(c.save('w01-access.svg'))
# W02
c=Canvas(1100,800,'W02 · Cuentas y tarjetas');c.shell('Cuentas y tarjetas');c.button(856,114,214,'Añadir cuenta o tarjeta')
c.text(254,151,'Tu dinero',18,weight=500)
for y,name,amount in [(176,'Cuenta diaria','$8,000.00'),(264,'Fondo de ahorro','$2,000.00')]:
 c.rect(254,y,816,72,'#FFFFFF',12,PALETTE['line']);c.text(276,y+29,name,16,weight=500);c.text(276,y+54,'Saldo registrado · MXN',12,PALETTE['muted']);c.text(864,y+42,amount,20,weight=500)
c.text(254,395,'Tus tarjetas',18,weight=500)
for x,alias,debt in [(254,'Compras','$6,000.00'),(672,'Viajes','Sin registrar')]:
 c.rect(x,416,398,208,'#FFFFFF',16,PALETTE['line']);c.rect(x+20,436,36,36,PALETTE['soft'],8);c.text(x+31,460,'A',14,PALETTE['accent'],500);c.text(x+72,460,'Banco A · '+alias,16,weight=500);c.text(x+20,510,'Deuda registrada',13,PALETTE['muted']);c.text(x+20,548,debt,26,weight=500);c.text(x+20,594,'Ver tarjeta →',14,PALETTE['accent'],500)
c.text(254,676,'El ahorro está incluido en el dinero de tus cuentas.',14,PALETTE['muted'])
c.footer('W02 · Propuesta · Banco A es un identificador ficticio. La ausencia de deuda no se representa como cero.')
manifest.append(c.save('w02-accounts.svg'))
# W03
c=Canvas(1100,870,'W03 · Detalle de tarjeta');c.shell('Banco A · Compras',sub='Cuentas y tarjetas / Compras · Datos sintéticos en MXN')
c.button(870,113,200,'Registrar pago')
c.rect(254,178,816,172,'#FFFFFF',16,PALETTE['line']);c.text(276,214,'Deuda registrada',14,PALETTE['muted']);c.text(276,267,'$6,000.00',36,weight=500);c.text(276,319,'Actualizada el 16 sep 2026 · Registro manual',12,PALETTE['muted'])
for x,label,value in [(254,'Límite de crédito','$20,000.00'),(532,'Crédito utilizado','$6,000.00'),(810,'Crédito disponible','$14,000.00')]:
 c.rect(x,374,260,114,'#FFFFFF',12,PALETTE['line']);c.text(x+20,408,label,14,PALETTE['muted']);c.text(x+20,452,value,26,weight=500)
c.text(254,529,'Uso de crédito: 30% del límite registrado',14)
c.rect(254,560,398,188,PALETTE['soft'],16);c.text(276,599,'Corte y pago',18,weight=500);c.text(276,636,'Datos del periodo sin registrar',14);c.text(276,671,'Completa las fechas y el importe',14,PALETTE['muted']);c.text(276,694,'correspondiente al concepto de pago.',14,PALETTE['muted']);c.text(276,726,'Completar datos →',14,PALETTE['accent'],500)
c.rect(672,560,398,188,'#FFFFFF',16,PALETTE['line']);c.text(694,599,'Compras a meses',18,weight=500);c.text(694,640,'$3,000.00 pendientes',24,weight=500);c.text(694,681,'Incluidos en la deuda registrada.',13,PALETTE['muted']);c.text(694,726,'Ver planes →',14,PALETTE['accent'],500)
c.footer('W03 · Datos ilustrativos; deuda usada = crédito utilizado solo en este ejemplo. No fija equivalencia general.')
manifest.append(c.save('w03-card.svg'))
# W04
c=Canvas(1100,820,'W04 · Registrar pago');c.shell('Registrar pago',sub='Banco A · Compras / Captura · Datos sintéticos')
c.rect(254,126,580,610,'#FFFFFF',16,PALETTE['line']);c.field(278,169,532,'Cuenta de origen','Cuenta diaria');c.field(278,271,532,'Tarjeta de destino','Banco A · Compras');c.field(278,373,250,'Importe · MXN','1,500.00');c.field(558,373,252,'Fecha del pago','16/09/2026');c.field(278,475,532,'Concepto','Pago de tarjeta')
c.text(278,575,'Registrar este dato no envía dinero al banco.',14,PALETTE['muted'],maxw=500);c.button(278,646,184,'Cancelar',False);c.button(582,646,228,'Revisar pago')
c.text(868,169,'Antes de registrar',16,weight=500,maxw=190);c.text(868,213,'Comprueba la cuenta de origen y la tarjeta de destino.',14,PALETTE['muted'],maxw=185)
c.footer('W04 · Flujo propuesto bajo límite de registro sin ejecutar pagos; UX-P01 pendiente de producto.')
manifest.append(c.save('w04-payment.svg'))
# W05
c=Canvas(1100,800,'W05 · Revisión de pago');c.shell('Revisar pago',sub='Banco A · Compras / Revisión · Datos sintéticos')
c.rect(254,128,816,522,'#FFFFFF',16,PALETTE['line']);c.text(282,178,'$1,500.00 MXN',32,weight=500)
for y,label,value in [(227,'Origen','Cuenta diaria'),(280,'Destino','Banco A · Compras'),(333,'Fecha del pago','16 sep 2026'),(386,'Tipo','Pago de tarjeta')]:
 c.text(282,y,label,14,PALETTE['muted']);c.text(542,y,value,16,weight=500);c.line(282,y+20,754)
c.rect(282,438,754,98,PALETTE['soft'],12);c.text(300,467,'Efecto del registro',14,weight=500);c.text(300,496,'Reduce dinero en la cuenta de origen y deuda en la tarjeta.',14);c.text(300,519,'No cuenta como una nueva compra.',13,PALETTE['muted'])
c.button(282,576,210,'Volver a los datos',False);c.button(824,576,212,'Registrar pago')
c.footer('W05 · Efecto ilustrativo condicionado a RN-06. Revisión conserva datos; no hay guardado en esta muestra.')
manifest.append(c.save('w05-review.svg'))
# W06
c=Canvas(1100,800,'W06 · Historial con ámbito explícito');c.shell('Movimientos','Movimientos',sub='Del 1 al 16 sep 2026 · Datos sintéticos en MXN')
c.button(900,114,170,'Registrar');c.text(254,155,'Totales del periodo · sin filtros',14,PALETTE['muted']);c.text(254,200,'Ingresos  $12,000.00',22,weight=500);c.text(644,200,'Gastos  $4,000.00',22,weight=500)
c.rect(254,240,816,436,'#FFFFFF',16,PALETTE['line']);c.text(276,279,'Historial',18,weight=500);c.text(276,318,'Tipo: Pago de tarjeta  ×',14,PALETTE['accent'],500);c.text(798,318,'Limpiar filtros',14,PALETTE['accent']);c.line(276,339,772);c.text(276,375,'1 movimiento filtrado',13,PALETTE['muted'])
c.text(276,432,'Pago de tarjeta',16,weight=500);c.text(276,463,'16 sep · Cuenta diaria → Banco A · Compras',13,PALETTE['muted']);c.text(878,432,'−$1,500.00',20,weight=500);c.text(891,463,'Pago de deuda',12,PALETTE['muted']);c.line(276,493,772)
c.text(276,548,'Los filtros cambian esta lista.',14,PALETTE['muted']);c.text(276,576,'Los totales de arriba corresponden al periodo completo.',14,PALETTE['muted']);c.text(276,623,'Abrir movimiento →',14,PALETTE['accent'],500)
c.footer('W06 · Totales ficticios de periodo; no constituyen una conciliación global de las demás pantallas.')
manifest.append(c.save('w06-movements.svg'))
# W07 mobile
c=Canvas(390,920,'W07 · Tarjeta en móvil');c.rect(16,16,358,128,PALETTE['rail'],20);c.parts.append(f'<image href="{LOGOD}" x="32" y="30" width="96" height="31"/>')
for x,l in [(28,'Resumen'),(110,'Movimientos'),(218,'Cuentas'),(300,'Ahorro')]:
 if l=='Cuentas':c.rect(x-8,81,80,48,PALETTE['soft'],8)
 c.text(x,110,l,11,PALETTE['rail'] if l=='Cuentas' else '#C4DCD8',500)
c.text(20,180,'Cuentas y tarjetas / Compras',12,PALETTE['muted']);c.text(20,221,'Banco A · Compras',24,weight=500);c.text(20,252,'Registro manual · MXN',13,PALETTE['muted']);c.rect(16,276,358,158,'#FFFFFF',16,PALETTE['line']);c.text(36,312,'Deuda registrada',14,PALETTE['muted']);c.text(36,359,'$6,000.00',36,weight=500);c.text(36,405,'Actualizada el 16 sep 2026',12,PALETTE['muted'])
for y,label,value in [(473,'Límite','$20,000.00'),(519,'Crédito utilizado','$6,000.00'),(565,'Crédito disponible','$14,000.00')]:
 c.text(20,y,label,14,PALETTE['muted']);c.text(238,y,value,18,weight=500)
c.line(20,586,350);c.text(20,623,'Corte y pago',18,weight=500);c.text(20,657,'Datos del periodo sin registrar',14,PALETTE['muted']);c.text(20,704,'Compras a meses →',16,PALETTE['accent'],500);c.button(20,751,350,'Registrar pago');c.footer('W07 · Propuesta móvil; selección 48 px pendiente de revisión.')
manifest.append(c.save('w07-mobile-card.svg'))
# W08 mobile recovery
c=Canvas(390,880,'W08 · Registro incierto en móvil');c.rect(16,16,358,128,PALETTE['rail'],20);c.parts.append(f'<image href="{LOGOD}" x="32" y="36" width="110" height="36"/>');c.text(32,115,'Pago de tarjeta',16,'#F5F6F7',500)
c.text(20,194,'No pudimos confirmar',24,weight=500);c.text(20,226,'el registro',24,weight=500);c.text(20,274,'Se interrumpió la conexión. Comprueba el estado antes de registrar otro pago.',16,PALETTE['muted'],maxw=342)
c.rect(16,371,358,220,'#FFFFFF',16,PALETTE['line']);c.text(36,416,'$1,500.00 MXN',28,weight=500);c.text(36,460,'Cuenta diaria',16);c.text(36,495,'→ Banco A · Compras',16);c.text(36,545,'16 sep 2026 · Pago de tarjeta',13,PALETTE['muted']);c.button(20,627,350,'Consultar estado');c.button(20,687,350,'Volver al historial',False);c.footer('W08 · Propuesta; consulta de estado requiere contrato de servidor.')
manifest.append(c.save('w08-mobile-uncertain.svg'))
# W09 first account
c=Canvas(1100,850,'W09 · Añadir primera cuenta');c.shell('Añadir cuenta',sub='Primera cuenta / Datos sintéticos')
c.rect(254,126,580,640,'#FFFFFF',16,PALETTE['line']);c.field(278,168,532,'Nombre de la cuenta','Cuenta diaria');c.field(278,270,250,'Tipo de cuenta','Dinero en banco');c.field(558,270,252,'Moneda','MXN');c.field(278,372,250,'Saldo inicial','8,000.00');c.field(558,372,252,'Fecha de referencia','16/09/2026')
c.text(278,483,'Indica a qué fecha corresponde este saldo.',14,PALETTE['muted'],maxw=500);c.text(278,529,'Si no lo conoces, no escribas cero para sustituirlo.',14,PALETTE['muted'],maxw=500);c.button(278,669,184,'Cancelar',False);c.button(582,669,228,'Revisar cuenta')
c.text(868,169,'Punto de partida',16,weight=500,maxw=185);c.text(868,215,'La fecha ayuda a interpretar los movimientos que registres después.',14,PALETTE['muted'],maxw=180)
c.footer('W09 · Tipo, moneda y tratamiento del saldo inicial pendientes de producto; ejemplo de captura.')
manifest.append(c.save('w09-add-account.svg'))
# W10 first card
c=Canvas(1100,860,'W10 · Añadir tarjeta');c.shell('Añadir tarjeta',sub='Cuentas y tarjetas / Identificación · Datos sintéticos')
c.rect(254,126,580,644,'#FFFFFF',16,PALETTE['line']);c.field(278,168,532,'Banco','Banco A');c.field(278,270,532,'Alias para reconocerla','Compras');c.field(278,372,250,'Tipo de tarjeta','Crédito');c.field(558,372,252,'Moneda','MXN');c.rect(278,464,532,80,PALETTE['soft'],12);c.text(294,494,'Siguiente paso',13,PALETTE['muted'],500);c.text(294,523,'Completar deuda, crédito y fechas',16)
c.text(278,583,'No te pediremos número de tarjeta, titular, CVV ni fecha de vencimiento.',14,PALETTE['muted'],maxw=490);c.button(278,674,184,'Cancelar',False);c.button(582,674,228,'Continuar')
c.text(868,168,'Identifica cada tarjeta',16,weight=500,maxw=185);c.text(868,220,'Usa un alias distinto si tienes varias del mismo banco.',14,PALETTE['muted'],maxw=180)
c.footer('W10 · Primer paso propuesto; crédito/corte/pago se detallan cuando producto cierre campos y reglas.')
manifest.append(c.save('w10-add-card.svg'))
(OUT/'wireframe-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
