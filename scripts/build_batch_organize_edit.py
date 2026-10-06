import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NAVBAR = '''  <nav class="navbar" id="main-nav">
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
          <a href="../pdf/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> PDF Compressor</a>
          <a href="../pdf/merge.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Merge PDFs</a>
          <a href="../pdf/split.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Split PDF</a>
          <a href="../pdf/organize.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Organize PDF</a>
          <a href="../pdf/crop.html" class="dropdown-link"><span class="dropdown-icon">📐</span> Crop PDF</a>
          <a href="../pdf/page-numbers.html" class="dropdown-link"><span class="dropdown-icon">🔢</span> Page Numbers</a>
          <a href="../pdf/edit.html" class="dropdown-link"><span class="dropdown-icon">✏️</span> Edit PDF</a>
          <a href="../pdf/sign.html" class="dropdown-link"><span class="dropdown-icon">✍️</span> Sign PDF</a>
          <a href="../pdf/watermark.html" class="dropdown-link"><span class="dropdown-icon">💧</span> Watermark PDF</a>
          <a href="../pdf/pdf-to-jpg.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> PDF to JPG</a>
          <a href="../pdf/jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
          <a href="../pdf/index.html" class="dropdown-link" style="color:var(--primary);font-weight:600;"><span class="dropdown-icon">✨</span> View All 33 Tools →</a>
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

FOOTER = '''  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <div class="logo footer-logo">
          <span class="logo-badge">🌐</span>
          <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
        </div>
        <p class="footer-desc">Your all-in-one free digital companion for Indian students, job seekers, and cyber cafés. 100% private, client-side, and secure.</p>
        <p class="privacy-badge">🔒 Zero Server Uploads • 100% In-Browser Processing</p>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Top PDF Tools</h4>
        <ul class="footer-links">
          <li><a href="compress.html">PDF Compressor</a></li>
          <li><a href="merge.html">Merge PDF Files</a></li>
          <li><a href="split.html">Split PDF Pages</a></li>
          <li><a href="organize.html">Organize PDF</a></li>
          <li><a href="crop.html">Crop PDF</a></li>
          <li><a href="index.html">All 33 PDF Tools →</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Cyber Café Tools</h4>
        <ul class="footer-links">
          <li><a href="../cybercafe/passport-photo.html">Passport Photo Maker</a></li>
          <li><a href="../cybercafe/signature.html">Signature Resizer (&lt;20KB)</a></li>
          <li><a href="../image/resize.html">Image Resizer</a></li>
          <li><a href="../image/compress.html">Image Compressor</a></li>
          <li><a href="../image/jpg-to-pdf.html">JPG to PDF Converter</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 class="footer-heading">Student & Jobs</h4>
        <ul class="footer-links">
          <li><a href="../student/resume.html">Resume Builder</a></li>
          <li><a href="../calculators/cgpa.html">CGPA Calculator</a></li>
          <li><a href="../calculators/attendance.html">Attendance Tracker (75%)</a></li>
          <li><a href="../jobs/government.html">Government Jobs 2026</a></li>
          <li><a href="../about.html">About & Privacy</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; 2026 DigitalSaathi. Built for India with privacy by design. All file processing occurs strictly in your browser.</p>
    </div>
  </footer>'''

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Generated {path} ({len(content)} bytes)")

print("Ready to generate tools...")
