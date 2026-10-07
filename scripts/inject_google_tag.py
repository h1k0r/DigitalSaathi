"""
Inject Google tag (gtag.js) G-R2EMRPEG70 into <head> of all HTML pages.
"""

import os
import glob
import re

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"

GTAG_SCRIPT = """<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R2EMRPEG70"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-R2EMRPEG70');
  </script>"""

html_files = glob.glob(os.path.join(BASE_DIR, '**', '*.html'), recursive=True)
html_files = [
    f for f in html_files
    if not os.path.normpath(f).startswith(os.path.normpath(os.path.join(BASE_DIR, 'tests')))
    and not os.path.normpath(f).startswith(os.path.normpath(os.path.join(BASE_DIR, '.git')))
]

injected_count = 0

for filepath in html_files:
    rel_path = os.path.relpath(filepath, BASE_DIR)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'G-R2EMRPEG70' in content:
        continue

    if re.search(r'<head\b[^>]*>', content, re.IGNORECASE):
        updated_content = re.sub(r'<head\b[^>]*>', GTAG_SCRIPT, content, count=1, flags=re.IGNORECASE)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        injected_count += 1
        print(f"Injected gtag: {rel_path}")

print("=" * 60)
print(f"Successfully injected Google Tag (G-R2EMRPEG70) into {injected_count} HTML pages!")
print("=" * 60)
