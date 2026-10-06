"""
Inject official Google AdSense verification & auto ads script into <head> of all HTML pages.
"""

import os
import glob
import re

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"

ADSENSE_SCRIPT = """  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7919122689237518"
     crossorigin="anonymous"></script>
</head>"""

html_files = glob.glob(os.path.join(BASE_DIR, '**', '*.html'), recursive=True)
html_files = [f for f in html_files if not os.path.normpath(f).startswith(os.path.normpath(os.path.join(BASE_DIR, 'tests'))) and not os.path.normpath(f).startswith(os.path.normpath(os.path.join(BASE_DIR, '.git')))]

injected_count = 0

for filepath in html_files:
    rel_path = os.path.relpath(filepath, BASE_DIR)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'ca-pub-7919122689237518' in content:
        continue

    if '</head>' in content:
        # Replace the last or primary </head>
        updated_content = re.sub(r'</head>', ADSENSE_SCRIPT, content, count=1, flags=re.IGNORECASE)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        injected_count += 1
        print(f"Injected AdSense tag: {rel_path}")

print("=" * 60)
print(f"Successfully injected Google AdSense script into {injected_count} HTML pages!")
print("=" * 60)
