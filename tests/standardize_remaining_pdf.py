import os
import glob
import re

PDF_FILES_TO_STANDARDIZE = [
    ('pdf/pdf-to-jpg.html', 'PDF to JPG', 'Convert'),
    ('pdf/jpg-to-pdf.html', 'JPG to PDF', 'Convert'),
    ('pdf/rotate.html', 'Rotate PDF', 'Organize'),
    ('pdf/extract.html', 'Extract Pages', 'Organize'),
    ('pdf/reorder.html', 'Reorder Pages', 'Organize'),
    ('pdf/viewer.html', 'PDF Viewer', 'Analysis'),
    ('pdf/page-counter.html', 'PDF Page Counter', 'Analysis')
]

for rel_path, title, cat in PDF_FILES_TO_STANDARDIZE:
    if not os.path.exists(rel_path):
        continue
    with open(rel_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add breadcrumb if missing
    if 'breadcrumb-nav' not in content:
        bc_html = f'''    <!-- Breadcrumb -->
    <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="display:flex;align-items:center;gap:8px;font-size:0.8125rem;color:var(--text-muted);margin-bottom:var(--space-4);">
      <a href="../index.html" style="color:var(--text-muted);text-decoration:none;">Home</a>
      <span>/</span>
      <a href="index.html" style="color:var(--text-muted);text-decoration:none;">PDF Tools</a>
      <span>/</span>
      <span style="color:var(--text-main);font-weight:600;">{title}</span>
    </nav>
'''
        # insert right after <main class="container ...">
        content = re.sub(r'(<main\b[^>]*>)', r'\1\n' + bc_html, content, count=1)

    # Standardize upload-area to upload-zone
    content = content.replace('class="upload-area"', 'class="upload-zone"')
    content = content.replace("class='upload-area'", "class='upload-zone'")

    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Standardized: {rel_path}")

print("All tool pages standardized!")
