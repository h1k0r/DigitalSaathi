#!/usr/bin/env python3
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"
IMAGE_DIR = os.path.join(BASE_DIR, "image")
os.makedirs(IMAGE_DIR, exist_ok=True)

NAV_HEADER = """  <nav class="navbar" id="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="logo">
        <span class="logo-badge">🌐</span>
        <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      <ul class="nav-links">
        <li class="nav-item">
          <a href="../pdf/index.html" class="nav-link">📑 PDF Tools</a>
          <div class="nav-dropdown">
            <a href="../pdf/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> PDF Compressor</a>
            <a href="../pdf/merge.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Merge PDFs</a>
            <a href="../pdf/split.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Split PDF</a>
            <a href="../pdf/pdf-to-jpg.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> PDF to JPG</a>
            <a href="../pdf/jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
            <a href="../pdf/rotate.html" class="dropdown-link"><span class="dropdown-icon">🔄</span> Rotate PDF</a>
            <a href="../pdf/index.html" class="dropdown-link"><span class="dropdown-icon">✨</span> All 38 PDF Tools →</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="index.html" class="nav-link active">🖼️ Image Tools</a>
          <div class="nav-dropdown">
            <a href="compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> Image Compressor</a>
            <a href="resize.html" class="dropdown-link"><span class="dropdown-icon">📐</span> Image Resizer</a>
            <a href="crop.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Crop Image</a>
            <a href="convert.html" class="dropdown-link"><span class="dropdown-icon">🔄</span> Image Converter</a>
            <a href="jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
            <a href="remove-bg.html" class="dropdown-link"><span class="dropdown-icon">🎭</span> Photo BG Changer</a>
            <a href="index.html" class="dropdown-link"><span class="dropdown-icon">✨</span> All Image Tools →</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../cybercafe/passport-photo.html" class="nav-link">🖥️ Cyber Café</a>
          <div class="nav-dropdown">
            <a href="../cybercafe/passport-photo.html" class="dropdown-link"><span class="dropdown-icon">📸</span> Passport Photo Maker</a>
            <a href="../cybercafe/signature.html" class="dropdown-link"><span class="dropdown-icon">✍️</span> Signature Resizer (&lt;20KB)</a>
            <a href="resize.html" class="dropdown-link"><span class="dropdown-icon">📐</span> Image Resizer</a>
            <a href="compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> Image Compressor</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../student/resume.html" class="nav-link">🎓 Student & Jobs</a>
          <div class="nav-dropdown">
            <a href="../student/resume.html" class="dropdown-link"><span class="dropdown-icon">📝</span> Live Resume Builder</a>
            <a href="../jobs/government.html" class="dropdown-link"><span class="dropdown-icon">🏛️</span> Government Jobs 2026</a>
            <a href="../calculators/cgpa.html" class="dropdown-link"><span class="dropdown-icon">🎓</span> CGPA Calculator</a>
            <a href="../calculators/attendance.html" class="dropdown-link"><span class="dropdown-icon">📅</span> Attendance Calculator</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../developer/json.html" class="nav-link">💻 Dev Tools</a>
          <div class="nav-dropdown">
            <a href="../developer/json.html" class="dropdown-link"><span class="dropdown-icon">💻</span> JSON Formatter</a>
            <a href="../developer/sql.html" class="dropdown-link"><span class="dropdown-icon">💾</span> SQL Query Formatter</a>
          </div>
        </li>
      </ul>
      <div class="nav-actions">
        <a href="compress.html" class="btn btn-primary btn-sm">Compress Image</a>
      </div>
    </div>
  </nav>"""

FOOTER_HTML = """  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-col footer-about">
        <div class="logo">
          <span class="logo-badge">🌐</span>
          <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
        </div>
        <p class="footer-tagline">Your Digital Companion for Students, Job Seekers & Cyber Cafés across India.</p>
        <div class="footer-badges">
          <span class="badge badge-success">✓ 100% Free</span>
          <span class="badge badge-info">✓ Client-Side Privacy</span>
          <span class="badge badge-warning">✓ Offline Ready</span>
        </div>
      </div>
      <div class="footer-col">
        <h4 class="footer-title">Image Tools</h4>
        <ul class="footer-links">
          <li><a href="compress.html">Image Compressor</a></li>
          <li><a href="resize.html">Image Resizer</a></li>
          <li><a href="crop.html">Image Cropper</a></li>
          <li><a href="convert.html">Image Format Converter</a></li>
          <li><a href="jpg-to-pdf.html">JPG to PDF</a></li>
          <li><a href="remove-bg.html">Passport BG Changer</a></li>
          <li><a href="bulk-resize.html">Bulk Image Resizer</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-title">Govt Exam Tools</h4>
        <ul class="footer-links">
          <li><a href="../cybercafe/passport-photo.html">Passport Photo (3.5x4.5cm)</a></li>
          <li><a href="../cybercafe/signature.html">Signature Resizer (&lt;20KB)</a></li>
          <li><a href="dpi-converter.html">DPI / PPI Converter (300 DPI)</a></li>
          <li><a href="blur-face.html">Blur & Redact Aadhaar/PAN</a></li>
          <li><a href="../jobs/government.html">Government Jobs 2026</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-title">PDF & Dev Tools</h4>
        <ul class="footer-links">
          <li><a href="../pdf/compress.html">Compress PDF (&lt;100KB)</a></li>
          <li><a href="../pdf/merge.html">Merge PDF Documents</a></li>
          <li><a href="../student/resume.html">Live Resume Builder</a></li>
          <li><a href="../developer/json.html">JSON Formatter</a></li>
          <li><a href="../privacy.html">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container footer-bottom-container">
        <p>&copy; 2026 DigitalSaathi. Built for India. Free & Open Client-Side Web Platform.</p>
        <div class="footer-bottom-links">
          <a href="../privacy.html">Privacy Policy</a>
          <a href="../terms.html">Terms of Service</a>
          <a href="../contact.html">Contact Support</a>
        </div>
      </div>
    </div>
  </footer>"""

def wrap_page(title, desc, filename, body_inner, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | DigitalSaathi</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://digitalsaathi.in/image/{filename}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} | DigitalSaathi">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://digitalsaathi.in/image/{filename}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  {extra_head}
  <style>
    .tool-page-container {{ max-width: 900px; margin: 2rem auto 4rem; padding: 0 1rem; }}
    .tool-header-box {{ text-align: center; margin-bottom: 2rem; }}
    .tool-header-title {{ font-size: clamp(1.8rem, 3.5vw, 2.3rem); font-weight: 800; color: var(--text-main, #0f172a); margin-bottom: 0.5rem; letter-spacing: -0.02em; }}
    .tool-header-desc {{ color: var(--text-muted, #64748b); font-size: 1.05rem; max-width: 650px; margin: 0 auto; }}
    .tool-main-card {{ background: var(--bg-surface, #ffffff); border: 1px solid var(--border-subtle, #e2e8f0); border-radius: var(--radius-xl, 16px); padding: 2rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }}
    .tool-upload-box {{ border: 2px dashed var(--primary-300, #93c5fd); background: var(--primary-50, #eff6ff); border-radius: 12px; padding: 2.5rem 1.5rem; text-align: center; cursor: pointer; transition: all 0.2s; }}
    .tool-upload-box:hover {{ background: #dbeafe; border-color: var(--primary, #2563eb); }}
    .tool-controls-panel {{ margin-top: 1.5rem; background: var(--bg-surface-subtle, #f8fafc); border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 12px; padding: 1.5rem; }}
    .tool-preview-panel {{ margin-top: 1.5rem; text-align: center; }}
    .tool-stat-badge {{ display: inline-block; padding: 0.4rem 0.8rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem; margin: 0.25rem; }}
    .badge-stat-orig {{ background: #f1f5f9; color: #475569; }}
    .badge-stat-new {{ background: #ecfdf5; color: #059669; }}
    .badge-stat-saved {{ background: #eff6ff; color: #2563eb; }}
  </style>
</head>
<body>
{NAV_HEADER}
  <main class="tool-page-container">
{body_inner}
  </main>
{FOOTER_HTML}
  <script src="../assets/js/common.js"></script>
</body>
</html>"""

def write_file(filename, content):
    filepath = os.path.join(IMAGE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Generated image/{filename}")

print("Creating image tools...")
