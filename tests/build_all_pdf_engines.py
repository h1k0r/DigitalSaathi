import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 65)
print("BUILDING COMPLETE WORKING ENGINES FOR ALL DIGITALSAATHI PDF TOOLS")
print("=" * 65)

def get_nav_html():
    return '''<nav class="navbar" id="main-nav">
  <div class="container nav-container">
    <a href="../index.html" class="logo">
      <span class="logo-badge">🌐</span>
      <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
    </a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
    <ul class="nav-links">
      <li class="nav-item">
        <a href="index.html" class="nav-link active">📑 PDF Tools</a>
        <div class="nav-dropdown">
          <a href="compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> PDF Compressor</a>
          <a href="merge.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Merge PDFs</a>
          <a href="split.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Split PDF</a>
          <a href="pdf-to-jpg.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> PDF to JPG</a>
          <a href="jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
          <a href="rotate.html" class="dropdown-link"><span class="dropdown-icon">🔄</span> Rotate PDF</a>
          <a href="page-numbers.html" class="dropdown-link"><span class="dropdown-icon">🔢</span> Page Numbers</a>
          <a href="watermark.html" class="dropdown-link"><span class="dropdown-icon">🌊</span> Watermark PDF</a>
          <a href="protect.html" class="dropdown-link"><span class="dropdown-icon">🔒</span> Protect PDF</a>
          <a href="unlock.html" class="dropdown-link"><span class="dropdown-icon">🔓</span> Unlock PDF</a>
          <a href="sign.html" class="dropdown-link"><span class="dropdown-icon">✍️</span> Sign PDF</a>
          <a href="pdf-to-word.html" class="dropdown-link"><span class="dropdown-icon">📝</span> PDF to Word</a>
          <a href="pdf-to-markdown.html" class="dropdown-link"><span class="dropdown-icon">📄</span> PDF to Markdown</a>
          <a href="ai-summarizer.html" class="dropdown-link"><span class="dropdown-icon">✨</span> AI Summarizer</a>
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
</nav>'''

def get_footer_html():
    return '''<footer class="footer">
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
        <div style="display:flex;gap:8px;">
          <span class="badge badge-success">✓ 100% Free</span>
          <span class="badge badge-primary">🔒 Zero Server Uploads</span>
        </div>
      </div>
      <div class="footer-col">
        <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;">PDF Suite</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
          <li><a href="compress.html">PDF Compressor</a></li>
          <li><a href="merge.html">PDF Merge</a></li>
          <li><a href="split.html">PDF Split</a></li>
          <li><a href="rotate.html">Rotate PDF</a></li>
          <li><a href="page-numbers.html">Page Numbers</a></li>
          <li><a href="watermark.html">Watermark PDF</a></li>
          <li><a href="protect.html">Protect PDF</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;">Students & CSC</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
          <li><a href="../student/resume.html">Live Resume Builder</a></li>
          <li><a href="../student/resume-templates.html">500+ Resume Templates</a></li>
          <li><a href="../cybercafe/passport-photo.html">Passport Photo Maker</a></li>
          <li><a href="../cybercafe/signature.html">Signature Resizer</a></li>
          <li><a href="../calculators/cgpa.html">CGPA Calculator</a></li>
          <li><a href="../calculators/attendance.html">Attendance Bunk Tracker</a></li>
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
</footer>'''

print("Building core PDF working engines...")
