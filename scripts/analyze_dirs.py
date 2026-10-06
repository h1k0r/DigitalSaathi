import glob
import re
from collections import defaultdict

dir_classes = defaultdict(set)
for f in glob.glob('**/*.html', recursive=True):
    parts = f.replace('\\', '/').split('/')
    d = parts[0] if len(parts) > 1 else 'root'
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for match in re.finditer(r'class=["\']([^"\']+)["\']', fp.read()):
            for cls in match.group(1).split():
                dir_classes[d].add(cls)

with open('assets/css/style.css', 'r', encoding='utf-8', errors='ignore') as fp:
    css = fp.read()

for d, classes in sorted(dir_classes.items()):
    unmatched = [c for c in sorted(classes) if not re.search(r'\.' + re.escape(c) + r'(?![a-zA-Z0-9_-])', css)]
    print(f'{d} ({len(classes)} classes): {len(unmatched)} missing')
    if unmatched:
        print('   ', ', '.join(unmatched[:15]))
