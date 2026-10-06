import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from build_batch_organize_edit import NAVBAR, FOOTER, write_file

# ==========================================
# 1. CROP PDF
# ==========================================
crop_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Crop PDF Pages Online Free — Custom PDF Margins | DigitalSaathi</title>
  <meta name="description" content="Crop PDF margins online for free. Visual interactive crop box and fine percentage margins. Trim white borders and crop pages client-side with 100% privacy.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .crop-workspace {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 24px;
      margin: 24px 0;
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .crop-workspace {{
        grid-template-columns: 1fr;
      }}
    }}
    .crop-preview-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: var(--shadow-sm);
    }}
    .crop-canvas-container {{
      position: relative;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      max-width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    #cropCanvas {{
      max-width: 100%;
      height: auto;
      display: block;
    }}
    .crop-overlay {{
      position: absolute;
      border: 2px dashed #2563eb;
      background: rgba(37, 99, 235, 0.15);
      cursor: move;
      box-sizing: border-box;
    }}
    .crop-controls-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }}
    .margin-inputs-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin: 16px 0;
    }}
    .page-nav-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      margin-bottom: 12px;
      padding: 8px 12px;
      background: #f1f5f9;
      border-radius: 6px;
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
      <span>Crop PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#f0fdf4;color:#16a34a;">📐</div>
      <h1 class="tool-title">Crop PDF Pages</h1>
      <p class="tool-desc">Trim white borders, remove margins, and crop your PDF pages to custom dimensions with live preview. 100% private in-browser tool.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">📐 Visual Crop Box</span>
        <span class="badge badge-neutral">⚡ Instant Download</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Adjust margins and crop pages with interactive visual controls</p>
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

    <!-- Workspace -->
    <div id="cropWorkspace" class="crop-workspace" style="display:none;">
      <!-- Preview Pane -->
      <div class="crop-preview-card">
        <div class="page-nav-bar">
          <button class="btn btn-sm btn-outline" id="prevPageBtn">◀ Prev Page</button>
          <span style="font-weight:600;font-size:0.9rem;" id="pageIndicator">Page 1 of 1</span>
          <button class="btn btn-sm btn-outline" id="nextPageBtn">Next Page ▶</button>
        </div>
        <div class="crop-canvas-container" id="canvasContainer">
          <canvas id="cropCanvas"></canvas>
          <div id="cropOverlay" class="crop-overlay"></div>
        </div>
      </div>

      <!-- Settings Pane -->
      <div class="crop-controls-card">
        <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:12px;color:#1e293b;">Crop Settings</h3>
        
        <div class="form-group" style="margin-bottom:14px;">
          <label class="form-label" style="font-weight:600;">Crop Preset</label>
          <select id="cropPreset" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="custom">Custom Margins</option>
            <option value="trim5">Trim 5% Borders (Standard Clean)</option>
            <option value="trim10">Trim 10% Borders (Wide Margins)</option>
            <option value="trim15">Trim 15% Borders (Tight Content)</option>
          </select>
        </div>

        <div class="margin-inputs-grid">
          <div>
            <label class="form-label" style="font-size:0.8rem;font-weight:600;">Top Crop (%)</label>
            <input type="number" id="cropTop" class="form-input" min="0" max="45" value="5" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:4px;">
          </div>
          <div>
            <label class="form-label" style="font-size:0.8rem;font-weight:600;">Bottom Crop (%)</label>
            <input type="number" id="cropBottom" class="form-input" min="0" max="45" value="5" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:4px;">
          </div>
          <div>
            <label class="form-label" style="font-size:0.8rem;font-weight:600;">Left Crop (%)</label>
            <input type="number" id="cropLeft" class="form-input" min="0" max="45" value="5" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:4px;">
          </div>
          <div>
            <label class="form-label" style="font-size:0.8rem;font-weight:600;">Right Crop (%)</label>
            <input type="number" id="cropRight" class="form-input" min="0" max="45" value="5" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:4px;">
          </div>
        </div>

        <div class="form-group" style="margin-bottom:18px;">
          <label class="form-label" style="font-weight:600;">Apply Crop To</label>
          <div style="display:flex;flex-direction:column;gap:6px;margin-top:6px;">
            <label style="font-size:0.9rem;display:flex;align-items:center;gap:6px;cursor:pointer;">
              <input type="radio" name="applyScope" value="all" checked> All Pages in Document
            </label>
            <label style="font-size:0.9rem;display:flex;align-items:center;gap:6px;cursor:pointer;">
              <input type="radio" name="applyScope" value="current"> Current Page Only
            </label>
          </div>
        </div>

        <button class="btn btn-primary" id="processCropBtn" style="width:100%;padding:12px;font-weight:700;font-size:1rem;">Crop PDF & Download</button>
        <button class="btn btn-outline" id="resetCropBtn" style="width:100%;margin-top:8px;padding:8px;">Reset Settings</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Processing crop... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Cropped Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your PDF pages have been cropped to the specified dimensions.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="cropped.pdf">⬇️ Download Cropped PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Crop Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Crop PDF Margins</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select your PDF file. The first page is rendered with a live visual crop box.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Set Margins</h4>
          <p class="step-desc">Choose a quick preset or adjust Top, Bottom, Left, and Right crop percentages.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Save & Download</h4>
          <p class="step-desc">Click Crop PDF. The CropBox coordinates are updated and your file downloads instantly.</p>
        </div>
      </div>
    </div>

    <!-- FAQ -->
    <div class="faq-section">
      <h3 class="faq-heading">Frequently Asked Questions</h3>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question">Does cropping reduce PDF file size?</summary>
          <div class="faq-answer">Cropping updates the visible bounding box (CropBox) of the PDF, trimming away headers, footers, or blank margins for cleaner printing and viewing.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Can I apply different crops to different pages?</summary>
          <div class="faq-answer">Yes, you can choose to apply the crop to all pages or apply it specifically to the active page.</div>
        </details>
      </div>
    </div>
  </div>

{FOOTER}

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
    let currentPageNum = 1;
    let totalPages = 1;

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const cropWorkspace = document.getElementById('cropWorkspace');
    const cropCanvas = document.getElementById('cropCanvas');
    const cropOverlay = document.getElementById('cropOverlay');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const pageIndicator = document.getElementById('pageIndicator');
    const cropTop = document.getElementById('cropTop');
    const cropBottom = document.getElementById('cropBottom');
    const cropLeft = document.getElementById('cropLeft');
    const cropRight = document.getElementById('cropRight');
    const cropPreset = document.getElementById('cropPreset');
    const processCropBtn = document.getElementById('processCropBtn');
    const resetCropBtn = document.getElementById('resetCropBtn');
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

    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{
      fileInput.value = '';
      fileInput.click();
    }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
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
      progressFill.style.width = '30%';
      progressText.textContent = 'Loading pages for visual crop...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        pdfDocProxy = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes) }}).promise;
        totalPages = pdfDocProxy.numPages;
        currentPageNum = 1;
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{totalPages}} ${{totalPages === 1 ? 'Page' : 'Pages'}}`;

        progressContainer.style.display = 'none';
        cropWorkspace.style.display = 'grid';
        await renderCurrentPage();
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    async function renderCurrentPage() {{
      if (!pdfDocProxy) return;
      pageIndicator.textContent = `Page ${{currentPageNum}} of ${{totalPages}}`;
      prevPageBtn.disabled = currentPageNum <= 1;
      nextPageBtn.disabled = currentPageNum >= totalPages;

      const page = await pdfDocProxy.getPage(currentPageNum);
      const viewport = page.getViewport({{ scale: 1.0 }});
      const ctx = cropCanvas.getContext('2d');
      cropCanvas.width = viewport.width;
      cropCanvas.height = viewport.height;
      await page.render({{ canvasContext: ctx, viewport: viewport }}).promise;

      updateOverlay();
    }}

    function updateOverlay() {{
      const t = parseFloat(cropTop.value) || 0;
      const b = parseFloat(cropBottom.value) || 0;
      const l = parseFloat(cropLeft.value) || 0;
      const r = parseFloat(cropRight.value) || 0;

      const w = cropCanvas.clientWidth;
      const h = cropCanvas.clientHeight;

      const topPx = (t / 100) * h;
      const bottomPx = (b / 100) * h;
      const leftPx = (l / 100) * w;
      const rightPx = (r / 100) * w;

      cropOverlay.style.top = topPx + 'px';
      cropOverlay.style.left = leftPx + 'px';
      cropOverlay.style.width = (w - leftPx - rightPx) + 'px';
      cropOverlay.style.height = (h - topPx - bottomPx) + 'px';
    }}

    [cropTop, cropBottom, cropLeft, cropRight].forEach(input => {{
      input.addEventListener('input', () => {{
        cropPreset.value = 'custom';
        updateOverlay();
      }});
    }});

    cropPreset.addEventListener('change', () => {{
      const val = cropPreset.value;
      if (val === 'trim5') {{
        cropTop.value = 5; cropBottom.value = 5; cropLeft.value = 5; cropRight.value = 5;
      }} else if (val === 'trim10') {{
        cropTop.value = 10; cropBottom.value = 10; cropLeft.value = 10; cropRight.value = 10;
      }} else if (val === 'trim15') {{
        cropTop.value = 15; cropBottom.value = 15; cropLeft.value = 15; cropRight.value = 15;
      }}
      updateOverlay();
    }});

    prevPageBtn.addEventListener('click', () => {{
      if (currentPageNum > 1) {{
        currentPageNum--;
        renderCurrentPage();
      }}
    }});

    nextPageBtn.addEventListener('click', () => {{
      if (currentPageNum < totalPages) {{
        currentPageNum++;
        renderCurrentPage();
      }}
    }});

    window.addEventListener('resize', updateOverlay);

    processCropBtn.addEventListener('click', async () => {{
      cropWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '20%';
      progressText.textContent = 'Applying crop coordinates...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const pages = pdfDoc.getPages();
        const applyScope = document.querySelector('input[name="applyScope"]:checked').value;

        const tPct = (parseFloat(cropTop.value) || 0) / 100;
        const bPct = (parseFloat(cropBottom.value) || 0) / 100;
        const lPct = (parseFloat(cropLeft.value) || 0) / 100;
        const rPct = (parseFloat(cropRight.value) || 0) / 100;

        for (let i = 0; i < pages.length; i++) {{
          if (applyScope === 'current' && i !== (currentPageNum - 1)) continue;

          const p = pages[i];
          const {{ width, height }} = p.getSize();

          const x = width * lPct;
          const y = height * bPct;
          const cropW = width * (1 - lPct - rPct);
          const cropH = height * (1 - tPct - bPct);

          p.setCropBox(x, y, cropW, cropH);
        }}

        progressFill.style.width = '80%';
        progressText.textContent = 'Saving cropped PDF...';

        const croppedBytes = await pdfDoc.save();
        const blob = new Blob([croppedBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_cropped.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Crop applied successfully. New file size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error cropping PDF: ' + err.message);
        progressContainer.style.display = 'none';
        cropWorkspace.style.display = 'grid';
      }}
    }});

    resetCropBtn.addEventListener('click', () => {{
      cropTop.value = 0; cropBottom.value = 0; cropLeft.value = 0; cropRight.value = 0;
      cropPreset.value = 'custom';
      updateOverlay();
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      cropWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/crop.html', crop_html)

# ==========================================
# 2. PAGE NUMBERS
# ==========================================
page_numbers_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Add Page Numbers to PDF Online Free | DigitalSaathi</title>
  <meta name="description" content="Add page numbers to PDF documents online for free. Custom positions, formats (Page X of Y), fonts, starting numbers, and styles. 100% private in browser.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .position-matrix {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      grid-template-rows: repeat(2, 60px);
      gap: 10px;
      margin: 16px 0;
      background: #f8fafc;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
    }}
    .pos-btn {{
      border: 2px solid #cbd5e1;
      background: #ffffff;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 600;
      color: #64748b;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .pos-btn:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}
    .pos-btn.active {{
      border-color: var(--primary);
      background: #eff6ff;
      color: var(--primary);
      box-shadow: 0 0 0 2px rgba(37,99,235,0.2);
    }}
    .options-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin: 20px 0;
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
      <span>Page Numbers</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#fdf4ff;color:#9333ea;">🔢</div>
      <h1 class="tool-title">Add Page Numbers to PDF</h1>
      <p class="tool-desc">Stamp customizable page numbers into your PDF documents with custom position, format, font, and margins. 100% private in-browser.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">🔢 "Page X of Y" Presets</span>
        <span class="badge badge-neutral">📍 6 Position Slots</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Customize position, typography, and number formats</p>
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

    <!-- Settings Workspace -->
    <div id="numWorkspace" style="display:none;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:24px;margin:24px 0;box-shadow:var(--shadow-sm);">
      <h3 style="font-size:1.15rem;font-weight:700;color:#1e293b;margin-bottom:16px;">1. Choose Position on Page</h3>
      
      <div class="position-matrix">
        <div class="pos-btn" data-pos="top-left">Top Left</div>
        <div class="pos-btn" data-pos="top-center">Top Center</div>
        <div class="pos-btn" data-pos="top-right">Top Right</div>
        <div class="pos-btn" data-pos="bottom-left">Bottom Left</div>
        <div class="pos-btn active" data-pos="bottom-center">Bottom Center</div>
        <div class="pos-btn" data-pos="bottom-right">Bottom Right</div>
      </div>

      <h3 style="font-size:1.15rem;font-weight:700;color:#1e293b;margin:24px 0 16px;">2. Format & Styling Options</h3>
      
      <div class="options-grid">
        <div class="form-group">
          <label class="form-label" style="font-weight:600;">Number Format</label>
          <select id="numFormat" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="p_of_n">Page {{n}} of {{total}}</option>
            <option value="p_slash_n">{{n}} / {{total}}</option>
            <option value="page_n">Page {{n}}</option>
            <option value="num_only">{{n}}</option>
            <option value="dash_n">- {{n}} -</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" style="font-weight:600;">Font Family</label>
          <select id="fontFamily" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="Helvetica">Helvetica (Standard Clean)</option>
            <option value="TimesRoman">Times New Roman (Academic)</option>
            <option value="Courier">Courier (Monospace / Code)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" style="font-weight:600;">Font Size</label>
          <select id="fontSize" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="9">9 pt (Small)</option>
            <option value="11" selected>11 pt (Standard)</option>
            <option value="13">13 pt (Medium)</option>
            <option value="16">16 pt (Large)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" style="font-weight:600;">Font Color</label>
          <select id="fontColor" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="black" selected>Black (#000000)</option>
            <option value="gray">Slate Gray (#475569)</option>
            <option value="blue">Royal Blue (#1e40af)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" style="font-weight:600;">Starting Number</label>
          <input type="number" id="startNumber" class="form-input" value="1" min="1" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
        </div>

        <div class="form-group">
          <label class="form-label" style="font-weight:600;">Cover Page Handling</label>
          <select id="coverOption" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="all">Number all pages</option>
            <option value="skip_first">Skip Page 1 (Cover page without number)</option>
          </select>
        </div>
      </div>

      <div class="action-buttons text-center" style="margin-top:28px;">
        <button class="btn btn-primary btn-lg" id="processBtn">Add Page Numbers & Download</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Stamping numbers... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">Page Numbers Added Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your PDF now has numbered pages.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="numbered.pdf">⬇️ Download Numbered PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Process Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Add Page Numbers to PDF</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select your PDF file from your device.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Select Position & Style</h4>
          <p class="step-desc">Choose from 6 positions (e.g. Bottom Center), font, size, and formatting style.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Download File</h4>
          <p class="step-desc">Your numbered PDF is compiled instantly client-side and downloaded.</p>
        </div>
      </div>
    </div>

    <!-- FAQ -->
    <div class="faq-section">
      <h3 class="faq-heading">Frequently Asked Questions</h3>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question">Can I skip numbering the title / cover page?</summary>
          <div class="faq-answer">Yes, select the "Skip Page 1" option under Cover Page Handling to leave the first page clean.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Does it support "Page X of Y" formatting?</summary>
          <div class="faq-answer">Yes, it automatically calculates the total page count and stamps dynamic "Page X of Y" or "X / Y" text.</div>
        </details>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    let currentFile = null;
    let originalPdfBytes = null;
    let selectedPosition = 'bottom-center';

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const numWorkspace = document.getElementById('numWorkspace');
    const processBtn = document.getElementById('processBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    // Position matrix buttons
    document.querySelectorAll('.pos-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.pos-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedPosition = btn.dataset.pos;
      }});
    }});

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{
      if (e.target !== selectBtn) fileInput.click();
    }});

    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{
      fileInput.value = '';
      fileInput.click();
    }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '40%';
      progressText.textContent = 'Loading document...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const count = pdfDoc.getPageCount();
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{count}} ${{count === 1 ? 'Page' : 'Pages'}}`;

        progressContainer.style.display = 'none';
        numWorkspace.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    processBtn.addEventListener('click', async () => {{
      numWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '20%';
      progressText.textContent = 'Applying page numbers...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const fontChoice = document.getElementById('fontFamily').value;
        let font;
        if (fontChoice === 'TimesRoman') font = await pdfDoc.embedFont(PDFLib.StandardFonts.TimesRoman);
        else if (fontChoice === 'Courier') font = await pdfDoc.embedFont(PDFLib.StandardFonts.Courier);
        else font = await pdfDoc.embedFont(PDFLib.StandardFonts.Helvetica);

        const fontSize = parseInt(document.getElementById('fontSize').value, 10);
        const format = document.getElementById('numFormat').value;
        const startNum = parseInt(document.getElementById('startNumber').value, 10) || 1;
        const skipFirst = document.getElementById('coverOption').value === 'skip_first';
        const colorVal = document.getElementById('fontColor').value;

        let textColor = PDFLib.rgb(0, 0, 0);
        if (colorVal === 'gray') textColor = PDFLib.rgb(0.28, 0.33, 0.41);
        else if (colorVal === 'blue') textColor = PDFLib.rgb(0.12, 0.25, 0.68);

        const pages = pdfDoc.getPages();
        const total = pages.length;

        for (let i = 0; i < total; i++) {{
          if (skipFirst && i === 0) continue;

          progressFill.style.width = `${{Math.round(20 + ((i + 1) / total) * 60)}}%`;
          const page = pages[i];
          const {{ width, height }} = page.getSize();
          const n = startNum + (skipFirst ? i - 1 : i);

          let textStr = '';
          if (format === 'p_of_n') textStr = `Page ${{n}} of ${{total}}`;
          else if (format === 'p_slash_n') textStr = `${{n}} / ${{total}}`;
          else if (format === 'page_n') textStr = `Page ${{n}}`;
          else if (format === 'num_only') textStr = `${{n}}`;
          else if (format === 'dash_n') textStr = `- ${{n}} -`;

          const textWidth = font.widthOfTextAtSize(textStr, fontSize);
          const margin = 28;

          let x = margin;
          let y = margin;

          if (selectedPosition.includes('center')) x = (width - textWidth) / 2;
          else if (selectedPosition.includes('right')) x = width - textWidth - margin;
          else if (selectedPosition.includes('left')) x = margin;

          if (selectedPosition.startsWith('top')) y = height - margin - fontSize;
          else y = margin;

          page.drawText(textStr, {{
            x: x,
            y: y,
            size: fontSize,
            font: font,
            color: textColor
          }});
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Saving PDF binary...';

        const pdfBytes = await pdfDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_numbered.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Numbered ${{total}} pages successfully. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error stamping page numbers: ' + err.message);
        progressContainer.style.display = 'none';
        numWorkspace.style.display = 'block';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      numWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/page-numbers.html', page_numbers_html)

print("Finished Crop and Page-Numbers.")
# ==========================================
# 3. WATERMARK PDF
# ==========================================
watermark_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Add Watermark to PDF Online Free — Text & Logo | DigitalSaathi</title>
  <meta name="description" content="Add text or image watermark to PDF documents online for free. Custom transparency, rotation, repeat patterns, and colors. 100% private in browser.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .watermark-tabs {{
      display: flex;
      gap: 12px;
      margin-bottom: 20px;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 8px;
    }}
    .wm-tab-btn {{
      background: none;
      border: none;
      font-size: 1rem;
      font-weight: 600;
      color: #64748b;
      padding: 8px 16px;
      cursor: pointer;
      border-radius: 6px;
      transition: all 0.2s;
    }}
    .wm-tab-btn.active {{
      background: #eff6ff;
      color: var(--primary);
    }}
    .wm-workspace-grid {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 24px;
      margin: 24px 0;
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .wm-workspace-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .wm-preview-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: var(--shadow-sm);
    }}
    .wm-controls-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 20px;
      box-shadow: var(--shadow-sm);
    }}
    #wmPreviewCanvas {{
      max-width: 100%;
      height: auto;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      background: #ffffff;
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
      <span>Watermark PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#ecfdf5;color:#059669;">💧</div>
      <h1 class="tool-title">Add Watermark to PDF</h1>
      <p class="tool-desc">Stamp text or custom image logos onto your PDF pages. Configure rotation, opacity, and repeat patterns with real-time preview.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">✍️ Text & Logo Stamps</span>
        <span class="badge badge-neutral">🔄 Diagonal Angle Controls</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Add confidential, draft, or branded copyright stamps</p>
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

    <!-- Workspace -->
    <div id="wmWorkspace" class="wm-workspace-grid" style="display:none;">
      <!-- Preview -->
      <div class="wm-preview-card">
        <h4 style="font-size:0.95rem;font-weight:700;margin-bottom:12px;color:#334155;">Live Preview (Page 1)</h4>
        <canvas id="wmPreviewCanvas"></canvas>
      </div>

      <!-- Controls -->
      <div class="wm-controls-card">
        <div class="watermark-tabs">
          <button class="wm-tab-btn active" id="tabTextBtn">Text Stamp</button>
          <button class="wm-tab-btn" id="tabImgBtn">Image Logo</button>
        </div>

        <!-- Text Tab Content -->
        <div id="textTabContent">
          <div class="form-group" style="margin-bottom:12px;">
            <label class="form-label" style="font-weight:600;">Watermark Text</label>
            <input type="text" id="wmText" class="form-input" value="CONFIDENTIAL" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
          </div>

          <div class="form-group" style="margin-bottom:12px;">
            <label class="form-label" style="font-weight:600;">Color Preset</label>
            <select id="wmColor" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
              <option value="red" selected>Crimson Red (#dc2626)</option>
              <option value="gray">Slate Gray (#64748b)</option>
              <option value="blue">Deep Blue (#1d4ed8)</option>
              <option value="black">Pure Black (#000000)</option>
            </select>
          </div>

          <div class="form-group" style="margin-bottom:12px;">
            <label class="form-label" style="font-weight:600;">Font Size (<span id="fontSizeVal">48</span> pt)</label>
            <input type="range" id="wmFontSize" min="16" max="96" value="48" style="width:100%;">
          </div>

          <div class="form-group" style="margin-bottom:12px;">
            <label class="form-label" style="font-weight:600;">Rotation (<span id="wmRotVal">45</span>°)</label>
            <input type="range" id="wmRotation" min="-90" max="90" value="45" style="width:100%;">
          </div>
        </div>

        <!-- Image Tab Content -->
        <div id="imgTabContent" style="display:none;">
          <div class="form-group" style="margin-bottom:12px;">
            <label class="form-label" style="font-weight:600;">Upload Watermark Logo (PNG/JPG)</label>
            <input type="file" id="wmImageInput" accept="image/*" class="form-input" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:6px;">
          </div>
          <div class="form-group" style="margin-bottom:12px;">
            <label class="form-label" style="font-weight:600;">Logo Scale (<span id="wmImgScaleVal">50</span>%)</label>
            <input type="range" id="wmImgScale" min="10" max="100" value="50" style="width:100%;">
          </div>
        </div>

        <!-- Common Controls -->
        <div class="form-group" style="margin-bottom:12px;">
          <label class="form-label" style="font-weight:600;">Opacity (<span id="wmOpacityVal">30</span>%)</label>
          <input type="range" id="wmOpacity" min="5" max="90" value="30" style="width:100%;">
        </div>

        <div class="form-group" style="margin-bottom:18px;">
          <label class="form-label" style="font-weight:600;">Layout Pattern</label>
          <select id="wmLayout" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
            <option value="center" selected>Single Center Stamp</option>
            <option value="repeat">Tiled 3x3 Repeat Grid</option>
          </select>
        </div>

        <button class="btn btn-primary" id="processWmBtn" style="width:100%;padding:12px;font-weight:700;font-size:1rem;">Apply Watermark & Download</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Stamping watermark... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">Watermark Applied Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your document is now stamped and protected.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="watermarked.pdf">⬇️ Download Watermarked PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Watermark Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Watermark PDF Files</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select your PDF document. The first page is rendered with a live preview.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Customize Stamp</h4>
          <p class="step-desc">Type your text or upload a logo, set angle, opacity, and choose single or repeating pattern.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Download File</h4>
          <p class="step-desc">Click Apply Watermark to export your protected PDF file instantly.</p>
        </div>
      </div>
    </div>

    <!-- FAQ -->
    <div class="faq-section">
      <h3 class="faq-heading">Frequently Asked Questions</h3>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question">Can I use transparent PNG logos?</summary>
          <div class="faq-answer">Yes, PNG files with transparent backgrounds are fully supported and will blend seamlessly with your document pages.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Will the watermark be applied to all pages?</summary>
          <div class="faq-answer">Yes, the watermark is stamped across every single page in the entire document.</div>
        </details>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    if (typeof pdfjsLib !== 'undefined') {{
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }}

    let currentFile = null;
    let originalPdfBytes = null;
    let baseCanvasImg = null;
    let activeMode = 'text'; // 'text' | 'image'
    let loadedLogoImg = null;

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const wmWorkspace = document.getElementById('wmWorkspace');
    const wmPreviewCanvas = document.getElementById('wmPreviewCanvas');
    const tabTextBtn = document.getElementById('tabTextBtn');
    const tabImgBtn = document.getElementById('tabImgBtn');
    const textTabContent = document.getElementById('textTabContent');
    const imgTabContent = document.getElementById('imgTabContent');
    const wmText = document.getElementById('wmText');
    const wmColor = document.getElementById('wmColor');
    const wmFontSize = document.getElementById('wmFontSize');
    const fontSizeVal = document.getElementById('fontSizeVal');
    const wmRotation = document.getElementById('wmRotation');
    const wmRotVal = document.getElementById('wmRotVal');
    const wmOpacity = document.getElementById('wmOpacity');
    const wmOpacityVal = document.getElementById('wmOpacityVal');
    const wmLayout = document.getElementById('wmLayout');
    const wmImageInput = document.getElementById('wmImageInput');
    const wmImgScale = document.getElementById('wmImgScale');
    const wmImgScaleVal = document.getElementById('wmImgScaleVal');
    const processWmBtn = document.getElementById('processWmBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    tabTextBtn.addEventListener('click', () => {{
      activeMode = 'text';
      tabTextBtn.classList.add('active');
      tabImgBtn.classList.remove('active');
      textTabContent.style.display = 'block';
      imgTabContent.style.display = 'none';
      drawPreview();
    }});

    tabImgBtn.addEventListener('click', () => {{
      activeMode = 'image';
      tabImgBtn.classList.add('active');
      tabTextBtn.classList.remove('active');
      imgTabContent.style.display = 'block';
      textTabContent.style.display = 'none';
      drawPreview();
    }});

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{
      if (e.target !== selectBtn) fileInput.click();
    }});

    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{
      fileInput.value = '';
      fileInput.click();
    }});

    wmImageInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) {{
        const reader = new FileReader();
        reader.onload = (ev) => {{
          const img = new Image();
          img.onload = () => {{
            loadedLogoImg = img;
            drawPreview();
          }};
          img.src = ev.target.result;
        }};
        reader.readAsDataURL(e.target.files[0]);
      }}
    }});

    [wmText, wmColor, wmLayout].forEach(el => el.addEventListener('input', drawPreview));
    wmFontSize.addEventListener('input', () => {{ fontSizeVal.textContent = wmFontSize.value; drawPreview(); }});
    wmRotation.addEventListener('input', () => {{ wmRotVal.textContent = wmRotation.value; drawPreview(); }});
    wmOpacity.addEventListener('input', () => {{ wmOpacityVal.textContent = wmOpacity.value; drawPreview(); }});
    wmImgScale.addEventListener('input', () => {{ wmImgScaleVal.textContent = wmImgScale.value; drawPreview(); }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Rendering preview...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        const pdfDocProxy = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes) }}).promise;
        const total = pdfDocProxy.numPages;
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{total}} ${{total === 1 ? 'Page' : 'Pages'}}`;

        const page = await pdfDocProxy.getPage(1);
        const viewport = page.getViewport({{ scale: 0.8 }});
        const offscreen = document.createElement('canvas');
        offscreen.width = viewport.width;
        offscreen.height = viewport.height;
        const offCtx = offscreen.getContext('2d');
        await page.render({{ canvasContext: offCtx, viewport: viewport }}).promise;

        baseCanvasImg = offscreen;
        wmPreviewCanvas.width = viewport.width;
        wmPreviewCanvas.height = viewport.height;

        progressContainer.style.display = 'none';
        wmWorkspace.style.display = 'grid';
        drawPreview();
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    function drawPreview() {{
      if (!baseCanvasImg) return;
      const ctx = wmPreviewCanvas.getContext('2d');
      ctx.clearRect(0, 0, wmPreviewCanvas.width, wmPreviewCanvas.height);
      ctx.drawImage(baseCanvasImg, 0, 0);

      const op = (parseInt(wmOpacity.value, 10) || 30) / 100;
      const rot = (parseInt(wmRotation.value, 10) || 0) * Math.PI / 180;
      const isRepeat = wmLayout.value === 'repeat';

      ctx.save();
      ctx.globalAlpha = op;

      if (activeMode === 'text') {{
        const text = wmText.value || 'WATERMARK';
        const size = parseInt(wmFontSize.value, 10) || 48;
        const color = wmColor.value;
        ctx.font = `bold ${{size}}px Inter, sans-serif`;
        ctx.fillStyle = color === 'red' ? '#dc2626' : (color === 'blue' ? '#1d4ed8' : (color === 'gray' ? '#64748b' : '#000000'));
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        if (isRepeat) {{
          const stepX = wmPreviewCanvas.width / 3;
          const stepY = wmPreviewCanvas.height / 3;
          for (let i = 0; i < 3; i++) {{
            for (let j = 0; j < 3; j++) {{
              ctx.save();
              ctx.translate((i + 0.5) * stepX, (j + 0.5) * stepY);
              ctx.rotate(rot);
              ctx.fillText(text, 0, 0);
              ctx.restore();
            }}
          }}
        }} else {{
          ctx.translate(wmPreviewCanvas.width / 2, wmPreviewCanvas.height / 2);
          ctx.rotate(rot);
          ctx.fillText(text, 0, 0);
        }}
      }} else if (activeMode === 'image' && loadedLogoImg) {{
        const scale = (parseInt(wmImgScale.value, 10) || 50) / 100;
        const targetW = (wmPreviewCanvas.width * 0.4) * scale;
        const targetH = (loadedLogoImg.height / loadedLogoImg.width) * targetW;

        if (isRepeat) {{
          const stepX = wmPreviewCanvas.width / 3;
          const stepY = wmPreviewCanvas.height / 3;
          for (let i = 0; i < 3; i++) {{
            for (let j = 0; j < 3; j++) {{
              ctx.drawImage(loadedLogoImg, (i + 0.5) * stepX - targetW / 2, (j + 0.5) * stepY - targetH / 2, targetW, targetH);
            }}
          }}
        }} else {{
          ctx.drawImage(loadedLogoImg, (wmPreviewCanvas.width - targetW) / 2, (wmPreviewCanvas.height - targetH) / 2, targetW, targetH);
        }}
      }}
      ctx.restore();
    }}

    processWmBtn.addEventListener('click', async () => {{
      wmWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '20%';
      progressText.textContent = 'Stamping watermark on document...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const pages = pdfDoc.getPages();
        const total = pages.length;

        const opacity = (parseInt(wmOpacity.value, 10) || 30) / 100;
        const rotDeg = parseInt(wmRotation.value, 10) || 0;
        const isRepeat = wmLayout.value === 'repeat';

        let font = null;
        let embeddedImg = null;

        if (activeMode === 'text') {{
          font = await pdfDoc.embedFont(PDFLib.StandardFonts.HelveticaBold);
        }} else if (activeMode === 'image' && loadedLogoImg) {{
          const imgBytes = await (await fetch(loadedLogoImg.src)).arrayBuffer();
          if (loadedLogoImg.src.startsWith('data:image/png')) {{
            embeddedImg = await pdfDoc.embedPng(imgBytes);
          }} else {{
            embeddedImg = await pdfDoc.embedJpg(imgBytes);
          }}
        }}

        for (let idx = 0; idx < total; idx++) {{
          progressFill.style.width = `${{Math.round(20 + ((idx + 1) / total) * 60)}}%`;
          const page = pages[idx];
          const {{ width, height }} = page.getSize();

          if (activeMode === 'text') {{
            const text = wmText.value || 'WATERMARK';
            const size = parseInt(wmFontSize.value, 10) || 48;
            const color = wmColor.value;
            let c = PDFLib.rgb(0.86, 0.15, 0.15);
            if (color === 'gray') c = PDFLib.rgb(0.39, 0.45, 0.54);
            else if (color === 'blue') c = PDFLib.rgb(0.11, 0.31, 0.85);
            else if (color === 'black') c = PDFLib.rgb(0, 0, 0);

            const textWidth = font.widthOfTextAtSize(text, size);
            const textHeight = font.heightAtSize(size);

            if (isRepeat) {{
              const stepX = width / 3;
              const stepY = height / 3;
              for (let i = 0; i < 3; i++) {{
                for (let j = 0; j < 3; j++) {{
                  page.drawText(text, {{
                    x: (i + 0.5) * stepX - (textWidth / 2),
                    y: (j + 0.5) * stepY - (textHeight / 2),
                    size: size,
                    font: font,
                    color: c,
                    opacity: opacity,
                    rotate: PDFLib.degrees(rotDeg)
                  }});
                }}
              }}
            }} else {{
              page.drawText(text, {{
                x: (width - textWidth) / 2,
                y: (height - textHeight) / 2,
                size: size,
                font: font,
                color: c,
                opacity: opacity,
                rotate: PDFLib.degrees(rotDeg)
              }});
            }}
          }} else if (embeddedImg) {{
            const scale = (parseInt(wmImgScale.value, 10) || 50) / 100;
            const targetW = (width * 0.4) * scale;
            const targetH = (embeddedImg.height / embeddedImg.width) * targetW;

            if (isRepeat) {{
              const stepX = width / 3;
              const stepY = height / 3;
              for (let i = 0; i < 3; i++) {{
                for (let j = 0; j < 3; j++) {{
                  page.drawImage(embeddedImg, {{
                    x: (i + 0.5) * stepX - targetW / 2,
                    y: (j + 0.5) * stepY - targetH / 2,
                    width: targetW,
                    height: targetH,
                    opacity: opacity
                  }});
                }}
              }}
            }} else {{
              page.drawImage(embeddedImg, {{
                x: (width - targetW) / 2,
                y: (height - targetH) / 2,
                width: targetW,
                height: targetH,
                opacity: opacity
              }});
            }}
          }}
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Saving stamped PDF...';

        const pdfBytes = await pdfDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_watermarked.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Watermark stamped on all ${{total}} pages. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error applying watermark: ' + err.message);
        progressContainer.style.display = 'none';
        wmWorkspace.style.display = 'grid';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      wmWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/watermark.html', watermark_html)

# ==========================================
# 4. SIGN PDF
# ==========================================
sign_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sign PDF Online Free — Draw, Type or Upload Signature | DigitalSaathi</title>
  <meta name="description" content="Sign PDF documents online for free. Draw your digital signature with mouse/touch, type with cursive handwriting fonts, or upload signature image. 100% private.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Inter:wght@400;500;600;700;800&family=Pacifico&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .sign-workspace {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 24px;
      margin: 24px 0;
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .sign-workspace {{
        grid-template-columns: 1fr;
      }}
    }}
    .sign-preview-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: var(--shadow-sm);
    }}
    .pdf-stage-container {{
      position: relative;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: crosshair;
    }}
    #pdfStageCanvas {{
      display: block;
      max-width: 100%;
      height: auto;
    }}
    .sign-placed-box {{
      position: absolute;
      border: 2px dashed #2563eb;
      background: rgba(37, 99, 235, 0.08);
      cursor: move;
      user-select: none;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .sign-placed-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      pointer-events: none;
    }}
    .sign-pad-container {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      background: #ffffff;
      margin: 10px 0;
      position: relative;
    }}
    #signCanvas {{
      display: block;
      width: 100%;
      height: 160px;
      cursor: crosshair;
      border-radius: 6px;
    }}
    .cursive-preview {{
      font-size: 2rem;
      text-align: center;
      padding: 16px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      margin: 10px 0;
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
      <span>Sign PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#eff6ff;color:#2563eb;">✍️</div>
      <h1 class="tool-title">Sign PDF Document</h1>
      <p class="tool-desc">Draw, type, or upload your signature and place it anywhere on your PDF. 100% private, legally styled, and client-side processed.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">✍️ Draw / Type / Upload</span>
        <span class="badge badge-neutral">⚡ Instant Placement</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Add signatures to job applications, agreements, or affidavits</p>
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

    <!-- Workspace -->
    <div id="signWorkspace" class="sign-workspace" style="display:none;">
      <!-- PDF Preview Page -->
      <div class="sign-preview-card">
        <div style="display:flex;justify-content:space-between;width:100%;align-items:center;margin-bottom:12px;">
          <button class="btn btn-sm btn-outline" id="prevPageBtn">◀ Prev Page</button>
          <span style="font-weight:600;font-size:0.9rem;" id="pageIndicator">Page 1 of 1</span>
          <button class="btn btn-sm btn-outline" id="nextPageBtn">Next Page ▶</button>
        </div>
        <p style="font-size:0.8rem;color:#64748b;margin-bottom:8px;">💡 Click anywhere on the document to position your signature, then drag to adjust.</p>
        <div class="pdf-stage-container" id="stageContainer">
          <canvas id="pdfStageCanvas"></canvas>
          <div id="placedSignBox" class="sign-placed-box" style="display:none;">
            <img id="placedSignImg" src="" alt="Signature">
          </div>
        </div>
      </div>

      <!-- Signature Creator Controls -->
      <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:20px;box-shadow:var(--shadow-sm);">
        <h3 style="font-size:1.15rem;font-weight:700;color:#1e293b;margin-bottom:14px;">1. Create Signature</h3>
        
        <div style="display:flex;gap:6px;margin-bottom:12px;border-bottom:2px solid #f1f5f9;padding-bottom:8px;">
          <button class="btn btn-sm btn-primary" id="modeDrawBtn">✍️ Draw</button>
          <button class="btn btn-sm btn-outline" id="modeTypeBtn">⌨️ Type</button>
          <button class="btn btn-sm btn-outline" id="modeUploadBtn">📁 Upload</button>
        </div>

        <!-- DRAW MODE -->
        <div id="drawSection">
          <div class="sign-pad-container">
            <canvas id="signCanvas"></canvas>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px;">
            <div style="display:flex;gap:8px;align-items:center;">
              <span style="font-size:0.8rem;font-weight:600;">Ink:</span>
              <button class="btn btn-sm" id="inkBlue" style="background:#1e40af;color:#fff;padding:2px 8px;border-radius:4px;">Blue</button>
              <button class="btn btn-sm" id="inkBlack" style="background:#000000;color:#fff;padding:2px 8px;border-radius:4px;">Black</button>
            </div>
            <button class="btn btn-sm btn-outline" id="clearPadBtn">Clear</button>
          </div>
        </div>

        <!-- TYPE MODE -->
        <div id="typeSection" style="display:none;">
          <input type="text" id="typeInput" class="form-input" placeholder="Type your full name" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;margin-bottom:8px;">
          <select id="typeFont" class="form-select" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;margin-bottom:8px;">
            <option value="'Caveat', cursive">Style 1: Caveat Elegant</option>
            <option value="'Pacifico', cursive">Style 2: Pacifico Bold</option>
          </select>
          <div class="cursive-preview" id="cursivePreview" style="font-family:'Caveat', cursive;color:#1e40af;">Your Name</div>
        </div>

        <!-- UPLOAD MODE -->
        <div id="uploadSection" style="display:none;">
          <input type="file" id="signImgFile" accept="image/*" class="form-input" style="width:100%;padding:8px;border:1px solid #cbd5e1;border-radius:6px;">
          <p style="font-size:0.75rem;color:#64748b;margin-top:4px;">Supports PNG, JPG, JPEG with auto background transparency.</p>
        </div>

        <h3 style="font-size:1.15rem;font-weight:700;color:#1e293b;margin:20px 0 12px;">2. Signature Size</h3>
        <div class="form-group" style="margin-bottom:16px;">
          <label class="form-label" style="font-size:0.85rem;font-weight:600;">Size (<span id="signSizeVal">140</span> px)</label>
          <input type="range" id="signSizeSlider" min="60" max="300" value="140" style="width:100%;">
        </div>

        <button class="btn btn-primary" id="burnSignBtn" style="width:100%;padding:12px;font-weight:700;font-size:1rem;">Sign & Download PDF</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Embedding signature... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Signed Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your signature has been burned securely into the document.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="signed.pdf">⬇️ Download Signed PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Sign Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Digitally Sign a PDF</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select your PDF document.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Create Signature</h4>
          <p class="step-desc">Draw with touch/mouse, type cursive letters, or upload a photo of your signature.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Position & Burn</h4>
          <p class="step-desc">Click on document to place, drag to position, and download your signed PDF.</p>
        </div>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    if (typeof pdfjsLib !== 'undefined') {{
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }}

    let currentFile = null;
    let originalPdfBytes = null;
    let pdfDocProxy = null;
    let totalPages = 1;
    let currentPageNum = 1;
    let activeMethod = 'draw'; // 'draw' | 'type' | 'upload'
    let inkColor = '#1e40af';
    let isDrawing = false;
    let placedSignData = null; // {{ pageNum, xRatio, yRatio, widthRatio, heightRatio, pngDataUrl }}

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const signWorkspace = document.getElementById('signWorkspace');
    const pdfStageCanvas = document.getElementById('pdfStageCanvas');
    const stageContainer = document.getElementById('stageContainer');
    const placedSignBox = document.getElementById('placedSignBox');
    const placedSignImg = document.getElementById('placedSignImg');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const pageIndicator = document.getElementById('pageIndicator');
    const signCanvas = document.getElementById('signCanvas');
    const signCtx = signCanvas.getContext('2d');
    const modeDrawBtn = document.getElementById('modeDrawBtn');
    const modeTypeBtn = document.getElementById('modeTypeBtn');
    const modeUploadBtn = document.getElementById('modeUploadBtn');
    const drawSection = document.getElementById('drawSection');
    const typeSection = document.getElementById('typeSection');
    const uploadSection = document.getElementById('uploadSection');
    const typeInput = document.getElementById('typeInput');
    const typeFont = document.getElementById('typeFont');
    const cursivePreview = document.getElementById('cursivePreview');
    const signImgFile = document.getElementById('signImgFile');
    const signSizeSlider = document.getElementById('signSizeSlider');
    const signSizeVal = document.getElementById('signSizeVal');
    const clearPadBtn = document.getElementById('clearPadBtn');
    const inkBlue = document.getElementById('inkBlue');
    const inkBlack = document.getElementById('inkBlack');
    const burnSignBtn = document.getElementById('burnSignBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    // Init canvas pad
    function resizePad() {{
      const rect = signCanvas.getBoundingClientRect();
      signCanvas.width = rect.width || 300;
      signCanvas.height = 160;
      signCtx.strokeStyle = inkColor;
      signCtx.lineWidth = 2.5;
      signCtx.lineCap = 'round';
      signCtx.lineJoin = 'round';
    }}

    modeDrawBtn.addEventListener('click', () => {{
      activeMethod = 'draw';
      modeDrawBtn.className = 'btn btn-sm btn-primary';
      modeTypeBtn.className = 'btn btn-sm btn-outline';
      modeUploadBtn.className = 'btn btn-sm btn-outline';
      drawSection.style.display = 'block';
      typeSection.style.display = 'none';
      uploadSection.style.display = 'none';
      resizePad();
    }});

    modeTypeBtn.addEventListener('click', () => {{
      activeMethod = 'type';
      modeTypeBtn.className = 'btn btn-sm btn-primary';
      modeDrawBtn.className = 'btn btn-sm btn-outline';
      modeUploadBtn.className = 'btn btn-sm btn-outline';
      typeSection.style.display = 'block';
      drawSection.style.display = 'none';
      uploadSection.style.display = 'none';
    }});

    modeUploadBtn.addEventListener('click', () => {{
      activeMethod = 'upload';
      modeUploadBtn.className = 'btn btn-sm btn-primary';
      modeDrawBtn.className = 'btn btn-sm btn-outline';
      modeTypeBtn.className = 'btn btn-sm btn-outline';
      uploadSection.style.display = 'block';
      drawSection.style.display = 'none';
      typeSection.style.display = 'none';
    }});

    inkBlue.addEventListener('click', () => {{ inkColor = '#1e40af'; signCtx.strokeStyle = inkColor; cursivePreview.style.color = inkColor; }});
    inkBlack.addEventListener('click', () => {{ inkColor = '#000000'; signCtx.strokeStyle = inkColor; cursivePreview.style.color = inkColor; }});
    clearPadBtn.addEventListener('click', () => signCtx.clearRect(0, 0, signCanvas.width, signCanvas.height));

    // Pad Drawing Listeners
    function getPadPos(e) {{
      const rect = signCanvas.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {{ x: clientX - rect.left, y: clientY - rect.top }};
    }}

    signCanvas.addEventListener('mousedown', (e) => {{
      isDrawing = true;
      const pos = getPadPos(e);
      signCtx.beginPath();
      signCtx.moveTo(pos.x, pos.y);
    }});
    signCanvas.addEventListener('mousemove', (e) => {{
      if (!isDrawing) return;
      const pos = getPadPos(e);
      signCtx.lineTo(pos.x, pos.y);
      signCtx.stroke();
    }});
    window.addEventListener('mouseup', () => isDrawing = false);

    signCanvas.addEventListener('touchstart', (e) => {{
      e.preventDefault();
      isDrawing = true;
      const pos = getPadPos(e);
      signCtx.beginPath();
      signCtx.moveTo(pos.x, pos.y);
    }}, {{ passive: false }});
    signCanvas.addEventListener('touchmove', (e) => {{
      e.preventDefault();
      if (!isDrawing) return;
      const pos = getPadPos(e);
      signCtx.lineTo(pos.x, pos.y);
      signCtx.stroke();
    }}, {{ passive: false }});

    typeInput.addEventListener('input', () => {{
      cursivePreview.textContent = typeInput.value || 'Your Name';
    }});
    typeFont.addEventListener('change', () => {{
      cursivePreview.style.fontFamily = typeFont.value;
    }});

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{ if (e.target !== selectBtn) fileInput.click(); }});
    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{ fileInput.value = ''; fileInput.click(); }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Rendering PDF stage...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        pdfDocProxy = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes) }}).promise;
        totalPages = pdfDocProxy.numPages;
        currentPageNum = 1;
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{totalPages}} ${{totalPages === 1 ? 'Page' : 'Pages'}}`;

        progressContainer.style.display = 'none';
        signWorkspace.style.display = 'grid';
        resizePad();
        await renderStagePage();
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    async function renderStagePage() {{
      if (!pdfDocProxy) return;
      pageIndicator.textContent = `Page ${{currentPageNum}} of ${{totalPages}}`;
      prevPageBtn.disabled = currentPageNum <= 1;
      nextPageBtn.disabled = currentPageNum >= totalPages;

      const page = await pdfDocProxy.getPage(currentPageNum);
      const viewport = page.getViewport({{ scale: 1.0 }});
      const ctx = pdfStageCanvas.getContext('2d');
      pdfStageCanvas.width = viewport.width;
      pdfStageCanvas.height = viewport.height;
      await page.render({{ canvasContext: ctx, viewport: viewport }}).promise;

      if (placedSignData && placedSignData.pageNum === currentPageNum) {{
        placedSignBox.style.display = 'flex';
      }} else {{
        placedSignBox.style.display = 'none';
      }}
    }}

    prevPageBtn.addEventListener('click', () => {{ if (currentPageNum > 1) {{ currentPageNum--; renderStagePage(); }} }});
    nextPageBtn.addEventListener('click', () => {{ if (currentPageNum < totalPages) {{ currentPageNum++; renderStagePage(); }} }});

    function generateSignaturePngData() {{
      if (activeMethod === 'draw') {{
        return signCanvas.toDataURL('image/png');
      }} else if (activeMethod === 'type') {{
        const temp = document.createElement('canvas');
        temp.width = 400;
        temp.height = 160;
        const tCtx = temp.getContext('2d');
        tCtx.font = `64px ${{typeFont.value.includes('Pacifico') ? "'Pacifico', cursive" : "'Caveat', cursive"}}`;
        tCtx.fillStyle = inkColor;
        tCtx.textAlign = 'center';
        tCtx.textBaseline = 'middle';
        tCtx.fillText(typeInput.value || 'Your Name', 200, 80);
        return temp.toDataURL('image/png');
      }} else if (activeMethod === 'upload' && signImgFile.files && signImgFile.files[0]) {{
        return placedSignImg.src;
      }}
      return null;
    }}

    signImgFile.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files[0]) {{
        const reader = new FileReader();
        reader.onload = (ev) => {{
          placedSignImg.src = ev.target.result;
        }};
        reader.readAsDataURL(e.target.files[0]);
      }}
    }});

    stageContainer.addEventListener('click', (e) => {{
      if (e.target === placedSignBox || placedSignBox.contains(e.target)) return;

      const rect = stageContainer.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;

      const png = generateSignaturePngData();
      if (!png && activeMethod !== 'upload') {{
        alert('Please draw or type a signature first!');
        return;
      }}

      if (png) placedSignImg.src = png;

      const widthPx = parseInt(signSizeSlider.value, 10);
      const heightPx = widthPx * 0.45;

      placedSignBox.style.width = widthPx + 'px';
      placedSignBox.style.height = heightPx + 'px';
      placedSignBox.style.left = (clickX - widthPx / 2) + 'px';
      placedSignBox.style.top = (clickY - heightPx / 2) + 'px';
      placedSignBox.style.display = 'flex';

      placedSignData = {{
        pageNum: currentPageNum,
        x: clickX - widthPx / 2,
        y: clickY - heightPx / 2,
        width: widthPx,
        height: heightPx,
        canvasW: pdfStageCanvas.clientWidth,
        canvasH: pdfStageCanvas.clientHeight,
        pngDataUrl: png || placedSignImg.src
      }};
    }});

    signSizeSlider.addEventListener('input', () => {{
      signSizeVal.textContent = signSizeSlider.value;
      if (placedSignBox.style.display !== 'none') {{
        const widthPx = parseInt(signSizeSlider.value, 10);
        const heightPx = widthPx * 0.45;
        placedSignBox.style.width = widthPx + 'px';
        placedSignBox.style.height = heightPx + 'px';
        if (placedSignData) {{
          placedSignData.width = widthPx;
          placedSignData.height = heightPx;
        }}
      }}
    }});

    burnSignBtn.addEventListener('click', async () => {{
      if (!placedSignData || !placedSignData.pngDataUrl) {{
        alert('Please click on the document to place your signature first!');
        return;
      }}

      signWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Burning signature into PDF...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const pages = pdfDoc.getPages();
        const targetPage = pages[placedSignData.pageNum - 1];
        const {{ width: pdfPageW, height: pdfPageH }} = targetPage.getSize();

        const imgBytes = await (await fetch(placedSignData.pngDataUrl)).arrayBuffer();
        const embeddedImg = await pdfDoc.embedPng(imgBytes);

        // Map screen canvas pixels to PDF point dimensions
        const scaleX = pdfPageW / placedSignData.canvasW;
        const scaleY = pdfPageH / placedSignData.canvasH;

        const drawX = placedSignData.x * scaleX;
        const drawY = pdfPageH - ((placedSignData.y + placedSignData.height) * scaleY);
        const drawW = placedSignData.width * scaleX;
        const drawH = placedSignData.height * scaleY;

        targetPage.drawImage(embeddedImg, {{
          x: drawX,
          y: drawY,
          width: drawW,
          height: drawH
        }});

        progressFill.style.width = '90%';
        progressText.textContent = 'Saving signed PDF binary...';

        const pdfBytes = await pdfDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_signed.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Signature embedded on page ${{placedSignData.pageNum}}. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error embedding signature: ' + err.message);
        progressContainer.style.display = 'none';
        signWorkspace.style.display = 'grid';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      signWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
      placedSignData = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/sign.html', sign_html)
print("Finished Watermark and Sign tools.")
# ==========================================
# 5. EDIT PDF
# ==========================================
edit_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Edit PDF Online Free — Annotate, Add Text & Draw | DigitalSaathi</title>
  <meta name="description" content="Edit PDF documents online for free. Add text, draw with pen, highlight lines, erase mistakes with whiteout, and insert shapes. 100% private in browser.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .editor-toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      background: #f8fafc;
      padding: 10px 16px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      margin-bottom: 16px;
    }}
    .tool-btn {{
      padding: 6px 12px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .tool-btn:hover {{
      background: #f1f5f9;
      border-color: #94a3b8;
    }}
    .tool-btn.active {{
      background: #eff6ff;
      border-color: var(--primary);
      color: var(--primary);
      box-shadow: 0 0 0 2px rgba(37,99,235,0.15);
    }}
    .canvas-stage-wrapper {{
      position: relative;
      background: #e2e8f0;
      padding: 20px;
      border-radius: 8px;
      display: flex;
      justify-content: center;
      overflow: auto;
      max-height: 75vh;
    }}
    .canvas-container-stack {{
      position: relative;
      background: #ffffff;
      box-shadow: var(--shadow-md);
      border-radius: 4px;
    }}
    #pdfBgCanvas {{
      display: block;
    }}
    #drawingCanvas {{
      position: absolute;
      top: 0;
      left: 0;
      cursor: crosshair;
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
      <span>Edit PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#eff6ff;color:#2563eb;">✏️</div>
      <h1 class="tool-title">Edit PDF Document</h1>
      <p class="tool-desc">Annotate, add text, draw freehand, highlight content, or whiteout mistakes directly on your PDF pages. 100% private in browser.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">✏️ Pen & Highlighter</span>
        <span class="badge badge-neutral">🔤 Add Custom Text</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Add text, annotations, signatures, and drawings directly to PDF</p>
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

    <!-- Workspace -->
    <div id="editorWorkspace" style="display:none;margin:24px 0;">
      <!-- Toolbar -->
      <div class="editor-toolbar">
        <button class="tool-btn active" data-tool="pen">✏️ Pen</button>
        <button class="tool-btn" data-tool="highlight">🖍️ Highlight</button>
        <button class="tool-btn" data-tool="text">🔤 Text</button>
        <button class="tool-btn" data-tool="whiteout">⬜ Whiteout</button>
        <button class="tool-btn" data-tool="rectangle">⬛ Rectangle</button>

        <div style="height:24px;width:1px;background:#cbd5e1;margin:0 4px;"></div>

        <span style="font-size:0.8rem;font-weight:600;">Color:</span>
        <input type="color" id="toolColor" value="#2563eb" style="width:32px;height:32px;border:none;border-radius:4px;cursor:pointer;padding:0;">

        <span style="font-size:0.8rem;font-weight:600;">Size:</span>
        <select id="toolSize" class="form-select" style="padding:4px 8px;border:1px solid #cbd5e1;border-radius:4px;">
          <option value="2">Fine (2px)</option>
          <option value="4" selected>Medium (4px)</option>
          <option value="8">Bold (8px)</option>
          <option value="16">Thick (16px)</option>
        </select>

        <div style="height:24px;width:1px;background:#cbd5e1;margin:0 4px;"></div>

        <button class="tool-btn" id="undoBtn">↩️ Undo</button>
        <button class="tool-btn" id="clearPageBtn">🗑️ Clear Page</button>

        <div style="margin-left:auto;display:flex;gap:8px;align-items:center;">
          <button class="btn btn-sm btn-outline" id="prevPageBtn">◀ Prev</button>
          <span style="font-size:0.85rem;font-weight:600;" id="pageIndicator">1 / 1</span>
          <button class="btn btn-sm btn-outline" id="nextPageBtn">Next ▶</button>
          <button class="btn btn-sm btn-primary" id="savePdfBtn">Save & Download</button>
        </div>
      </div>

      <!-- Stage -->
      <div class="canvas-stage-wrapper">
        <div class="canvas-container-stack" id="stageStack">
          <canvas id="pdfBgCanvas"></canvas>
          <canvas id="drawingCanvas"></canvas>
        </div>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Saving edited PDF... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Edited Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your annotations and text have been merged into the document.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="edited.pdf">⬇️ Download Edited PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Edit Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Edit PDF Files</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select or drop your PDF document.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Annotate & Draw</h4>
          <p class="step-desc">Select pen, highlighter, text, or whiteout tool and draw directly on the canvas.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Export PDF</h4>
          <p class="step-desc">Click Save & Download to export your clean, annotated PDF document.</p>
        </div>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    if (typeof pdfjsLib !== 'undefined') {{
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }}

    let currentFile = null;
    let originalPdfBytes = null;
    let pdfDocProxy = null;
    let totalPages = 1;
    let currentPageNum = 1;
    let activeTool = 'pen'; // 'pen', 'highlight', 'text', 'whiteout', 'rectangle'
    let isDrawing = false;
    let startX = 0, startY = 0;
    let pageDrawings = {{}}; // {{ [pageNum]: [drawingCommands] }}
    let currentPath = [];

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const editorWorkspace = document.getElementById('editorWorkspace');
    const pdfBgCanvas = document.getElementById('pdfBgCanvas');
    const drawingCanvas = document.getElementById('drawingCanvas');
    const drawCtx = drawingCanvas.getContext('2d');
    const toolColor = document.getElementById('toolColor');
    const toolSize = document.getElementById('toolSize');
    const undoBtn = document.getElementById('undoBtn');
    const clearPageBtn = document.getElementById('clearPageBtn');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const pageIndicator = document.getElementById('pageIndicator');
    const savePdfBtn = document.getElementById('savePdfBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    // Tool switcher
    document.querySelectorAll('.tool-btn[data-tool]').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.tool-btn[data-tool]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeTool = btn.dataset.tool;
      }});
    }});

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{ if (e.target !== selectBtn) fileInput.click(); }});
    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{ fileInput.value = ''; fileInput.click(); }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Opening editor...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        pdfDocProxy = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes) }}).promise;
        totalPages = pdfDocProxy.numPages;
        currentPageNum = 1;
        pageDrawings = {{}};
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{totalPages}} ${{totalPages === 1 ? 'Page' : 'Pages'}}`;

        progressContainer.style.display = 'none';
        editorWorkspace.style.display = 'block';
        await renderPage();
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    async function renderPage() {{
      if (!pdfDocProxy) return;
      pageIndicator.textContent = `${{currentPageNum}} / ${{totalPages}}`;
      prevPageBtn.disabled = currentPageNum <= 1;
      nextPageBtn.disabled = currentPageNum >= totalPages;

      const page = await pdfDocProxy.getPage(currentPageNum);
      const viewport = page.getViewport({{ scale: 1.2 }});
      const bgCtx = pdfBgCanvas.getContext('2d');

      pdfBgCanvas.width = viewport.width;
      pdfBgCanvas.height = viewport.height;
      drawingCanvas.width = viewport.width;
      drawingCanvas.height = viewport.height;

      await page.render({{ canvasContext: bgCtx, viewport: viewport }}).promise;
      redrawPageDrawings();
    }}

    function redrawPageDrawings() {{
      drawCtx.clearRect(0, 0, drawingCanvas.width, drawingCanvas.height);
      const items = pageDrawings[currentPageNum] || [];
      items.forEach(cmd => {{
        drawCtx.save();
        if (cmd.type === 'pen' || cmd.type === 'highlight') {{
          drawCtx.strokeStyle = cmd.color;
          drawCtx.lineWidth = cmd.size;
          drawCtx.lineCap = 'round';
          drawCtx.lineJoin = 'round';
          if (cmd.type === 'highlight') drawCtx.globalAlpha = 0.4;
          drawCtx.beginPath();
          cmd.points.forEach((pt, idx) => {{
            if (idx === 0) drawCtx.moveTo(pt.x, pt.y);
            else drawCtx.lineTo(pt.x, pt.y);
          }});
          drawCtx.stroke();
        }} else if (cmd.type === 'whiteout') {{
          drawCtx.fillStyle = '#ffffff';
          drawCtx.fillRect(cmd.x, cmd.y, cmd.w, cmd.h);
        }} else if (cmd.type === 'rectangle') {{
          drawCtx.strokeStyle = cmd.color;
          drawCtx.lineWidth = cmd.size;
          drawCtx.strokeRect(cmd.x, cmd.y, cmd.w, cmd.h);
        }} else if (cmd.type === 'text') {{
          drawCtx.font = `${{cmd.size * 3}}px Inter, sans-serif`;
          drawCtx.fillStyle = cmd.color;
          drawCtx.fillText(cmd.text, cmd.x, cmd.y);
        }}
        drawCtx.restore();
      }});
    }}

    function getCanvasPos(e) {{
      const rect = drawingCanvas.getBoundingClientRect();
      const scaleX = drawingCanvas.width / rect.width;
      const scaleY = drawingCanvas.height / rect.height;
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {{
        x: (clientX - rect.left) * scaleX,
        y: (clientY - rect.top) * scaleY
      }};
    }}

    drawingCanvas.addEventListener('mousedown', (e) => {{
      const pos = getCanvasPos(e);
      startX = pos.x;
      startY = pos.y;
      isDrawing = true;

      if (activeTool === 'pen' || activeTool === 'highlight') {{
        currentPath = [pos];
      }} else if (activeTool === 'text') {{
        isDrawing = false;
        const text = prompt('Enter text to insert:');
        if (text) {{
          if (!pageDrawings[currentPageNum]) pageDrawings[currentPageNum] = [];
          pageDrawings[currentPageNum].push({{
            type: 'text',
            text: text,
            x: pos.x,
            y: pos.y,
            color: toolColor.value,
            size: parseInt(toolSize.value, 10)
          }});
          redrawPageDrawings();
        }}
      }}
    }});

    drawingCanvas.addEventListener('mousemove', (e) => {{
      if (!isDrawing) return;
      const pos = getCanvasPos(e);

      if (activeTool === 'pen' || activeTool === 'highlight') {{
        currentPath.push(pos);
        drawCtx.save();
        drawCtx.strokeStyle = toolColor.value;
        drawCtx.lineWidth = parseInt(toolSize.value, 10) * (activeTool === 'highlight' ? 3 : 1);
        drawCtx.lineCap = 'round';
        drawCtx.lineJoin = 'round';
        if (activeTool === 'highlight') drawCtx.globalAlpha = 0.4;
        drawCtx.beginPath();
        const prev = currentPath[currentPath.length - 2];
        drawCtx.moveTo(prev.x, prev.y);
        drawCtx.lineTo(pos.x, pos.y);
        drawCtx.stroke();
        drawCtx.restore();
      }} else if (activeTool === 'whiteout' || activeTool === 'rectangle') {{
        redrawPageDrawings();
        drawCtx.save();
        if (activeTool === 'whiteout') {{
          drawCtx.fillStyle = '#ffffff';
          drawCtx.fillRect(startX, startY, pos.x - startX, pos.y - startY);
        }} else {{
          drawCtx.strokeStyle = toolColor.value;
          drawCtx.lineWidth = parseInt(toolSize.value, 10);
          drawCtx.strokeRect(startX, startY, pos.x - startX, pos.y - startY);
        }}
        drawCtx.restore();
      }}
    }});

    window.addEventListener('mouseup', (e) => {{
      if (!isDrawing) return;
      isDrawing = false;
      const pos = getCanvasPos(e);

      if (!pageDrawings[currentPageNum]) pageDrawings[currentPageNum] = [];

      if (activeTool === 'pen' || activeTool === 'highlight') {{
        if (currentPath.length > 1) {{
          pageDrawings[currentPageNum].push({{
            type: activeTool,
            points: currentPath,
            color: toolColor.value,
            size: parseInt(toolSize.value, 10) * (activeTool === 'highlight' ? 3 : 1)
          }});
        }}
      }} else if (activeTool === 'whiteout') {{
        pageDrawings[currentPageNum].push({{
          type: 'whiteout',
          x: Math.min(startX, pos.x),
          y: Math.min(startY, pos.y),
          w: Math.abs(pos.x - startX),
          h: Math.abs(pos.y - startY)
        }});
      }} else if (activeTool === 'rectangle') {{
        pageDrawings[currentPageNum].push({{
          type: 'rectangle',
          x: Math.min(startX, pos.x),
          y: Math.min(startY, pos.y),
          w: Math.abs(pos.x - startX),
          h: Math.abs(pos.y - startY),
          color: toolColor.value,
          size: parseInt(toolSize.value, 10)
        }});
      }}
      redrawPageDrawings();
    }});

    undoBtn.addEventListener('click', () => {{
      if (pageDrawings[currentPageNum] && pageDrawings[currentPageNum].length > 0) {{
        pageDrawings[currentPageNum].pop();
        redrawPageDrawings();
      }}
    }});

    clearPageBtn.addEventListener('click', () => {{
      if (confirm('Clear all annotations on this page?')) {{
        pageDrawings[currentPageNum] = [];
        redrawPageDrawings();
      }}
    }});

    prevPageBtn.addEventListener('click', () => {{ if (currentPageNum > 1) {{ currentPageNum--; renderPage(); }} }});
    nextPageBtn.addEventListener('click', () => {{ if (currentPageNum < totalPages) {{ currentPageNum++; renderPage(); }} }});

    savePdfBtn.addEventListener('click', async () => {{
      editorWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '20%';
      progressText.textContent = 'Saving annotations into PDF...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const pages = pdfDoc.getPages();

        for (let pNum = 1; pNum <= pages.length; pNum++) {{
          const items = pageDrawings[pNum];
          if (!items || items.length === 0) continue;

          progressFill.style.width = `${{Math.round(20 + (pNum / pages.length) * 60)}}%`;
          progressText.textContent = `Processing page ${{pNum}} annotations...`;

          const page = pages[pNum - 1];
          const {{ width: pdfW, height: pdfH }} = page.getSize();

          // Render overlay items to temporary canvas to get clean PNG overlay
          const tempCanvas = document.createElement('canvas');
          tempCanvas.width = drawingCanvas.width;
          tempCanvas.height = drawingCanvas.height;
          const tCtx = tempCanvas.getContext('2d');

          items.forEach(cmd => {{
            tCtx.save();
            if (cmd.type === 'pen' || cmd.type === 'highlight') {{
              tCtx.strokeStyle = cmd.color;
              tCtx.lineWidth = cmd.size;
              tCtx.lineCap = 'round';
              tCtx.lineJoin = 'round';
              if (cmd.type === 'highlight') tCtx.globalAlpha = 0.4;
              tCtx.beginPath();
              cmd.points.forEach((pt, idx) => {{
                if (idx === 0) tCtx.moveTo(pt.x, pt.y);
                else tCtx.lineTo(pt.x, pt.y);
              }});
              tCtx.stroke();
            }} else if (cmd.type === 'whiteout') {{
              tCtx.fillStyle = '#ffffff';
              tCtx.fillRect(cmd.x, cmd.y, cmd.w, cmd.h);
            }} else if (cmd.type === 'rectangle') {{
              tCtx.strokeStyle = cmd.color;
              tCtx.lineWidth = cmd.size;
              tCtx.strokeRect(cmd.x, cmd.y, cmd.w, cmd.h);
            }} else if (cmd.type === 'text') {{
              tCtx.font = `${{cmd.size * 3}}px Inter, sans-serif`;
              tCtx.fillStyle = cmd.color;
              tCtx.fillText(cmd.text, cmd.x, cmd.y);
            }}
            tCtx.restore();
          }});

          const pngDataUrl = tempCanvas.toDataURL('image/png');
          const imgBytes = await (await fetch(pngDataUrl)).arrayBuffer();
          const embeddedImg = await pdfDoc.embedPng(imgBytes);

          page.drawImage(embeddedImg, {{
            x: 0,
            y: 0,
            width: pdfW,
            height: pdfH
          }});
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Generating PDF binary...';

        const pdfBytes = await pdfDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_edited.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Document edited successfully. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error saving edited PDF: ' + err.message);
        progressContainer.style.display = 'none';
        editorWorkspace.style.display = 'block';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      editorWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
      pageDrawings = {{}};
    }});
  </script>
</body>
</html>'''

write_file('pdf/edit.html', edit_html)

# ==========================================
# 6. REDACT PDF
# ==========================================
redact_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Redact PDF Online Free — Blackout Sensitive Data | DigitalSaathi</title>
  <meta name="description" content="Permanently redact and blackout sensitive data in PDF documents online for free. Mask Aadhaar numbers, PAN cards, phone numbers, and private text with 100% privacy.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .redact-workspace {{
      display: grid;
      grid-template-columns: 1fr 320px;
      gap: 24px;
      margin: 24px 0;
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .redact-workspace {{
        grid-template-columns: 1fr;
      }}
    }}
    .redact-stage-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: var(--shadow-sm);
    }}
    .stage-wrapper {{
      position: relative;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
      cursor: crosshair;
    }}
    #redactBgCanvas {{
      display: block;
    }}
    #redactOverlayCanvas {{
      position: absolute;
      top: 0;
      left: 0;
    }}
    .redact-list {{
      max-height: 240px;
      overflow-y: auto;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px;
      margin: 12px 0;
    }}
    .redact-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 6px 10px;
      background: #f8fafc;
      border-radius: 4px;
      margin-bottom: 6px;
      font-size: 0.85rem;
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
      <span>Redact PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#fee2e2;color:#dc2626;">⬛</div>
      <h1 class="tool-title">Redact Sensitive Data in PDF</h1>
      <p class="tool-desc">Permanently blackout confidential information like Aadhaar numbers, PAN cards, phone numbers, and addresses. Irreversible client-side sanitization.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">⬛ Permanent Blackout</span>
        <span class="badge badge-neutral">🛡️ Unrecoverable Data Removal</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Mask Aadhaar numbers, PAN cards, and sensitive information</p>
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

    <!-- Workspace -->
    <div id="redactWorkspace" class="redact-workspace" style="display:none;">
      <!-- Canvas Stage -->
      <div class="redact-stage-card">
        <div style="display:flex;justify-content:space-between;width:100%;align-items:center;margin-bottom:12px;">
          <button class="btn btn-sm btn-outline" id="prevPageBtn">◀ Prev Page</button>
          <span style="font-weight:600;font-size:0.9rem;" id="pageIndicator">Page 1 of 1</span>
          <button class="btn btn-sm btn-outline" id="nextPageBtn">Next Page ▶</button>
        </div>
        <p style="font-size:0.8rem;color:#64748b;margin-bottom:8px;">💡 Click and drag across any text or area to draw a blackout redaction rectangle.</p>
        <div class="stage-wrapper">
          <canvas id="redactBgCanvas"></canvas>
          <canvas id="redactOverlayCanvas"></canvas>
        </div>
      </div>

      <!-- Controls & List -->
      <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:20px;box-shadow:var(--shadow-sm);">
        <h3 style="font-size:1.1rem;font-weight:700;color:#1e293b;margin-bottom:12px;">Redaction Color</h3>
        
        <div style="display:flex;gap:10px;margin-bottom:16px;">
          <label style="display:flex;align-items:center;gap:6px;font-size:0.9rem;cursor:pointer;">
            <input type="radio" name="redactColor" value="black" checked> Solid Black (⬛ Blackout)
          </label>
          <label style="display:flex;align-items:center;gap:6px;font-size:0.9rem;cursor:pointer;">
            <input type="radio" name="redactColor" value="white"> Solid White (⬜ Whiteout)
          </label>
        </div>

        <h4 style="font-size:0.95rem;font-weight:700;color:#334155;margin-bottom:6px;">Redaction Boxes (<span id="boxCount">0</span>)</h4>
        <div class="redact-list" id="redactList">
          <div style="text-align:center;color:#94a3b8;padding:16px;font-size:0.85rem;">No areas marked on this page yet. Drag on the preview to redact.</div>
        </div>

        <button class="btn btn-outline btn-sm" id="clearRedactsBtn" style="width:100%;margin-bottom:16px;">Clear Page Redactions</button>

        <button class="btn btn-primary" id="applyRedactionBtn" style="width:100%;padding:12px;font-weight:700;font-size:1rem;background:#dc2626;border-color:#dc2626;">Permanently Redact & Download</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Sanitizing and redacting PDF... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Redacted Successfully!</h3>
      <p class="result-desc" id="resultDesc">All marked sensitive areas have been permanently sanitized and locked.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="redacted.pdf">⬇️ Download Redacted PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Redact Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Permanently Redact a PDF</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select your document containing private numbers or details.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Mark Blackout Boxes</h4>
          <p class="step-desc">Click and drag over sensitive lines (Aadhaar, PAN, phone numbers, marks).</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Sanitize & Download</h4>
          <p class="step-desc">Click Permanently Redact. The boxes are baked directly into the PDF coordinate tree.</p>
        </div>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    if (typeof pdfjsLib !== 'undefined') {{
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }}

    let currentFile = null;
    let originalPdfBytes = null;
    let pdfDocProxy = null;
    let totalPages = 1;
    let currentPageNum = 1;
    let isDrawing = false;
    let startX = 0, startY = 0;
    let pageRedactions = {{}}; // {{ [pageNum]: [ {{ x, y, w, h, color }} ] }}

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const redactWorkspace = document.getElementById('redactWorkspace');
    const redactBgCanvas = document.getElementById('redactBgCanvas');
    const redactOverlayCanvas = document.getElementById('redactOverlayCanvas');
    const overCtx = redactOverlayCanvas.getContext('2d');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const pageIndicator = document.getElementById('pageIndicator');
    const redactList = document.getElementById('redactList');
    const boxCount = document.getElementById('boxCount');
    const clearRedactsBtn = document.getElementById('clearRedactsBtn');
    const applyRedactionBtn = document.getElementById('applyRedactionBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{ if (e.target !== selectBtn) fileInput.click(); }});
    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{ fileInput.value = ''; fileInput.click(); }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Loading pages for redaction...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        pdfDocProxy = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes) }}).promise;
        totalPages = pdfDocProxy.numPages;
        currentPageNum = 1;
        pageRedactions = {{}};
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{totalPages}} ${{totalPages === 1 ? 'Page' : 'Pages'}}`;

        progressContainer.style.display = 'none';
        redactWorkspace.style.display = 'grid';
        await renderPage();
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    async function renderPage() {{
      if (!pdfDocProxy) return;
      pageIndicator.textContent = `Page ${{currentPageNum}} of ${{totalPages}}`;
      prevPageBtn.disabled = currentPageNum <= 1;
      nextPageBtn.disabled = currentPageNum >= totalPages;

      const page = await pdfDocProxy.getPage(currentPageNum);
      const viewport = page.getViewport({{ scale: 1.1 }});
      const bgCtx = redactBgCanvas.getContext('2d');

      redactBgCanvas.width = viewport.width;
      redactBgCanvas.height = viewport.height;
      redactOverlayCanvas.width = viewport.width;
      redactOverlayCanvas.height = viewport.height;

      await page.render({{ canvasContext: bgCtx, viewport: viewport }}).promise;
      renderOverlayAndList();
    }}

    function renderOverlayAndList() {{
      overCtx.clearRect(0, 0, redactOverlayCanvas.width, redactOverlayCanvas.height);
      const list = pageRedactions[currentPageNum] || [];
      boxCount.textContent = list.length;

      if (list.length === 0) {{
        redactList.innerHTML = '<div style="text-align:center;color:#94a3b8;padding:16px;font-size:0.85rem;">No areas marked on this page yet. Drag on the preview to redact.</div>';
      }} else {{
        redactList.innerHTML = '';
        list.forEach((box, idx) => {{
          // Draw on overlay
          overCtx.fillStyle = box.color === 'white' ? '#ffffff' : '#000000';
          overCtx.fillRect(box.x, box.y, box.w, box.h);
          overCtx.strokeStyle = '#ef4444';
          overCtx.lineWidth = 1;
          overCtx.strokeRect(box.x, box.y, box.w, box.h);

          // Build list item
          const item = document.createElement('div');
          item.className = 'redact-item';
          item.innerHTML = `
            <span>Box #${{idx + 1}} (${{Math.round(box.w)}}x${{Math.round(box.h)}}px)</span>
            <button class="btn btn-sm btn-outline" style="padding:2px 6px;font-size:0.75rem;color:#dc2626;" data-del="${{idx}}">✕ Remove</button>
          `;
          item.querySelector('button').addEventListener('click', () => {{
            list.splice(idx, 1);
            renderOverlayAndList();
          }});
          redactList.appendChild(item);
        }});
      }}
    }}

    function getCanvasPos(e) {{
      const rect = redactOverlayCanvas.getBoundingClientRect();
      const scaleX = redactOverlayCanvas.width / rect.width;
      const scaleY = redactOverlayCanvas.height / rect.height;
      return {{
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY
      }};
    }}

    redactOverlayCanvas.addEventListener('mousedown', (e) => {{
      const pos = getCanvasPos(e);
      startX = pos.x;
      startY = pos.y;
      isDrawing = true;
    }});

    redactOverlayCanvas.addEventListener('mousemove', (e) => {{
      if (!isDrawing) return;
      const pos = getCanvasPos(e);
      renderOverlayAndList();

      const colorVal = document.querySelector('input[name="redactColor"]:checked').value;
      overCtx.fillStyle = colorVal === 'white' ? 'rgba(255,255,255,0.7)' : 'rgba(0,0,0,0.7)';
      overCtx.fillRect(
        Math.min(startX, pos.x),
        Math.min(startY, pos.y),
        Math.abs(pos.x - startX),
        Math.abs(pos.y - startY)
      );
    }});

    window.addEventListener('mouseup', (e) => {{
      if (!isDrawing) return;
      isDrawing = false;
      const pos = getCanvasPos(e);
      const w = Math.abs(pos.x - startX);
      const h = Math.abs(pos.y - startY);

      if (w > 5 && h > 5) {{
        if (!pageRedactions[currentPageNum]) pageRedactions[currentPageNum] = [];
        const colorVal = document.querySelector('input[name="redactColor"]:checked').value;
        pageRedactions[currentPageNum].push({{
          x: Math.min(startX, pos.x),
          y: Math.min(startY, pos.y),
          w: w,
          h: h,
          color: colorVal
        }});
      }}
      renderOverlayAndList();
    }});

    clearRedactsBtn.addEventListener('click', () => {{
      pageRedactions[currentPageNum] = [];
      renderOverlayAndList();
    }});

    prevPageBtn.addEventListener('click', () => {{ if (currentPageNum > 1) {{ currentPageNum--; renderPage(); }} }});
    nextPageBtn.addEventListener('click', () => {{ if (currentPageNum < totalPages) {{ currentPageNum++; renderPage(); }} }});

    applyRedactionBtn.addEventListener('click', async () => {{
      const hasAny = Object.values(pageRedactions).some(arr => arr && arr.length > 0);
      if (!hasAny) {{
        alert('Please draw at least one redaction box on the document first!');
        return;
      }}

      redactWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '25%';
      progressText.textContent = 'Sanitizing document and applying blackouts...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const pages = pdfDoc.getPages();

        for (let pNum = 1; pNum <= pages.length; pNum++) {{
          const boxes = pageRedactions[pNum];
          if (!boxes || boxes.length === 0) continue;

          progressFill.style.width = `${{Math.round(25 + (pNum / pages.length) * 55)}}%`;
          const page = pages[pNum - 1];
          const {{ width: pdfW, height: pdfH }} = page.getSize();

          const scaleX = pdfW / redactBgCanvas.width;
          const scaleY = pdfH / redactBgCanvas.height;

          boxes.forEach(box => {{
            const drawX = box.x * scaleX;
            const drawY = pdfH - ((box.y + box.h) * scaleY);
            const drawW = box.w * scaleX;
            const drawH = box.h * scaleY;
            const c = box.color === 'white' ? PDFLib.rgb(1, 1, 1) : PDFLib.rgb(0, 0, 0);

            page.drawRectangle({{
              x: drawX,
              y: drawY,
              width: drawW,
              height: drawH,
              color: c,
              opacity: 1
            }});
          }});
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Generating sanitized PDF...';

        const pdfBytes = await pdfDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_redacted.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Sensitive data redacted and sanitized permanently. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error redacting PDF: ' + err.message);
        progressContainer.style.display = 'none';
        redactWorkspace.style.display = 'grid';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      redactWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
      pageRedactions = {{}};
    }});
  </script>
</body>
</html>'''

write_file('pdf/redact.html', redact_html)

# ==========================================
# 7. FORMS PDF
# ==========================================
forms_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fill & Flatten PDF Forms Online Free | DigitalSaathi</title>
  <meta name="description" content="Fill out interactive PDF forms online for free. Fill text fields, checkboxes, dropdowns, and flatten PDF forms client-side with 100% privacy.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="tool-page">

{NAVBAR}

  <div class="container page-content">
    <div class="breadcrumb">
      <a href="../index.html">Home</a>
      <span>›</span>
      <a href="index.html">PDF Tools</a>
      <span>›</span>
      <span>PDF Forms</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#e0f2fe;color:#0284c7;">📋</div>
      <h1 class="tool-title">Fill & Flatten PDF Forms</h1>
      <p class="tool-desc">Detect, fill, and flatten interactive AcroForm fields in official government and university PDF documents. 100% private in-browser.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">📋 AcroForm Auto-Detection</span>
        <span class="badge badge-neutral">🔒 Form Flattening</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF Form or drag & drop here</h3>
      <p class="upload-subtitle">Automatically detects form fields, checkboxes, and text inputs</p>
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

    <!-- Form Fields Workspace -->
    <div id="formsWorkspace" style="display:none;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:24px;margin:24px 0;box-shadow:var(--shadow-sm);">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid #e2e8f0;padding-bottom:12px;">
        <h3 style="font-size:1.15rem;font-weight:700;color:#1e293b;">Detected Form Fields (<span id="detectedCount">0</span>)</h3>
        <label style="display:flex;align-items:center;gap:6px;font-size:0.9rem;cursor:pointer;font-weight:600;">
          <input type="checkbox" id="flattenCheck" checked> Flatten Form (Lock values permanently)
        </label>
      </div>

      <div id="fieldsContainer" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:16px;margin:20px 0;">
        <!-- Injected form fields dynamically -->
      </div>

      <div class="action-buttons text-center" style="margin-top:24px;">
        <button class="btn btn-primary btn-lg" id="saveFormBtn">Save & Download Filled Form</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Processing form... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Form Saved Successfully!</h3>
      <p class="result-desc" id="resultDesc">All fields have been filled and compiled.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="filled_form.pdf">⬇️ Download Filled Form</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Fill Another Form</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Fill PDF Forms</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload Form</h4>
          <p class="step-desc">Select any interactive PDF application form or document.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Enter Details</h4>
          <p class="step-desc">All detected text fields, checkboxes, and dropdowns are laid out cleanly for you to fill.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Download Form</h4>
          <p class="step-desc">Save as interactive PDF or flatten to make non-editable.</p>
        </div>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="../assets/js/common.js"></script>
  <script>
    let currentFile = null;
    let originalPdfBytes = null;
    let loadedPdfDoc = null;
    let formFieldsList = [];

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const formsWorkspace = document.getElementById('formsWorkspace');
    const detectedCount = document.getElementById('detectedCount');
    const fieldsContainer = document.getElementById('fieldsContainer');
    const flattenCheck = document.getElementById('flattenCheck');
    const saveFormBtn = document.getElementById('saveFormBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultCard = document.getElementById('resultCard');
    const downloadBtn = document.getElementById('downloadBtn');
    const processAnotherBtn = document.getElementById('processAnotherBtn');

    selectBtn.addEventListener('click', () => fileInput.click());
    uploadZone.addEventListener('click', (e) => {{ if (e.target !== selectBtn) fileInput.click(); }});
    uploadZone.addEventListener('dragover', (e) => {{ e.preventDefault(); uploadZone.classList.add('drag-over'); }});
    uploadZone.addEventListener('dragleave', () => {{ uploadZone.classList.remove('drag-over'); }});
    uploadZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    fileInput.addEventListener('change', (e) => {{
      if (e.target.files && e.target.files.length > 0) handleFile(e.target.files[0]);
    }});

    changeFileBtn.addEventListener('click', () => {{ fileInput.value = ''; fileInput.click(); }});

    async function handleFile(file) {{
      if (!file || !file.name.toLowerCase().endsWith('.pdf')) {{
        alert('Please select a valid PDF file.');
        return;
      }}
      currentFile = file;
      fileName.textContent = file.name;
      uploadZone.style.display = 'none';
      fileInfo.style.display = 'flex';
      resultCard.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '40%';
      progressText.textContent = 'Inspecting AcroForm fields...';

      try {{
        originalPdfBytes = await file.arrayBuffer();
        loadedPdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const form = loadedPdfDoc.getForm();
        const fields = form.getFields();

        formFieldsList = fields;
        detectedCount.textContent = fields.length;
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • ${{fields.length}} Form Fields`;

        fieldsContainer.innerHTML = '';

        if (fields.length === 0) {{
          fieldsContainer.innerHTML = `
            <div style="grid-column:1/-1;background:#fef2f2;border:1px solid #fecaca;padding:16px;border-radius:6px;color:#991b1b;">
              ⚠️ No interactive AcroForm fields were detected in this document. If this is a scanned form, you can use the <b>Edit PDF</b> or <b>Sign PDF</b> tool to type text directly on top of the document.
            </div>
          `;
        }} else {{
          fields.forEach((field, i) => {{
            const name = field.getName();
            const type = field.constructor.name;
            const fieldBox = document.createElement('div');
            fieldBox.className = 'form-group';
            fieldBox.style.background = '#f8fafc';
            fieldBox.style.padding = '12px';
            fieldBox.style.borderRadius = '6px';
            fieldBox.style.border = '1px solid #e2e8f0';

            let inputHtml = '';
            if (field instanceof PDFLib.PDFCheckBox) {{
              const isChecked = field.isChecked();
              inputHtml = `
                <label style="display:flex;align-items:center;gap:8px;font-weight:600;font-size:0.9rem;cursor:pointer;">
                  <input type="checkbox" id="field_${{i}}" data-field-name="${{name}}" ${{isChecked ? 'checked' : ''}}>
                  ${{name}} (Checkbox)
                </label>
              `;
            }} else if (field instanceof PDFLib.PDFDropdown) {{
              const options = field.getOptions();
              const selected = field.getSelected();
              inputHtml = `
                <label class="form-label" style="font-weight:600;font-size:0.85rem;">${{name}} (Dropdown)</label>
                <select id="field_${{i}}" data-field-name="${{name}}" class="form-select" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:4px;">
                  ${{options.map(opt => `<option value="${{opt}}" ${{selected.includes(opt) ? 'selected' : ''}}>${{opt}}</option>`).join('')}}
                </select>
              `;
            }} else {{
              let val = '';
              try {{ val = field.getText() || ''; }} catch (e) {{}}
              inputHtml = `
                <label class="form-label" style="font-weight:600;font-size:0.85rem;">${{name}}</label>
                <input type="text" id="field_${{i}}" data-field-name="${{name}}" class="form-input" value="${{val}}" style="width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:4px;">
              `;
            }}

            fieldBox.innerHTML = inputHtml;
            fieldsContainer.appendChild(fieldBox);
          }});
        }}

        progressContainer.style.display = 'none';
        formsWorkspace.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Failed to load PDF Form: ' + err.message);
        progressContainer.style.display = 'none';
        uploadZone.style.display = 'block';
      }}
    }}

    saveFormBtn.addEventListener('click', async () => {{
      formsWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Filling form data...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        const form = pdfDoc.getForm();

        formFieldsList.forEach((field, i) => {{
          const el = document.getElementById(`field_${{i}}`);
          if (!el) return;
          const name = el.dataset.fieldName;

          try {{
            const target = form.getField(name);
            if (target instanceof PDFLib.PDFCheckBox) {{
              if (el.checked) target.check();
              else target.uncheck();
            }} else if (target instanceof PDFLib.PDFDropdown) {{
              target.select(el.value);
            }} else if (target instanceof PDFLib.PDFTextField) {{
              target.setText(el.value);
            }}
          }} catch (e) {{
            console.warn('Field update error:', e);
          }}
        }});

        if (flattenCheck.checked) {{
          progressFill.style.width = '70%';
          progressText.textContent = 'Flattening form fields...';
          form.flatten();
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Saving PDF binary...';

        const pdfBytes = await pdfDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_filled.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Form saved successfully. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error saving PDF form: ' + err.message);
        progressContainer.style.display = 'none';
        formsWorkspace.style.display = 'block';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      formsWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/forms.html', forms_html)
print("Finished All Organize & Edit tools.")
