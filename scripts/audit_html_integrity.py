import glob
import os
import re

html_files = glob.glob('**/*.html', recursive=True)

issues = []
for file_path in html_files:
    file_norm = file_path.replace('\\', '/')
    depth = file_norm.count('/')
    expected_css_rel = '../' * depth + 'assets/css/style.css' if depth > 0 else 'assets/css/style.css'
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check CSS link
    if 'assets/css/style.css' not in content:
        issues.append((file_norm, 'Missing style.css link'))
    
    # Check viewport meta
    if 'name="viewport"' not in content and "name='viewport'" not in content:
        issues.append((file_norm, 'Missing viewport meta tag'))

print(f'Total HTML files scanned: {len(html_files)}')
print(f'Issues found: {len(issues)}')
for iss in issues:
    print(' ', iss)
