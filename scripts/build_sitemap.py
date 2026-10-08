"""
Sitemap Generator for Vytra
Domain: https://vytra.in/
"""

import os
from datetime import datetime

ROOT_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"
BASE_URL = "https://vytra.in/"

# Canonical entries
entries = [
    # Homepage
    ("", "daily", "1.00"),
    # Master directory
    ("tools/index.html", "daily", "0.95"),
    # Category Hubs
    ("pdf/index.html", "weekly", "0.90"),
    ("image/index.html", "weekly", "0.90"),
    ("calculators/index.html", "weekly", "0.90"),
    ("developer/index.html", "weekly", "0.90"),
    ("text/index.html", "weekly", "0.90"),
    ("utilities/index.html", "weekly", "0.90"),
    # Legal / About
    ("about.html", "monthly", "0.70"),
    ("contact.html", "monthly", "0.70"),
    ("privacy.html", "monthly", "0.70"),
    ("terms.html", "monthly", "0.70"),
    ("cookie-policy.html", "monthly", "0.70")
]

# Add all tool files
categories = ["pdf", "image", "calculators", "developer", "text", "utilities"]
for cat in categories:
    dirpath = os.path.join(ROOT_DIR, cat)
    if os.path.exists(dirpath):
        for f in sorted(os.listdir(dirpath)):
            if f.endswith(".html") and f != "index.html":
                relpath = f"{cat}/{f}"
                entries.append((relpath, "weekly", "0.85"))

# Exclude design-system.html
today = datetime.now().strftime("%Y-%m-%d")

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for path, freq, priority in entries:
    loc = f"{BASE_URL}/{path}".rstrip("/") if path else f"{BASE_URL}/"
    xml_lines.append("  <url>")
    xml_lines.append(f"    <loc>{loc}</loc>")
    xml_lines.append(f"    <lastmod>{today}</lastmod>")
    xml_lines.append(f"    <changefreq>{freq}</changefreq>")
    xml_lines.append(f"    <priority>{priority}</priority>")
    xml_lines.append("  </url>")

xml_lines.append("</urlset>")
xml_content = "\n".join(xml_lines)

sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

print(f"Generated clean sitemap.xml with {len(entries)} URLs.")
