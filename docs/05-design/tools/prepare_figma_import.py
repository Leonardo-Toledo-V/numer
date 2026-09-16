"""Prepare existing SVG wireframes for Figma import, without changing the sources."""
from pathlib import Path
import base64
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'docs/05-design/assets/ux-002'
NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', NS[1:-1])
payload = []
for path in sorted(SOURCE.glob('w[0-9][0-9]-*.svg')):
    root = ET.fromstring(path.read_text())
    for node in list(root):
        if node.tag == NS + 'style':
            root.remove(node)
        elif node.tag == NS + 'text':
            node.set('font-family', 'Manrope')
        elif node.tag == NS + 'image':
            # Inline the original vector wordmark; no raster image upload is needed.
            logo = ET.fromstring(base64.b64decode(node.attrib['href'].split(',')[1]))
            for attr in ['x', 'y', 'width', 'height']:
                logo.set(attr, node.attrib[attr])
            index = list(root).index(node)
            root.remove(node)
            root.insert(index, logo)
    payload.append({'file': path.name, 'title': root.find(NS+'title').text,
                    'mediumTexts': [t.text for t in root.findall(NS+'text') if int(t.attrib.get('font-weight', 400)) >= 500],
                    'svg': ET.tostring(root, encoding='unicode')})
Path('/private/tmp/numer-ux-figma-import.json').write_text(json.dumps(payload, ensure_ascii=False))
print(f'{len(payload)} SVG prepared; original assets preserved')
