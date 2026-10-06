import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

used_classes = set()
for html_file in glob.glob('**/*.html', recursive=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    classes = re.findall(r'class=["\']([^"\']+)["\']', content)
    for c_str in classes:
        for c in c_str.split():
            used_classes.add(c)

missing = []
for c in sorted(used_classes):
    # Check if .classname is present in css
    if not re.search(r'\.' + re.escape(c) + r'(?=[^a-zA-Z0-9_-]|$)', css):
        missing.append(c)

print(f'Total unique classes in HTML: {len(used_classes)}')
print(f'Missing in CSS ({len(missing)}):')
for m in missing:
    print('  .' + m)
