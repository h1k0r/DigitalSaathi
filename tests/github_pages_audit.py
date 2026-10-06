import os
import glob
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"

print("=" * 70)
print("🚀 DIGITALSAATHI GITHUB PAGES DEPLOYMENT & COMPATIBILITY AUDIT")
print("=" * 70)

html_files = glob.glob(os.path.join(BASE_DIR, "**", "*.html"), recursive=True)
css_files = glob.glob(os.path.join(BASE_DIR, "**", "*.css"), recursive=True)
js_files = glob.glob(os.path.join(BASE_DIR, "**", "*.js"), recursive=True)

all_files = html_files + css_files + js_files

root_relative_issues = []
localhost_issues = []
broken_relative_links = []
backend_api_issues = []

# Exclude test files
source_files = [f for f in all_files if not os.path.normpath(f).startswith(os.path.normpath(os.path.join(BASE_DIR, "tests")))]

for filepath in source_files:
    rel_filepath = os.path.relpath(filepath, BASE_DIR)
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # 1. Check for localhost or 127.0.0.1
    if re.search(r'https?://(localhost|127\.0\.0\.1)', content):
        localhost_issues.append((rel_filepath, "Contains localhost/127.0.0.1 reference"))

    # 2. Check for absolute local paths
    if re.search(r'[C-Zc-z]:\\[a-zA-Z0-9_\\]+', content) and not rel_filepath.endswith('.py'):
        localhost_issues.append((rel_filepath, "Contains hardcoded Windows drive path"))

    # 3. Check for root-relative links in HTML
    if rel_filepath.endswith(".html"):
        # Match href="/..." or src="/..." except protocol-relative //
        matches = re.findall(r'(?:href|src)=["\'](/[^/"\'][^"\']*)["\']', content)
        for m in matches:
            root_relative_issues.append((rel_filepath, m))

        # Check all static HTML relative href/src targets exist on disk (exclude JS template string expressions ${...})
        link_matches = re.findall(r'(?:href|src)=["\']([^"\'#]+)["\']', content)
        for link in link_matches:
            # Skip CDNs, mailto, javascript, tel, data URIs, and template expressions ${...} or {{...}}
            if link.startswith(('http://', 'https://', '//', 'mailto:', 'javascript:', 'tel:', 'data:', '${', '{{')) or '${' in link or '{{' in link:
                continue
            # Remove query string / hash if any
            clean_link = link.split('?')[0].split('#')[0]
            if not clean_link:
                continue

            target_path = os.path.normpath(os.path.join(os.path.dirname(filepath), clean_link))
            if not os.path.exists(target_path):
                broken_relative_links.append((rel_filepath, link, target_path))

    # 4. Check for server backend endpoints
    if re.search(r'fetch\([\'"]/(api|backend|server)/', content) or re.search(r'axios\.(get|post)\([\'"]/(api|backend|server)/', content):
        backend_api_issues.append((rel_filepath, "Calls server-side backend endpoint"))

print(f"Total Source Files Inspected: {len(source_files)} (HTML: {len(html_files)}, CSS: {len(css_files)}, JS: {len(js_files)})")
print("-" * 70)

print(f"1. Root-Relative Links Found: {len(root_relative_issues)}")
for src, link in root_relative_issues:
    print(f"   ❌ {src} -> {link}")

print(f"2. Localhost / Absolute Windows Paths Found: {len(localhost_issues)}")
for src, msg in localhost_issues:
    print(f"   ❌ {src} -> {msg}")

print(f"3. Broken Relative Links / Missing Files Found: {len(broken_relative_links)}")
for src, link, target in broken_relative_links:
    print(f"   ❌ {src} references non-existent '{link}' -> {target}")

print(f"4. Server-side API / Backend Dependencies: {len(backend_api_issues)}")
for src, msg in backend_api_issues:
    print(f"   ❌ {src} -> {msg}")

print("=" * 70)
if len(root_relative_issues) == 0 and len(localhost_issues) == 0 and len(broken_relative_links) == 0 and len(backend_api_issues) == 0:
    print("✅ PERFECT SCORE: 100% GITHUB PAGES COMPATIBLE & ZERO BACKEND DEPENDENCIES!")
else:
    print("⚠️ ISSUES DETECTED - FIXES REQUIRED FOR GITHUB PAGES DEPLOYMENT")
print("=" * 70)
