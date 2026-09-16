from pathlib import Path
import hashlib,json,re,zipfile,xml.etree.ElementTree as ET
from pypdf import PdfReader
from PIL import Image,ImageChops

root=Path(__file__).resolve().parents[1]
kit=root/'deliverables/numer-brand-kit-v1.0'
old=root/'deliverables/numer-brand-kit-v0.1'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
preserved=[]
for folder in ['wordmark','symbol','icon','favicon']:
 for src in (old/folder).iterdir():
  dst=kit/folder/src.name
  assert src.read_bytes()==dst.read_bytes(),src
  preserved.append(str(dst.relative_to(kit)))
for name in ['Manrope-Regular.ttf','Manrope-Medium.ttf','Manrope-Semibold.ttf','Manrope-OFL.txt']:
 assert (kit/'typography'/name).read_bytes()==(root/'assets/typography'/name).read_bytes()
for folder,prefix in [('wordmark','numer-wordmark'),('symbol','numer-symbol')]:
 base=Image.open(kit/folder/(prefix+'-petroleum.png')).getchannel('A')
 for color in ['porcelain','graphite']:
  alpha=Image.open(kit/folder/(prefix+'-'+color+'.png')).getchannel('A')
  assert ImageChops.difference(base,alpha).getbbox() is None
for p in kit.rglob('*.svg'):ET.parse(p)
for p in kit.rglob('*.md'):
 for ref in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not ref.startswith(('http:','https:','#')):assert (p.parent/ref.split('#')[0]).exists(),(p,ref)
reader=PdfReader(kit/'guide/numer-brand-manual-v1.0.pdf')
assert len(reader.pages)==7
texts=[p.extract_text() for p in reader.pages]
for i,needle in enumerate(['Tus cuentas y tarjetas','Una identidad','Dale espacio','Petróleo mineral','Clara. Calmada. Cercana.','La confianza','La identidad de Numer']):assert needle in texts[i],(i,needle)
embedded=[]
for p in reader.pages:
 for font in p['/Resources']['/Font'].get_object().values():
  f=font.get_object();d=f.get('/FontDescriptor')
  if d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']):embedded.append(str(f.get('/BaseFont')))
assert len(set(embedded))>=2
pngs={str(p.relative_to(kit)):Image.open(p).size for p in kit.rglob('*.png')}
ico=Image.open(kit/'favicon/favicon.ico');assert {(16,16),(32,32),(48,48)}.issubset(ico.ico.sizes())
verification={'edition':'1.0','status':'original approved wordmark restored under BR-C32; remaining brand criteria approved BR-A07','date':'2026-09-15','original_assets_byte_identical':preserved,'font_files_byte_identical':True,'variant_alpha_identical':True,'svg_xml_valid':True,'local_document_links_valid':True,'pdf_pages':7,'pdf_text_checked':True,'pdf_embedded_fonts':sorted(set(embedded)),'pdf_visual_review':'All seven final rendered pages inspected; no clipping or overlap observed.','size_review':json.loads((root/'assets/brand-final/render-verification.json').read_text()),'png_dimensions':pngs,'ico_sizes':sorted(ico.ico.sizes()),'limitations':['No print validation','No full accessibility audit','No commercial name clearance','No app or security implementation']}
(kit/'verification.json').write_text(json.dumps(verification,indent=2,ensure_ascii=False)+'\n')
entries=[{'path':str(p.relative_to(kit)),'bytes':p.stat().st_size,'sha256':digest(p)}for p in sorted(kit.rglob('*')) if p.is_file() and p.name!='manifest.json']
(kit/'manifest.json').write_text(json.dumps({'edition':'1.0','files':entries},indent=2,ensure_ascii=False)+'\n')
# Preserve the full dotted version name.
archive=kit.parent/(kit.name+'.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(kit.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(kit.parent)))
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 for e in entries:assert hashlib.sha256(z.read(kit.name+'/'+e['path'])).hexdigest()==e['sha256']
print(json.dumps({'files':len(entries)+1,'pdf_pages':7,'archive':str(archive),'archive_bytes':archive.stat().st_size,'archive_sha256':digest(archive)}))
