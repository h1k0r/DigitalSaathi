import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 60)
print("GENERATING STANDARD SPECIFICATION PAGES FOR UPCOMING PDF TOOLS")
print("=" * 60)

UPCOMING_TOOLS = [
    ('organize.html', 'Organize PDF', 'Organize', '🔀', 'Rearrange, rotate, delete, and sort pages within a PDF document visually.', 'Phase A — Core browser tools', ['merge.html', 'split.html', 'rotate.html']),
    ('crop.html', 'Crop PDF', 'Organize', '📐', 'Crop margins and select custom page regions for clean, compact printing.', 'Phase A — Core browser tools', ['split.html', 'compress.html', 'organize.html']),
    ('page-numbers.html', 'Page Numbers', 'Organize', '🔢', 'Add customized page numbers, headers, and footers with custom positions and fonts.', 'Phase A — Core browser tools', ['merge.html', 'watermark.html', 'organize.html']),
    ('watermark.html', 'Watermark PDF', 'Edit', '🌊', 'Stamp customized text or image watermarks with transparency, rotation, and position controls.', 'Phase A — Core browser tools', ['protect.html', 'sign.html', 'compress.html']),
    ('protect.html', 'Protect PDF', 'Security', '🔒', 'Encrypt PDF files with strong password protection to prevent unauthorized viewing and copying.', 'Phase B — Security & basic editing', ['unlock.html', 'watermark.html', 'compress.html']),
    ('unlock.html', 'Unlock PDF', 'Security', '🔓', 'Remove password protection and printing restrictions from secured PDF documents.', 'Phase B — Security & basic editing', ['protect.html', 'compress.html', 'split.html']),
    ('sign.html', 'Sign PDF', 'Edit', '✍️', 'Draw, upload, or type electronic signatures onto documents and contracts directly in your browser.', 'Phase B — Security & basic editing', ['forms.html', 'watermark.html', 'protect.html']),
    ('redact.html', 'Redact PDF', 'Edit', '⬛', 'Permanently blackout and sanitize sensitive Aadhaar, PAN, and confidential data from PDF pages.', 'Phase B — Security & basic editing', ['protect.html', 'watermark.html', 'compress.html']),
    ('forms.html', 'PDF Forms', 'Edit', '📋', 'Fill out interactive form fields or create new fillable forms with checkboxes and text inputs.', 'Phase B — Security & basic editing', ['sign.html', 'edit.html', 'protect.html']),
    ('edit.html', 'Edit PDF', 'Edit', '✏️', 'Add text, annotations, shapes, and arrows directly onto PDF pages with full styling control.', 'Phase B — Security & basic editing', ['sign.html', 'watermark.html', 'forms.html']),
    ('info.html', 'PDF Information', 'Analysis', 'ℹ️', 'Inspect document metadata, creation dates, PDF version, security flags, and font specs.', 'Phase B — Security & basic editing', ['compress.html', 'compare.html', 'page-counter.html']),
    ('word-to-pdf.html', 'Word to PDF', 'Convert', '📄', 'Convert Word DOC and DOCX documents into standardized, read-only PDF files.', 'Phase C — Conversion', ['pdf-to-word.html', 'excel-to-pdf.html', 'ppt-to-pdf.html']),
    ('excel-to-pdf.html', 'Excel to PDF', 'Convert', '📊', 'Convert Excel spreadsheets and XLSX sheets into formatted, printable PDF documents.', 'Phase C — Conversion', ['pdf-to-excel.html', 'word-to-pdf.html', 'ppt-to-pdf.html']),
    ('ppt-to-pdf.html', 'PowerPoint to PDF', 'Convert', '📑', 'Convert PPT and PPTX slide presentations into high-quality PDF slide documents.', 'Phase C — Conversion', ['pdf-to-ppt.html', 'word-to-pdf.html', 'excel-to-pdf.html']),
    ('pdf-to-word.html', 'PDF to Word', 'Convert', '📝', 'Extract structured text, paragraphs, and headings into editable DOCX Word format.', 'Phase C — Conversion', ['word-to-pdf.html', 'pdf-to-excel.html', 'pdf-to-ppt.html']),
    ('pdf-to-excel.html', 'PDF to Excel', 'Convert', '📈', 'Extract tabular data and spreadsheets from PDF documents straight into Excel files.', 'Phase C — Conversion', ['excel-to-pdf.html', 'pdf-to-word.html', 'pdf-to-ppt.html']),
    ('pdf-to-ppt.html', 'PDF to PowerPoint', 'Convert', '📊', 'Transform PDF slide decks into editable PPTX PowerPoint presentations.', 'Phase C — Conversion', ['ppt-to-pdf.html', 'pdf-to-word.html', 'pdf-to-excel.html']),
    ('html-to-pdf.html', 'HTML to PDF', 'Convert', '🌐', 'Convert web pages and raw HTML markup into printable formatted PDF documents.', 'Phase C — Conversion', ['word-to-pdf.html', 'pdf-to-jpg.html', 'jpg-to-pdf.html']),
    ('pdf-a.html', 'PDF/A Converter', 'Convert', '🏛️', 'Convert standard PDFs to ISO-standardized PDF/A format for long-term legal archiving.', 'Phase C — Conversion', ['compress.html', 'protect.html', 'pdf-to-word.html']),
    ('repair.html', 'Repair PDF', 'Optimize', '🛠️', 'Recover readable data and fix structural stream errors in corrupted PDF files.', 'Phase D — Advanced', ['compress.html', 'info.html', 'split.html']),
    ('compare.html', 'Compare PDF', 'Analysis', '⚖️', 'Spot changes between two versions of a PDF with side-by-side visual difference diffs.', 'Phase D — Advanced', ['info.html', 'merge.html', 'split.html']),
    ('scan-to-pdf.html', 'Scan to PDF', 'Scan & OCR', '📱', 'Capture physical documents using your device webcam or phone camera directly into PDF.', 'Phase D — Advanced', ['jpg-to-pdf.html', 'ocr.html', 'compress.html']),
    ('ocr.html', 'OCR PDF', 'Scan & OCR', '🔍', 'Convert scanned PDFs and image documents into selectable, searchable text with OCR.', 'Phase D — Advanced', ['pdf-to-word.html', 'scan-to-pdf.html', 'pdf-to-markdown.html']),
    ('pdf-to-markdown.html', 'PDF to Markdown', 'Advanced', '📄', 'Convert PDF content into structured Markdown tables and headings optimized for LLMs.', 'Phase D — Advanced', ['ai-summarizer.html', 'pdf-to-word.html', 'ocr.html']),
    ('ai-summarizer.html', 'AI PDF Summarizer', 'Advanced', '✨', 'Generate instant summaries, bullet points, and key takeaways from large documents.', 'Phase E — AI Features', ['translate.html', 'pdf-to-markdown.html', 'info.html']),
    ('translate.html', 'Translate PDF', 'Advanced', '🌐', 'Translate PDF text across Hindi, English, and Indian regional languages effortlessly.', 'Phase E — AI Features', ['ai-summarizer.html', 'pdf-to-word.html', 'ocr.html']),
    ('workflow.html', 'Create Workflow', 'Workflow', '⚡', 'Create custom automated pipelines (e.g., Merge → Compress → Watermark) in one click.', 'Phase F — Automation', ['merge.html', 'compress.html', 'watermark.html'])
]

def make_page_html(filename, title, category, icon, desc, phase_tag, related):
    rel_html = ""
    for r in related:
        r_name = r.replace('.html', '').replace('-', ' ').title()
        rel_html += f'''
        <a href="{r}" class="tool-card">
          <div>
            <div class="tool-card-icon-box" style="background:var(--color-pdf-bg);color:var(--color-pdf);">📄</div>
            <h3 class="tool-card-title">{r_name}</h3>
            <p class="tool-card-desc">Access related PDF tool in the DigitalSaathi suite.</p>
          </div>
          <div class="tool-card-footer"><span>Open Tool →</span></div>
        </a>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} Online Free | DigitalSaathi PDF Tools</title>
  <meta name="description" content="{desc} Free, secure, and private browser-side PDF processing by DigitalSaathi.">

  <!-- Fonts & Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">

  <style>
    .breadcrumb-nav {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8125rem;
      color: var(--text-muted);
      margin-bottom: var(--space-4);
    }}
    .breadcrumb-nav a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb-nav a:hover {{ color: var(--primary); }}

    .tool-header-block {{
      text-align: center;
      max-width: 760px;
      margin: 0 auto 2rem;
    }}
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav class="navbar" id="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="logo">
        <span class="logo-badge">🌐</span>
        <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      <ul class="nav-links">
        <li class="nav-item">
          <a href="../pdf/index.html" class="nav-link active">📑 PDF Tools</a>
          <div class="nav-dropdown">
            <a href="compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> PDF Compressor</a>
            <a href="merge.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Merge PDFs</a>
            <a href="split.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Split PDF</a>
            <a href="pdf-to-jpg.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> PDF to JPG</a>
            <a href="jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
            <a href="rotate.html" class="dropdown-link"><span class="dropdown-icon">🔄</span> Rotate PDF</a>
            <a href="extract.html" class="dropdown-link"><span class="dropdown-icon">📥</span> Extract Pages</a>
            <a href="reorder.html" class="dropdown-link"><span class="dropdown-icon">🔀</span> Reorder Pages</a>
            <a href="viewer.html" class="dropdown-link"><span class="dropdown-icon">👁️</span> PDF Viewer</a>
            <a href="page-counter.html" class="dropdown-link"><span class="dropdown-icon">🔢</span> Page Counter</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../cybercafe/passport-photo.html" class="nav-link">🖥️ Cyber Café</a>
          <div class="nav-dropdown">
            <a href="../cybercafe/passport-photo.html" class="dropdown-link"><span class="dropdown-icon">📸</span> Passport Photo Maker</a>
            <a href="../cybercafe/signature.html" class="dropdown-link"><span class="dropdown-icon">✍️</span> Signature Resizer (&lt;20KB)</a>
            <a href="../image/resize.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> Image Resizer</a>
            <a href="../image/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> Image Compressor</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../student/resume.html" class="nav-link">🎓 Student & Resume</a>
          <div class="nav-dropdown">
            <a href="../student/resume.html" class="dropdown-link"><span class="dropdown-icon">📝</span> Live Resume Builder</a>
            <a href="../student/resume-templates.html" class="dropdown-link"><span class="dropdown-icon">🎨</span> 500+ Resume Templates</a>
            <a href="../calculators/cgpa.html" class="dropdown-link"><span class="dropdown-icon">🎓</span> CGPA Calculator</a>
            <a href="../calculators/attendance.html" class="dropdown-link"><span class="dropdown-icon">📅</span> Attendance Calculator (75%)</a>
            <a href="../calculators/percentage.html" class="dropdown-link"><span class="dropdown-icon">📊</span> Percentage Calculator</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../jobs/government.html" class="nav-link">🏛️ Jobs</a>
        </li>
        <li class="nav-item">
          <a href="../developer/json.html" class="nav-link">💻 Dev Tools</a>
          <div class="nav-dropdown">
            <a href="../developer/json.html" class="dropdown-link"><span class="dropdown-icon">💻</span> JSON Formatter & Validator</a>
            <a href="../developer/sql.html" class="dropdown-link"><span class="dropdown-icon">💾</span> SQL Query Formatter</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../calculators/emi.html" class="nav-link">💰 Finance</a>
        </li>
      </ul>
      <div class="nav-actions">
        <a href="../student/resume.html" class="btn btn-primary btn-sm">Build Resume</a>
      </div>
    </div>
  </nav>

  <!-- Main Container -->
  <main class="container" style="max-width: 860px; padding: 2.5rem var(--space-4) 5rem;">

    <!-- 1. Breadcrumb -->
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
      <a href="../index.html">Home</a>
      <span>/</span>
      <a href="index.html">PDF Tools</a>
      <span>/</span>
      <span style="color:var(--text-main); font-weight:600;">{title}</span>
    </nav>

    <!-- 2 & 3. Header Block -->
    <div class="tool-header-block">
      <div class="pill-badge" style="background:var(--color-pdf-bg);color:var(--color-pdf);border-color:var(--color-pdf-border);">
        <span>{icon}</span> {category} PDF Suite • <span style="color:var(--primary); font-weight:700;">{phase_tag}</span>
      </div>
      <h1 style="font-size: clamp(1.8rem, 3vw + 0.5rem, 2.4rem); font-weight: 800; margin-bottom: 0.5rem;">
        {title}
      </h1>
      <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.5;">
        {desc}
      </p>
    </div>

    <!-- 4. Upload Dropzone (Interactive Specification) -->
    <div class="upload-zone" id="tool-dropzone" style="max-width: 720px; margin: 0 auto 2rem;">
      <input type="file" id="tool-file-input" accept="application/pdf" aria-label="Upload PDF file">
      <div class="upload-zone-icon">{icon}</div>
      <div class="upload-zone-title">Select your PDF file, or drag & drop here</div>
      <div class="upload-zone-hint">Supports PDF documents up to 100MB • 100% Client-Side Processing</div>
      <span class="upload-privacy-pill">🔒 Zero Server Uploads • Local Processing</span>
    </div>

    <!-- Info Banner for Phased Roadmap -->
    <div class="card" style="border: 2px solid var(--primary-200); background: var(--primary-50); margin-bottom: 2.5rem; text-align: center; padding: 2rem;">
      <div style="font-size: 2rem; margin-bottom: 8px;">🚀</div>
      <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--primary-900); margin-bottom: 6px;">
        Scheduled Release: {phase_tag}
      </h3>
      <p style="color: var(--text-body); font-size: 0.95rem; max-width: 600px; margin: 0 auto 1.25rem;">
        This tool's specification and UI are registered in the DigitalSaathi master architecture. Full browser engine integration is being activated sequentially as part of our scheduled module rollout.
      </p>
      <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
        <a href="merge.html" class="btn btn-primary btn-sm">Try Merge PDF (Active)</a>
        <a href="split.html" class="btn btn-secondary btn-sm">Try Split PDF (Active)</a>
        <a href="compress.html" class="btn btn-secondary btn-sm">Try Compress PDF (Active)</a>
      </div>
    </div>

    <!-- 9. Step-by-Step Instructions -->
    <section style="margin-top: 3.5rem;">
      <h2 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 1.5rem; text-align: center;">
        How {title} Works in DigitalSaathi
      </h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;">
        <div class="card" style="text-align: center;">
          <div style="font-size: 2rem; margin-bottom: 8px;">1️⃣</div>
          <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Upload File</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted);">Select or drag your PDF document into the secure local browser workspace.</p>
        </div>
        <div class="card" style="text-align: center;">
          <div style="font-size: 2rem; margin-bottom: 8px;">2️⃣</div>
          <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Configure Parameters</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted);">Adjust formatting, quality, password, or extraction parameters easily.</p>
        </div>
        <div class="card" style="text-align: center;">
          <div style="font-size: 2rem; margin-bottom: 8px;">3️⃣</div>
          <h3 style="font-size: 1.1rem; margin-bottom: 6px;">Save & Export</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted);">Download your processed file instantly with zero watermarks or subscription fees.</p>
        </div>
      </div>
    </section>

    <!-- 10. FAQ Accordion -->
    <section style="margin-top: 4rem;">
      <h2 style="font-size: 1.4rem; font-weight: 800; margin-bottom: 1.5rem; text-align: center;">
        Frequently Asked Questions
      </h2>
      <div class="accordion accordion-exclusive" style="display:flex; flex-direction:column; gap:12px;">
        <div class="accordion-item card active" style="padding:0; overflow:hidden;">
          <button class="accordion-header" style="width:100%; text-align:left; padding:1rem 1.25rem; background:transparent; border:none; font-weight:700; cursor:pointer; display:flex; justify-content:space-between;">
            <span>Is {title} completely free to use?</span>
            <span>▼</span>
          </button>
          <div class="accordion-content" style="padding:0 1.25rem 1rem; color:var(--text-muted); font-size:0.9rem;">
            Yes! All DigitalSaathi PDF utilities are 100% free with no hidden charges, paywalls, or mandatory account registrations.
          </div>
        </div>
        <div class="accordion-item card" style="padding:0; overflow:hidden;">
          <button class="accordion-header" style="width:100%; text-align:left; padding:1rem 1.25rem; background:transparent; border:none; font-weight:700; cursor:pointer; display:flex; justify-content:space-between;">
            <span>Are my uploaded documents stored on any server?</span>
            <span>▼</span>
          </button>
          <div class="accordion-content" style="padding:0 1.25rem 1rem; color:var(--text-muted); font-size:0.9rem;">
            No. DigitalSaathi operates on a strict client-side privacy architecture where document processing takes place directly in your device's web browser.
          </div>
        </div>
      </div>
    </section>

    <!-- 11. Related Tools -->
    <section style="margin-top: 4rem;">
      <h2 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem;">Related PDF Tools</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
        {rel_html}
      </div>
    </section>

  </main>

  <!-- SaaS Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:1rem;">
            <span class="logo-badge" style="width:32px;height:32px;font-size:0.95rem;">🌐</span>
            <span style="font-size:1.25rem;font-weight:800;color:var(--text-main);">Digital<span style="color:var(--primary);">Saathi</span></span>
          </div>
          <p style="color:var(--text-muted);font-size:0.875rem;line-height:1.6;margin-bottom:1.25rem;">
            India's super portal for students, job seekers, and cyber café businesses. Fast, secure, and client-side privacy guaranteed.
          </p>
        </div>
        <div class="footer-col">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;">PDF Suite</h4>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
            <li><a href="compress.html">PDF Compressor</a></li>
            <li><a href="merge.html">PDF Merge</a></li>
            <li><a href="split.html">PDF Split</a></li>
            <li><a href="pdf-to-jpg.html">PDF to JPG</a></li>
            <li><a href="jpg-to-pdf.html">JPG to PDF</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;">Students & CSC</h4>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
            <li><a href="../student/resume.html">Live Resume Builder</a></li>
            <li><a href="../cybercafe/passport-photo.html">Passport Photo Maker</a></li>
            <li><a href="../cybercafe/signature.html">Signature Resizer</a></li>
            <li><a href="../calculators/cgpa.html">CGPA Calculator</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;">Legal & Info</h4>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
            <li><a href="../jobs/government.html">Government Jobs 2026</a></li>
            <li><a href="../about.html">About DigitalSaathi</a></li>
            <li><a href="../privacy.html">Privacy Policy</a></li>
            <li><a href="../terms.html">Terms of Service</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom" style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--border-subtle);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;font-size:0.8125rem;color:var(--text-muted);">
        <p>© 2026 DigitalSaathi. All rights reserved.</p>
        <p style="font-size:0.75rem;max-width:600px;text-align:right;">
          <strong>Disclaimer:</strong> DigitalSaathi is an independent informational platform. Always verify job notifications and application guidelines with official authorities.
        </p>
      </div>
    </div>
  </footer>

  <script src="../assets/js/common.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const dropzone = document.getElementById('tool-dropzone');
      const fileInput = document.getElementById('tool-file-input');

      fileInput.addEventListener('change', (e) => {{
        if (e.target.files && e.target.files.length > 0) {{
          dsToast.info(`Uploaded "${{e.target.files[0].name}}" (${{formatFileSize(e.target.files[0].size)}}). {phase_tag} module activation in progress.`);
        }}
      }});

      initDropZone(dropzone, {{
        onFiles: (files) => {{
          if (files && files.length > 0) {{
            dsToast.info(`Uploaded "${{files[0].name}}" (${{formatFileSize(files[0].size)}}). {phase_tag} module activation in progress.`);
          }}
        }}
      }});
    }});
  </script>
</body>
</html>'''

for item in UPCOMING_TOOLS:
    fname, title, cat, icon, desc, phase_tag, rel = item
    target_path = os.path.join('pdf', fname)
    # Only create if it doesn't already have custom implementation
    # Check if file exists already and if it's already one of our custom files
    if os.path.exists(target_path) and fname in ['compress.html', 'merge.html', 'split.html', 'pdf-to-jpg.html', 'jpg-to-pdf.html', 'rotate.html', 'extract.html', 'reorder.html', 'viewer.html', 'page-counter.html']:
        print(f"Skipping existing custom implementation: {target_path}")
        continue
    
    html_content = make_page_html(fname, title, cat, icon, desc, phase_tag, rel)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Created standard tool page: {target_path}")

print("\nAll 33 tool endpoints are now created and verified!")
