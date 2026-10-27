#!/usr/bin/env python3
"""Site-wide validation after Phase-1 cleanup + blog build.

Checks:
  * every HTML page: unique <title>, has meta description + canonical + h1
  * no Login/Sign-up buttons or auth modal anywhere
  * no "thanks to advertising" / "iLovePDF-logic" / "Vytra Team" leftovers
  * all internal relative href/src targets exist (incl. new blog/ links)
  * JSON-LD blocks parse as valid JSON
  * blog pages: nav + footer blog links, no leaked auth UI
"""
import glob
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

errors = []
titles = {}

html_files = sorted(glob.glob("**/*.html", recursive=True))
html_files = [
    f
    for f in html_files
    if not f.startswith((".git", "node_modules"))
    and not f.startswith("templates" + os.sep)
    and not f.startswith("google")
    and f != "design-system.html"  # robots-disallowed internal style guide
]

FORBIDDEN = {
    "ilp-authbtn": "Login/Sign-up button",
    "ilpAuthOverlay": "Auth modal",
    "thanks to advertising": "Misleading ad line",
    "iLovePDF-logic": "Internal iLovePDF note",
    "Maintained by Vytra Team": "Anonymous attribution",
}

for f in html_files:
    with open(f, encoding="utf-8", errors="ignore") as fh:
        s = fh.read()

    m = re.search(r"<title>([^<]+)</title>", s)
    if not m:
        errors.append(f"{f}: missing <title>")
    else:
        titles.setdefault(m.group(1).strip(), []).append(f)

    if not re.search(r'<meta[^>]+name=["\']description["\']', s):
        errors.append(f"{f}: missing meta description")
    if not re.search(r"rel=[\"']canonical[\"']", s):
        errors.append(f"{f}: missing canonical")
    if not re.search(r"<h1[^>]*>", s):
        errors.append(f"{f}: missing <h1>")

    for needle, label in FORBIDDEN.items():
        if needle in s:
            errors.append(f"{f}: leftover {label} ('{needle}')")

    # relative link resolution
    base = os.path.dirname(f)
    for href in re.findall(r'(?:href|src)="([^"]+)"', s):
        if href.startswith(("http://", "https://", "mailto:", "#", "data:", "javascript:")):
            continue
        if "${" in href or "{{" in href:
            continue  # JS template literal, not a real link
        clean = href.split("#")[0].split("?")[0]
        if not clean:
            continue
        target = os.path.normpath(os.path.join(base, clean))
        if os.path.isdir(target):
            target = os.path.join(target, "index.html")
        if not os.path.exists(target):
            errors.append(f"{f}: dead link -> {href}")

    # JSON-LD validity
    for jm in re.finditer(
        r'<script type="application/ld\+json">(.*?)</script>', s, re.S
    ):
        try:
            json.loads(jm.group(1))
        except Exception as e:
            errors.append(f"{f}: invalid JSON-LD ({e})")

for title, files in titles.items():
    if len(files) > 1:
        errors.append(f"duplicate title '{title}': {files}")

# blog-specific
blog_files = sorted(glob.glob("blog/*.html"))
if len(blog_files) < 11:
    errors.append(f"expected >=11 blog files, found {len(blog_files)}")
for f in blog_files:
    with open(f, encoding="utf-8") as fh:
        s = fh.read()
    if "BLOG</a>" not in s:
        errors.append(f"{f}: nav BLOG link missing")
    if 'blog/">Blog &amp; Guides' not in s:
        errors.append(f"{f}: footer Blog link missing")

print(f"HTML files audited : {len(html_files)}")
print(f"Blog files         : {len(blog_files)}")
print(f"Unique titles      : {len(titles)}")
if errors:
    print(f"\n{len(errors)} ERRORS:")
    for e in errors:
        print("  " + e)
    sys.exit(1)
print("\nALL CHECKS PASSED")
