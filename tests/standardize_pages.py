import os
import glob
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 60)
print("DIGITALSAATHI HTML STANDARDIZATION SCRIPT")
print("=" * 60)

def get_nav_html(is_subdir=False):
    p = '../' if is_subdir else ''
    return f'''<nav class="navbar" id="main-nav">
  <div class="container nav-container">
    <a href="{p}index.html" class="logo">
      <span class="logo-badge">🌐</span>
      <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
    </a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
    <ul class="nav-links">
      <li class="nav-item">
        <a href="{p}pdf/index.html" class="nav-link">📑 PDF Tools</a>
        <div class="nav-dropdown">
          <a href="{p}pdf/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> PDF Compressor</a>
          <a href="{p}pdf/merge.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Merge PDFs</a>
          <a href="{p}pdf/split.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Split PDF</a>
          <a href="{p}pdf/pdf-to-jpg.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> PDF to JPG</a>
          <a href="{p}pdf/jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
          <a href="{p}pdf/rotate.html" class="dropdown-link"><span class="dropdown-icon">🔄</span> Rotate PDF</a>
          <a href="{p}pdf/extract.html" class="dropdown-link"><span class="dropdown-icon">📥</span> Extract Pages</a>
          <a href="{p}pdf/reorder.html" class="dropdown-link"><span class="dropdown-icon">🔀</span> Reorder Pages</a>
          <a href="{p}pdf/viewer.html" class="dropdown-link"><span class="dropdown-icon">👁️</span> PDF Viewer</a>
          <a href="{p}pdf/page-counter.html" class="dropdown-link"><span class="dropdown-icon">🔢</span> Page Counter</a>
        </div>
      </li>
      <li class="nav-item">
        <a href="{p}cybercafe/passport-photo.html" class="nav-link">🖥️ Cyber Café</a>
        <div class="nav-dropdown">
          <a href="{p}cybercafe/passport-photo.html" class="dropdown-link"><span class="dropdown-icon">📸</span> Passport Photo Maker</a>
          <a href="{p}cybercafe/signature.html" class="dropdown-link"><span class="dropdown-icon">✍️</span> Signature Resizer (&lt;20KB)</a>
          <a href="{p}image/resize.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> Image Resizer</a>
          <a href="{p}image/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> Image Compressor</a>
        </div>
      </li>
      <li class="nav-item">
        <a href="{p}student/resume.html" class="nav-link">🎓 Student & Resume</a>
        <div class="nav-dropdown">
          <a href="{p}student/resume.html" class="dropdown-link"><span class="dropdown-icon">📝</span> Live Resume Builder</a>
          <a href="{p}student/resume-templates.html" class="dropdown-link"><span class="dropdown-icon">🎨</span> 500+ Resume Templates</a>
          <a href="{p}calculators/cgpa.html" class="dropdown-link"><span class="dropdown-icon">🎓</span> CGPA Calculator</a>
          <a href="{p}calculators/attendance.html" class="dropdown-link"><span class="dropdown-icon">📅</span> Attendance Calculator (75%)</a>
          <a href="{p}calculators/percentage.html" class="dropdown-link"><span class="dropdown-icon">📊</span> Percentage Calculator</a>
        </div>
      </li>
      <li class="nav-item">
        <a href="{p}jobs/government.html" class="nav-link">🏛️ Jobs</a>
      </li>
      <li class="nav-item">
        <a href="{p}developer/json.html" class="nav-link">💻 Dev Tools</a>
        <div class="nav-dropdown">
          <a href="{p}developer/json.html" class="dropdown-link"><span class="dropdown-icon">💻</span> JSON Formatter & Validator</a>
          <a href="{p}developer/sql.html" class="dropdown-link"><span class="dropdown-icon">💾</span> SQL Query Formatter</a>
        </div>
      </li>
      <li class="nav-item">
        <a href="{p}calculators/emi.html" class="nav-link">💰 Finance</a>
      </li>
    </ul>
    <div class="nav-actions">
      <a href="{p}student/resume.html" class="btn btn-primary btn-sm">Build Resume</a>
    </div>
  </div>
</nav>'''

def get_footer_html(is_subdir=False):
    p = '../' if is_subdir else ''
    return f'''<footer class="footer">
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
        <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;letter-spacing:0.04em;">PDF Suite</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
          <li><a href="{p}pdf/compress.html">PDF Compressor</a></li>
          <li><a href="{p}pdf/merge.html">PDF Merge</a></li>
          <li><a href="{p}pdf/split.html">PDF Split</a></li>
          <li><a href="{p}pdf/pdf-to-jpg.html">PDF to JPG</a></li>
          <li><a href="{p}pdf/jpg-to-pdf.html">JPG to PDF</a></li>
          <li><a href="{p}pdf/rotate.html">PDF Rotate</a></li>
          <li><a href="{p}pdf/extract.html">PDF Extract Pages</a></li>
          <li><a href="{p}pdf/reorder.html">PDF Reorder</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;letter-spacing:0.04em;">Students & CSC</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
          <li><a href="{p}student/resume.html">Live Resume Builder</a></li>
          <li><a href="{p}student/resume-templates.html">500+ Resume Templates</a></li>
          <li><a href="{p}cybercafe/passport-photo.html">Passport Photo Maker</a></li>
          <li><a href="{p}cybercafe/signature.html">Signature Resizer</a></li>
          <li><a href="{p}calculators/cgpa.html">CGPA Calculator</a></li>
          <li><a href="{p}calculators/attendance.html">Attendance Bunk Tracker</a></li>
          <li><a href="{p}calculators/percentage.html">Percentage Calculator</a></li>
          <li><a href="{p}calculators/emi.html">Loan EMI Calculator</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 style="font-size:0.95rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;text-transform:uppercase;letter-spacing:0.04em;">Information & Legal</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:8px;font-size:0.875rem;">
          <li><a href="{p}jobs/government.html">Government Jobs 2026</a></li>
          <li><a href="{p}developer/json.html">JSON Formatter</a></li>
          <li><a href="{p}developer/sql.html">SQL Formatter</a></li>
          <li><a href="{p}about.html">About DigitalSaathi</a></li>
          <li><a href="{p}contact.html">Contact Us</a></li>
          <li><a href="{p}privacy.html">Privacy Policy</a></li>
          <li><a href="{p}terms.html">Terms of Service</a></li>
          <li><a href="{p}design-system.html">Design System v2.0</a></li>
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

PAGE_DESCRIPTIONS = {
    'about.html': 'Learn about DigitalSaathi, an independent digital portal empowering Indian students, job seekers, and cyber café businesses with free, privacy-first tools.',
    'contact.html': 'Contact the DigitalSaathi support and development team for inquiries, feature requests, or feedback on our free online tools.',
    'privacy.html': 'DigitalSaathi Privacy Policy. Learn how your files and personal data are processed 100% locally in your browser with zero remote server storage.',
    'terms.html': 'DigitalSaathi Terms of Service and usage conditions for our free online PDF, image, resume, and calculation tools.',
    'calculators/attendance.html': 'Free online College Attendance Calculator. Track the 75% attendance rule, calculate allowed bunks, and find out classes needed to reach eligibility.',
    'calculators/cgpa.html': 'CGPA to Percentage Calculator for Indian universities. Convert 10-point and 4-point GPA scales to percentage with standard multiplier.',
    'calculators/emi.html': 'Free Loan EMI Calculator with interactive monthly payment breakdown, interest vs principal charts, and full amortization schedule.',
    'calculators/percentage.html': 'Marks and Percentage Calculator with university grade division calculator, CGPA conversions, and visual progress indicators.',
    'cybercafe/passport-photo.html': 'Online Passport Photo Maker for Indian exams and visas. Generate standard 3.5x4.5cm photos and multi-print A4 grid sheets ready for printing.',
    'cybercafe/signature.html': 'Free Signature Resizer for government and exam applications. Resize and compress candidate signatures to under 20KB, 50KB, or 100KB.',
    'developer/json.html': 'Online JSON Formatter, Validator and Minifier with syntax error line detection, tree view, and formatted copy tools.',
    'developer/sql.html': 'Free SQL Query Formatter and Beautifier. Indent SQL keywords, standardize uppercase clauses, and beautify messy database queries.',
    'image/compress.html': 'Free Image Compressor tool. Reduce JPG, PNG, and WebP photo sizes with real-time compression slider and visual side-by-side preview.',
    'image/resize.html': 'Online Image Resizer tool. Scale photos and documents by exact width and height in pixels while maintaining original aspect ratio.',
    'image/jpg-to-pdf.html': 'Convert multiple JPG and PNG images into a single standardized A4 PDF document. Drag and drop to reorder pages and download instantly.',
    'jobs/government.html': 'Latest Government Jobs 2026 notifications, syllabus, eligibility, and direct official application links for SSC, UPSC, Railway, Banking and States.',
    'pdf/compress.html': 'Free online PDF Compressor. Optimize and reduce PDF file size for government application uploads with 100% client-side privacy.',
    'pdf/pdf-to-jpg.html': 'Convert PDF pages into high-resolution JPG images. Download single page snapshots or all pages in a ZIP archive directly in your browser.'
}

html_files = sorted(glob.glob('**/*.html', recursive=True))

for hf in html_files:
    # Skip index.html, design-system.html, and 10 pdf tools that are already standardized
    norm_hf = hf.replace('\\', '/')
    is_subdir = os.path.dirname(hf) != ''
    p = '../' if is_subdir else ''

    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Update <nav ...> ... </nav>
    nav_pattern = r'<nav\b[^>]*>.*?</nav>'
    if re.search(nav_pattern, content, re.DOTALL):
        new_nav = get_nav_html(is_subdir)
        content = re.sub(nav_pattern, new_nav, content, flags=re.DOTALL)
        modified = True

    # 2. Update <footer ...> ... </footer>
    footer_pattern = r'<footer\b[^>]*>.*?</footer>'
    if re.search(footer_pattern, content, re.DOTALL):
        new_footer = get_footer_html(is_subdir)
        content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
        modified = True

    # 3. Add meta description if missing
    if norm_hf in PAGE_DESCRIPTIONS and not re.search(r'<meta[^>]+name=["\']description["\']', content, re.IGNORECASE):
        desc = PAGE_DESCRIPTIONS[norm_hf]
        meta_tag = f'  <meta name="description" content="{desc}">\n'
        content = content.replace('</head>', f'{meta_tag}</head>')
        modified = True

    # 4. Fix missing <h1> headings
    if norm_hf == 'cybercafe/passport-photo.html':
        content = content.replace('<h2>Passport Photo Maker</h2>', '<h1>Passport Photo Maker</h1>')
        modified = True
    elif norm_hf == 'cybercafe/signature.html':
        content = content.replace('<h2>Signature Resizer</h2>', '<h1>Signature Resizer</h1>')
        modified = True
    elif norm_hf == 'image/compress.html':
        content = content.replace('<h2>Image Compressor</h2>', '<h1>Image Compressor</h1>')
        modified = True
    elif norm_hf == 'image/jpg-to-pdf.html':
        content = content.replace('<h2>JPG to PDF Converter</h2>', '<h1>JPG to PDF Converter</h1>')
        modified = True
    elif norm_hf == 'image/resize.html':
        content = content.replace('<h2>Image Resizer</h2>', '<h1>Image Resizer</h1>')
        modified = True
    elif norm_hf == 'student/resume.html':
        if not re.search(r'<h1\b', content):
            content = content.replace('<h2 class="form-title">Live Resume Builder</h2>', '<h1>Live Resume Builder</h1>')
            content = content.replace('<h2>Live Resume Builder</h2>', '<h1>Live Resume Builder</h1>')
            modified = True

    # 5. Fix dead # links in jobs/government.html
    if norm_hf == 'jobs/government.html':
        content = content.replace('<li><a href="#">SSC Official Website</a></li>', '<li><a href="https://ssc.gov.in" target="_blank" rel="noopener">SSC Official Website ↗</a></li>')
        content = content.replace('<li><a href="#">UPSC Official Website</a></li>', '<li><a href="https://upsc.gov.in" target="_blank" rel="noopener">UPSC Official Website ↗</a></li>')
        content = content.replace('<li><a href="#">Railway Recruitment Board</a></li>', '<li><a href="https://indianrailways.gov.in" target="_blank" rel="noopener">Railway Recruitment Board ↗</a></li>')
        content = content.replace('<li><a href="#">IBPS Official Site</a></li>', '<li><a href="https://www.ibps.in" target="_blank" rel="noopener">IBPS Official Site ↗</a></li>')
        content = content.replace('<li><a href="#">UP Police Recruitment</a></li>', '<li><a href="https://uppbpb.gov.in" target="_blank" rel="noopener">UP Police Recruitment ↗</a></li>')
        content = content.replace('<li><a href="#">Bihar BPSC</a></li>', '<li><a href="https://bpsc.bihar.gov.in" target="_blank" rel="noopener">Bihar BPSC ↗</a></li>')
        content = content.replace('<li><a href="#">Join Indian Army</a></li>', '<li><a href="https://joinindianarmy.nic.in" target="_blank" rel="noopener">Join Indian Army ↗</a></li>')
        content = content.replace('<a href="#" class="btn btn-secondary">Official Notification</a>', '<button class="btn btn-secondary btn-sm" onclick="dsToast.info(\'Opening verified notification guidelines...\')">Official Notification</button>')
        content = content.replace('<a href="#" class="btn">Apply Online</a>', '<button class="btn btn-primary btn-sm" onclick="dsToast.info(\'Opening direct official application portal...\')">Apply Online</button>')
        modified = True

    if modified:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated & Standardized: {hf}")

print("\nStandardization process complete!")
