import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)
print(f'Total HTML files: {len(html_files)}')

classes_used = set()
for f in html_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
        for match in re.finditer(r'class=["\']([^"\']+)["\']', content):
            for cls in match.group(1).split():
                classes_used.add(cls)

print(f'Unique classes found in HTML files: {len(classes_used)}')

with open('assets/css/style.css', 'r', encoding='utf-8', errors='ignore') as fp:
    css_content = fp.read()

missing = []
for cls in sorted(classes_used):
    if not re.search(r'\.' + re.escape(cls) + r'(?![a-zA-Z0-9_-])', css_content):
        missing.append(cls)

print(f'Classes not directly matched in style.css: {len(missing)}')
print('Missing classes count:', len(missing))
with open('missing_classes.txt', 'w', encoding='utf-8') as out:
    for m in sorted(missing):
        out.write(m + '\n')
print('Wrote missing_classes.txt')
