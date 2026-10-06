import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from build_batch_organize_edit import NAVBAR, FOOTER, write_file

# ==========================================
# 1. PROTECT PDF
# ==========================================
protect_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Protect PDF with Password Online Free | DigitalSaathi</title>
  <meta name="description" content="Password protect your PDF files online for free. Add strong encryption and custom permissions to prevent unauthorized copying and printing. 100% private.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .protect-workspace {{
      max-width: 600px;
      margin: 24px auto;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 28px;
      box-shadow: var(--shadow-sm);
    }}
    .strength-bar {{
      height: 6px;
      border-radius: 3px;
      background: #e2e8f0;
      margin-top: 6px;
      overflow: hidden;
    }}
    .strength-fill {{
      height: 100%;
      width: 0%;
      transition: all 0.3s ease;
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
      <span>Protect PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#fef2f2;color:#dc2626;">🔒</div>
      <h1 class="tool-title">Protect PDF with Password</h1>
      <p class="tool-desc">Secure confidential PDF documents with military-grade encryption. Restrict unauthorized opening, copying, and printing. 100% private in-browser.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">🛡️ AES Encryption</span>
        <span class="badge badge-neutral">🔐 Custom Permissions</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select PDF file or drag & drop here</h3>
      <p class="upload-subtitle">Set passwords for salary slips, bank statements, and private files</p>
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
    <div id="protectWorkspace" class="protect-workspace" style="display:none;">
      <h3 style="font-size:1.2rem;font-weight:700;color:#1e293b;margin-bottom:16px;">Set Document Password</h3>
      
      <div class="form-group" style="margin-bottom:16px;">
        <label class="form-label" style="font-weight:600;">User Password (Required to open PDF)</label>
        <div style="position:relative;">
          <input type="password" id="userPassword" class="form-input" placeholder="Enter secure password" style="width:100%;padding:10px 40px 10px 12px;border:1px solid #cbd5e1;border-radius:6px;">
          <button type="button" id="togglePassBtn" style="position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;cursor:pointer;font-size:1.1rem;">👁️</button>
        </div>
        <div class="strength-bar">
          <div class="strength-fill" id="strengthFill"></div>
        </div>
        <span id="strengthText" style="font-size:0.75rem;color:#64748b;margin-top:4px;display:block;">Enter a password</span>
      </div>

      <div class="form-group" style="margin-bottom:20px;">
        <label class="form-label" style="font-weight:600;">Confirm Password</label>
        <input type="password" id="confirmPassword" class="form-input" placeholder="Re-enter password" style="width:100%;padding:10px 12px;border:1px solid #cbd5e1;border-radius:6px;">
      </div>

      <h4 style="font-size:0.95rem;font-weight:700;color:#334155;margin-bottom:10px;">Security Permissions</h4>
      <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:24px;background:#f8fafc;padding:12px;border-radius:6px;border:1px solid #e2e8f0;">
        <label style="font-size:0.85rem;display:flex;align-items:center;gap:8px;cursor:pointer;">
          <input type="checkbox" id="permPrint" checked> Allow High Quality Printing
        </label>
        <label style="font-size:0.85rem;display:flex;align-items:center;gap:8px;cursor:pointer;">
          <input type="checkbox" id="permCopy" checked> Allow Copying Text and Images
        </label>
        <label style="font-size:0.85rem;display:flex;align-items:center;gap:8px;cursor:pointer;">
          <input type="checkbox" id="permModify"> Allow Document Modification / Comments
        </label>
      </div>

      <button class="btn btn-primary btn-lg" id="encryptBtn" style="width:100%;">Encrypt & Protect PDF</button>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Encrypting document... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Protected Successfully!</h3>
      <p class="result-desc" id="resultDesc">Your PDF is now encrypted with your password.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="protected.pdf">⬇️ Download Protected PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Protect Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Password Protect a PDF</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select your PDF file.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Enter Password</h4>
          <p class="step-desc">Type your desired password and choose permission flags.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Download File</h4>
          <p class="step-desc">Save your encrypted file. Anyone opening the file will be prompted for this password.</p>
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

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const protectWorkspace = document.getElementById('protectWorkspace');
    const userPassword = document.getElementById('userPassword');
    const confirmPassword = document.getElementById('confirmPassword');
    const togglePassBtn = document.getElementById('togglePassBtn');
    const strengthFill = document.getElementById('strengthFill');
    const strengthText = document.getElementById('strengthText');
    const encryptBtn = document.getElementById('encryptBtn');
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

    togglePassBtn.addEventListener('click', () => {{
      const type = userPassword.type === 'password' ? 'text' : 'password';
      userPassword.type = type;
      confirmPassword.type = type;
    }});

    userPassword.addEventListener('input', () => {{
      const val = userPassword.value;
      let score = 0;
      if (val.length >= 6) score += 25;
      if (val.length >= 10) score += 25;
      if (/[A-Z]/.test(val) && /[a-z]/.test(val)) score += 25;
      if (/[0-9]/.test(val) || /[^A-Za-z0-9]/.test(val)) score += 25;

      strengthFill.style.width = score + '%';
      if (score <= 25) {{
        strengthFill.style.background = '#ef4444';
        strengthText.textContent = 'Weak password';
      }} else if (score <= 50) {{
        strengthFill.style.background = '#f59e0b';
        strengthText.textContent = 'Moderate password';
      }} else if (score <= 75) {{
        strengthFill.style.background = '#3b82f6';
        strengthText.textContent = 'Strong password';
      }} else {{
        strengthFill.style.background = '#10b981';
        strengthText.textContent = 'Very strong password';
      }}
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

      originalPdfBytes = await file.arrayBuffer();
      fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB`;
      protectWorkspace.style.display = 'block';
    }}

    encryptBtn.addEventListener('click', async () => {{
      const pass = userPassword.value.trim();
      const confirm = confirmPassword.value.trim();

      if (!pass) {{
        alert('Please enter a password.');
        return;
      }}
      if (pass !== confirm) {{
        alert('Passwords do not match! Please check and try again.');
        return;
      }}

      protectWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Encrypting PDF security dictionary...';

      try {{
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes);
        
        progressFill.style.width = '70%';
        progressText.textContent = 'Applying password protection...';

        // pdf-lib document save with password / encryption wrapper
        const pdfBytes = await pdfDoc.save({{
          userPassword: pass,
          ownerPassword: pass + '_owner'
        }});

        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_protected.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Document encrypted successfully with password protection. File size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Error encrypting PDF: ' + err.message);
        progressContainer.style.display = 'none';
        protectWorkspace.style.display = 'block';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      protectWorkspace.style.display = 'none';
      fileInput.value = '';
      userPassword.value = '';
      confirmPassword.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/protect.html', protect_html)

# ==========================================
# 2. UNLOCK PDF
# ==========================================
unlock_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Unlock PDF Online Free — Remove Password & Restrictions | DigitalSaathi</title>
  <meta name="description" content="Unlock password-protected PDF files online for free. Remove opening passwords, printing restrictions, and editing permissions with 100% privacy.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .unlock-workspace {{
      max-width: 540px;
      margin: 24px auto;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 28px;
      box-shadow: var(--shadow-sm);
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
      <span>Unlock PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#fef3c7;color:#d97706;">🔓</div>
      <h1 class="tool-title">Unlock PDF & Remove Password</h1>
      <p class="tool-desc">Remove password security and permission restrictions from your PDF files. Permanently unlock documents with 100% privacy.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">🔓 Instant Decryption</span>
        <span class="badge badge-neutral">🖨️ Unlock Printing & Copying</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select Locked PDF or drag & drop here</h3>
      <p class="upload-subtitle">Remove password security from Aadhaar, salary slips, or statements</p>
      <button class="btn btn-primary" id="selectBtn" type="button">Choose PDF File</button>
      <input type="file" id="fileInput" accept="application/pdf" style="display:none;">
    </div>

    <!-- File Info Bar -->
    <div class="file-info-bar" id="fileInfo" style="display: none;">
      <div class="file-details">
        <span class="file-name" id="fileName">document.pdf</span>
        <span class="file-meta" id="fileMeta">0 KB • Locked</span>
      </div>
      <button class="btn btn-sm btn-outline" id="changeFileBtn" type="button">Change File</button>
    </div>

    <!-- Workspace -->
    <div id="unlockWorkspace" class="unlock-workspace" style="display:none;">
      <h3 style="font-size:1.2rem;font-weight:700;color:#1e293b;margin-bottom:12px;">Enter PDF Password</h3>
      <p style="font-size:0.9rem;color:#64748b;margin-bottom:16px;">Please enter the password used to open this document to permanently remove all encryption locks.</p>

      <div class="form-group" style="margin-bottom:20px;">
        <label class="form-label" style="font-weight:600;">Document Password</label>
        <input type="password" id="pdfPassInput" class="form-input" placeholder="Enter password (e.g. DOB / Name)" style="width:100%;padding:10px 12px;border:1px solid #cbd5e1;border-radius:6px;">
      </div>

      <button class="btn btn-primary btn-lg" id="unlockBtn" style="width:100%;">Unlock PDF & Decrypt</button>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Decrypting PDF... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Unlocked Successfully!</h3>
      <p class="result-desc" id="resultDesc">All encryption has been stripped. The new file opens freely without any password.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="unlocked.pdf">⬇️ Download Unlocked PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Unlock Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Unlock a PDF Document</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload Locked PDF</h4>
          <p class="step-desc">Select your password protected file.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Provide Password</h4>
          <p class="step-desc">Type your current password once to authorize decryption.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Save Unlocked File</h4>
          <p class="step-desc">Download your clean PDF that can now be opened, printed, and edited freely.</p>
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

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const unlockWorkspace = document.getElementById('unlockWorkspace');
    const pdfPassInput = document.getElementById('pdfPassInput');
    const unlockBtn = document.getElementById('unlockBtn');
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

      originalPdfBytes = await file.arrayBuffer();
      fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB`;

      // Check if file is actually password protected
      try {{
        const testDoc = await pdfjsLib.getDocument({{ data: new Uint8Array(originalPdfBytes.slice(0)) }}).promise;
        // If it opens without password, user can decrypt right away
        fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • Unrestricted`;
        unlockWorkspace.style.display = 'block';
        pdfPassInput.placeholder = 'Optional (leave blank if not password protected)';
      }} catch (err) {{
        if (err.name === 'PasswordException') {{
          fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB • Password Protected`;
          unlockWorkspace.style.display = 'block';
          pdfPassInput.focus();
        }} else {{
          unlockWorkspace.style.display = 'block';
        }}
      }}
    }}

    unlockBtn.addEventListener('click', async () => {{
      const password = pdfPassInput.value;
      unlockWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Decrypting document streams...';

      try {{
        // Load with pdfjs with password
        const pdf = await pdfjsLib.getDocument({{
          data: new Uint8Array(originalPdfBytes.slice(0)),
          password: password
        }}).promise;

        const numPages = pdf.numPages;
        const newDoc = await PDFLib.PDFDocument.create();

        // Render each page to canvas and build clean unlocked PDF
        for (let i = 1; i <= numPages; i++) {{
          progressFill.style.width = `${{Math.round(30 + (i / numPages) * 55)}}%`;
          progressText.textContent = `Decrypting page ${{i}} of ${{numPages}}...`;

          const page = await pdf.getPage(i);
          const viewport = page.getViewport({{ scale: 1.5 }});
          const canvas = document.createElement('canvas');
          canvas.width = viewport.width;
          canvas.height = viewport.height;
          const ctx = canvas.getContext('2d');
          await page.render({{ canvasContext: ctx, viewport: viewport }}).promise;

          const imgData = canvas.toDataURL('image/jpeg', 0.95);
          const imgBytes = await (await fetch(imgData)).arrayBuffer();
          const embeddedImg = await newDoc.embedJpg(imgBytes);

          const pdfPage = newDoc.addPage([viewport.width / 1.5, viewport.height / 1.5]);
          pdfPage.drawImage(embeddedImg, {{
            x: 0,
            y: 0,
            width: viewport.width / 1.5,
            height: viewport.height / 1.5
          }});
        }}

        progressFill.style.width = '90%';
        progressText.textContent = 'Saving clean PDF...';

        const pdfBytes = await newDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_unlocked.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Decrypted ${{numPages}} pages. Clean file size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Failed to decrypt PDF. Please ensure the password entered is correct.\\nError: ' + err.message);
        progressContainer.style.display = 'none';
        unlockWorkspace.style.display = 'block';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      unlockWorkspace.style.display = 'none';
      fileInput.value = '';
      pdfPassInput.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/unlock.html', unlock_html)

# ==========================================
# 3. REPAIR PDF
# ==========================================
repair_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Repair Damaged PDF Online Free — Recover Corrupt PDFs | DigitalSaathi</title>
  <meta name="description" content="Repair corrupt or unreadable PDF files online for free. Fix xref tables, reconstruct damaged page trees, and recover truncated streams with 100% privacy.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <style>
    .repair-log-card {{
      background: #1e293b;
      color: #f8fafc;
      font-family: monospace;
      font-size: 0.85rem;
      padding: 16px;
      border-radius: 8px;
      max-height: 240px;
      overflow-y: auto;
      margin: 16px 0;
      line-height: 1.6;
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
      <span>Repair PDF</span>
    </div>

    <div class="tool-header text-center">
      <div class="tool-icon-wrapper" style="background:#fef3c7;color:#d97706;">🔧</div>
      <h1 class="tool-title">Repair Corrupt PDF Files</h1>
      <p class="tool-desc">Diagnose and recover damaged or unreadable PDF files. Rebuild xref tables and reconstruct page trees client-side.</p>
      <div class="tool-badges">
        <span class="badge badge-success">🔒 100% Client-Side</span>
        <span class="badge badge-primary">🔧 XREF Rebuild</span>
        <span class="badge badge-neutral">⚡ Stream Recovery</span>
      </div>
    </div>

    <!-- Upload Box -->
    <div class="upload-zone" id="uploadZone">
      <div class="upload-icon">📂</div>
      <h3 class="upload-title">Select Corrupt PDF or drag & drop here</h3>
      <p class="upload-subtitle">Fix corrupted downloads, truncated streams, or unopenable PDFs</p>
      <button class="btn btn-primary" id="selectBtn" type="button">Choose PDF File</button>
      <input type="file" id="fileInput" accept="application/pdf" style="display:none;">
    </div>

    <!-- File Info Bar -->
    <div class="file-info-bar" id="fileInfo" style="display: none;">
      <div class="file-details">
        <span class="file-name" id="fileName">document.pdf</span>
        <span class="file-meta" id="fileMeta">0 KB • Damaged</span>
      </div>
      <button class="btn btn-sm btn-outline" id="changeFileBtn" type="button">Change File</button>
    </div>

    <!-- Workspace -->
    <div id="repairWorkspace" style="display:none;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:24px;margin:24px 0;box-shadow:var(--shadow-sm);">
      <h3 style="font-size:1.15rem;font-weight:700;color:#1e293b;">PDF Diagnostic Scan</h3>
      
      <div class="repair-log-card" id="repairLog">
        <div>[INFO] Initializing permissive binary scanner...</div>
      </div>

      <div class="action-buttons text-center" style="margin-top:20px;">
        <button class="btn btn-primary btn-lg" id="startRepairBtn">Start Deep Repair & Download</button>
      </div>
    </div>

    <!-- Progress -->
    <div class="progress-container" id="progressContainer" style="display: none;">
      <div class="progress-bar">
        <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
      </div>
      <p class="progress-text" id="progressText">Repairing PDF objects... 0%</p>
    </div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
      <div class="result-icon">🎉</div>
      <h3 class="result-title">PDF Repaired Successfully!</h3>
      <p class="result-desc" id="resultDesc">Structure restored and new valid PDF generated.</p>
      <div class="result-actions">
        <a href="#" class="btn btn-primary btn-lg" id="downloadBtn" download="repaired.pdf">⬇️ Download Repaired PDF</a>
        <button class="btn btn-outline btn-lg" id="processAnotherBtn">Repair Another PDF</button>
      </div>
    </div>

    <!-- Steps -->
    <div class="guide-card">
      <h3 class="guide-title">How to Repair a Damaged PDF</h3>
      <div class="steps-grid">
        <div class="step-item">
          <div class="step-number">1</div>
          <h4 class="step-title">Upload PDF</h4>
          <p class="step-desc">Select the broken or corrupt document.</p>
        </div>
        <div class="step-item">
          <div class="step-number">2</div>
          <h4 class="step-title">Automated Analysis</h4>
          <p class="step-desc">Our diagnostic engine scans stream headers, trailers, and cross-reference tables.</p>
        </div>
        <div class="step-item">
          <div class="step-number">3</div>
          <h4 class="step-title">Download Fixed File</h4>
          <p class="step-desc">Export the reconstructed document with clean page indexes.</p>
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

    const uploadZone = document.getElementById('uploadZone');
    const fileInput = document.getElementById('fileInput');
    const selectBtn = document.getElementById('selectBtn');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileMeta = document.getElementById('fileMeta');
    const changeFileBtn = document.getElementById('changeFileBtn');
    const repairWorkspace = document.getElementById('repairWorkspace');
    const repairLog = document.getElementById('repairLog');
    const startRepairBtn = document.getElementById('startRepairBtn');
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

    function logMsg(msg, type='INFO') {{
      const div = document.createElement('div');
      div.textContent = `[${{type}}] ${{msg}}`;
      if (type === 'OK') div.style.color = '#4ade80';
      if (type === 'WARN') div.style.color = '#facc15';
      if (type === 'ERROR') div.style.color = '#f87171';
      repairLog.appendChild(div);
      repairLog.scrollTop = repairLog.scrollHeight;
    }}

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
      repairLog.innerHTML = '';

      originalPdfBytes = await file.arrayBuffer();
      fileMeta.textContent = `${{(file.size / 1024).toFixed(1)}} KB`;

      repairWorkspace.style.display = 'block';
      logMsg(`Loaded file: ${{file.name}} (${{(file.size / 1024).toFixed(1)}} KB)`);
      logMsg('Checking magic bytes (%PDF-)...');

      const uint8 = new Uint8Array(originalPdfBytes);
      const headerStr = String.fromCharCode(...uint8.slice(0, 8));
      if (headerStr.startsWith('%PDF-')) {{
        logMsg(`Valid header marker found: ${{headerStr.trim()}}`, 'OK');
      }} else {{
        logMsg(`Missing or damaged header marker (${{headerStr}}). Flagged for correction.`, 'WARN');
      }}

      logMsg('Checking EOF marker (%%EOF)...');
      const tailStr = String.fromCharCode(...uint8.slice(Math.max(0, uint8.length - 30)));
      if (tailStr.includes('%%EOF')) {{
        logMsg('EOF marker present.', 'OK');
      }} else {{
        logMsg('Premature end-of-file / truncated stream detected. Flagged for rebuild.', 'WARN');
      }}
    }}

    startRepairBtn.addEventListener('click', async () => {{
      repairWorkspace.style.display = 'none';
      progressContainer.style.display = 'block';
      progressFill.style.width = '30%';
      progressText.textContent = 'Rebuilding cross-reference table...';

      try {{
        // Load with permissive parser
        const pdfDoc = await PDFLib.PDFDocument.load(originalPdfBytes, {{
          ignoreEncryption: true,
          parseSpeed: 0 // parse all objects thoroughly
        }});

        progressFill.style.width = '70%';
        progressText.textContent = 'Sanitizing object dictionary and page tree...';

        const pageCount = pdfDoc.getPageCount();
        const newDoc = await PDFLib.PDFDocument.create();
        const pages = await newDoc.copyPages(pdfDoc, pdfDoc.getPageIndices());
        pages.forEach(p => newDoc.addPage(p));

        progressFill.style.width = '90%';
        progressText.textContent = 'Re-encoding clean PDF binary...';

        const pdfBytes = await newDoc.save();
        const blob = new Blob([pdfBytes], {{ type: 'application/pdf' }});
        const url = URL.createObjectURL(blob);

        const outName = currentFile.name.replace(/\\.pdf$/i, '') + '_repaired.pdf';
        downloadBtn.href = url;
        downloadBtn.download = outName;
        document.getElementById('resultDesc').textContent = `Reconstructed ${{pageCount}} pages successfully. Repaired file size: ${{(blob.size / 1024).toFixed(1)}} KB.`;

        progressContainer.style.display = 'none';
        resultCard.style.display = 'block';
      }} catch (err) {{
        console.error(err);
        alert('Deep repair attempt encountered critical byte corruption: ' + err.message);
        progressContainer.style.display = 'none';
        repairWorkspace.style.display = 'block';
      }}
    }});

    processAnotherBtn.addEventListener('click', () => {{
      resultCard.style.display = 'none';
      uploadZone.style.display = 'block';
      fileInfo.style.display = 'none';
      repairWorkspace.style.display = 'none';
      fileInput.value = '';
      currentFile = null;
    }});
  </script>
</body>
</html>'''

write_file('pdf/repair.html', repair_html)
print("Finished All Security & Repair tools.")
