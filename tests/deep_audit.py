import os
import glob
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 60)
print("DEEP JS, CSS & PERFORMANCE AUDIT")
print("=" * 60)

js_files = glob.glob('**/*.js', recursive=True)
html_files = glob.glob('**/*.html', recursive=True)
css_files = glob.glob('**/*.css', recursive=True)

# 1. CDN Dependencies
cdns_found = set()
for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    scripts = re.findall(r'<script[^>]+src=["\'](https?://[^"\']+)["\']', content)
    links = re.findall(r'<link[^>]+href=["\'](https?://[^"\']+)["\']', content)
    for s in scripts:
        cdns_found.add((hf, 'script', s))
    for l in links:
        cdns_found.add((hf, 'link', l))

print("\n1. EXTERNAL CDN DEPENDENCIES AUDIT:")
cdn_by_url = {}
for hf, tag_type, url in cdns_found:
    cdn_by_url.setdefault(url, []).append(hf)

for url, pages in sorted(cdn_by_url.items()):
    print(f"  [{len(pages)} pages] {url}")

# 2. Check JavaScript files for syntax/runtime risks
print("\n2. JAVASCRIPT CODE INSPECTION:")
for jf in js_files:
    with open(jf, 'r', encoding='utf-8', errors='ignore') as f:
        js_code = f.read()
    
    console_logs = len(re.findall(r'console\.(log|warn|error)', js_code))
    inner_htmls = len(re.findall(r'\.innerHTML\s*=', js_code))
    try_catches = len(re.findall(r'try\s*\{', js_code))
    event_listeners = len(re.findall(r'addEventListener', js_code))
    
    print(f"  File: {jf} ({len(js_code)} bytes)")
    print(f"    - Event Listeners: {event_listeners}, Try/Catch blocks: {try_catches}")
    print(f"    - innerHTML assignments: {inner_htmls}, console statements: {console_logs}")

# 3. CSS Tokens & Media Queries
print("\n3. CSS TOKENS & RESPONSIVE BREAKPOINTS:")
for cf in css_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        css_code = f.read()
    
    media_queries = re.findall(r'@media[^{]+', css_code)
    css_vars = re.findall(r'--[a-zA-Z0-9_-]+:', css_code)
    importants = len(re.findall(r'!important', css_code))
    
    print(f"  File: {cf} ({len(css_code)} bytes)")
    print(f"    - CSS Variables defined: {len(set(css_vars))}")
    print(f"    - !important usages: {importants}")
    print(f"    - Media Queries ({len(media_queries)}):")
    for mq in media_queries:
        print(f"       * {mq.strip()}")

print("\n" + "=" * 60)
print("DEEP AUDIT FINISHED")
print("=" * 60)
