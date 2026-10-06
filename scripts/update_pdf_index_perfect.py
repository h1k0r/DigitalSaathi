import os
import re

pdf_cards_html = '''      <!-- Row 1: Merge, Split, Compress, PDF to Word, PDF to PPT, PDF to Excel -->
      <a href="merge.html" class="saas-tool-card" data-cat="organize" data-name="merge pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fff1f2;color:#e11d48;"><span>📑</span></div>
        </div>
        <h3 class="saas-tool-title">Merge PDF</h3>
        <p class="saas-tool-desc">Combine PDFs in the order you want with the easiest PDF merger available.</p>
      </a>

      <a href="split.html" class="saas-tool-card" data-cat="organize" data-name="split pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fff7ed;color:#ea580c;"><span>✂️</span></div>
        </div>
        <h3 class="saas-tool-title">Split PDF</h3>
        <p class="saas-tool-desc">Separate one page or a whole set for easy conversion into independent PDF files.</p>
      </a>

      <a href="compress.html" class="saas-tool-card" data-cat="optimize" data-name="compress pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f0fdf4;color:#16a34a;"><span>🗜️</span></div>
        </div>
        <h3 class="saas-tool-title">Compress PDF</h3>
        <p class="saas-tool-desc">Reduce file size while optimizing for maximal PDF quality.</p>
      </a>

      <a href="pdf-to-word.html" class="saas-tool-card" data-cat="convert" data-name="pdf to word">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#2563eb;"><span>📄</span></div>
        </div>
        <h3 class="saas-tool-title">PDF to Word</h3>
        <p class="saas-tool-desc">Easily convert your PDF files into easy to edit DOC and DOCX documents. 100% accurate.</p>
      </a>

      <a href="pdf-to-ppt.html" class="saas-tool-card" data-cat="convert" data-name="pdf to powerpoint">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fff7ed;color:#c2410c;"><span>📽️</span></div>
        </div>
        <h3 class="saas-tool-title">PDF to PowerPoint</h3>
        <p class="saas-tool-desc">Turn your PDF files into easy to edit PPT and PPTX slideshows.</p>
      </a>

      <a href="pdf-to-excel.html" class="saas-tool-card" data-cat="convert" data-name="pdf to excel">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#ecfdf5;color:#059669;"><span>📊</span></div>
        </div>
        <h3 class="saas-tool-title">PDF to Excel</h3>
        <p class="saas-tool-desc">Pull data straight from PDFs into Excel spreadsheets in a few short seconds.</p>
      </a>

      <!-- Row 2: Word to PDF, PowerPoint to PDF, Excel to PDF, Edit PDF, PDF to JPG, JPG to PDF -->
      <a href="word-to-pdf.html" class="saas-tool-card" data-cat="convert" data-name="word to pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#1d4ed8;"><span>📝</span></div>
        </div>
        <h3 class="saas-tool-title">Word to PDF</h3>
        <p class="saas-tool-desc">Make DOC and DOCX files easy to read by converting them to PDF.</p>
      </a>

      <a href="ppt-to-pdf.html" class="saas-tool-card" data-cat="convert" data-name="powerpoint to pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fff7ed;color:#ea580c;"><span>📽️</span></div>
        </div>
        <h3 class="saas-tool-title">PowerPoint to PDF</h3>
        <p class="saas-tool-desc">Make PPT and PPTX slideshows easy to view by converting them to PDF.</p>
      </a>

      <a href="excel-to-pdf.html" class="saas-tool-card" data-cat="convert" data-name="excel to pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#ecfdf5;color:#047857;"><span>📈</span></div>
        </div>
        <h3 class="saas-tool-title">Excel to PDF</h3>
        <p class="saas-tool-desc">Make EXCEL spreadsheets easy to read by converting them to PDF.</p>
      </a>

      <a href="edit.html" class="saas-tool-card" data-cat="edit" data-name="edit pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fdf4ff;color:#9333ea;"><span>✏️</span></div>
        </div>
        <h3 class="saas-tool-title">Edit PDF</h3>
        <p class="saas-tool-desc">Add text, images, shapes or freehand annotations to a PDF document. Edit size, font, and color.</p>
      </a>

      <a href="pdf-to-jpg.html" class="saas-tool-card" data-cat="convert" data-name="pdf to jpg">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fffbeb;color:#d97706;"><span>🖼️</span></div>
        </div>
        <h3 class="saas-tool-title">PDF to JPG</h3>
        <p class="saas-tool-desc">Convert each PDF page into a JPG or extract all images contained in a PDF.</p>
      </a>

      <a href="jpg-to-pdf.html" class="saas-tool-card" data-cat="convert" data-name="jpg to pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fef2f2;color:#dc2626;"><span>📄</span></div>
        </div>
        <h3 class="saas-tool-title">JPG to PDF</h3>
        <p class="saas-tool-desc">Convert JPG images to PDF in seconds. Easily adjust orientation and margins.</p>
      </a>

      <!-- Row 3: Sign PDF, Watermark, Rotate PDF, HTML to PDF, Unlock PDF, Protect PDF -->
      <a href="sign.html" class="saas-tool-card" data-cat="edit" data-name="sign pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#2563eb;"><span>✍️</span></div>
        </div>
        <h3 class="saas-tool-title">Sign PDF</h3>
        <p class="saas-tool-desc">Sign yourself or request electronic signatures from others.</p>
      </a>

      <a href="watermark.html" class="saas-tool-card" data-cat="edit" data-name="watermark pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f5f3ff;color:#7c3aed;"><span>💧</span></div>
        </div>
        <h3 class="saas-tool-title">Watermark</h3>
        <p class="saas-tool-desc">Stamp an image or text over your PDF in seconds. Choose typography, transparency and position.</p>
      </a>

      <a href="rotate.html" class="saas-tool-card" data-cat="organize" data-name="rotate pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fdf4ff;color:#a855f7;"><span>🔄</span></div>
        </div>
        <h3 class="saas-tool-title">Rotate PDF</h3>
        <p class="saas-tool-desc">Rotate your PDFs the way you need them. You can even rotate multiple PDFs at once!</p>
      </a>

      <a href="html-to-pdf.html" class="saas-tool-card" data-cat="convert" data-name="html to pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fefce8;color:#ca8a04;"><span>🌐</span></div>
        </div>
        <h3 class="saas-tool-title">HTML to PDF</h3>
        <p class="saas-tool-desc">Convert webpages to PDF in HTML. Copy and paste the URL of the page you want and convert it to PDF with a click.</p>
      </a>

      <a href="unlock.html" class="saas-tool-card" data-cat="security" data-name="unlock pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#0284c7;"><span>🔓</span></div>
        </div>
        <h3 class="saas-tool-title">Unlock PDF</h3>
        <p class="saas-tool-desc">Remove PDF password security, giving you the freedom to use your PDFs as you want.</p>
      </a>

      <a href="protect.html" class="saas-tool-card" data-cat="security" data-name="protect pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#e0f2fe;color:#0369a1;"><span>🔒</span></div>
        </div>
        <h3 class="saas-tool-title">Protect PDF</h3>
        <p class="saas-tool-desc">Protect PDF files with a password. Encrypt PDF documents to prevent unauthorized access.</p>
      </a>

      <!-- Row 4: Organize PDF, PDF to PDF/A, Repair PDF, Page numbers, Scan to PDF, OCR PDF -->
      <a href="organize.html" class="saas-tool-card" data-cat="organize" data-name="organize pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fff7ed;color:#ea580c;"><span>📑</span></div>
        </div>
        <h3 class="saas-tool-title">Organize PDF</h3>
        <p class="saas-tool-desc">Sort pages of your PDF file however you like. Delete PDF pages or add PDF pages to your document at your convenience.</p>
      </a>

      <a href="pdf-a.html" class="saas-tool-card" data-cat="convert" data-name="pdf/a converter">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f0fdfa;color:#0d9488;"><span>🏛️</span></div>
        </div>
        <h3 class="saas-tool-title">PDF to PDF/A</h3>
        <p class="saas-tool-desc">Transform your PDF to PDF/A, the ISO-standardized version of PDF for long-term archiving.</p>
      </a>

      <a href="repair.html" class="saas-tool-card" data-cat="optimize" data-name="repair pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f0fdf4;color:#16a34a;"><span>🔧</span></div>
        </div>
        <h3 class="saas-tool-title">Repair PDF</h3>
        <p class="saas-tool-desc">Repair a damaged PDF and recover data from corrupt PDF. Fix PDF files with our Repair tool.</p>
      </a>

      <a href="page-numbers.html" class="saas-tool-card" data-cat="organize" data-name="page numbers">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fdf2f8;color:#db2777;"><span>🔢</span></div>
        </div>
        <h3 class="saas-tool-title">Page numbers</h3>
        <p class="saas-tool-desc">Add page numbers into PDFs with ease. Choose your positions, dimensions, typography.</p>
      </a>

      <a href="scan-to-pdf.html" class="saas-tool-card" data-cat="scan" data-name="scan to pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fff7ed;color:#ea580c;"><span>📷</span></div>
        </div>
        <h3 class="saas-tool-title">Scan to PDF</h3>
        <p class="saas-tool-desc">Capture document scans from your mobile device and send them instantly to your browser.</p>
      </a>

      <a href="ocr.html" class="saas-tool-card" data-cat="scan" data-name="ocr pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f0fdf4;color:#16a34a;"><span>👁️</span></div>
        </div>
        <h3 class="saas-tool-title">OCR PDF</h3>
        <p class="saas-tool-desc">Easily convert scanned PDF into searchable and selectable documents.</p>
      </a>

      <!-- Row 5: Compare PDF, Redact PDF, Crop PDF, PDF Forms, AI Summarizer, Translate PDF -->
      <a href="compare.html" class="saas-tool-card" data-cat="analysis" data-name="compare pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#2563eb;"><span>⚖️</span></div>
        </div>
        <h3 class="saas-tool-title">Compare PDF</h3>
        <p class="saas-tool-desc">Show a side-by-side document comparison and easily spot all changes between different file versions.</p>
      </a>

      <a href="redact.html" class="saas-tool-card" data-cat="edit" data-name="redact pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#1e40af;"><span>⬛</span></div>
        </div>
        <h3 class="saas-tool-title">Redact PDF</h3>
        <p class="saas-tool-desc">Redact text and graphics to permanently remove sensitive information from a PDF.</p>
      </a>

      <a href="crop.html" class="saas-tool-card" data-cat="organize" data-name="crop pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fdf2f8;color:#db2777;"><span>📐</span></div>
          <span class="saas-badge-new">New!</span>
        </div>
        <h3 class="saas-tool-title">Crop PDF</h3>
        <p class="saas-tool-desc">Crop margins of PDF documents or select specific areas, then apply the changes to one page or the whole document.</p>
      </a>

      <a href="forms.html" class="saas-tool-card" data-cat="edit" data-name="pdf forms">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f5f3ff;color:#7c3aed;"><span>📋</span></div>
          <span class="saas-badge-new">New!</span>
        </div>
        <h3 class="saas-tool-title">PDF Forms</h3>
        <p class="saas-tool-desc">Create and fill out forms online easily, create interactive fillable PDFs with fillable form-fields, checkboxes, and lists.</p>
      </a>

      <a href="ai-summarizer.html" class="saas-tool-card" data-cat="intelligence" data-name="ai summarizer">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#fdf4ff;color:#9333ea;"><span>✨</span></div>
          <span class="saas-badge-new">New!</span>
        </div>
        <h3 class="saas-tool-title">AI Summarizer</h3>
        <p class="saas-tool-desc">Quickly generate concise summaries from articles, paragraphs, and essays, providing clear and precise key points in seconds.</p>
      </a>

      <a href="translate.html" class="saas-tool-card" data-cat="intelligence" data-name="translate pdf">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f5f3ff;color:#6366f1;"><span>🌐</span></div>
          <span class="saas-badge-new">New!</span>
        </div>
        <h3 class="saas-tool-title">Translate PDF</h3>
        <p class="saas-tool-desc">Fast translation from and into 100+ languages. Keep fonts, layout, and formatting privacy-aware.</p>
      </a>

      <!-- Row 6: PDF to Markdown, Create a workflow (Banner 2-col) -->
      <a href="pdf-to-markdown.html" class="saas-tool-card" data-cat="intelligence" data-name="pdf to markdown">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f5f3ff;color:#7c3aed;"><span>🤖</span></div>
          <span class="saas-badge-new">New!</span>
        </div>
        <h3 class="saas-tool-title">PDF to Markdown</h3>
        <p class="saas-tool-desc">Easily turn PDFs into Markdown files. Perfect for notes, docs, and LLMs: headings, tables, lists, and links preserved automatically.</p>
      </a>

      <a href="workflow.html" class="saas-tool-card saas-workflow-banner-card" data-cat="workflow" data-name="create a workflow">
        <div class="workflow-content">
          <h3 class="saas-tool-title" style="color:#c2410c;font-size:1.15rem;margin-bottom:6px;">Create a workflow</h3>
          <p class="saas-tool-desc" style="color:#7c2d12;margin-bottom:14px;">Create custom workflows with your favorite tools, automate tasks, and expand your outputs.</p>
          <span style="font-weight:700;font-size:0.85rem;color:#ea580c;display:inline-flex;align-items:center;gap:4px;">Customize flow &gt;</span>
        </div>
      </a>

      <!-- Extra Analysis & Inspection Tools -->
      <a href="info.html" class="saas-tool-card" data-cat="analysis" data-name="pdf information">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eff6ff;color:#2563eb;"><span>ℹ️</span></div>
        </div>
        <h3 class="saas-tool-title">PDF Information</h3>
        <p class="saas-tool-desc">Inspect page dimensions, PDF version, author metadata, and document properties.</p>
      </a>

      <a href="page-counter.html" class="saas-tool-card" data-cat="analysis" data-name="pdf page counter">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#ecfdf5;color:#059669;"><span>🔢</span></div>
        </div>
        <h3 class="saas-tool-title">PDF Page Counter</h3>
        <p class="saas-tool-desc">Quickly count exact pages and calculate printing cost estimates for PDF batches.</p>
      </a>

      <a href="viewer.html" class="saas-tool-card" data-cat="analysis" data-name="pdf viewer">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eef2ff;color:#6366f1;"><span>👁️</span></div>
        </div>
        <h3 class="saas-tool-title">PDF Viewer</h3>
        <p class="saas-tool-desc">Open and read PDF files directly in your web browser with zoom and search controls.</p>
      </a>

      <a href="extract.html" class="saas-tool-card" data-cat="organize" data-name="extract pages">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#eef2ff;color:#6366f1;"><span>📥</span></div>
        </div>
        <h3 class="saas-tool-title">Extract Pages</h3>
        <p class="saas-tool-desc">Extract specific pages or custom ranges into a new separate PDF file.</p>
      </a>

      <a href="reorder.html" class="saas-tool-card" data-cat="organize" data-name="reorder pages">
        <div class="card-header-row">
          <div class="saas-tool-icon-wrap" style="background:#f0fdfa;color:#14b8a6;"><span>🔀</span></div>
        </div>
        <h3 class="saas-tool-title">Reorder Pages</h3>
        <p class="saas-tool-desc">Rearrange and re-sequence PDF pages visually in your browser.</p>
      </a>'''

# Let's read pdf/index.html and update the styles, category bar, and cards grid
with open('pdf/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace category nav
category_nav_html = '''      <!-- Category Filter Pills matching Reference -->
      <div class="saas-category-nav" id="categoryFilterBar">
        <button type="button" class="saas-pill-btn active" data-filter="all">All</button>
        <button type="button" class="saas-pill-btn" data-filter="organize">Organize PDF</button>
        <button type="button" class="saas-pill-btn" data-filter="optimize">Optimize PDF</button>
        <button type="button" class="saas-pill-btn" data-filter="convert">Convert PDF</button>
        <button type="button" class="saas-pill-btn" data-filter="edit">Edit PDF</button>
        <button type="button" class="saas-pill-btn" data-filter="security">PDF Security</button>
        <button type="button" class="saas-pill-btn" data-filter="intelligence">PDF Intelligence</button>
      </div>'''

html = re.sub(r'<div class="saas-category-nav"[\s\S]*?</div>', category_nav_html, html, count=1)

# Replace cards grid content
html = re.sub(r'<div class="saas-grid-container" id="toolGrid">[\s\S]*?</div>\s*<!-- SEO Content', f'<div class="saas-grid-container" id="toolGrid">\n{pdf_cards_html}\n    </div>\n\n    <!-- SEO Content', html, count=1)

# Add CSS styles for the grid, new badge, card header row, and workflow banner
custom_styles = '''  <style>
    .saas-grid-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 14px;
      margin-top: 1.5rem;
      margin-bottom: 3.5rem;
    }
    @media (min-width: 1280px) {
      .saas-grid-container {
        grid-template-columns: repeat(6, 1fr);
      }
    }
    .saas-tool-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 16px 14px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
      position: relative;
      min-height: 140px;
    }
    .saas-tool-card:hover {
      transform: translateY(-3px);
      border-color: var(--primary-300);
      box-shadow: 0 10px 20px -3px rgba(15, 23, 42, 0.09);
    }
    .card-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }
    .saas-tool-icon-wrap {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
    }
    .saas-badge-new {
      background: #eff6ff;
      color: #2563eb;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid #bfdbfe;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }
    .saas-tool-title {
      font-size: 1rem;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 4px;
      line-height: 1.3;
    }
    .saas-tool-desc {
      font-size: 0.78rem;
      color: #64748b;
      line-height: 1.42;
      margin: 0;
    }
    .saas-workflow-banner-card {
      grid-column: span 2;
      background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
      border: 1.5px dashed #fdba74;
      justify-content: center;
      padding: 18px 20px;
    }
    @media (max-width: 768px) {
      .saas-workflow-banner-card {
        grid-column: span 1;
      }
    }
    .search-filter-wrap {
      max-width: 520px;
      margin: 0 auto 1.5rem;
      position: relative;
    }
    .search-filter-input {
      width: 100%;
      padding: 12px 18px 12px 42px;
      border: 1.5px solid #cbd5e1;
      border-radius: 30px;
      font-size: 0.95rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      outline: none;
      transition: all 0.2s;
    }
    .search-filter-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.2);
    }
    .search-icon-pos {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: #94a3b8;
      font-size: 1.1rem;
    }
    .saas-category-nav {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 8px;
      margin: 1.5rem 0 2rem;
    }
    .saas-pill-btn {
      padding: 7px 18px;
      font-size: 0.88rem;
      font-weight: 600;
      border-radius: 999px;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      color: #334155;
      cursor: pointer;
      transition: all 0.2s;
    }
    .saas-pill-btn:hover {
      background: #eff6ff;
      color: #2563eb;
      border-color: #93c5fd;
    }
    .saas-pill-btn.active {
      background: #2563eb;
      color: #ffffff;
      border-color: #2563eb;
      box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25);
    }
  </style>'''

html = re.sub(r'<style>[\s\S]*?</style>', custom_styles, html, count=1)

with open('pdf/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated pdf/index.html with pixel-perfect reference layout!")
