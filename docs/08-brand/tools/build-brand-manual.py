from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import json

ROOT=Path(__file__).resolve().parents[1]
KIT=ROOT/'deliverables/numer-brand-kit-v1.0-rc1'
OUT=ROOT/'assets/brand-review'
for family,file in [('Manrope','Manrope-Regular.ttf'),('ManropeMedium','Manrope-Medium.ttf'),('ManropeBold','Manrope-Semibold.ttf')]:
    pdfmetrics.registerFont(TTFont(family,str(KIT/'typography'/file)))
W,H=595.28,841.89
P='#185B56'; INK='#222629'; PAPER='#F5F6F7'; MIST='#E1E8E7'; MUTED='#566265'
pdf=KIT/'guide/numer-brand-manual-v1.0-rc1.pdf'
c=canvas.Canvas(str(pdf),pagesize=(W,H));c.setTitle('Numer | Manual de marca 1.0 - para revisión');c.setAuthor('Numer / Brand strategy')
boxes=[]
def rect(x,y,w,h,color):
    c.setFillColor(HexColor(color));c.rect(x,H-y-h,w,h,stroke=0,fill=1)
def text(s,x,y,size=12,color=INK,font='Manrope'):
    c.setFont(font,size);c.setFillColor(HexColor(color));c.drawString(x,H-y-size,s)
def para(s,x,y,w,size=11,color=INK,font='Manrope',leading=None):
    style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.5,textColor=HexColor(color))
    p=Paragraph(s,style);pw,ph=p.wrap(w,1000);p.drawOn(c,x,H-y-ph);boxes.append({'page':c.getPageNumber(),'x':x,'y':y,'width':w,'height':ph});return ph
def img(name,x,y,w):
    h=w*(70/313 if name.startswith('numer-wordmark') else 1)
    c.drawImage(str(OUT/(name+'.png')),x,H-y-h,width=w,height=h,mask='auto')
def label(s,x,y,color=MUTED):text(s,x,y,9,color,'ManropeMedium')
def base(n,section):
    rect(0,0,W,H,PAPER);label('NUMER / MANUAL DE MARCA',44,28);label(section,350,28)
    c.setStrokeColor(HexColor('#D4DCDA'));c.line(44,57,W-44,57)
    label('1.0 RC1 · Para revisión · 15.09.2026',44,H-33);label(f'{n:02d} / 07',500,H-33)
def heading(kicker,title,desc=None):
    label(kicker,44,88,P);text(title,44,113,28,INK,'ManropeMedium')
    if desc:para(desc,44,163,507,11,MUTED)
def nextpage():c.showPage()

# 1: cover and status
rect(0,0,W,H,P)
label('IDENTIDAD / EDICIÓN PARA REVISIÓN',44,36,PAPER)
img('numer-wordmark-porcelain',42,128,320)
para('Tus cuentas y tarjetas,<br/>en un mismo lugar.',44,276,495,33,PAPER,'ManropeMedium',42)
para('Organiza tu dinero, tu crédito y tus pagos con claridad.',46,397,425,14,'#D7E7E3')
rect(44,507,507,170,'#124D49')
label('BASE ELEGIDA',64,529,'#D7E7E3')
para('Numer · Logotipo en minúsculas · Monograma continuo<br/>Petróleo mineral · Manrope',64,552,453,13,PAPER)
para('Esta edición reúne los activos elegidos y las propuestas de voz y uso. La versión 1.0 definitiva queda pendiente de tu visto bueno.',64,607,450,10,'#D7E7E3')
label('MANUAL DE MARCA 1.0 RC1',44,739,PAPER);label('15.09.2026 / 01',437,739,PAPER)
nextpage()

# 2: assets and variants
base(2,'IDENTIDAD');heading('01 / FIRMA','Una identidad, dos piezas.','El nombre dibujado conserva el corte diagonal. El símbolo conserva su trazo continuo. Ambos dibujos están aprobados; cumplen funciones diferentes.')
img('numer-wordmark-petroleum',57,239,290);img('numer-icon',438,221,86)
label('NOMBRE COMPLETO / BR-A03',57,328);label('ICONO / BR-A05',424,328)
para('Usa el nombre completo en presentación y acceso. Usa el icono en favicon y espacios pequeños. No sustituyas la primera letra del nombre por el monograma.',44,370,500,11)
label('VARIANTES DE TINTA / PROPUESTAS PARA REVISIÓN',44,458,P)
for x,bg,ink,name in [(44,PAPER,'petroleum','Petróleo'),(216,P,'porcelain','Porcelana'),(388,PAPER,'graphite','Grafito')]:
    rect(x,490,163,116,bg);img('numer-wordmark-'+ink,x+16,529,130);label(name,x+14,619)
para('SVG con contornos, sin dependencia de fuentes. Las variantes nuevas cambian únicamente la tinta: geometría, proporciones y máscara permanecen intactas.',44,685,500,11,MUTED)
nextpage()

# 3: clearspace and sizes
base(3,'USO DEL LOGO');heading('02 / ESPACIO Y ESCALA','Dale espacio para respirar.','Reglas propuestas y comprobación local de lectura. El tamaño mínimo es una referencia de pantalla, no una certificación para todos los soportes.')
img('numer-wordmark-petroleum',107,262,313)
c.setStrokeColor(HexColor(P));c.setDash(3,3)
# Visible bounds are x=6.95, y=16.5, w=289.4, h=57 in viewBox 0 9 313 70.
c.rect(107+6.95-28.5,H-(262+7.5+57+28.5),289.4+57,114,stroke=1,fill=0);c.setDash()
label('MARGEN EXTERIOR = 0.5 h',165,222,P)
para('h es la altura visible de las letras. Conserva al menos 0.5 h libres alrededor. El margen transparente del SVG no reemplaza esta área de protección.',44,390,500,11)
label('NOMBRE / ANCHO DE LA CAJA SVG',44,473,P)
for x,w,cap in [(44,80,'80 px · mínimo'),(210,96,'96 px · habitual'),(382,128,'128 px · amplio')]:
    img('numer-wordmark-petroleum',x,510,w);label(cap,x,550)
label('ICONO / CONSERVAR LOS MÁRGENES INTERNOS',44,610,P)
for x,w in [(44,16),(160,24),(278,32),(406,48)]:
    img('numer-icon',x,648,w);label(str(w)+' px',x,708)
para('Revisado en Chrome a escala 1x: el nombre se lee a 80 px; el detalle del corte pierde presencia al reducir. Por debajo de 80 px, prefiere el icono.',44,744,505,9,MUTED,leading=13)
nextpage()

# 4: palette and fonts
base(4,'COLOR Y TIPOGRAFÍA');heading('03 / SISTEMA DE MARCA','Petróleo mineral + Manrope.','La base neutra da prioridad a la información. El petróleo identifica a Numer; los colores de cada banco permanecen como identificadores secundarios.')
for i,(name,col) in enumerate([('Petróleo',P),('Porcelana',PAPER),('Grafito',INK),('Niebla',MIST)]):
    x=44+i*129;rect(x,230,120,90,col)
    if col==PAPER:c.setStrokeColor(HexColor('#D4DCDA'));c.rect(x,H-320,120,90,stroke=1,fill=0)
    label(name,x,335);text(col,x,355,10,MUTED)
text('Manrope',44,417,38,INK,'ManropeMedium')
para('Regular para lectura. Medium para títulos y controles. Semibold para énfasis puntual. El logotipo se utiliza como archivo vectorial, no se recompone escribiendo el nombre.',44,478,495,12)
text('Tu dinero, tu crédito y tus pagos.',44,567,20,INK,'ManropeMedium')
text('$24,680.50',44,613,30,P,'ManropeMedium');label('IMPORTE SINTÉTICO / CIFRAS CLARAS Y ALINEADAS',44,659)
para('Incluidas las fuentes Manrope 400, 500 y 600 con su licencia SIL OFL. Escala de interfaz, colores de estado y modo oscuro completo: trabajo posterior de UX/UI.',44,717,500,10,MUTED)
nextpage()

# 5 voice
base(5,'VOZ');heading('04 / VOZ PROPUESTA','Clara. Calmada. Cercana.','Habla de tú, explica el siguiente paso y describe hechos. Numer acompaña sin juzgar cómo una persona gasta, ahorra o gestiona sus deudas.')
messages=[('BIENVENIDA','Tus cuentas y tarjetas, en un mismo lugar.'),('ALTA DE TARJETA','Añade una tarjeta y elige su banco.'),('CONFIRMACIÓN','Gasto registrado.'),('DATO POR COMPLETAR','Aún no has registrado la deuda de esta tarjeta.'),('RESULTADO INCIERTO','No pudimos confirmar si se guardó el movimiento.')]
y=224
for k,v in messages:
    label(k,44,y,P);para(v,44,y+20,492,15,INK,'ManropeMedium',22);y+=84
rect(44,663,507,99,MIST);label('TRANSPARENCIA EN EL ALTA',60,677,P)
para('No te pediremos el número de tarjeta, el nombre del titular, el CVV ni la fecha de vencimiento.',60,700,467,11)
nextpage()

# 6 contexts and motion
base(6,'CUENTAS, TARJETAS Y MOVIMIENTO');heading('05 / COHERENCIA','La confianza está en la precisión.','Las palabras distinguen dinero propio, crédito y deuda. Un registro no equivale a ejecutar un pago o conectarse a un banco.')
rows=[('Dinero propio','Dinero en tus cuentas'),('Obligaciones','Deuda de tus tarjetas'),('Crédito libre','Crédito disponible'),('Compras a meses','Pendiente en compras a meses'),('Calendario','Periodo de corte / Periodo de pago')]
y=230
for a,b in rows:
    label(a,44,y);text(b,210,y-1,11,INK,'ManropeMedium');c.setStrokeColor(HexColor('#D4DCDA'));c.line(44,H-y-32,551,H-y-32);y+=53
para('El banco se reconoce por icono y texto. No añadir numeración, titular, CVV, vencimiento o chip decorativo. Varias tarjetas del mismo banco necesitan identificación clara sin usar números de tarjeta.',44,514,500,11)
label('MOVIMIENTO DE MARCA / PROPUESTA',44,613,P)
para('Transiciones discretas, respuesta suave y lectura estable. Evitar rebotes, confeti y contadores decorativos de dinero. Respetar movimiento reducido.',44,635,500,11)
para('GSAP o Motion: alternativas solicitadas para el futuro frontend. La elección técnica corresponde a ese equipo. Sin cambios a Sites.',44,712,500,10,MUTED)
nextpage()

# 7 approval and handoff
base(7,'CIERRE Y ENTREGA');heading('06 / REVISIÓN FINAL','Listo para decidir la versión 1.0.','Este paquete prepara el cierre de marca. La maqueta sigue siendo provisional; no necesita quedar terminada para aprobar la identidad.')
sections=[('YA ELEGIDO','Nombre Numer, dibujo del logotipo, monograma e icono. Dirección Petróleo mineral y preferencia por Manrope. Base visual del resumen aceptada, excepto el sidebar.'),('REVISAR EN ESTA ENTREGA','Mensaje principal y descriptor; voz; variantes de tinta porcelana/grafito; área de protección; mínimo de 80 px; usos del logo, tipografía de marca y movimiento propuesto.'),('DESPUÉS, CON UX/UI','Radios y altura del estado activo del sidebar; componentes, recorridos, estados, contraste y adaptación. Producto y tecnología definen reglas financieras y seguridad.'),('ARCHIVOS INCLUIDOS','SVG de logo y símbolo, icono SVG/PNG, favicon ICO, fuentes y licencia, manual PDF, guías editables, handoff e inventario de integridad.')]
y=230
for title,body in sections:
    label(title,44,y,P);para(body,44,y+23,500,11);y+=119
para('Validación local: geometría preservada, variantes renderizadas y tamaños revisados. No acredita registro comercial, impresión ni accesibilidad completa. La disponibilidad comercial del nombre permanece pendiente.',44,725,500,9,MUTED,leading=13)
c.save()
for b in boxes:
    assert b['y']+b['height']<800,(b,'Overflow')
(OUT/'pdf-layout-boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(pdf)
