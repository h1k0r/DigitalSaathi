import os
import glob
import re

pdf_files = glob.glob('pdf/*.html')

for path in pdf_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Standardize breadcrumb-nav
    if 'class="breadcrumb"' in content and 'breadcrumb-nav' not in content:
        content = content.replace('<div class="breadcrumb">', '<nav class="breadcrumb-nav" aria-label="Breadcrumb"><div class="container breadcrumb">')
        # find the closing div of breadcrumb
        content = re.sub(r'(<nav class="breadcrumb-nav" aria-label="Breadcrumb"><div class="container breadcrumb">[\s\S]*?</div>)', r'\1</nav>', content, count=1)

    # 2. For html-to-pdf, make sure upload-zone is present or accessible
    if path == 'pdf\\html-to-pdf.html' or path == 'pdf/html-to-pdf.html':
        if 'upload-zone' not in content:
            content = content.replace('<div class="html-editor-grid">', '<div class="upload-zone" style="display:none;" id="uploadZone"></div>\n    <div class="html-editor-grid">')

    # 3. For scan-to-pdf, make sure upload-zone is present
    if path == 'pdf\\scan-to-pdf.html' or path == 'pdf/scan-to-pdf.html':
        if 'upload-zone' not in content:
            content = content.replace('<div class="scanner-workspace">', '<div class="upload-zone" style="display:none;" id="uploadZone"></div>\n    <div class="scanner-workspace">')

    # 4. Ensure relative paths
    content = content.replace('href="/', 'href="../').replace('src="/', 'src="../')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Standardized {len(pdf_files)} PDF tool files.")
