import os
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_navbar_html(prefix, current_dir, current_file):
    act_tools = ' active' if current_dir == 'tools' else ''
    act_pdf   = ' active' if current_dir == 'pdf' else ''
    act_img   = ' active' if current_dir == 'image' else ''
    act_dev   = ' active' if current_dir == 'developer' else ''
    act_calc  = ' active' if current_dir == 'calculators' else ''
    act_text  = ' active' if current_dir == 'text' else ''
    act_util  = ' active' if current_dir == 'utilities' else ''

    nav_html = f'''  <nav class="navbar" id="main-nav">
    <div class="container nav-container">
      <a href="{prefix}index.html" class="logo">
        <span class="logo-badge">🌐</span>
        <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
      </a>

      <ul class="nav-links" id="navLinks">
        <li class="nav-item">
          <a href="{prefix}tools/index.html" class="nav-link{act_tools}">🧰 Tools</a>
          <div class="nav-dropdown">
            <a href="{prefix}pdf/index.html" class="dropdown-link"><span class="dropdown-icon">📑</span> PDF Tools</a>
            <a href="{prefix}image/index.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> Image Tools</a>
            <a href="{prefix}developer/json.html" class="dropdown-link"><span class="dropdown-icon">💻</span> Developer Tools</a>
            <a href="{prefix}calculators/percentage.html" class="dropdown-link"><span class="dropdown-icon">🧮</span> Calculators</a>
            <a href="{prefix}text/word-counter.html" class="dropdown-link"><span class="dropdown-icon">📝</span> Text Tools</a>
            <a href="{prefix}utilities/qr-generator.html" class="dropdown-link"><span class="dropdown-icon">⚡</span> Utility Tools</a>
            <a href="{prefix}tools/index.html" class="dropdown-link dropdown-view-all"><span class="dropdown-icon">✨</span> Full Directory →</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="{prefix}pdf/index.html" class="nav-link{act_pdf}">📑 PDF</a>
          <div class="nav-dropdown">
            <a href="{prefix}pdf/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> Compress PDF</a>
            <a href="{prefix}pdf/merge.html" class="dropdown-link"><span class="dropdown-icon">📑</span> Merge PDF</a>
            <a href="{prefix}pdf/split.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Split PDF</a>
            <a href="{prefix}pdf/jpg-to-pdf.html" class="dropdown-link"><span class="dropdown-icon">📄</span> JPG to PDF</a>
            <a href="{prefix}pdf/pdf-to-jpg.html" class="dropdown-link"><span class="dropdown-icon">🖼️</span> PDF to JPG</a>
            <a href="{prefix}pdf/edit.html" class="dropdown-link"><span class="dropdown-icon">✏️</span> Edit PDF</a>
            <a href="{prefix}pdf/sign.html" class="dropdown-link"><span class="dropdown-icon">✍️</span> Sign PDF</a>
            <a href="{prefix}pdf/protect.html" class="dropdown-link"><span class="dropdown-icon">🔒</span> Protect PDF</a>
            <a href="{prefix}pdf/index.html" class="dropdown-link dropdown-view-all"><span class="dropdown-icon">✨</span> All PDF Tools →</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="{prefix}image/index.html" class="nav-link{act_img}">🖼️ Images</a>
          <div class="nav-dropdown">
            <a href="{prefix}image/compress.html" class="dropdown-link"><span class="dropdown-icon">🗜️</span> Image Compressor</a>
            <a href="{prefix}image/resize.html" class="dropdown-link"><span class="dropdown-icon">📐</span> Image Resizer</a>
            <a href="{prefix}image/crop.html" class="dropdown-link"><span class="dropdown-icon">✂️</span> Crop Photo</a>
            <a href="{prefix}image/convert.html" class="dropdown-link"><span class="dropdown-icon">🔄</span> Image Converter</a>
            <a href="{prefix}image/remove-bg.html" class="dropdown-link"><span class="dropdown-icon">🎭</span> Passport BG Replacer</a>
            <a href="{prefix}image/blur-face.html" class="dropdown-link"><span class="dropdown-icon">🔒</span> Blur &amp; Redact</a>
            <a href="{prefix}image/index.html" class="dropdown-link dropdown-view-all"><span class="dropdown-icon">✨</span> All Image Tools →</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="{prefix}developer/json.html" class="nav-link{act_dev}">💻 Developer</a>
          <div class="nav-dropdown">
            <a href="{prefix}developer/json.html" class="dropdown-link"><span class="dropdown-icon">💻</span> JSON Formatter</a>
            <a href="{prefix}developer/base64.html" class="dropdown-link"><span class="dropdown-icon">🔤</span> Base64 Converter</a>
            <a href="{prefix}developer/sql.html" class="dropdown-link"><span class="dropdown-icon">💾</span> SQL Formatter</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="{prefix}calculators/percentage.html" class="nav-link{act_calc}">🧮 Calculators</a>
          <div class="nav-dropdown">
            <a href="{prefix}calculators/percentage.html" class="dropdown-link"><span class="dropdown-icon">📊</span> Percentage Calculator</a>
            <a href="{prefix}calculators/age.html" class="dropdown-link"><span class="dropdown-icon">🎂</span> Age Calculator</a>
            <a href="{prefix}calculators/emi.html" class="dropdown-link"><span class="dropdown-icon">💰</span> Loan EMI Calculator</a>
            <a href="{prefix}calculators/cgpa.html" class="dropdown-link"><span class="dropdown-icon">🎓</span> CGPA Calculator</a>
            <a href="{prefix}calculators/attendance.html" class="dropdown-link"><span class="dropdown-icon">📅</span> Attendance Calculator</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="{prefix}text/word-counter.html" class="nav-link{act_text}">📝 Text</a>
          <div class="nav-dropdown">
            <a href="{prefix}text/word-counter.html" class="dropdown-link"><span class="dropdown-icon">📝</span> Word Counter</a>
            <a href="{prefix}developer/base64.html" class="dropdown-link"><span class="dropdown-icon">🔤</span> Base64 Text</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="{prefix}utilities/qr-generator.html" class="nav-link{act_util}">⚡ Utilities</a>
          <div class="nav-dropdown">
            <a href="{prefix}utilities/qr-generator.html" class="dropdown-link"><span class="dropdown-icon">📱</span> QR Code Generator</a>
            <a href="{prefix}utilities/password-generator.html" class="dropdown-link"><span class="dropdown-icon">🔐</span> Password Generator</a>
          </div>
        </li>
      </ul>

      <div class="nav-actions">
        <button class="nav-search-btn" id="headerSearchBtn" title="Search all tools (Ctrl+K)" aria-label="Search tools">
          <span class="search-icon">🔍</span>
          <span class="search-placeholder">Search tools...</span>
          <kbd class="nav-search-key">Ctrl K</kbd>
        </button>
        <button class="mobile-search-btn" id="mobileSearchBtn" title="Search tools" aria-label="Search tools">🔍</button>
        <button class="nav-toggle" id="navToggleBtn" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      </div>
    </div>
  </nav>'''
    return nav_html

def update_all_files():
    html_files = glob.glob('**/*.html', recursive=True)
    updated_count = 0

    for file_path in html_files:
        norm_path = os.path.normpath(file_path).replace('\\', '/')
        parts = norm_path.split('/')
        
        if len(parts) == 1:
            prefix = ""
            current_dir = "."
        else:
            prefix = "../"
            current_dir = parts[0]
            
        current_file = parts[-1]

        with open(file_path, 'r', encoding='utf-8') as fp:
            content = fp.read()

        new_nav = build_navbar_html(prefix, current_dir, current_file)

        pattern = r'<nav class=[\"\']navbar[\"\'][^>]*>[\s\S]*?</nav>'
        if re.search(pattern, content):
            updated_content = re.sub(pattern, new_nav, content, count=1)
            with open(file_path, 'w', encoding='utf-8') as fp:
                fp.write(updated_content)
            updated_count += 1
        else:
            print(f"Warning: No <nav class='navbar'> found in {file_path}")

    print(f"Successfully updated navigation across {updated_count} / {len(html_files)} files.")

if __name__ == '__main__':
    update_all_files()
