"""Check documentary/artifact integrity. Not an application or accessibility test."""
from pathlib import Path
import base64, hashlib, json, re, sys, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
D = ROOT/'docs/05-design'
A = D/'assets/ux-002'
report = {'task':'T-UX-002','date':'2026-09-16','python':sys.version.split()[0]}
broken = []
checked = 0
for file in D.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', file.read_text()):
        target = target.split('#')[0]
        if not target or '://' in target:
            continue
        checked += 1
        if not (file.parent/target).exists():
            broken.append({'file':file.name,'target':target})
report['local_links'] = {'checked':checked,'broken':broken}
all_text = '\n'.join(f.read_text() for f in D.glob('*.md'))
report['ids'] = {}
for prefix, n in [('UX-N',15),('UX-B',8),('UX-F',13),('UX-E',10),('UX-I',10),('UX-C',20),('UX-CMP',12),('UX2-AC',9)]:
    report['ids'][prefix] = {'expected':n,'missing':[f'{prefix}{i:02}' for i in range(1,n+1) if f'{prefix}{i:02}' not in all_text]}
def luminance(h):
    rgb=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    rgb=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in rgb]
    return sum(c*w for c,w in zip(rgb,[.2126,.7152,.0722]))
def contrast(a,b):
    l=sorted([luminance(a),luminance(b)])
    return (l[1]+.05)/(l[0]+.05)
tokens=json.loads((A/'design-tokens.json').read_text())
pairs=[]
for theme in ('light','dark'):
    t=tokens['themes'][theme]
    for fg,bg,minimum in [('text','background',4.5),('text','surface',4.5),('muted','surface',4.5),('muted','background',4.5),('accent','surface',4.5),('onAccent','accent',4.5),('errorText','errorSurface',4.5),('warningText','warningSurface',4.5),('fieldBorder','surface',3)]:
        ratio=contrast(t[fg],t[bg])
        pairs.append({'theme':theme,'foreground':fg,'background':bg,'ratio':round(ratio,2),'threshold':minimum,'pass':ratio>=minimum})
report['token_contrast'] = pairs
ns='{http://www.w3.org/2000/svg}'
logo=(ROOT/'docs/08-brand/deliverables/numer-brand-kit-v1.0/wordmark/numer-wordmark-porcelain.svg').read_bytes()
assets=[]
for f in sorted(A.glob('w[0-9][0-9]-*.svg')):
    svg=ET.fromstring(f.read_text())
    images=svg.findall(ns+'image')
    assets.append({'file':f.name,'dimensions':[int(svg.attrib['width']),int(svg.attrib['height'])],
      'png_exists':f.with_suffix('.png').exists(),'has_title_and_desc':svg.find(ns+'title') is not None and svg.find(ns+'desc') is not None,
      'original_wordmark':bool(images) and all(base64.b64decode(n.attrib['href'].split(',')[1])==logo for n in images),
      'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
report['wireframes'] = assets
skills=[]
for name in ('apple-design','emil-design-eng'):
    installed=Path.home()/'.codex/skills'/name/'SKILL.md'
    upstream=Path('/private/tmp/numer-ux-skills')/(name+'.md')
    data=installed.read_bytes()
    skills.append({'name':name,'installed':True,'sha256':hashlib.sha256(data).hexdigest(),'matches_downloaded_revision':data==upstream.read_bytes() if upstream.exists() else None})
report['skills'] = {'repo':'emilkowalski/skills','revision':'85e8e2363b713506e1d5b6e07a0eb2da66be1bc3','items':skills}
f=json.loads((A/'figma-manifest.json').read_text())
report['figma']={'file':f['url'],'frames':len(f['frames']),'captured_and_inspected':10,'font_family':'Manrope',
  'medium_corrected':len(f['mediumCorrectedIds']),'medium_pending':len(f['remainingMediumIds']),
  'layout_pending':f['remainingLayout'],'limitation':'Starter MCP tool quota reached; final cleanup not verified',
  'native_component_library':False,'connected_prototype':False}
report['visual_review']={'local_frames':10,'method':'Sharp render and view_image inspection; Figma frame.screenshot for imported versions',
  'local_corrections':['W01 heading overlap','W10 next-step information styling'],
  'source_bounds':'Generator asserts text within canvas; no dynamic layout behavior proven'}
report['not_tested']=['User research sessions','Keyboard and screen reader','Responsive browser behavior','Financial calculations or persistence','Auth and RLS','Final Figma layout after quota limit']
report['scope']='Documentation and design only; no frontend or product rules implemented'
(D/'verification/T-UX-002.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
failures = broken + [p for p in pairs if not p['pass']] + [p for p in report['ids'].values() if p['missing']]
failures += [a for a in assets if not all(a[k] for k in ('png_exists','has_title_and_desc','original_wordmark'))]
print(json.dumps({'links':checked,'wireframes':len(assets),'contrast_pairs':len(pairs),'failures':failures},ensure_ascii=False))
sys.exit(bool(failures))
