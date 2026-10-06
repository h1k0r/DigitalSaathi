import os
import glob
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

html_files = sorted(glob.glob('**/*.html', recursive=True))

print(f"Total HTML files to audit: {len(html_files)}")
for hf in html_files:
    is_subdir = os.path.dirname(hf) != ''
    rel_prefix = '../' if is_subdir else ''
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    has_h1 = bool(re.search(r'<h1[^>]*>', content, re.IGNORECASE))
    has_desc = bool(re.search(r'<meta[^>]+name=["\']description["\']', content, re.IGNORECASE))
    root_rel_count = len(re.findall(r'(?:href|src)=["\']/[^"\']+', content))
    inline_styles = len(re.findall(r'<style[^>]*>', content, re.IGNORECASE))

    print(f"{hf:35} | Subdir: {str(is_subdir):5} | H1: {str(has_h1):5} | Desc: {str(has_desc):5} | Root-Rel Links: {root_rel_count:2} | Inline <style>: {inline_styles}")
