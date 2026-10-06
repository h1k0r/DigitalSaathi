#!/usr/bin/env python3
"""
DigitalSaathi — Complete Image Tools Suite Generator (Phase 4)
Generates:
1. image/index.html (Central Hub)
2. 17 Specialized Client-Side Image Tools with HTML5 Canvas, JSZip, and jsPDF.
100% Client-Side, 0% Server Cost, 100% GitHub Pages Compatible.
"""

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

def get_page_scaffold(title, desc, canonical, tool_content, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | DigitalSaathi</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://digitalsaathi.in/image/{canonical}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} | DigitalSaathi">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://digitalsaathi.in/image/{canonical}">

  <!-- Fonts & Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  {extra_head}

  <style>
    .tool-page-container {{
      max-width: 900px;
      margin: 2rem auto 4rem;
      padding: 0 1rem;
    }}
    .tool-header-box {{
      text-align: center;
      margin-bottom: 2rem;
    }}
    .tool-header-title {{
      font-size: clamp(1.8rem, 3.5vw, 2.3rem);
      font-weight: 800;
      color: var(--text-main, #0f172a);
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }}
    .tool-header-desc {{
      color: var(--text-muted, #64748b);
      font-size: 1.05rem;
      max-width: 650px;
      margin: 0 auto;
    }}
    .tool-main-card {{
      background: var(--bg-surface, #ffffff);
      border: 1px solid var(--border-subtle, #e2e8f0);
      border-radius: var(--radius-xl, 16px);
      padding: 2rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    }}
    .tool-upload-box {{
      border: 2px dashed var(--primary-300, #93c5fd);
      background: var(--primary-50, #eff6ff);
      border-radius: 12px;
      padding: 2.5rem 1.5rem;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .tool-upload-box:hover, .tool-upload-box.drag-over {{
      background: #dbeafe;
      border-color: var(--primary, #2563eb);
    }}
    .tool-controls-panel {{
      margin-top: 1.5rem;
      background: var(--bg-surface-subtle, #f8fafc);
      border: 1px solid var(--border-subtle, #e2e8f0);
      border-radius: 12px;
      padding: 1.5rem;
    }}
    .tool-preview-panel {{
      margin-top: 1.5rem;
      text-align: center;
    }}
    .tool-stat-badge {{
      display: inline-block;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.85rem;
      margin: 0.25rem;
    }}
    .badge-stat-orig {{ background: #f1f5f9; color: #475569; }}
    .badge-stat-new {{ background: #ecfdf5; color: #059669; }}
    .badge-stat-saved {{ background: #eff6ff; color: #2563eb; }}
  </style>
</head>
<body>

{NAV_HEADER}

  <main class="tool-page-container">
    {tool_content}
  </main>

{FOOTER_HTML}

  <script src="../assets/js/common.js"></script>
</body>
</html>"""

def build_hub_page():
    print("Generating image/index.html...")

    tools_data = [
        # Compress & Resize
        {"url": "compress.html", "title": "Image Compressor", "cat": "compress-resize", "cat_name": "Compress & Resize", "badge": "🔥 Most Popular", "badge_class": "badge-primary", "desc": "Compress JPG, PNG & WebP images to exact target sizes (under 20KB, 50KB, 100KB) or custom quality slider with side-by-side preview.", "icon_bg": "#f5f3ff", "icon_color": "#8b5cf6", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 12v9"/><path d="m8 17 4 4 4-4"/></svg>'},
        {"url": "resize.html", "title": "Image Resizer", "cat": "compress-resize", "cat_name": "Compress & Resize", "badge": "SSC/UPSC Ready", "badge_class": "badge-success", "desc": "Resize photos by exact pixels (e.g. 140x160px), percentage scale, or presets for Indian Govt exams, social media and passports.", "icon_bg": "#eff6ff", "icon_color": "#2563eb", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>'},
        {"url": "bulk-resize.html", "title": "Bulk Image Resizer", "cat": "compress-resize", "cat_name": "Compress & Resize", "badge": "⚡ Batch Mode", "badge_class": "badge-info", "desc": "Upload and process up to 50 photos simultaneously. Compress, resize, and download all as a single ZIP archive.", "icon_bg": "#ecfdf5", "icon_color": "#059669", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>'},
        {"url": "dpi-converter.html", "title": "DPI / PPI Converter", "cat": "compress-resize", "cat_name": "Compress & Resize", "badge": "300 DPI Print", "badge_class": "badge-warning", "desc": "Set photo resolution to 200 DPI or 300 DPI required for official Indian government and university exam uploads.", "icon_bg": "#fffbeb", "icon_color": "#d97706", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m12 6 4 6h-8z"/><circle cx="12" cy="16" r="1"/></svg>'},

        # Crop & Edit
        {"url": "crop.html", "title": "Image Cropper", "cat": "crop-edit", "cat_name": "Crop & Edit", "badge": "Interactive", "badge_class": "badge-primary", "desc": "Crop photos with drag handles, freeform or presets (1:1 Square, 3.5x4.5cm Passport, 16:9 Landscape, Circular Avatar).", "icon_bg": "#fff1f2", "icon_color": "#f43f5e", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>'},
        {"url": "rotate.html", "title": "Rotate & Flip Image", "cat": "crop-edit", "cat_name": "Crop & Edit", "badge": "Instant", "badge_class": "badge-neutral", "desc": "Rotate photos 90°, 180°, 270°, mirror flip horizontally, or flip vertically with custom degree angle alignment.", "icon_bg": "#eef2ff", "icon_color": "#6366f1", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6"/><path d="M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>'},
        {"url": "photo-enhancer.html", "title": "Photo Enhancer & Filters", "cat": "crop-edit", "cat_name": "Crop & Edit", "badge": "Auto Contrast", "badge_class": "badge-success", "desc": "Adjust brightness, contrast, sharpness, and saturation. One-click Document Scan Filter clarifies dim xerox text.", "icon_bg": "#f0fdf4", "icon_color": "#16a34a", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>'},
        {"url": "watermark.html", "title": "Image Watermark", "cat": "crop-edit", "cat_name": "Crop & Edit", "badge": "Text & Logo", "badge_class": "badge-info", "desc": "Add custom copyright text or logo stamps with customizable opacity, rotation, 9-point grid alignment, or full repeating tile.", "icon_bg": "#e0f2fe", "icon_color": "#0284c7", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>'},

        # Convert Format
        {"url": "convert.html", "title": "Universal Image Converter", "cat": "convert", "cat_name": "Convert Format", "badge": "JPG, PNG, WebP", "badge_class": "badge-primary", "desc": "Batch convert photos between JPG, PNG, WebP, BMP, and GIF format with instant client-side processing.", "icon_bg": "#eff6ff", "icon_color": "#2563eb", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/></svg>'},
        {"url": "jpg-to-pdf.html", "title": "JPG to PDF Converter", "cat": "convert", "cat_name": "Convert Format", "badge": "Multi-Page", "badge_class": "badge-success", "desc": "Combine multiple JPG and PNG images into a clean single PDF document. Customize A4 size, orientation, and margins.", "icon_bg": "#fef2f2", "icon_color": "#dc2626", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><path d="M10 13v-2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1Z"/><path d="M10 17v-1a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v1"/></svg>'},
        {"url": "png-to-jpg.html", "title": "PNG to JPG Converter", "cat": "convert", "cat_name": "Convert Format", "badge": "Custom BG Color", "badge_class": "badge-neutral", "desc": "Convert PNGs to JPG with custom background color filler (white, black, transparent fill) and adjustable compression.", "icon_bg": "#fff7ed", "icon_color": "#ea580c", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>'},
        {"url": "jpg-to-png.html", "title": "JPG to PNG Converter", "cat": "convert", "cat_name": "Convert Format", "badge": "Lossless", "badge_class": "badge-neutral", "desc": "Convert standard JPEG photographs to crisp, uncompressed lossless PNG format with zero degradation.", "icon_bg": "#f5f3ff", "icon_color": "#8b5cf6", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7"/><line x1="16" x2="22" y1="5" y2="5"/><line x1="19" x2="19" y1="2" y2="8"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>'},
        {"url": "webp-converter.html", "title": "WebP Converter", "cat": "convert", "cat_name": "Convert Format", "badge": "70% Smaller", "badge_class": "badge-info", "desc": "Two-way modern format converter: Convert JPG/PNG to WebP for faster websites or WebP back to JPG/PNG for universal compatibility.", "icon_bg": "#ecfeff", "icon_color": "#0891b2", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'},

        # Passport & Forms (Cyber Café)
        {"url": "remove-bg.html", "title": "Passport BG Color Changer", "cat": "passport-forms", "cat_name": "Passport & Forms", "badge": "🔥 Cyber Café", "badge_class": "badge-warning", "desc": "Change passport photo background to Plain White, Light Blue, or Red for Indian government job portals and passport seva.", "icon_bg": "#fffbeb", "icon_color": "#f59e0b", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m19 11-8-8-8.6 8.6a2 2 0 0 0 0 2.8l5.2 5.2c.8.8 2 .8 2.8 0L19 11Z"/><path d="m5 2 5 5"/><path d="M2 13h15"/><path d="M22 20a2 2 0 1 1-4 0c0-1.6 1.7-2.4 2-4 .3 1.6 2 2.4 2 4Z"/></svg>'},
        {"url": "../cybercafe/passport-photo.html", "title": "Passport Photo Sheet Maker", "cat": "passport-forms", "cat_name": "Passport & Forms", "badge": "A4 Print Sheet", "badge_class": "badge-primary", "desc": "Create standard Indian Passport (3.5x4.5cm), Visa US (2x2\"), or 8/12/16 multi-photo grid sheets ready for instant A4 printing.", "icon_bg": "#eff6ff", "icon_color": "#1d4ed8", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'},
        {"url": "../cybercafe/signature.html", "title": "Signature Resizer (<20KB)", "cat": "passport-forms", "cat_name": "Passport & Forms", "badge": "IBPS / SSC Ready", "badge_class": "badge-success", "desc": "Resize candidate signatures to exact 140x60px dimensions and auto-compress strictly under 20KB for Indian online job forms.", "icon_bg": "#ecfdf5", "icon_color": "#047857", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 2 4 4-10 10H8v-4L18 2z"/><path d="m15 5 3 3"/><path d="M2 22h20"/></svg>'},
        {"url": "blur-face.html", "title": "Blur & Redact Image", "cat": "passport-forms", "cat_name": "Passport & Forms", "badge": "Privacy Censor", "badge_class": "badge-danger", "desc": "Censor sensitive information, redact Aadhaar / PAN card numbers, and blur faces on identity cards before sharing online.", "icon_bg": "#fef2f2", "icon_color": "#dc2626", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/><path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/><line x1="2" x2="22" y1="2" y2="22"/></svg>'},

        # Utilities & Web
        {"url": "color-picker.html", "title": "Image Color Picker & Palette", "cat": "utilities", "cat_name": "Utilities", "badge": "Eyedropper", "badge_class": "badge-info", "desc": "Pick exact pixel colors from any photo with magnifying loupe and auto-extract top dominant 8-color design palette.", "icon_bg": "#f5f3ff", "icon_color": "#7c3aed", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/></svg>'},
        {"url": "base64.html", "title": "Image to Base64 Encoder", "cat": "utilities", "cat_name": "Utilities", "badge": "Dev Tool", "badge_class": "badge-neutral", "desc": "Convert images to Base64 Data URI strings for HTML/CSS embedding or decode Base64 strings back to downloadable image files.", "icon_bg": "#f1f5f9", "icon_color": "#475569", "icon_svg": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'}
    ]

    cards_html = ""
    for t in tools_data:
        cards_html += f"""      <a href="{t['url']}" class="tool-card saas-card" data-category="{t['cat']}" data-keywords="{t['title'].lower()} {t['desc'].lower()} {t['cat_name'].lower()}">
        <div class="card-header">
          <div class="tool-icon-box" style="background:{t['icon_bg']}; color:{t['icon_color']};">
            {t['icon_svg']}
          </div>
          <span class="badge {t['badge_class']}">{t['badge']}</span>
        </div>
        <h3 class="tool-title">{t['title']}</h3>
        <p class="tool-desc">{t['desc']}</p>
        <div class="tool-card-footer">
          <span class="tool-action-link">Open Tool &rarr;</span>
        </div>
      </a>\n"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free Online Image Tools — Compress, Resize, Crop & Passport Photos | DigitalSaathi</title>
  <meta name="description" content="100% Free Client-Side Image Tools Suite. Compress images under 20KB/50KB/100KB, resize for SSC/UPSC forms, crop photos, make passport photo sheets, remove backgrounds, and convert formats with zero server uploads.">
  <meta name="keywords" content="image compressor, resize image for ssc, passport photo maker, crop photo online, convert jpg to pdf, background remover, reduce photo size kb, digitalsaathi image tools">
  <link rel="canonical" href="https://digitalsaathi.in/image/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="DigitalSaathi Image Tools — 100% Free & Private Photo Processing">
  <meta property="og:description" content="Every image tool you need for Indian government forms, college applications, cyber cafés, and web tasks. 100% free and client-side.">
  <meta property="og:url" content="https://digitalsaathi.in/image/">

  <!-- Fonts & Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">

  <!-- JSON-LD Schema for Top SEO Ranking -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "name": "DigitalSaathi Image Tools Suite",
        "url": "https://digitalsaathi.in/image/",
        "description": "Free client-side image compressor, resizer, cropper, converter, and passport photo sheet maker.",
        "applicationCategory": "MultimediaApplication",
        "operatingSystem": "All (Web Browser)",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "INR"
        }},
        "featureList": [
          "Compress Image under 20KB/50KB/100KB",
          "SSC & UPSC Photo Resizer",
          "Passport Photo 3.5x4.5cm Grid Sheet",
          "Signature Resizer",
          "JPG to PDF Converter",
          "Passport Background Color Replacer",
          "DPI Converter (300 DPI)"
        ]
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://digitalsaathi.in/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Image Tools",
            "item": "https://digitalsaathi.in/image/"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "How to compress an image to under 50KB or 20KB for government job forms?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Open the DigitalSaathi Image Compressor, choose the preset 'Under 50KB' or 'Under 20KB', upload your photo, and our client-side engine automatically adjusts dimensions and quality to match the exact requirement."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Are my uploaded photos and signatures saved on your servers?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "No. All photo and signature processing happens 100% locally in your web browser using HTML5 Canvas and Web Workers. Your personal documents are never transmitted to any external server."
            }}
          }},
          {{
            "@type": "Question",
            "name": "What is the standard photo and signature size for SSC CGL / UPSC / IBPS?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "For SSC and UPSC, passport photos typically require 3.5cm x 4.5cm (approx 140x160 pixels) between 20KB to 50KB. Candidate signatures require 140x60 pixels between 10KB to 20KB."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    .saas-grid-container {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
      margin-bottom: 3.5rem;
    }}
    .saas-card {{
      background: var(--bg-surface, #ffffff);
      border: 1px solid var(--border-subtle, #e2e8f0);
      border-radius: var(--radius-lg, 14px);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }}
    .saas-card:hover {{
      transform: translateY(-3px);
      border-color: var(--primary-300, #93c5fd);
      box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.1), 0 8px 10px -6px rgba(37, 99, 235, 0.05);
    }}
    .tool-icon-box {{
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1rem;
    }}
    .tool-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main, #0f172a);
      margin-bottom: 0.5rem;
    }}
    .tool-desc {{
      font-size: 0.88rem;
      color: var(--text-muted, #64748b);
      line-height: 1.45;
      flex-grow: 1;
      margin-bottom: 1.25rem;
    }}
    .tool-card-footer {{
      display: flex;
      align-items: center;
      border-top: 1px solid var(--border-subtle, #f1f5f9);
      padding-top: 0.85rem;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--primary, #2563eb);
    }}
    .filter-pills-bar {{
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
      padding-bottom: 0.5rem;
      margin: 1.5rem 0;
      scrollbar-width: none;
    }}
    .filter-pills-bar::-webkit-scrollbar {{
      display: none;
    }}
    .filter-pill {{
      background: var(--bg-surface, #ffffff);
      border: 1px solid var(--border-subtle, #e2e8f0);
      padding: 0.5rem 1.1rem;
      border-radius: 9999px;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-body, #334155);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .filter-pill:hover {{
      background: var(--bg-surface-subtle, #f8fafc);
      border-color: var(--border-default, #cbd5e1);
    }}
    .filter-pill.active {{
      background: var(--primary, #2563eb);
      border-color: var(--primary, #2563eb);
      color: #ffffff;
    }}
    .exam-specs-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.9rem;
    }}
    .exam-specs-table th, .exam-specs-table td {{
      padding: 0.75rem 1rem;
      border: 1px solid var(--border-subtle, #e2e8f0);
      text-align: left;
    }}
    .exam-specs-table th {{
      background: var(--bg-surface-subtle, #f8fafc);
      font-weight: 700;
      color: var(--text-main, #0f172a);
    }}
  </style>
</head>
<body>

{NAV_HEADER}

  <main>
    <!-- Hero Section -->
    <section class="section" style="padding: 2.5rem 0 1rem; text-align: center;">
      <div class="container" style="max-width: 820px;">
        <div style="display:inline-flex; align-items:center; gap:0.5rem; background:#eff6ff; color:#2563eb; padding:0.35rem 0.85rem; border-radius:9999px; font-size:0.82rem; font-weight:700; margin-bottom:1rem;">
          ⚡ 100% Free & Browser-Powered &bull; No File Upload to Cloud
        </div>
        <h1 style="font-size: clamp(2rem, 4vw, 2.75rem); font-weight: 800; color: var(--text-main, #0f172a); letter-spacing: -0.025em; line-height: 1.2; margin-bottom: 0.75rem;">
          Image Tools for Every Photo, Scan & Document
        </h1>
        <p style="font-size: 1.1rem; color: var(--text-muted, #64748b); line-height: 1.5; margin-bottom: 1.5rem;">
          Compress, resize, crop, convert, remove background, and format photos for SSC, UPSC, passports, and cyber café printouts with instant speed.
        </p>

        <!-- Search Bar -->
        <div style="position: relative; max-width: 520px; margin: 0 auto;">
          <input type="text" id="image-tool-search" placeholder="Search image tools (e.g. compress under 20kb, resize, passport)..." 
                 style="width: 100%; padding: 0.85rem 1rem 0.85rem 2.8rem; border-radius: 9999px; border: 1.5px solid var(--border-default, #cbd5e1); font-size: 0.95rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); outline: none;">
          <svg style="position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); width: 18px; height: 18px; color: var(--text-muted, #64748b);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </div>
      </div>
    </section>

    <!-- Category Filter Bar -->
    <div class="container">
      <div class="filter-pills-bar" id="category-filter-bar">
        <button class="filter-pill active" data-filter="all">All Image Tools (18)</button>
        <button class="filter-pill" data-filter="compress-resize">Compress & Resize</button>
        <button class="filter-pill" data-filter="crop-edit">Crop & Edit</button>
        <button class="filter-pill" data-filter="convert">Convert Format</button>
        <button class="filter-pill" data-filter="passport-forms">Passport & Govt Forms</button>
        <button class="filter-pill" data-filter="utilities">Utilities & Web</button>
      </div>

      <!-- Tools Grid -->
      <div class="saas-grid-container" id="tools-grid">
{cards_html}
      </div>
    </div>

    <!-- Indian Exam Photo Specs Reference Table -->
    <section class="section" style="background: var(--bg-surface-subtle, #f8fafc); padding: 3rem 0; border-top: 1px solid var(--border-subtle, #e2e8f0); border-bottom: 1px solid var(--border-subtle, #e2e8f0);">
      <div class="container" style="max-width: 900px;">
        <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--text-main, #0f172a); margin-bottom: 0.5rem; text-align: center;">
          📋 Official Indian Government Exam Photo & Signature Guide (2026)
        </h2>
        <p style="text-align: center; color: var(--text-muted, #64748b); font-size: 0.95rem; margin-bottom: 1.5rem;">
          Quick reference dimensions and file size limits for major entrance examinations and recruitment portals.
        </p>
        <div style="overflow-x: auto; background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); border: 1px solid var(--border-subtle, #e2e8f0);">
          <table class="exam-specs-table">
            <thead>
              <tr>
                <th>Exam / Portal</th>
                <th>Photo Dimensions</th>
                <th>Photo File Size</th>
                <th>Signature Size</th>
                <th>Format</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>SSC CGL / CHSL / MTS</strong></td>
                <td>3.5 cm &times; 4.5 cm (140&times;160 px)</td>
                <td>20 KB to 50 KB</td>
                <td>10 KB to 20 KB (140&times;60 px)</td>
                <td>JPEG / JPG</td>
              </tr>
              <tr>
                <td><strong>UPSC Civil Services (CSE)</strong></td>
                <td>350 &times; 350 px (Min 110&times;140)</td>
                <td>20 KB to 300 KB</td>
                <td>20 KB to 300 KB (350&times;350 px)</td>
                <td>JPG only</td>
              </tr>
              <tr>
                <td><strong>IBPS PO / Clerk / RRB</strong></td>
                <td>4.5 cm &times; 3.5 cm (200&times;230 px)</td>
                <td>20 KB to 50 KB</td>
                <td>10 KB to 20 KB (140&times;60 px)</td>
                <td>JPG / JPEG</td>
              </tr>
              <tr>
                <td><strong>NTA JEE Main / NEET UG</strong></td>
                <td>Postcard (4&times;6\") &amp; Passport</td>
                <td>10 KB to 200 KB</td>
                <td>4 KB to 30 KB</td>
                <td>JPG / JPEG (White BG)</td>
              </tr>
              <tr>
                <td><strong>Indian Passport Seva (PSP)</strong></td>
                <td>3.5 cm &times; 4.5 cm (300 DPI)</td>
                <td>10 KB to 200 KB</td>
                <td>10 KB to 50 KB</td>
                <td>JPG (White / Light BG)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Trust & Privacy Section -->
    <section class="section" style="padding: 3.5rem 0;">
      <div class="container">
        <div style="text-align: center; max-width: 700px; margin: 0 auto 2.5rem;">
          <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--text-main, #0f172a); margin-bottom: 0.5rem;">
            Why Students & Cyber Cafés Trust DigitalSaathi
          </h2>
          <p style="color: var(--text-muted, #64748b); font-size: 0.95rem;">
            Built from the ground up for high speed, absolute privacy, and strict government portal compliance.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem;">
          <div style="background: white; border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 12px; padding: 1.5rem; text-align: center;">
            <div style="width: 50px; height: 50px; background: #eff6ff; color: #2563eb; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem;">🔒</div>
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">100% Client-Side Privacy</h3>
            <p style="font-size: 0.88rem; color: var(--text-muted, #64748b); line-height: 1.5;">Your private certificates, photos, and signatures are processed entirely in your web browser. No cloud uploads, no server tracking.</p>
          </div>
          <div style="background: white; border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 12px; padding: 1.5rem; text-align: center;">
            <div style="width: 50px; height: 50px; background: #ecfdf5; color: #059669; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem;">⚡</div>
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">Zero Waiting & Instant Speed</h3>
            <p style="font-size: 0.88rem; color: var(--text-muted, #64748b); line-height: 1.5;">No uploading or downloading delays. Files are processed in milliseconds using high-performance HTML5 Canvas and WebAssembly.</p>
          </div>
          <div style="background: white; border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 12px; padding: 1.5rem; text-align: center;">
            <div style="width: 50px; height: 50px; background: #fffbeb; color: #d97706; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem;">🇮🇳</div>
            <h3 style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem;">Tailored for Indian Cyber Cafés</h3>
            <p style="font-size: 0.88rem; color: var(--text-muted, #64748b); line-height: 1.5;">Pre-calibrated with exact pixel and kilobyte specifications for SSC, UPSC, NTA, IBPS, and State PSC recruitment portals.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section class="section" style="background: var(--bg-surface-subtle, #f8fafc); padding: 3.5rem 0; border-top: 1px solid var(--border-subtle, #e2e8f0);">
      <div class="container" style="max-width: 800px;">
        <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--text-main, #0f172a); margin-bottom: 1.5rem; text-align: center;">
          Frequently Asked Questions
        </h2>
        <div class="accordion" id="faq-accordion">
          <div class="accordion-item" style="background: white; border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 10px; margin-bottom: 0.75rem; overflow: hidden;">
            <button class="accordion-header" style="width: 100%; text-align: left; padding: 1.1rem 1.25rem; font-weight: 700; font-size: 1rem; display: flex; justify-content: space-between; align-items: center; background: none; border: none; cursor: pointer; color: var(--text-main, #0f172a);">
              <span>How do I compress a photo to exactly under 20KB for SSC or IBPS signature?</span>
              <span class="accordion-icon">+</span>
            </button>
            <div class="accordion-body" style="padding: 0 1.25rem 1.1rem; font-size: 0.92rem; color: var(--text-muted, #64748b); line-height: 1.5; display: none;">
              Go to the <a href="compress.html" style="color: #2563eb; font-weight: 600;">Image Compressor</a> or <a href="../cybercafe/signature.html" style="color: #2563eb; font-weight: 600;">Signature Resizer</a>, choose the preset "Under 20KB", upload your photo or signature scan, and click "Process". The tool automatically calculates the exact dimensions and quality needed.
            </div>
          </div>
          <div class="accordion-item" style="background: white; border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 10px; margin-bottom: 0.75rem; overflow: hidden;">
            <button class="accordion-header" style="width: 100%; text-align: left; padding: 1.1rem 1.25rem; font-weight: 700; font-size: 1rem; display: flex; justify-content: space-between; align-items: center; background: none; border: none; cursor: pointer; color: var(--text-main, #0f172a);">
              <span>Can I create passport photos on an A4 sheet for home or studio printing?</span>
              <span class="accordion-icon">+</span>
            </button>
            <div class="accordion-body" style="padding: 0 1.25rem 1.1rem; font-size: 0.92rem; color: var(--text-muted, #64748b); line-height: 1.5; display: none;">
              Yes! Using our <a href="../cybercafe/passport-photo.html" style="color: #2563eb; font-weight: 600;">Passport Photo Maker</a>, you can crop your photo to standard 3.5cm &times; 4.5cm and generate an 8-photo (2&times;4) or 12-photo (3&times;4) grid on standard 4x6" photo paper or A4 sheets ready to print.
            </div>
          </div>
          <div class="accordion-item" style="background: white; border: 1px solid var(--border-subtle, #e2e8f0); border-radius: 10px; margin-bottom: 0.75rem; overflow: hidden;">
            <button class="accordion-header" style="width: 100%; text-align: left; padding: 1.1rem 1.25rem; font-weight: 700; font-size: 1rem; display: flex; justify-content: space-between; align-items: center; background: none; border: none; cursor: pointer; color: var(--text-main, #0f172a);">
              <span>Is DigitalSaathi completely free without watermark or daily limits?</span>
              <span class="accordion-icon">+</span>
            </button>
            <div class="accordion-body" style="padding: 0 1.25rem 1.1rem; font-size: 0.92rem; color: var(--text-muted, #64748b); line-height: 1.5; display: none;">
              Yes, 100% free with unlimited usage, zero watermarks added to your images, and no registration or signup required.
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{FOOTER_HTML}

  <script src="../assets/js/common.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const searchInput = document.getElementById('image-tool-search');
      const filterPills = document.querySelectorAll('.filter-pill');
      const cards = document.querySelectorAll('#tools-grid .tool-card');

      function filterTools() {{
        const query = (searchInput.value || '').toLowerCase().trim();
        const activeFilter = document.querySelector('.filter-pill.active')?.dataset.filter || 'all';

        cards.forEach(card => {{
          const category = card.dataset.category;
          const keywords = card.dataset.keywords || '';
          const matchesCategory = (activeFilter === 'all' || category === activeFilter);
          const matchesSearch = (!query || keywords.includes(query));

          if (matchesCategory && matchesSearch) {{
            card.style.display = 'flex';
          }} else {{
            card.style.display = 'none';
          }}
        }});
      }}

      if (searchInput) {{
        searchInput.addEventListener('input', filterTools);
      }}

      filterPills.forEach(pill => {{
        pill.addEventListener('click', () => {{
          filterPills.forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          filterTools();
        }});
      }});

      document.querySelectorAll('.accordion-header').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const body = btn.nextElementSibling;
          const icon = btn.querySelector('.accordion-icon');
          const isClosed = body.style.display === 'none' || !body.style.display;
          body.style.display = isClosed ? 'block' : 'none';
          if (icon) icon.textContent = isClosed ? '−' : '+';
        }});
      }});
    }});
  </script>
</body>
</html>"""

    hub_path = os.path.join(IMAGE_DIR, "index.html")
    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ Created image/index.html")

def build_all_image_tools():
    print("Building all image tool pages...")

    pages = [
        ("compress.html", generate_compress),
        ("resize.html", generate_resize),
        ("crop.html", generate_crop),
        ("convert.html", generate_convert),
        ("jpg-to-pdf.html", generate_jpg_to_pdf),
        ("remove-bg.html", generate_remove_bg),
        ("blur-face.html", generate_blur_face),
        ("watermark.html", generate_watermark),
        ("photo-enhancer.html", generate_photo_enhancer),
        ("bulk-resize.html", generate_bulk_resize),
        ("rotate.html", generate_rotate),
        ("color-picker.html", generate_color_picker),
        ("base64.html", generate_base64),
        ("dpi-converter.html", generate_dpi_converter),
        ("png-to-jpg.html", generate_png_to_jpg),
        ("jpg-to-png.html", generate_jpg_to_png),
        ("webp-converter.html", generate_webp)
    ]

    for filename, generator in pages:
        filepath = os.path.join(IMAGE_DIR, filename)
        content = generator()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created image/{filename}")

if __name__ == "__main__":
    build_hub_page()
    build_all_image_tools()
    print("🎉 Phase 4 Image Tools Suite Successfully Generated!")
