import os
import glob
import re
import sys
from collections import defaultdict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("🚀 DIGITALSAATHI COMPREHENSIVE SEO & MENU AUDIT")
print("==================================================")

html_files = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__', 'scripts', 'tests', 'seo']]
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

print(f"Auditing {len(html_files)} HTML pages...")

seo_report = {
    'missing_title': [],
    'missing_description': [],
    'missing_canonical': [],
    'missing_og': [],
    'missing_schema': [],
    'missing_h1': [],
    'multiple_h1': [],
    'broken_links': []
}

for path in sorted(html_files):
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # 1. Title
    title_match = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
    if not title_match or not title_match.group(1).strip():
        seo_report['missing_title'].append(path)
    
    # 2. Meta description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if not desc_match or not desc_match.group(1).strip():
        # try alternative order
        desc_match = re.search(r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']description["\']', content, re.IGNORECASE)
    if not desc_match or not desc_match.group(1).strip():
        seo_report['missing_description'].append(path)
        
    # 3. Canonical
    canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if not canonical_match:
        seo_report['missing_canonical'].append(path)
        
    # 4. Open Graph
    og_match = re.search(r'<meta\s+property=["\']og:title["\']', content, re.IGNORECASE)
    if not og_match:
        seo_report['missing_og'].append(path)
        
    # 5. Schema JSON-LD
    schema_match = re.search(r'<script\s+type=["\']application/ld\+json["\']', content, re.IGNORECASE)
    if not schema_match:
        seo_report['missing_schema'].append(path)
        
    # 6. H1 count
    h1_matches = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', content, re.IGNORECASE)
    if len(h1_matches) == 0:
        seo_report['missing_h1'].append(path)
    elif len(h1_matches) > 1:
        seo_report['multiple_h1'].append((path, len(h1_matches)))
        
    # 7. Check internal links
    for match in re.finditer(r'<a\s+[^>]*href=["\']([^"\'#][^"\']*)["\']', content, re.IGNORECASE):
        href = match.group(1).split('?')[0].split('#')[0]
        if href.startswith(('http://', 'https://', 'mailto:', 'javascript:', 'tel:', '${')):
            continue
        # Resolve path
        curr_dir = os.path.dirname(path)
        target_path = os.path.normpath(os.path.join(curr_dir, href)).replace('\\', '/')
        if not os.path.exists(target_path):
            seo_report['broken_links'].append((path, href, target_path))

print("\n--- AUDIT SUMMARY ---")
for k, v in seo_report.items():
    print(f"{k}: {len(v)} issues")
    if len(v) > 0 and len(v) <= 10:
        for item in v:
            print(f"   • {item}")
    elif len(v) > 10:
        print(f"   • Sample: {v[:5]}")

