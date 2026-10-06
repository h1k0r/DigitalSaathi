import os
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def build_footer_html(prefix):
    footer_html = f'''  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="{prefix}index.html" class="logo" style="color:#ffffff;">
          <span class="logo-badge">🌐</span>
          <span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span>
        </a>
        <p style="color:#94a3b8; font-size:0.875rem; margin-top:1rem; line-height:1.6;">
          Free online tools for everyday digital work. Convert, compress, edit, calculate, and manage files securely in your browser.
        </p>
      </div>
      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Tool Categories</h4>
        <ul class="footer-links">
          <li><a href="{prefix}pdf/index.html">PDF Tools</a></li>
          <li><a href="{prefix}image/index.html">Image Tools</a></li>
          <li><a href="{prefix}developer/json.html">Developer Tools</a></li>
          <li><a href="{prefix}calculators/percentage.html">Calculators</a></li>
          <li><a href="{prefix}text/word-counter.html">Text Tools</a></li>
          <li><a href="{prefix}utilities/qr-generator.html">Utility Tools</a></li>
        </ul>
      </div>
      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Popular Tools</h4>
        <ul class="footer-links">
          <li><a href="{prefix}pdf/merge.html">Merge PDF</a></li>
          <li><a href="{prefix}pdf/compress.html">Compress PDF</a></li>
          <li><a href="{prefix}image/compress.html">Image Compressor</a></li>
          <li><a href="{prefix}developer/json.html">JSON Formatter</a></li>
          <li><a href="{prefix}utilities/qr-generator.html">QR Code Generator</a></li>
          <li><a href="{prefix}calculators/age.html">Age Calculator</a></li>
        </ul>
      </div>
      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Company &amp; Privacy</h4>
        <ul class="footer-links">
          <li><a href="{prefix}about.html">About DigitalSaathi</a></li>
          <li><a href="{prefix}privacy.html">Privacy Policy</a></li>
          <li><a href="{prefix}terms.html">Terms of Service</a></li>
          <li><a href="{prefix}contact.html">Contact Us</a></li>
          <li><a href="{prefix}tools/index.html">Tools Directory</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <div>&copy; 2026 DigitalSaathi. 100% Free Client-Side Tools.</div>
      <div>Hosted on GitHub Pages</div>
    </div>
  </footer>'''
    return footer_html

def update_all_footers():
    html_files = glob.glob('**/*.html', recursive=True)
    updated_count = 0

    for file_path in html_files:
        norm_path = os.path.normpath(file_path).replace('\\', '/')
        parts = norm_path.split('/')
        
        prefix = "" if len(parts) == 1 else "../"

        with open(file_path, 'r', encoding='utf-8') as fp:
            content = fp.read()

        new_footer = build_footer_html(prefix)

        pattern = r'<footer class=[\"\']footer[\"\'][^>]*>[\s\S]*?</footer>'
        if re.search(pattern, content):
            updated_content = re.sub(pattern, new_footer, content, count=1)
            with open(file_path, 'w', encoding='utf-8') as fp:
                fp.write(updated_content)
            updated_count += 1
        else:
            print(f"Warning: No <footer class='footer'> found in {file_path}")

    print(f"Successfully updated footer across {updated_count} / {len(html_files)} files.")

if __name__ == '__main__':
    update_all_footers()
