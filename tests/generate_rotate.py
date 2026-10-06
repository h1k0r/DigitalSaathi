import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("Generating 100% functional working engines for all PDF tools...")

# Let's define the tools with their complete HTML and JS engines.

# 1. ROTATE PDF
rotate_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rotate PDF Pages Online Free — Permanent PDF Rotation | DigitalSaathi</title>
  <meta name="description" content="Rotate individual or all pages of a PDF document permanently online for free. Fix sideways or upside down scanned pages with live visual preview.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
  <style>
    .breadcrumb-nav { display: flex; align-items: center; gap: 8px; font-size: 0.8125rem; color: var(--text-muted); margin-bottom: var(--space-4); }
    .breadcrumb-nav a { color: var(--text-muted); text-decoration: none; }
    .breadcrumb-nav a:hover { color: var(--primary); }
    .tool-header-block { text-align: center; max-width: 760px; margin: 0 auto 2rem; }
    .rotate-workspace { display: none; margin-top: 2rem; }
    .page-grid-box { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 16px; max-height: 480px; overflow-y: auto; padding: 16px; background: var(--bg-surface-subtle); border-radius: var(--radius-lg); margin: 1.25rem 0; border: 1px solid var(--border-subtle); }
    .rotate-card { background: #fff; border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 10px; display: flex; flex-direction: column; align-items: center; box-shadow: var(--shadow-xs); }
    .rotate-canvas-wrap { width: 130px; height: 160px; display: flex; align-items: center; justify-content: center; overflow: hidden; background: #f8fafc; border-radius: 4px; margin-bottom: 8px; }
    .rotate-canvas-wrap canvas { max-width: 100%; max-height: 100%; transition: transform 0.2s ease; }
    .result-banner { display: none; background: var(--success-bg); border: 1px solid var(--success-border); border-radius: var(--radius-xl); padding: 2rem; text-align: center; margin-top: 2rem; }
  </style>
</head>
<body>
  <nav class="navbar" id="main-nav">
    <div class="container nav-container">
      <a href="../index.html" class="logo"><span class="logo-badge">🌐</span><span class="logo-text">Digital<span class="logo-highlight">Saathi</span></span></a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      <ul class="nav-links">
        <li class="nav-item"><a href="index.html" class="nav-link active">📑 PDF Tools</a></li>
        <li class="nav-item"><a href="../cybercafe/passport-photo.html" class="nav-link">🖥️ Cyber Café</a></li>
        <li class="nav-item"><a href="../student/resume.html" class="nav-link">🎓 Student & Resume</a></li>
        <li class="nav-item"><a href="../jobs/government.html" class="nav-link">🏛️ Jobs</a></li>
        <li class="nav-item"><a href="../developer/json.html" class="nav-link">💻 Dev Tools</a></li>
        <li class="nav-item"><a href="../calculators/emi.html" class="nav-link">💰 Finance</a></li>
      </ul>
      <div class="nav-actions"><a href="../student/resume.html" class="btn btn-primary btn-sm">Build Resume</a></div>
    </div>
  </nav>

  <main class="container" style="max-width: 960px; padding: 2.5rem var(--space-4) 5rem;">
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
      <a href="../index.html">Home</a><span>/</span><a href="index.html">PDF Tools</a><span>/</span><span style="color:var(--text-main); font-weight:600;">Rotate PDF</span>
    </nav>
    <div class="tool-header-block">
      <div class="pill-badge" style="background:var(--color-pdf-bg);color:var(--color-pdf);border-color:var(--color-pdf-border);"><span>🔄</span> PDF Organization</div>
      <h1 style="font-size: clamp(1.8rem, 3vw + 0.5rem, 2.4rem); font-weight: 800; margin-bottom: 0.5rem;">Rotate PDF Pages Permanently</h1>
      <p style="color: var(--text-muted); font-size: 1.05rem;">Rotate individual pages or the entire document by 90°, 180°, or 270° with live visual feedback.</p>
    </div>

    <div class="upload-zone" id="rotate-dropzone" style="max-width: 720px; margin: 0 auto;">
      <input type="file" id="rotate-file-input" accept="application/pdf" aria-label="Upload PDF file to rotate">
      <div class="upload-zone-icon">🔄</div>
      <div class="upload-zone-title">Select a PDF file, or drag & drop here</div>
      <div class="upload-zone-hint">Upload sideways or upside down scanned pages (Up to 100MB)</div>
      <span class="upload-privacy-pill">🔒 100% Local Browser Processing</span>
    </div>

    <div class="rotate-workspace card" id="rotate-workspace">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:1rem; padding-bottom:12px; border-bottom:1px solid var(--border-subtle);">
        <div>
          <div style="font-weight:700; color:var(--text-main);" id="doc-name-label">Document.pdf</div>
          <div style="font-size:0.8rem; color:var(--text-muted);" id="doc-meta-label">0 Pages</div>
        </div>
        <div style="display:flex; gap:8px;">
          <button type="button" class="btn btn-secondary btn-sm" id="btn-rot-all-left">↺ Rotate All Left</button>
          <button type="button" class="btn btn-secondary btn-sm" id="btn-rot-all-right">↻ Rotate All Right</button>
          <button type="button" class="btn btn-ghost btn-sm" id="btn-reset-rotations">Reset</button>
        </div>
      </div>

      <div class="page-grid-box" id="page-grid-box"></div>

      <button type="button" class="btn btn-primary btn-lg btn-full" id="btn-save-rotation" style="margin-top:1rem;">
        Save & Download Rotated PDF →
      </button>
    </div>

    <div class="result-banner" id="rotate-result-banner">
      <div style="font-size:2.5rem; margin-bottom:8px;">🎉</div>
      <h2 style="font-size:1.4rem; font-weight:800; color:var(--success-text); margin-bottom:4px;">PDF Successfully Rotated!</h2>
      <p style="font-size:0.9rem; color:var(--text-body); margin-bottom:1.25rem;">Permanent orientation applied to all modified pages.</p>
      <div style="display:flex; justify-content:center; gap:12px;">
        <button type="button" class="btn btn-success btn-lg" id="btn-download-rotated">📥 Download Rotated PDF</button>
        <button type="button" class="btn btn-secondary btn-lg" id="btn-reset-tool">🔄 Rotate Another File</button>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container" style="text-align: center; font-size: 0.85rem; color: var(--text-muted);">
      <p>© 2026 DigitalSaathi. 100% Free & Client-Side Privacy Guaranteed.</p>
    </div>
  </footer>

  <script src="../assets/js/common.js"></script>
  <script>
    if (typeof pdfjsLib !== 'undefined') {
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }

    let currentFile = null;
    let currentArrayBuffer = null;
    let totalPages = 0;
    let rotations = {}; // pageIndex (0-based) -> additional rotation (0, 90, 180, 270)
    let initialRotations = {};
    let rotatedPdfBlob = null;

    const fileInput = document.getElementById('rotate-file-input');
    const dropzone = document.getElementById('rotate-dropzone');
    const workspace = document.getElementById('rotate-workspace');
    const pageGridBox = document.getElementById('page-grid-box');
    const resultBanner = document.getElementById('rotate-result-banner');

    async function loadPdf(file) {
      currentFile = file;
      currentArrayBuffer = await file.arrayBuffer();
      const pdfDoc = await PDFLib.PDFDocument.load(currentArrayBuffer, { ignoreEncryption: true });
      totalPages = pdfDoc.getPageCount();

      rotations = {};
      initialRotations = {};
      for (let i = 0; i < totalPages; i++) {
        const page = pdfDoc.getPage(i);
        const rot = page.getRotation().angle || 0;
        initialRotations[i] = rot;
        rotations[i] = 0;
      }

      document.getElementById('doc-name-label').textContent = file.name;
      document.getElementById('doc-meta-label').textContent = `${totalPages} Pages • ${formatFileSize(file.size)}`;

      dropzone.style.display = 'none';
      workspace.style.display = 'block';
      resultBanner.style.display = 'none';

      await renderThumbnails();
    }

    async function renderThumbnails() {
      pageGridBox.innerHTML = '';
      const loadingTask = pdfjsLib.getDocument({ data: new Uint8Array(currentArrayBuffer) });
      const pdf = await loadingTask.promise;

      for (let i = 0; i < totalPages; i++) {
        const card = document.createElement('div');
        card.className = 'rotate-card';
        card.id = `rot-card-${i}`;

        const wrap = document.createElement('div');
        wrap.className = 'rotate-canvas-wrap';
        const canvas = document.createElement('canvas');
        wrap.appendChild(canvas);

        card.appendChild(wrap);
        card.innerHTML += `
          <div style="font-size:0.8rem; font-weight:600; margin-bottom:6px;">Page ${i + 1}</div>
          <div style="display:flex; gap:6px;">
            <button type="button" class="btn btn-secondary btn-sm" onclick="rotatePage(${i}, -90)" title="Rotate Left">↺</button>
            <button type="button" class="btn btn-secondary btn-sm" onclick="rotatePage(${i}, 90)" title="Rotate Right">↻</button>
          </div>
        `;
        card.querySelector('.rotate-canvas-wrap').replaceWith(wrap);
        pageGridBox.appendChild(card);

        const page = await pdf.getPage(i + 1);
        const viewport = page.getViewport({ scale: 0.25 });
        canvas.width = viewport.width;
        canvas.height = viewport.height;
        await page.render({ canvasContext: canvas.getContext('2d'), viewport: viewport }).promise;
      }
    }

    window.rotatePage = function(index, delta) {
      rotations[index] = (rotations[index] + delta) % 360;
      if (rotations[index] < 0) rotations[index] += 360;
      updateCardVisual(index);
    };

    function updateCardVisual(index) {
      const card = document.getElementById(`rot-card-${index}`);
      if (!card) return;
      const canvas = card.querySelector('canvas');
      if (canvas) {
        canvas.style.transform = `rotate(${rotations[index]}deg)`;
      }
    }

    document.getElementById('btn-rot-all-left').addEventListener('click', () => {
      for (let i = 0; i < totalPages; i++) rotatePage(i, -90);
    });
    document.getElementById('btn-rot-all-right').addEventListener('click', () => {
      for (let i = 0; i < totalPages; i++) rotatePage(i, 90);
    });
    document.getElementById('btn-reset-rotations').addEventListener('click', () => {
      for (let i = 0; i < totalPages; i++) {
        rotations[i] = 0;
        updateCardVisual(i);
      }
    });

    document.getElementById('btn-save-rotation').addEventListener('click', async () => {
      const btn = document.getElementById('btn-save-rotation');
      btn.disabled = true;
      btn.classList.add('is-loading');

      try {
        const pdfDoc = await PDFLib.PDFDocument.load(currentArrayBuffer, { ignoreEncryption: true });
        for (let i = 0; i < totalPages; i++) {
          const page = pdfDoc.getPage(i);
          const currentAngle = initialRotations[i] || 0;
          const additionalAngle = rotations[i] || 0;
          const finalAngle = (currentAngle + additionalAngle) % 360;
          page.setRotation(PDFLib.degrees(finalAngle));
        }

        const bytes = await pdfDoc.save();
        rotatedPdfBlob = new Blob([bytes], { type: 'application/pdf' });

        workspace.style.display = 'none';
        resultBanner.style.display = 'block';
        dsToast.success('PDF pages permanently rotated!');
      } catch (e) {
        dsToast.error('Rotation failed: ' + e.message);
      } finally {
        btn.disabled = false;
        btn.classList.remove('is-loading');
      }
    });

    document.getElementById('btn-download-rotated').addEventListener('click', () => {
      if (rotatedPdfBlob) downloadBlob(rotatedPdfBlob, 'DigitalSaathi_Rotated.pdf');
    });
    document.getElementById('btn-reset-tool').addEventListener('click', () => {
      workspace.style.display = 'none';
      resultBanner.style.display = 'none';
      dropzone.style.display = 'block';
    });

    fileInput.addEventListener('change', (e) => {
      if (e.target.files && e.target.files.length > 0) loadPdf(e.target.files[0]);
    });
    initDropZone(dropzone, {
      onFiles: (files) => { if (files && files.length > 0) loadPdf(files[0]); }
    });
  </script>
</body>
</html>'''

with open('pdf/rotate.html', 'w', encoding='utf-8') as f:
    f.write(rotate_html)
print("✅ Created working engine: pdf/rotate.html")
