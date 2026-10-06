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
          <li><a href="pdf-to-word.html">PDF to Word</a></li>
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

# 1. ORGANIZE PDF
organize_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Organize PDF Pages Online Free — Reorder, Rotate & Delete | DigitalSaathi</title>
  <meta name="description" content="Organize PDF pages online for free. Visual drag-and-drop grid to sort, reorder, rotate, duplicate, and delete pages from any PDF document. 100% private in browser.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .organize-toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: space-between;
      align-items: center;
      background: #f8fafc;
      padding: 12px 18px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      margin: 20px 0 16px;
    }}
    .organize-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
      gap: 16px;
      margin: 20px 0;
      min-height: 200px;
    }}
    .organize-card {{
      background: #ffffff;
      border: 2px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      transition: all 0.2s ease;
      user-select: none;
      box-shadow: var(--shadow-sm);
    }}
    .organize-card:hover {{
      border-color: var(--primary);
      box-shadow: var(--shadow-md);
      transform: translateY(-2px);
    }}
    .organize-card.selected {{
      border-color: var(--primary);
      background: #eff6ff;
    }}
    .organize-card.dragging {{
      opacity: 0.4;
      border: 2px dashed var(--primary);
    }}
    .organize-thumb-wrap {{
      width: 130px;
      height: 170px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      margin-bottom: 8px;
    }}
    .organize-thumb-wrap canvas {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.2s ease;
    }}
    .organize-card-header {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}
    .organize-page-badge {{
      font-size: 0.75rem;
      font-weight: 700;
      background: #e2e8f0;
      color: #334155;
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .organize-card-actions {{
      display: flex;
      gap: 4px;
      margin-top: 4px;
      width: 100%;
      justify-content: center;
    }}
    .card-action-btn {{
      padding: 4px 6px;
      font-size: 0.75rem;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      border-radius: 4px;
      cursor: pointer;
      line-height: 1;
      transition: background 0.15s ease;
    }}
    .card-action-btn:hover {{
      background: #f1f5f9;
      border-color: #94a3b8;
    }}
    .card-action-btn.btn-delete:hover {{
      background: #fee2e2;
      border-color: #ef4444;
      color: #b91c1c;
    }}
  </style>
</head>
<body class="tool-page">

{NAVBAR}

  <div class="container page-content">
    <div class="breadcrumb">
      <a href="../index.html">Home</a>
      <span>›</span>
      <a href="index.html">PDF Tools</a>
      <span>›</span>
      <span>Organize PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#e0f2fe;color:#0284c7;">📑</div>
      <h1 class="tool-title">Organize PDF Pages</h1>
      <p class="tool-desc">Rearrange, rotate, delete, or duplicate pages in your PDF document with a visual drag-and-drop grid. 100% free and client-side secure.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% In-Browser Secure</span>
        <span class="badge badge-primary">⚡ Instant Reordering</span>
        <span class="badge badge-neutral">🔄 Rotate & Delete</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Rearrange, rotate, and delete pages with live interactive thumbnails</p>
      <button class="btn btn-primary" id="selectBtn" type="button">Choose PDF File</button>
      <input type="file" id="fileInput" accept="application/pdf" style="display:none;">
    </div>

    <!-- File Info Bar -->
    <div class="file-info-bar" id="fileInfo" style="display: none;">
      <div class="file-details">
        <span class="file-name" id="fileName">document.pdf</span>
        <span class="file-meta" id="fileMeta">0 KB • 0 Pages</span>
      </div>
      <button class="btn btn-sm btn-outline" id="changeFileBtn" type="button">Change File</button>
    </div>

    <!-- Organize Workspace -->
    <div id="organizeWorkspace" style="display:none;">
      <div class="organize-toolbar">
        <div style="display:flex;gap:8px;align-items:center;">
          <span style="font-weight:600;font-size:0.9rem;color:#334155;">Page Count: <span id="activePageCount" style="color:var(--primary);">0</span></span>
          <button class="btn btn-sm btn-outline" id="rotateAllLeftBtn" title="Rotate all pages left">↺ Rotate All Left</button>
          <button class="btn btn-sm btn-outline" id="rotateAllRightBtn" title="Rotate all pages right">↻ Rotate All Right</button>
        </div>
        <div style="display:flex;gap:8px;align-items:center;">
          <button class="btn btn-sm btn-outline" id="resetOrderBtn">Reset Default</button>
          <button class="btn btn-primary btn-sm" id="processBtnTop">Save Organized PDF</button>
        </div>
      </div>

      <div class="organize-grid" id="organizeGrid">
        <!-- Rendered page cards dynamically -->
      </div>

      <div class="action-buttons text-center" style="margin: 32px 0;">
        <button class="btn btn-primary btn-lg" id="processBtn">Save & Download PDF</button>
        <button class="btn btn-outline btn-lg" id="resetBtn">Clear All</button>
      </div>
    </div>

    <!-- Progress Indicator -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Building organized PDF... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Organized Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your pages have been reordered, rotated, and cleaned.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="organized.pdf">⬇️ Download Organized PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Organize Another File</button>
      </div>
    </div>

    <!-- Step by step instructions -->
    <div class="guide-card">
      <h3 class="guide-title">How to Organize PDF Pages Online</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select or drop your PDF document. All pages are rendered instantly as visual interactive cards.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Reorder & Rotate</h4>
          <p class="step-desc">Drag and drop cards to change sequence, click rotate buttons (↺ ↻) to orient, or trash icon (🗑️) to delete.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Download Saved PDF</h4>
          <p class="step-desc">Click "Save & Download PDF" to immediately compile and export your new PDF document.</p>
        </div>
      </div>
    </div>

    <!-- FAQs -->
    <div class="faq-section">
      <h3 class="faq-heading">Frequently Asked Questions</h3>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question">Can I delete unwanted pages from my PDF?</summary>
          <div class="faq-answer">Yes! Simply click the trash can icon (🗑️) on any page card to remove it from the final generated PDF.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Are my sensitive documents uploaded to any server?</summary>
          <div class="faq-answer">No. All rendering, page reorganization, and PDF compilation occurs 100% inside your web browser via WebAssembly and JavaScript. Zero data leaves your computer.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Can I rotate individual pages that were scanned upside down?</summary>
          <div class="faq-answer">Yes. Each card features dedicated 90-degree left and right rotation controls so you can fix misoriented pages individually.</div>
        </details>
      </div>
    </div>

    <!-- Related Tools -->
    <div class="related-tools-section">
      <h3 class="section-title">Related PDF Tools</h3>
      <div class="tools-grid">
        <a href="merge.html" class="tool-card">
          <div class="tool-icon" style="background:#eff6ff;color:#2563eb;">📑</div>
          <h4 class="tool-name">Merge PDF</h4>
          <p class="tool-short-desc">Combine multiple PDF documents into one single file.</p>
        </a>
        <a href="split.html" class="tool-card">
          <div class="tool-icon" style="background:#fef2f2;color:#dc2626;">✂️</div>
          <h4 class="tool-name">Split PDF</h4>
          <p class="tool-short-desc">Extract custom page ranges or split into separate files.</p>
        </a>
        <a href="crop.html" class="tool-card">
          <div class="tool-icon" style="background:#f0fdf4;color:#16a34a;">📐</div>
          <h4 class="tool-name">Crop PDF</h4>
          <p class="tool-short-desc">Trim margins and crop PDF pages visually.</p>
        </a>
        <a href="page-numbers.html" class="tool-card">
          <div class="tool-icon" style="background:#fdf4ff;color:#9333ea;">🔢</div>
          <h4 class="tool-name">Page Numbers</h4>
          <p class="tool-short-desc">Insert page numbers with custom positions and styles.</p>
        </a>
      </div>
    </div>
  </div>

{FOOTER}

  <!-- Scripts -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    if (typeof pdfjsLib !== 'undefined') {{
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }}

    let currentFile = null;
    let pdfDocProxy = null;
    let originalPdfBytes = null;
    let pageItems = []; // {{ originalIndex: 0, rotation: 0, canvasDataUrl: '' }}
    let draggedIndex = null;

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const organizeWorkspace = document.getElementById('organizeWorkspace');
    const organizeGrid = document.getElementById('organizeGrid');
    const activePageCount = document.getElementById('activePageCount');
    const rotateAllLeftBtn = document.getElementById('rotateAllLeftBtn');
    const rotateAllRightBtn = document.getElementById('rotateAllRightBtn');
    const resetOrderBtn = document.getElementById('resetOrderBtn');
    const processBtn = document.getElementById('processBtn');
    const processBtnTop = document.getElementById('processBtnTop');
    const resetBtn = document.getElementById('resetBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{
      if (e.target !== selectBtn) fileInput.click();
    }});

    uploadZone.addEventListener('dragover', (e) => {{
      e.preventDefault();
      uploadZone.classList.add('drag-over');
    }});

    uploadZone.addEventListener('dragleave', () => {{
      uploadZone.classList.remove('drag-over');
    }});

    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {{
        handleFile(e.dataTransfer.files[0]);
      }}
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) {{
        handleFile(e.target.files[0]);
      }}
    }});

    changeFileBtn.addEventListener('click', () => {{
      fileInput.value = '';
      fileInput.click();
    }});

    async function handleFile(file) {{
      if (!file || file.type !== 'application/pdf' && !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • Loading...`;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '15%';
      progressText.textContent = 'Reading document structure...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        pdfDocProxy = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes) }}).promise;
        const numPages = pdfDocProxy.numPages;
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{numPages}} ${{numPages === 1 ? 'Page' : 'Pages'}}`;

        pageItems = [];
        for (let i = 1; i <= numPages; i++) {{
          progressFill.style.width = `${{Math.round(15 + (i / numPages) * 75)}}%`;
          progressText.textContent = `Rendering page ${{i}} of ${{numPages}}...`;

          const page = await pdfDocProxy.getPage(i);
          const viewport = page.getViewport({{ scale: 0.35 }});
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          canvas.width = viewport.width;
          canvas.height = viewport.height;
          await page.render({{ canvasContext: ctx, viewport: viewport }}).promise;

          pageItems.push({{
            originalIndex: i - 1,
            originalPageNum: i,
            rotation: 0,
            canvasDataUrl: canvas.toDataURL('image/jpeg', 0.8)
          }});
        }}

        progressContainer.style.display = 'none';
        organizeWorkspace.style.display = 'block';
        renderGrid();
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
        fileInfo.style.display = 'none';
      }}
    }}

    function renderGrid() {{
      organizeGrid.innerHTML = '';
      activePageCount.textContent = pageItems.length;

      if (pageItems.length === 0) {{
        organizeGrid.innerHTML = '<div style="grid-column:1/-1;text-align:center;padding:40px;color:#94a3b8;">No pages remaining. Click "Reset Default" to restore original pages.</div>';
        return;
      }}

      pageItems.forEach((item, index) => {{
        const card = document.createElement('div');
        card.className = 'organize-card';
        card.draggable = true;
        card.dataset.index = index;

        card.innerHTML = `
          <div class="organize-card-header">
            <span class="organize-page-badge">Page ${{index + 1}} (Orig: #${{item.originalPageNum}})</span>
            <span style="font-size:0.7rem;color:#64748b;">${{item.rotation !== 0 ? item.rotation + '°' : ''}}</span>
          </div>
          <div class="organize-thumb-wrap">
            <img src="${{item.canvasDataUrl}}" style="max-width:100%;max-height:100%;transform:rotate(${{item.rotation}}deg);transition:transform 0.2s;" alt="Page ${{index + 1}}">
          </div>
          <div class="organize-card-actions">
            <button class="card-action-btn" data-action="rotate-left" title="Rotate Left 90°">↺</button>
            <button class="card-action-btn" data-action="rotate-right" title="Rotate Right 90°">↻</button>
            <button class="card-action-btn" data-action="move-left" title="Move Left" ${{index === 0 ? 'disabled' : ''}}>←</button>
            <button class="card-action-btn" data-action="move-right" title="Move Right" ${{index === pageItems.length - 1 ? 'disabled' : ''}}>→</button>
            <button class="card-action-btn" data-action="duplicate" title="Duplicate Page">📋</button>
            <button class="card-action-btn btn-delete" data-action="delete" title="Delete Page">🗑️</button>
          </div>
        `;

        // Card button actions
        card.addEventListener('click', (e) => {{
          const btn = e.target.closest('button');
          if (!btn) return;
          const action = btn.dataset.action;
          if (action === 'rotate-left') {{
            item.rotation = (item.rotation - 90 + 360) % 360;
            renderGrid();
          }} else if (action === 'rotate-right') {{
            item.rotation = (item.rotation + 90) % 360;
            renderGrid();
          }} else if (action === 'move-left' && index > 0) {{
            const temp = pageItems[index];
            pageItems[index] = pageItems[index - 1];
            pageItems[index - 1] = temp;
            renderGrid();
          }} else if (action === 'move-right' && index < pageItems.length - 1) {{
            const temp = pageItems[index];
            pageItems[index] = pageItems[index + 1];
            pageItems[index + 1] = temp;
            renderGrid();
          }} else if (action === 'duplicate') {{
            pageItems.splice(index + 1, 0, {{ ...item }});
            renderGrid();
          }} else if (action === 'delete') {{
            pageItems.splice(index, 1);
            renderGrid();
          }}
        }});

        // Drag and drop handling
        card.addEventListener('dragstart', () => {{
          draggedIndex = index;
          card.classList.add('dragging');
        }});
        card.addEventListener('dragend', () => {{
          card.classList.remove('dragging');
          draggedIndex = null;
        }});
        card.addEventListener('dragover', (e) => {{
          e.preventDefault();
        }});
        card.addEventListener('drop', (e) => {{
          e.preventDefault();
          if (draggedIndex !== null && draggedIndex !== index) {{
            const draggedItem = pageItems.splice(draggedIndex, 1)[0];
            pageItems.splice(index, 0, draggedItem);
            renderGrid();
          }}
        }});

        organizeGrid.appendChild(card);
      }});
    }}

    rotateAllLeftBtn.addEventListener('click', () => {{
      pageItems.forEach(p => p.rotation = (p.rotation - 90 + 360) % 360);
      renderGrid();
    }});

    rotateAllRightBtn.addEventListener('click', () => {{
      pageItems.forEach(p => p.rotation = (p.rotation + 90) % 360);
      renderGrid();
    }});

    resetOrderBtn.addEventListener('click', async () => {{
      if (!pdfDocProxy) return;
      handleFile(currentFile);
    }});

    async function executeOrganize() {{
      if (pageItems.length === 0) {{
        alert('Your document has no pages left! Please reset or add pages.');
        return;
      }}
      organizeWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '20%';
      progressText.textContent = 'Creating organized document...';

      try {{
        const srcDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const newDoc = await PDFLib.PDFDocument.create();

        for (let i = 0; i < pageItems.length; i++) {{
          const item = pageItems[i];
          progressFill.style.width = `${{Math.round(20 + ((i + 1) / pageItems.length) * 60)}}%`;
          progressText.textContent = `Assembling page ${{i + 1}} of ${{pageItems.length}}...`;

          const [copiedPage] = await newDoc.copyPages(srcDoc, [item.originalIndex]);
          if (item.rotation !== 0) {{
            const currentRot = copiedPage.getRotation().angle;
            copiedPage.setRotation(PDFLib.degrees((currentRot + item.rotation) % 360));
          }}
          newDoc.addPage(copiedPage);
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Generating PDF binary...';

        const pdfBytes = await newDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_organized.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Successfully saved ${{pageItems.length}} pages. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error saving organized PDF: ' + err.message);
        progressContainer.style.display = 'none';
        organizeWorkspace.style.display = 'block';
      }}
    }}

    processBtn.addEventListener('click', executeOrganize);
    processBtnTop.addEventListener('click', executeOrganize);

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      organizeWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
      originalPdfBytes = null;
      pageItems = [];
    }});

    resetBtn.addEventListener('click', () => {{
      if (confirm('Are you sure you want to clear this file?')) {{
        processAnotherBtn.click();
      }}
    }});
  </script>
</body>
</html>'''

write_file('pdf/organize.html', organize_html)
