import os
import glob
import re

pdf_files = glob.glob('pdf/*.html')

for path in pdf_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace href="#" on download buttons with href="javascript:void(0)"
    content = content.replace('href="#" class="btn btn-primary', 'href="javascript:void(0)" class="btn btn-primary')

    # Fix aria-label for radio buttons
    content = content.replace('name="applyScope" value="all"', 'name="applyScope" value="all" aria-label="Apply crop to all pages"')
    content = content.replace('name="applyScope" value="current"', 'name="applyScope" value="current" aria-label="Apply crop to current page only"')
    content = content.replace('name="redactColor" value="black"', 'name="redactColor" value="black" aria-label="Redact with black blackout rectangle"')
    content = content.replace('name="redactColor" value="white"', 'name="redactColor" value="white" aria-label="Redact with white whiteout rectangle"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Polished accessibility and hrefs.")
