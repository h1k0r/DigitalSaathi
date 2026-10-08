"""
Rebrand DigitalSaathi to Vytra across all HTML, JS, CSS, JSON, and Markdown files.
Maintains git remote URL and repository links (https://github.com/h1k0r/DigitalSaathi) intact.
"""

import os
import glob
import re

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"

# File patterns to update
target_extensions = ('.html', '.js', '.json', '.md', '.txt', '.xml')

# Files or folders to exclude
exclude_dirs = {'.git', '.system_generated', 'tests', '__pycache__'}

files_to_process = []
for root, dirs, files in os.walk(BASE_DIR):
    # filter excluded dirs in-place
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith(target_extensions):
            files_to_process.append(os.path.join(root, file))

print(f"Total files candidate for rebranding: {len(files_to_process)}")

modified_count = 0
total_replacements = 0

for filepath in files_to_process:
    rel_path = os.path.relpath(filepath, BASE_DIR)
    # Skip script itself
    if rel_path == os.path.join("scripts", "rebrand_to_vytra.py"):
        continue

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {rel_path}: {e}")
        continue

    original_content = content

    # 1. Protect github repo URL: temporarily replace it with a unique token
    content = content.replace("https://github.com/h1k0r/DigitalSaathi", "___GITHUB_REPO_URL_TOKEN___")
    content = content.replace("github.com/h1k0r/DigitalSaathi", "___GITHUB_REPO_URL_TOKEN_SHORT___")

    # 2. Rebrand Logo Spans
    content = re.sub(r'Digital\s*<span\s+class=["\']logo-highlight["\']>Saathi</span>', r'Vy<span class="logo-highlight">tra</span>', content, flags=re.I)
    content = re.sub(r'Digital\s*<span\s+class=\\"logo-highlight\\">Saathi</span>', r'Vy<span class=\\"logo-highlight\\">tra</span>', content, flags=re.I)
    
    # 3. Logo text inside plain spans or links
    content = re.sub(r'<span class=["\']logo-text["\']>DigitalSaathi</span>', r'<span class="logo-text">Vy<span class="logo-highlight">tra</span></span>', content, flags=re.I)

    # 4. Email addresses: update support email to support@vytra.in
    content = content.replace("support@vytra.in", "support@vytra.in")

    # 5. Titles and Brand Names
    content = content.replace("— DigitalSaathi", "— Vytra")
    content = content.replace("- DigitalSaathi", "- Vytra")
    content = content.replace("| DigitalSaathi", "| Vytra")
    content = content.replace("DigitalSaathi Online Tools Suite", "Vytra Online Tools Suite")
    content = content.replace("DigitalSaathi Tools Suite", "Vytra Tools Suite")
    content = content.replace("DigitalSaathi Tools", "Vytra Tools")
    content = content.replace("DigitalSaathi Platform", "Vytra Platform")
    content = content.replace("DigitalSaathi platform", "Vytra platform")
    content = content.replace("DigitalSaathi ecosystem", "Vytra ecosystem")
    content = content.replace("DigitalSaathi website", "Vytra website")
    content = content.replace("DigitalSaathi", "Vytra")
    content = content.replace("Digital Saathi", "Vytra")

    # 6. Restore github repo URL
    content = content.replace("___GITHUB_REPO_URL_TOKEN___", "https://github.com/h1k0r/DigitalSaathi")
    content = content.replace("___GITHUB_REPO_URL_TOKEN_SHORT___", "github.com/h1k0r/DigitalSaathi")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        modified_count += 1
        print(f"Updated: {rel_path}")

print("=" * 60)
print(f"Rebranding Complete: {modified_count} files successfully updated to 'Vytra'!")
print("=" * 60)
