import os
import glob
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

all_html = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__', 'scripts', 'tests', 'seo']]
    for f in files:
        if f.endswith(('.html', '.js', '.css', '.xml')):
            all_html.append(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

broken_refs = []
deleted_targets = ['jobs/', 'student/', 'cybercafe/', 'resume-templates.css', 'resume-data.js', 'resume-engine.js', 'resume-templates.js']

for src in all_html:
    with open(src, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    for dt in deleted_targets:
        if dt in content:
            broken_refs.append((src, dt))

print(f"Scanned {len(all_html)} files for references to deleted entities.")
if broken_refs:
    print(f"⚠️ Found {len(broken_refs)} references to deleted items:")
    for b in broken_refs:
        print(f"   {b[0]} -> contains '{b[1]}'")
else:
    print("✅ ZERO broken references to deleted files/folders found across the entire project!")
