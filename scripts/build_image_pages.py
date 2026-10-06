#!/usr/bin/env python3
"""
Step-by-step builder for all 17 Image Tool pages.
"""
import os
import sys

from make_image_suite import wrap_page, write_file

def build_crop():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#fff1f2; color:#f43f5e; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Interactive Drag & Drop Crop Handles
      </div>
      <h1 class="tool-header-title">Image Cropper</h1>
      <p class="tool-header-desc">Crop your photos with standard aspect ratios: 3.5:4.5cm Passport, 1:1 Square, 16:9 Landscape, or Freeform.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">✂️</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose an Image to Crop</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload JPG, PNG, or WebP photo</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
            <button type="button" class="btn btn-primary btn-sm ratio-btn" data-ratio="free">Freeform</button>
            <button type="button" class="btn btn-secondary btn-sm ratio-btn" data-ratio="1:1">1:1 Square</button>
            <button type="button" class="btn btn-secondary btn-sm ratio-btn" data-ratio="3.5:4.5">3.5:4.5 Passport</button>
            <button type="button" class="btn btn-secondary btn-sm ratio-btn" data-ratio="4:3">4:3 Standard</button>
            <button type="button" class="btn btn-secondary btn-sm ratio-btn" data-ratio="16:9">16:9 Widescreen</button>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <button type="button" class="btn btn-outline btn-sm" id="btn-rotate-cw">🔄 Rotate 90°</button>
            <button type="button" class="btn btn-outline btn-sm" id="btn-flip-h">↔️ Flip Horizontal</button>
          </div>
        </div>

        <div class="tool-preview-panel" style="margin-top: 1rem;">
          <div style="max-width: 100%; overflow: auto; text-align: center; background: #334155; padding: 1rem; border-radius: 8px;">
            <canvas id="crop-canvas" style="max-width: 100%; max-height: 500px; cursor: crosshair; box-shadow: 0 4px 12px rgba(0,0,0,0.3);"></canvas>
          </div>

          <div style="margin-top: 1.25rem;">
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Crop & Download Photo
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let img = null;
      let rotation = 0;
      let flipH = false;
      let cropRect = { x: 50, y: 50, w: 200, h: 200 };
      let isDragging = false;
      let dragMode = null;
      let startX, startY;
      let ratio = 'free';

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('crop-canvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            img = new Image();
            img.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              canvas.width = img.naturalWidth;
              canvas.height = img.naturalHeight;
              cropRect = {
                x: Math.round(img.naturalWidth * 0.1),
                y: Math.round(img.naturalHeight * 0.1),
                w: Math.round(img.naturalWidth * 0.8),
                h: Math.round(img.naturalHeight * 0.8)
              };
              draw();
            };
            img.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      document.querySelectorAll('.ratio-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.ratio-btn').forEach(b => { b.classList.remove('btn-primary'); b.classList.add('btn-secondary'); });
          btn.classList.add('btn-primary');
          btn.classList.remove('btn-secondary');
          ratio = btn.dataset.ratio;
          adjustCropForRatio();
          draw();
        });
      });

      function adjustCropForRatio() {
        if (ratio === '1:1') {
          const size = Math.min(cropRect.w, cropRect.h);
          cropRect.w = size; cropRect.h = size;
        } else if (ratio === '3.5:4.5') {
          cropRect.h = Math.round(cropRect.w * (4.5 / 3.5));
        } else if (ratio === '4:3') {
          cropRect.h = Math.round(cropRect.w * (3 / 4));
        } else if (ratio === '16:9') {
          cropRect.h = Math.round(cropRect.w * (9 / 16));
        }
      }

      document.getElementById('btn-rotate-cw').addEventListener('click', () => {
        rotation = (rotation + 90) % 360;
        draw();
      });
      document.getElementById('btn-flip-h').addEventListener('click', () => {
        flipH = !flipH;
        draw();
      });

      function draw() {
        if (!img) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

        ctx.fillStyle = 'rgba(0, 0, 0, 0.55)';
        ctx.fillRect(0, 0, canvas.width, cropRect.y);
        ctx.fillRect(0, cropRect.y + cropRect.h, canvas.width, canvas.height - (cropRect.y + cropRect.h));
        ctx.fillRect(0, cropRect.y, cropRect.x, cropRect.h);
        ctx.fillRect(cropRect.x + cropRect.w, cropRect.y, canvas.width - (cropRect.x + cropRect.w), cropRect.h);

        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.strokeRect(cropRect.x, cropRect.y, cropRect.w, cropRect.h);

        ctx.fillStyle = '#2563eb';
        ctx.fillRect(cropRect.x + cropRect.w - 12, cropRect.y + cropRect.h - 12, 14, 14);
        ctx.restore();
      }

      function getCanvasCoords(e) {
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        return {
          x: (e.clientX - rect.left) * scaleX,
          y: (e.clientY - rect.top) * scaleY
        };
      }

      canvas.addEventListener('mousedown', (e) => {
        const pt = getCanvasCoords(e);
        const handleX = cropRect.x + cropRect.w - 12;
        const handleY = cropRect.y + cropRect.h - 12;

        if (pt.x >= handleX && pt.x <= handleX + 24 && pt.y >= handleY && pt.y <= handleY + 24) {
          isDragging = true;
          dragMode = 'resize';
        } else if (pt.x >= cropRect.x && pt.x <= cropRect.x + cropRect.w && pt.y >= cropRect.y && pt.y <= cropRect.y + cropRect.h) {
          isDragging = true;
          dragMode = 'move';
          startX = pt.x - cropRect.x;
          startY = pt.y - cropRect.y;
        }
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const pt = getCanvasCoords(e);

        if (dragMode === 'move') {
          cropRect.x = Math.max(0, Math.min(canvas.width - cropRect.w, pt.x - startX));
          cropRect.y = Math.max(0, Math.min(canvas.height - cropRect.h, pt.y - startY));
        } else if (dragMode === 'resize') {
          cropRect.w = Math.max(50, Math.min(canvas.width - cropRect.x, pt.x - cropRect.x));
          if (ratio === 'free') {
            cropRect.h = Math.max(50, Math.min(canvas.height - cropRect.y, pt.y - cropRect.y));
          } else {
            adjustCropForRatio();
          }
        }
        draw();
      });

      window.addEventListener('mouseup', () => { isDragging = false; });

      downloadBtn.addEventListener('click', () => {
        if (!img) return;
        const outCanvas = document.createElement('canvas');
        outCanvas.width = cropRect.w;
        outCanvas.height = cropRect.h;
        const outCtx = outCanvas.getContext('2d');
        outCtx.drawImage(img, cropRect.x, cropRect.y, cropRect.w, cropRect.h, 0, 0, cropRect.w, cropRect.h);

        outCanvas.toBlob((blob) => {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'cropped-photo.jpg';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }, 'image/jpeg', 0.95);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Image Cropper (Passport & Social Ratios)", "Crop photos online with aspect ratios for Indian passport, SSC, and social media.", "crop.html", body)
    write_file("crop.html", html)

def build_convert():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#eff6ff; color:#2563eb; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Universal Client-Side Format Conversion
      </div>
      <h1 class="tool-header-title">Universal Image Converter</h1>
      <p class="tool-header-desc">Convert JPG, PNG, WebP, GIF, and BMP formats instantly in your browser. Single or batch conversion.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" multiple style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔄</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Images to Convert</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload one or multiple images (JPG, PNG, WebP, GIF, BMP)</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; justify-content: space-between;">
            <div>
              <label style="font-size: 0.88rem; font-weight: 600; margin-right: 0.5rem;">Convert To:</label>
              <select id="target-format" style="padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-size: 1rem; font-weight: 600;">
                <option value="image/jpeg">JPG / JPEG</option>
                <option value="image/png">PNG</option>
                <option value="image/webp">WebP</option>
              </select>
            </div>
            <button id="convert-all-btn" class="btn btn-primary">⚡ Convert All Images</button>
          </div>
        </div>

        <div id="items-list" style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;"></div>

        <div id="bulk-download-box" style="margin-top: 1.5rem; text-align: center; display: none;">
          <button id="zip-download-btn" class="btn btn-success" style="padding: 0.8rem 2rem; font-weight: 700;">
            📦 Download All Converted Files (ZIP)
          </button>
        </div>
      </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
    <script>
      let fileList = [];
      let convertedBlobs = [];

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const itemsList = document.getElementById('items-list');
      const targetFormat = document.getElementById('target-format');
      const convertAllBtn = document.getElementById('convert-all-btn');
      const zipDownloadBtn = document.getElementById('zip-download-btn');
      const bulkDownloadBox = document.getElementById('bulk-download-box');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
          fileList = Array.from(e.target.files);
          renderList();
          dropZone.style.display = 'none';
          controlsSection.style.display = 'block';
        }
      });

      function renderList() {
        itemsList.innerHTML = '';
        fileList.forEach((file, index) => {
          const item = document.createElement('div');
          item.style.cssText = 'background:white; border:1px solid #e2e8f0; border-radius:8px; padding:0.85rem 1.25rem; display:flex; justify-content:space-between; align-items:center;';
          item.innerHTML = '<div><strong style="color:#0f172a;">' + file.name + '</strong><div style="font-size:0.85rem; color:#64748b;">' + (file.size / 1024).toFixed(1) + ' KB</div></div><div id="status-' + index + '"><span class="badge badge-neutral">Ready</span></div>';
          itemsList.appendChild(item);
        });
      }

      convertAllBtn.addEventListener('click', async () => {
        convertAllBtn.disabled = true;
        convertAllBtn.textContent = 'Processing...';
        convertedBlobs = [];
        const format = targetFormat.value;
        const ext = format === 'image/png' ? 'png' : (format === 'image/webp' ? 'webp' : 'jpg');

        for (let i = 0; i < fileList.length; i++) {
          const file = fileList[i];
          const statusDiv = document.getElementById('status-' + i);
          statusDiv.innerHTML = '<span class="badge badge-info">Converting...</span>';

          const blob = await convertSingle(file, format);
          const baseName = file.name.substring(0, file.name.lastIndexOf('.')) || file.name;
          const newName = baseName + '.' + ext;
          convertedBlobs.push({ name: newName, blob });
          statusDiv.innerHTML = '<a href="' + URL.createObjectURL(blob) + '" download="' + newName + '" class="btn btn-sm btn-primary">Download ' + ext.toUpperCase() + '</a>';
        }

        convertAllBtn.disabled = false;
        convertAllBtn.textContent = '⚡ Re-Convert';
        bulkDownloadBox.style.display = 'block';
      });

      function convertSingle(file, format) {
        return new Promise((resolve) => {
          const reader = new FileReader();
          reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
              const canvas = document.createElement('canvas');
              canvas.width = img.naturalWidth;
              canvas.height = img.naturalHeight;
              const ctx = canvas.getContext('2d');
              if (format === 'image/jpeg') {
                ctx.fillStyle = '#ffffff';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
              }
              ctx.drawImage(img, 0, 0);
              canvas.toBlob(resolve, format, 0.92);
            };
            img.src = e.target.result;
          };
          reader.readAsDataURL(file);
        });
      }

      zipDownloadBtn.addEventListener('click', async () => {
        if (convertedBlobs.length === 0) return;
        const zip = new JSZip();
        convertedBlobs.forEach(item => {
          zip.file(item.name, item.blob);
        });
        const zipContent = await zip.generateAsync({ type: 'blob' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(zipContent);
        a.download = 'converted-images.zip';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });
    </script>"""
    html = wrap_page("Universal Image Converter (JPG, PNG, WebP)", "Convert image formats online in bulk. Free client-side JPG to PNG, PNG to JPG, WebP conversion.", "convert.html", body)
    write_file("convert.html", html)

def build_jpg_to_pdf():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#fef2f2; color:#dc2626; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Client-Side PDF Creation
      </div>
      <h1 class="tool-header-title">JPG to PDF Converter</h1>
      <p class="tool-header-desc">Convert and combine multiple JPG, PNG, and WebP images into a single standardized A4 PDF document with custom margins.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" multiple style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📄</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Images to Combine into PDF</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload one or multiple photos (JPG, PNG, WebP)</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Page Size:</label>
              <select id="page-size" style="width: 100%; padding: 0.5rem; border-radius: 6px; border: 1px solid #cbd5e1; font-weight: 600;">
                <option value="a4">A4 (Standard Document)</option>
                <option value="letter">Letter</option>
                <option value="fit">Fit to Image Size</option>
              </select>
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Page Orientation:</label>
              <select id="page-orientation" style="width: 100%; padding: 0.5rem; border-radius: 6px; border: 1px solid #cbd5e1; font-weight: 600;">
                <option value="portrait">Portrait (Vertical)</option>
                <option value="landscape">Landscape (Horizontal)</option>
                <option value="auto">Auto Match Each Image</option>
              </select>
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Margin:</label>
              <select id="page-margin" style="width: 100%; padding: 0.5rem; border-radius: 6px; border: 1px solid #cbd5e1;">
                <option value="0">No Margin (Full Bleed)</option>
                <option value="10" selected>Small Margin (10mm)</option>
                <option value="20">Big Margin (20mm)</option>
              </select>
            </div>
          </div>
        </div>

        <div style="margin-top: 1.5rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
            <h4 style="font-size: 1rem; font-weight: 700; color: #0f172a;">Selected Images (<span id="img-count">0</span>):</h4>
            <button type="button" class="btn btn-outline btn-sm" onclick="document.getElementById('file-input').click()">+ Add More Images</button>
          </div>
          <div id="image-list-container" style="display: flex; flex-direction: column; gap: 0.5rem; max-height: 350px; overflow-y: auto;"></div>
        </div>

        <div style="margin-top: 1.5rem; text-align: center;">
          <button id="generate-pdf-btn" class="btn btn-primary" style="padding: 0.85rem 2.5rem; font-size: 1.1rem; font-weight: 700;">
            📥 Convert & Download PDF
          </button>
        </div>
      </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script>
      let imagesData = [];

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const imageListContainer = document.getElementById('image-list-container');
      const imgCount = document.getElementById('img-count');
      const generatePdfBtn = document.getElementById('generate-pdf-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
          const files = Array.from(e.target.files);
          let loaded = 0;
          files.forEach(file => {
            const reader = new FileReader();
            reader.onload = (ev) => {
              const img = new Image();
              img.onload = () => {
                imagesData.push({
                  name: file.name,
                  src: ev.target.result,
                  width: img.naturalWidth,
                  height: img.naturalHeight
                });
                loaded++;
                if (loaded === files.length) {
                  renderImageList();
                  dropZone.style.display = 'none';
                  controlsSection.style.display = 'block';
                }
              };
              img.src = ev.target.result;
            };
            reader.readAsDataURL(file);
          });
        }
      });

      function renderImageList() {
        imageListContainer.innerHTML = '';
        imgCount.textContent = imagesData.length;
        imagesData.forEach((item, index) => {
          const row = document.createElement('div');
          row.style.cssText = 'background:#ffffff; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem 1rem; display:flex; align-items:center; justify-content:space-between; gap:1rem;';
          row.innerHTML = `
            <div style="display:flex; align-items:center; gap:0.75rem;">
              <span style="font-weight:700; color:#64748b; font-size:0.85rem; width:20px;">#${index + 1}</span>
              <img src="${item.src}" style="width:44px; height:44px; object-fit:cover; border-radius:6px; border:1px solid #cbd5e1;">
              <div>
                <strong style="font-size:0.9rem; color:#0f172a; display:block; max-width:240px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${item.name}</strong>
                <span style="font-size:0.78rem; color:#64748b;">${item.width} x ${item.height} px</span>
              </div>
            </div>
            <div style="display:flex; gap:0.25rem;">
              <button type="button" class="btn btn-outline btn-sm" onclick="moveImg(${index}, -1)" ${index === 0 ? 'disabled' : ''}>▲</button>
              <button type="button" class="btn btn-outline btn-sm" onclick="moveImg(${index}, 1)" ${index === imagesData.length - 1 ? 'disabled' : ''}>▼</button>
              <button type="button" class="btn btn-outline btn-sm" style="color:#dc2626;" onclick="removeImg(${index})">✕</button>
            </div>
          `;
          imageListContainer.appendChild(row);
        });
      }

      window.moveImg = function(index, direction) {
        const target = index + direction;
        if (target < 0 || target >= imagesData.length) return;
        const temp = imagesData[index];
        imagesData[index] = imagesData[target];
        imagesData[target] = temp;
        renderImageList();
      };

      window.removeImg = function(index) {
        imagesData.splice(index, 1);
        if (imagesData.length === 0) {
          dropZone.style.display = 'block';
          controlsSection.style.display = 'none';
        } else {
          renderImageList();
        }
      };

      generatePdfBtn.addEventListener('click', async () => {
        if (imagesData.length === 0) return;
        generatePdfBtn.disabled = true;
        generatePdfBtn.textContent = 'Generating PDF...';

        const { jsPDF } = window.jspdf;
        const size = document.getElementById('page-size').value;
        const orient = document.getElementById('page-orientation').value;
        const margin = parseInt(document.getElementById('page-margin').value, 10);

        let pdf = null;

        for (let i = 0; i < imagesData.length; i++) {
          const item = imagesData[i];
          let pageOrient = orient === 'auto' ? (item.width > item.height ? 'landscape' : 'portrait') : (orient === 'landscape' ? 'landscape' : 'portrait');
          
          if (i === 0) {
            pdf = new jsPDF({
              orientation: pageOrient,
              unit: 'mm',
              format: size === 'fit' ? [item.width * 0.264583, item.height * 0.264583] : size
            });
          } else {
            pdf.addPage(size === 'fit' ? [item.width * 0.264583, item.height * 0.264583] : size, pageOrient);
          }

          const pageWidth = pdf.internal.pageSize.getWidth();
          const pageHeight = pdf.internal.pageSize.getHeight();

          const availW = pageWidth - (margin * 2);
          const availH = pageHeight - (margin * 2);

          const imgRatio = item.width / item.height;
          let renderW = availW;
          let renderH = availW / imgRatio;

          if (renderH > availH) {
            renderH = availH;
            renderW = availH * imgRatio;
          }

          const posX = margin + (availW - renderW) / 2;
          const posY = margin + (availH - renderH) / 2;

          pdf.addImage(item.src, 'JPEG', posX, posY, renderW, renderH);
        }

        pdf.save('combined-images.pdf');
        generatePdfBtn.disabled = false;
        generatePdfBtn.textContent = '📥 Convert & Download PDF';
      });
    </script>"""
    html = wrap_page("JPG to PDF Converter (Combine Multiple Photos)", "Convert JPG images to single A4 PDF document online for free.", "jpg-to-pdf.html", body)
    write_file("jpg-to-pdf.html", html)

def build_remove_bg():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#fffbeb; color:#d97706; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Passport & Cyber Café Tool
      </div>
      <h1 class="tool-header-title">Passport Photo Background Changer</h1>
      <p class="tool-header-desc">Replace your photo background with Plain White, Light Sky Blue, or Red for Indian government exams & passport seva.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎭</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Passport Photo</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload photo with reasonably solid background</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.5rem;">Choose New Background Color:</label>
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
            <button type="button" class="btn btn-primary btn-sm bg-color-btn" data-color="#ffffff">Pure White (Govt / UPSC)</button>
            <button type="button" class="btn btn-secondary btn-sm bg-color-btn" data-color="#b0d4f1">Light Sky Blue</button>
            <button type="button" class="btn btn-secondary btn-sm bg-color-btn" data-color="#dc2626">Studio Red</button>
            <button type="button" class="btn btn-secondary btn-sm bg-color-btn" data-color="#475569">Slate Gray</button>
          </div>

          <div style="margin-bottom: 0.5rem;">
            <label style="font-size: 0.88rem; font-weight: 600;">Tolerance Threshold:</label>
            <input type="range" id="tolerance-slider" min="5" max="80" value="30" style="width: 100%;">
          </div>
          <p style="font-size: 0.8rem; color: var(--text-muted, #64748b);">Tip: Click directly on the photo background in the preview to select the exact background color to replace.</p>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: hidden; border-radius: 8px; border: 1px solid var(--border-subtle, #e2e8f0); background: #f8fafc; padding: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
            <canvas id="bg-canvas" style="max-width: 100%; max-height: 400px; cursor: crosshair;"></canvas>
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Updated Photo
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;
      let targetBgColor = '#ffffff';
      let sampleBgColor = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('bg-canvas');
      const ctx = canvas.getContext('2d');
      const toleranceSlider = document.getElementById('tolerance-slider');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              canvas.width = originalImg.naturalWidth;
              canvas.height = originalImg.naturalHeight;
              ctx.drawImage(originalImg, 0, 0);

              const p = ctx.getImageData(5, 5, 1, 1).data;
              sampleBgColor = { r: p[0], g: p[1], b: p[2] };
              processBg();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      document.querySelectorAll('.bg-color-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.bg-color-btn').forEach(b => { b.classList.remove('btn-primary'); b.classList.add('btn-secondary'); });
          btn.classList.add('btn-primary');
          btn.classList.remove('btn-secondary');
          targetBgColor = btn.dataset.color;
          processBg();
        });
      });

      toleranceSlider.addEventListener('input', processBg);

      canvas.addEventListener('click', (e) => {
        if (!originalImg) return;
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const x = Math.round((e.clientX - rect.left) * scaleX);
        const y = Math.round((e.clientY - rect.top) * scaleY);

        ctx.drawImage(originalImg, 0, 0);
        const p = ctx.getImageData(x, y, 1, 1).data;
        sampleBgColor = { r: p[0], g: p[1], b: p[2] };
        processBg();
      });

      function hexToRgb(hex) {
        const bigint = parseInt(hex.replace('#', ''), 16);
        return { r: (bigint >> 16) & 255, g: (bigint >> 8) & 255, b: bigint & 255 };
      }

      function processBg() {
        if (!originalImg || !sampleBgColor) return;
        ctx.drawImage(originalImg, 0, 0);
        const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const data = imgData.data;
        const tol = parseInt(toleranceSlider.value, 10) * 3;
        const replaceRgb = hexToRgb(targetBgColor);

        for (let i = 0; i < data.length; i += 4) {
          const r = data[i], g = data[i + 1], b = data[i + 2];
          const diff = Math.abs(r - sampleBgColor.r) + Math.abs(g - sampleBgColor.g) + Math.abs(b - sampleBgColor.b);
          if (diff <= tol) {
            data[i] = replaceRgb.r;
            data[i + 1] = replaceRgb.g;
            data[i + 2] = replaceRgb.b;
          }
        }
        ctx.putImageData(imgData, 0, 0);
      }

      downloadBtn.addEventListener('click', () => {
        canvas.toBlob((blob) => {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'passport-photo-bg.jpg';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }, 'image/jpeg', 0.95);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Passport Photo Background Changer", "Change photo background color to white or light blue for Indian exam forms and passport seva.", "remove-bg.html", body)
    write_file("remove-bg.html", html)

def build_blur_face():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#fef2f2; color:#dc2626; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        🔒 Privacy & Identity Protection
      </div>
      <h1 class="tool-header-title">Blur & Redact Image</h1>
      <p class="tool-header-desc">Censor sensitive Aadhaar card numbers, PAN card details, phone numbers, and blur faces before sharing documents.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔒</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Document or Photo to Redact</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload Aadhaar, PAN card, certificate, or identity photo</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; justify-content: space-between;">
            <div style="display: flex; gap: 0.5rem;">
              <button type="button" class="btn btn-primary btn-sm mode-btn" data-mode="pixelate">Pixelate / Mosaic</button>
              <button type="button" class="btn btn-secondary btn-sm mode-btn" data-mode="blackout">Solid Blackout</button>
            </div>
            <div>
              <button type="button" class="btn btn-outline btn-sm" id="undo-btn">↩️ Undo Last</button>
              <button type="button" class="btn btn-outline btn-sm" id="clear-btn">🗑️ Clear All</button>
            </div>
          </div>
          <p style="font-size: 0.82rem; color: var(--text-muted, #64748b); margin-top: 0.5rem;">Click and drag your mouse across any sensitive area to apply the censor stamp.</p>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: auto; text-align: center; background: #334155; padding: 1rem; border-radius: 8px;">
            <canvas id="censor-canvas" style="max-width: 100%; max-height: 500px; cursor: crosshair; box-shadow: 0 4px 12px rgba(0,0,0,0.3);"></canvas>
          </div>

          <div style="margin-top: 1.25rem;">
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Redacted Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Image
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;
      let censorHistory = [];
      let currentMode = 'pixelate';
      let isDrawing = false;
      let startX, startY;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('censor-canvas');
      const ctx = canvas.getContext('2d');
      const undoBtn = document.getElementById('undo-btn');
      const clearBtn = document.getElementById('clear-btn');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              canvas.width = originalImg.naturalWidth;
              canvas.height = originalImg.naturalHeight;
              censorHistory = [];
              redraw();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.mode-btn').forEach(b => { b.classList.remove('btn-primary'); b.classList.add('btn-secondary'); });
          btn.classList.add('btn-primary');
          btn.classList.remove('btn-secondary');
          currentMode = btn.dataset.mode;
        });
      });

      function getCoords(e) {
        const rect = canvas.getBoundingClientRect();
        return {
          x: Math.round((e.clientX - rect.left) * (canvas.width / rect.width)),
          y: Math.round((e.clientY - rect.top) * (canvas.height / rect.height))
        };
      }

      canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        const pt = getCoords(e);
        startX = pt.x;
        startY = pt.y;
      });

      canvas.addEventListener('mouseup', (e) => {
        if (!isDrawing) return;
        isDrawing = false;
        const pt = getCoords(e);
        const rect = {
          x: Math.min(startX, pt.x),
          y: Math.min(startY, pt.y),
          w: Math.abs(pt.x - startX),
          h: Math.abs(pt.y - startY),
          mode: currentMode
        };
        if (rect.w > 5 && rect.h > 5) {
          censorHistory.push(rect);
          redraw();
        }
      });

      undoBtn.addEventListener('click', () => {
        censorHistory.pop();
        redraw();
      });

      clearBtn.addEventListener('click', () => {
        censorHistory = [];
        redraw();
      });

      function redraw() {
        if (!originalImg) return;
        ctx.drawImage(originalImg, 0, 0);

        censorHistory.forEach(item => {
          if (item.mode === 'blackout') {
            ctx.fillStyle = '#000000';
            ctx.fillRect(item.x, item.y, item.w, item.h);
          } else {
            const blockSize = 14;
            const imgData = ctx.getImageData(item.x, item.y, item.w, item.h);
            const d = imgData.data;
            for (let py = 0; py < item.h; py += blockSize) {
              for (let px = 0; px < item.w; px += blockSize) {
                const pIndex = (py * item.w + px) * 4;
                const r = d[pIndex], g = d[pIndex + 1], b = d[pIndex + 2];
                for (let subY = py; subY < Math.min(py + blockSize, item.h); subY++) {
                  for (let subX = px; subX < Math.min(px + blockSize, item.w); subX++) {
                    const idx = (subY * item.w + subX) * 4;
                    d[idx] = r; d[idx + 1] = g; d[idx + 2] = b;
                  }
                }
              }
            }
            ctx.putImageData(imgData, item.x, item.y);
          }
        });
      }

      downloadBtn.addEventListener('click', () => {
        canvas.toBlob((blob) => {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'redacted-document.jpg';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }, 'image/jpeg', 0.95);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Blur & Redact Image (Aadhaar & Privacy)", "Censor sensitive information, Aadhaar card number, PAN number, and blur faces on photos.", "blur-face.html", body)
    write_file("blur-face.html", html)

def build_watermark():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#e0f2fe; color:#0284c7; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Text & Logo Stamp Protection
      </div>
      <h1 class="tool-header-title">Image Watermark Tool</h1>
      <p class="tool-header-desc">Protect your certificates, documents, and creative photos with custom text stamps or repeating watermarks.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💧</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Image to Watermark</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload photo or document image</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Watermark Text:</label>
              <input type="text" id="wm-text" value="DIGITALSAATHI" style="width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-weight: 600;">
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Font Size (px):</label>
              <input type="number" id="wm-size" value="48" min="12" max="200" style="width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1);">
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Opacity:</label>
              <input type="range" id="wm-opacity" min="5" max="100" value="40" style="width: 100%;">
            </div>
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;">
            <label style="font-size: 0.88rem; font-weight: 600;">Layout Style:</label>
            <select id="wm-style" style="padding: 0.45rem 0.75rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-size: 0.9rem;">
              <option value="diagonal-tile">Repeating Diagonal Tile (Maximum Security)</option>
              <option value="center">Single Center Watermark</option>
              <option value="bottom-right">Bottom-Right Corner</option>
            </select>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: auto; text-align: center; background: #334155; padding: 1rem; border-radius: 8px;">
            <canvas id="wm-canvas" style="max-width: 100%; max-height: 500px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);"></canvas>
          </div>

          <div style="margin-top: 1.25rem;">
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Watermarked Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('wm-canvas');
      const ctx = canvas.getContext('2d');
      const wmText = document.getElementById('wm-text');
      const wmSize = document.getElementById('wm-size');
      const wmOpacity = document.getElementById('wm-opacity');
      const wmStyle = document.getElementById('wm-style');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              canvas.width = originalImg.naturalWidth;
              canvas.height = originalImg.naturalHeight;
              draw();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      [wmText, wmSize, wmOpacity, wmStyle].forEach(el => el.addEventListener('input', draw));

      function draw() {
        if (!originalImg) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(originalImg, 0, 0);

        const text = wmText.value || 'WATERMARK';
        const size = parseInt(wmSize.value, 10) || 48;
        const opacity = (parseInt(wmOpacity.value, 10) || 40) / 100;
        const style = wmStyle.value;

        ctx.save();
        ctx.font = 'bold ' + size + 'px Inter, sans-serif';
        ctx.fillStyle = 'rgba(255, 255, 255, ' + opacity + ')';
        ctx.strokeStyle = 'rgba(0, 0, 0, ' + (opacity * 0.7) + ')';
        ctx.lineWidth = Math.max(1, size / 24);

        if (style === 'center') {
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.strokeText(text, canvas.width / 2, canvas.height / 2);
          ctx.fillText(text, canvas.width / 2, canvas.height / 2);
        } else if (style === 'bottom-right') {
          ctx.textAlign = 'right';
          ctx.textBaseline = 'bottom';
          ctx.strokeText(text, canvas.width - 20, canvas.height - 20);
          ctx.fillText(text, canvas.width - 20, canvas.height - 20);
        } else {
          ctx.rotate(-Math.PI / 4);
          const stepX = size * 6;
          const stepY = size * 3;
          for (let y = -canvas.height; y < canvas.height * 2; y += stepY) {
            for (let x = -canvas.width; x < canvas.width * 2; x += stepX) {
              ctx.strokeText(text, x, y);
              ctx.fillText(text, x, y);
            }
          }
        }
        ctx.restore();
      }

      downloadBtn.addEventListener('click', () => {
        canvas.toBlob((blob) => {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'watermarked-image.jpg';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }, 'image/jpeg', 0.95);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Image Watermark Tool", "Add custom text or logo watermark stamp to protect certificates and photos online.", "watermark.html", body)
    write_file("watermark.html", html)

def build_photo_enhancer():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#f0fdf4; color:#16a34a; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Document & Photo Clarity Filters
      </div>
      <h1 class="tool-header-title">Photo Enhancer & Scan Optimizer</h1>
      <p class="tool-header-desc">Enhance faint scanned documents, boost contrast, sharpen text, or convert to high-clarity black & white.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">✨</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Photo or Scanned Document</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload marksheet, xerox, certificate, or photo</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.25rem;">
            <button type="button" class="btn btn-primary btn-sm preset-filter" data-preset="doc">📄 Document Scan Optimizer</button>
            <button type="button" class="btn btn-secondary btn-sm preset-filter" data-preset="bw">⚫ Black & White</button>
            <button type="button" class="btn btn-secondary btn-sm preset-filter" data-preset="vivid">🌈 Vivid Colors</button>
            <button type="button" class="btn btn-outline btn-sm preset-filter" data-preset="reset">🔄 Reset</button>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Brightness:</label>
              <input type="range" id="b-slider" min="-100" max="100" value="0" style="width: 100%;">
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Contrast:</label>
              <input type="range" id="c-slider" min="-100" max="100" value="0" style="width: 100%;">
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Saturation:</label>
              <input type="range" id="s-slider" min="0" max="200" value="100" style="width: 100%;">
            </div>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: auto; text-align: center; background: #334155; padding: 1rem; border-radius: 8px;">
            <canvas id="filter-canvas" style="max-width: 100%; max-height: 500px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);"></canvas>
          </div>

          <div style="margin-top: 1.25rem;">
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Enhanced Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('filter-canvas');
      const ctx = canvas.getContext('2d');
      const bSlider = document.getElementById('b-slider');
      const cSlider = document.getElementById('c-slider');
      const sSlider = document.getElementById('s-slider');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              canvas.width = originalImg.naturalWidth;
              canvas.height = originalImg.naturalHeight;
              applyFilters();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      [bSlider, cSlider, sSlider].forEach(el => el.addEventListener('input', applyFilters));

      document.querySelectorAll('.preset-filter').forEach(btn => {
        btn.addEventListener('click', () => {
          const p = btn.dataset.preset;
          if (p === 'doc') {
            bSlider.value = 25;
            cSlider.value = 65;
            sSlider.value = 0;
          } else if (p === 'bw') {
            bSlider.value = 0;
            cSlider.value = 20;
            sSlider.value = 0;
          } else if (p === 'vivid') {
            bSlider.value = 5;
            cSlider.value = 25;
            sSlider.value = 140;
          } else if (p === 'reset') {
            bSlider.value = 0;
            cSlider.value = 0;
            sSlider.value = 100;
          }
          applyFilters();
        });
      });

      function applyFilters() {
        if (!originalImg) return;
        const b = parseInt(bSlider.value, 10);
        const c = parseInt(cSlider.value, 10);
        const s = parseInt(sSlider.value, 10);

        ctx.filter = 'brightness(' + (100 + b) + '%) contrast(' + (100 + c) + '%) saturate(' + s + '%)';
        ctx.drawImage(originalImg, 0, 0);
      }

      downloadBtn.addEventListener('click', () => {
        canvas.toBlob((blob) => {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'enhanced-photo.jpg';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }, 'image/jpeg', 0.95);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Photo Enhancer & Scan Optimizer", "Enhance document scans, sharpen xerox marksheet text, and boost photo clarity online.", "photo-enhancer.html", body)
    write_file("photo-enhancer.html", html)

def build_bulk_resize():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#ecfdf5; color:#059669; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ⚡ High-Speed Batch Processing
      </div>
      <h1 class="tool-header-title">Bulk Image Resizer & Compressor</h1>
      <p class="tool-header-desc">Upload up to 50 photos at once. Automatically compress, resize dimensions, and download all as a single ZIP archive.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" multiple style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Multiple Images (Up to 50)</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Supports batch JPG, PNG, and WebP processing</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Max Width (px):</label>
              <input type="number" id="max-w" value="1200" style="width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1);">
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Compression Quality:</label>
              <select id="bulk-quality" style="width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1);">
                <option value="0.8">Medium Quality (80%)</option>
                <option value="0.6">High Compression (60%)</option>
                <option value="0.95">Best Quality (95%)</option>
              </select>
            </div>
          </div>
          <button id="start-bulk-btn" class="btn btn-primary" style="width: 100%; font-weight: 700;">🚀 Process All Photos</button>
        </div>

        <div id="progress-bar-container" style="display: none; margin-top: 1.5rem;">
          <div style="background: #e2e8f0; border-radius: 9999px; height: 12px; overflow: hidden;">
            <div id="progress-fill" style="background: #2563eb; height: 100%; width: 0%; transition: width 0.2s;"></div>
          </div>
          <div id="progress-text" style="font-size: 0.85rem; color: #64748b; text-align: center; margin-top: 0.5rem;">Processing...</div>
        </div>

        <div id="bulk-download-box" style="margin-top: 1.5rem; text-align: center; display: none;">
          <button id="zip-download-btn" class="btn btn-success" style="padding: 0.85rem 2.5rem; font-size: 1.1rem; font-weight: 700;">
            📥 Download All as ZIP
          </button>
        </div>
      </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
    <script>
      let fileList = [];
      let processedList = [];

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const startBulkBtn = document.getElementById('start-bulk-btn');
      const progressBarContainer = document.getElementById('progress-bar-container');
      const progressFill = document.getElementById('progress-fill');
      const progressText = document.getElementById('progress-text');
      const bulkDownloadBox = document.getElementById('bulk-download-box');
      const zipDownloadBtn = document.getElementById('zip-download-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
          fileList = Array.from(e.target.files);
          dropZone.style.display = 'none';
          controlsSection.style.display = 'block';
        }
      });

      startBulkBtn.addEventListener('click', async () => {
        startBulkBtn.disabled = true;
        progressBarContainer.style.display = 'block';
        bulkDownloadBox.style.display = 'none';
        processedList = [];

        const maxW = parseInt(document.getElementById('max-w').value, 10) || 1200;
        const q = parseFloat(document.getElementById('bulk-quality').value) || 0.8;

        for (let i = 0; i < fileList.length; i++) {
          const file = fileList[i];
          progressText.textContent = 'Processing image ' + (i + 1) + ' of ' + fileList.length + ' (' + file.name + ')...';
          progressFill.style.width = Math.round(((i + 1) / fileList.length) * 100) + '%';

          const blob = await processSingle(file, maxW, q);
          const baseName = file.name.substring(0, file.name.lastIndexOf('.')) || file.name;
          processedList.push({ name: 'optimized-' + baseName + '.jpg', blob });
        }

        progressText.textContent = 'Completed ' + fileList.length + ' images successfully!';
        bulkDownloadBox.style.display = 'block';
        startBulkBtn.disabled = false;
      });

      function processSingle(file, maxW, q) {
        return new Promise((resolve) => {
          const reader = new FileReader();
          reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
              const canvas = document.createElement('canvas');
              let w = img.naturalWidth;
              let h = img.naturalHeight;
              if (w > maxW) {
                h = Math.round((h * maxW) / w);
                w = maxW;
              }
              canvas.width = w;
              canvas.height = h;
              const ctx = canvas.getContext('2d');
              ctx.drawImage(img, 0, 0, w, h);
              canvas.toBlob(resolve, 'image/jpeg', q);
            };
            img.src = e.target.result;
          };
          reader.readAsDataURL(file);
        });
      }

      zipDownloadBtn.addEventListener('click', async () => {
        const zip = new JSZip();
        processedList.forEach(item => zip.file(item.name, item.blob));
        const content = await zip.generateAsync({ type: 'blob' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(content);
        a.download = 'bulk-processed-images.zip';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });
    </script>"""
    html = wrap_page("Bulk Image Resizer & Compressor", "Batch compress and resize up to 50 images simultaneously and download as ZIP.", "bulk-resize.html", body)
    write_file("bulk-resize.html", html)

def build_rotate():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#eef2ff; color:#6366f1; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Instant Orientation Fix
      </div>
      <h1 class="tool-header-title">Rotate & Flip Image</h1>
      <p class="tool-header-desc">Fix sideways or upside-down photos, rotate 90°/180°, and mirror flip horizontally or vertically.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔄</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Image to Rotate</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload photo to correct orientation</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;">
            <button type="button" class="btn btn-secondary btn-sm" id="btn-ccw">↺ Rotate 90° Left</button>
            <button type="button" class="btn btn-primary btn-sm" id="btn-cw">↻ Rotate 90° Right</button>
            <button type="button" class="btn btn-secondary btn-sm" id="btn-180">🔃 Rotate 180°</button>
            <button type="button" class="btn btn-secondary btn-sm" id="btn-flip-h">↔️ Flip Horizontal</button>
            <button type="button" class="btn btn-secondary btn-sm" id="btn-flip-v">↕️ Flip Vertical</button>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: auto; text-align: center; background: #334155; padding: 1rem; border-radius: 8px;">
            <canvas id="rotate-canvas" style="max-width: 100%; max-height: 480px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);"></canvas>
          </div>

          <div style="margin-top: 1.25rem;">
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Rotated Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;
      let angle = 0;
      let flipH = 1;
      let flipV = 1;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('rotate-canvas');
      const ctx = canvas.getContext('2d');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              angle = 0; flipH = 1; flipV = 1;
              render();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      document.getElementById('btn-cw').addEventListener('click', () => { angle = (angle + 90) % 360; render(); });
      document.getElementById('btn-ccw').addEventListener('click', () => { angle = (angle + 270) % 360; render(); });
      document.getElementById('btn-180').addEventListener('click', () => { angle = (angle + 180) % 360; render(); });
      document.getElementById('btn-flip-h').addEventListener('click', () => { flipH *= -1; render(); });
      document.getElementById('btn-flip-v').addEventListener('click', () => { flipV *= -1; render(); });

      function render() {
        if (!originalImg) return;
        const rad = (angle * Math.PI) / 180;
        const sin = Math.abs(Math.sin(rad));
        const cos = Math.abs(Math.cos(rad));

        const w = originalImg.naturalWidth;
        const h = originalImg.naturalHeight;

        canvas.width = Math.round(w * cos + h * sin);
        canvas.height = Math.round(w * sin + h * cos);

        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.rotate(rad);
        ctx.scale(flipH, flipV);
        ctx.drawImage(originalImg, -w / 2, -h / 2);
        ctx.restore();
      }

      downloadBtn.addEventListener('click', () => {
        canvas.toBlob((blob) => {
          const a = document.createElement('a');
          a.href = URL.createObjectURL(blob);
          a.download = 'rotated-image.jpg';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        }, 'image/jpeg', 0.95);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Rotate & Flip Image Online", "Rotate and flip photos 90, 180 degrees, mirror flip horizontally in browser.", "rotate.html", body)
    write_file("rotate.html", html)

def build_color_picker():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#f5f3ff; color:#7c3aed; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        🎨 Eyedropper & Palette Extractor
      </div>
      <h1 class="tool-header-title">Image Color Picker & Palette</h1>
      <p class="tool-header-desc">Click anywhere on an image to extract exact HEX, RGB, and HSL color codes or auto-generate a dominant color palette.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎨</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose an Image to Pick Colors</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload photo, logo, or design banner</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem;">
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div id="swatch-preview" style="width: 54px; height: 54px; border-radius: 10px; border: 2px solid #cbd5e1; background: #2563eb;"></div>
            <div>
              <div id="hex-code" style="font-size: 1.3rem; font-weight: 800; color: #0f172a;">#2563eb</div>
              <div id="rgb-code" style="font-size: 0.85rem; color: #64748b;">rgb(37, 99, 235)</div>
            </div>
          </div>
          <button id="copy-hex-btn" class="btn btn-primary btn-sm">📋 Copy HEX Code</button>
        </div>

        <div style="margin-top: 1.25rem;">
          <h4 style="font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem; color: #0f172a;">Dominant Color Palette:</h4>
          <div id="palette-container" style="display: flex; flex-wrap: wrap; gap: 0.5rem;"></div>
        </div>

        <div class="tool-preview-panel">
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem;">Click on any pixel to inspect color:</p>
          <div style="max-width: 100%; overflow: auto; text-align: center; background: #f8fafc; padding: 0.5rem; border-radius: 8px; border: 1px solid #e2e8f0;">
            <canvas id="picker-canvas" style="max-width: 100%; max-height: 480px; cursor: crosshair;"></canvas>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;
      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const canvas = document.getElementById('picker-canvas');
      const ctx = canvas.getContext('2d');
      const swatchPreview = document.getElementById('swatch-preview');
      const hexCode = document.getElementById('hex-code');
      const rgbCode = document.getElementById('rgb-code');
      const copyHexBtn = document.getElementById('copy-hex-btn');
      const paletteContainer = document.getElementById('palette-container');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              canvas.width = originalImg.naturalWidth;
              canvas.height = originalImg.naturalHeight;
              ctx.drawImage(originalImg, 0, 0);
              extractPalette();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      canvas.addEventListener('click', (e) => {
        if (!originalImg) return;
        const rect = canvas.getBoundingClientRect();
        const x = Math.round((e.clientX - rect.left) * (canvas.width / rect.width));
        const y = Math.round((e.clientY - rect.top) * (canvas.height / rect.height));
        const p = ctx.getImageData(x, y, 1, 1).data;
        setColor(p[0], p[1], p[2]);
      });

      function rgbToHex(r, g, b) {
        return '#' + [r, g, b].map(x => x.toString(16).padStart(2, '0')).join('');
      }

      function setColor(r, g, b) {
        const hex = rgbToHex(r, g, b);
        swatchPreview.style.background = hex;
        hexCode.textContent = hex;
        rgbCode.textContent = 'rgb(' + r + ', ' + g + ', ' + b + ')';
      }

      copyHexBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(hexCode.textContent);
        copyHexBtn.textContent = '✓ Copied!';
        setTimeout(() => { copyHexBtn.textContent = '📋 Copy HEX Code'; }, 1500);
      });

      function extractPalette() {
        paletteContainer.innerHTML = '';
        const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
        const step = Math.max(1, Math.floor(imgData.length / 400));
        const samples = [];
        for (let i = 0; i < imgData.length; i += step * 4) {
          samples.push(rgbToHex(imgData[i], imgData[i + 1], imgData[i + 2]));
        }
        const unique = Array.from(new Set(samples)).slice(0, 8);
        unique.forEach(hex => {
          const chip = document.createElement('div');
          chip.style.cssText = 'background:' + hex + '; width:38px; height:38px; border-radius:8px; border:1px solid #cbd5e1; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);';
          chip.title = 'Click to copy ' + hex;
          chip.addEventListener('click', () => {
            navigator.clipboard.writeText(hex);
            hexCode.textContent = hex;
            swatchPreview.style.background = hex;
          });
          paletteContainer.appendChild(chip);
        });
      }
    </script>"""
    html = wrap_page("Image Color Picker & Palette Extractor", "Extract hex and rgb color codes from image online with loupe eyedropper.", "color-picker.html", body)
    write_file("color-picker.html", html)

def build_base64():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#f1f5f9; color:#475569; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        💻 Developer & Web Utility
      </div>
      <h1 class="tool-header-title">Image to Base64 Encoder</h1>
      <p class="tool-header-desc">Convert images to Base64 Data URI strings for HTML/CSS embedding or decode Base64 strings back to image files.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">💻</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Image to Encode</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Supports PNG, JPG, WebP, SVG</p>
      </div>

      <div id="controls-section" style="display: none; margin-top: 1.5rem;">
        <div>
          <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Data URI / Base64 Output:</label>
          <textarea id="base64-output" rows="6" style="width: 100%; padding: 0.75rem; font-family: monospace; font-size: 0.82rem; border-radius: 8px; border: 1px solid #cbd5e1;"></textarea>
        </div>

        <div style="display: flex; gap: 0.5rem; margin-top: 0.75rem;">
          <button id="copy-raw-btn" class="btn btn-primary btn-sm">📋 Copy Base64 String</button>
          <button id="copy-html-btn" class="btn btn-secondary btn-sm">📋 Copy &lt;img&gt; Tag</button>
          <button id="copy-css-btn" class="btn btn-secondary btn-sm">📋 Copy CSS url()</button>
        </div>
      </div>
    </div>

    <script>
      let base64String = '';
      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const base64Output = document.getElementById('base64-output');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            base64String = ev.target.result;
            base64Output.value = base64String;
            dropZone.style.display = 'none';
            controlsSection.style.display = 'block';
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      document.getElementById('copy-raw-btn').addEventListener('click', () => {
        navigator.clipboard.writeText(base64String);
        alert('Copied Base64 string to clipboard!');
      });
      document.getElementById('copy-html-btn').addEventListener('click', () => {
        navigator.clipboard.writeText('<img src="' + base64String + '" alt="Embedded Image" />');
        alert('Copied HTML <img> tag!');
      });
      document.getElementById('copy-css-btn').addEventListener('click', () => {
        navigator.clipboard.writeText("background-image: url('" + base64String + "');");
        alert('Copied CSS background-image!');
      });
    </script>"""
    html = wrap_page("Image to Base64 Encoder & Decoder", "Convert images to Base64 data URI string online with 1-click copy.", "base64.html", body)
    write_file("base64.html", html)

def build_dpi_converter():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#fffbeb; color:#d97706; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Official Government Form Compliance
      </div>
      <h1 class="tool-header-title">DPI / PPI Converter (300 DPI)</h1>
      <p class="tool-header-desc">Set photo resolution metadata to 200 DPI, 300 DPI, or 600 DPI required for UPSC, SSC, and passport portals.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/jpeg,image/jpg" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🖨️</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose JPEG Photo to Set DPI</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload photo to inject JFIF DPI header</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.5rem;">Target DPI Resolution:</label>
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
            <button type="button" class="btn btn-primary btn-sm dpi-btn" data-dpi="300">300 DPI (Standard Print & UPSC)</button>
            <button type="button" class="btn btn-secondary btn-sm dpi-btn" data-dpi="200">200 DPI (State PSC)</button>
            <button type="button" class="btn btn-secondary btn-sm dpi-btn" data-dpi="600">600 DPI (High Res Print)</button>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="margin-bottom: 1rem;">
            <span class="tool-stat-badge badge-stat-new" id="dpi-badge">Current Target: 300 DPI</span>
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download 300 DPI Photo
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalBytes = null;
      let targetDPI = 300;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');
      const dpiBadge = document.getElementById('dpi-badge');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalBytes = new Uint8Array(ev.target.result);
            dropZone.style.display = 'none';
            controlsSection.style.display = 'block';
          };
          reader.readAsArrayBuffer(e.target.files[0]);
        }
      });

      document.querySelectorAll('.dpi-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.dpi-btn').forEach(b => { b.classList.remove('btn-primary'); b.classList.add('btn-secondary'); });
          btn.classList.add('btn-primary');
          btn.classList.remove('btn-secondary');
          targetDPI = parseInt(btn.dataset.dpi, 10);
          dpiBadge.textContent = 'Current Target: ' + targetDPI + ' DPI';
          downloadBtn.textContent = '📥 Download ' + targetDPI + ' DPI Photo';
        });
      });

      function injectDpi(bytes, dpi) {
        const modified = new Uint8Array(bytes);
        for (let i = 0; i < modified.length - 10; i++) {
          if (modified[i] === 0xFF && modified[i + 1] === 0xE0 &&
              modified[i + 4] === 0x4A && modified[i + 5] === 0x46 && modified[i + 6] === 0x49 && modified[i + 7] === 0x46) {
            modified[i + 9] = 1;
            modified[i + 10] = (dpi >> 8) & 0xFF;
            modified[i + 11] = dpi & 0xFF;
            modified[i + 12] = (dpi >> 8) & 0xFF;
            modified[i + 13] = dpi & 0xFF;
            return modified;
          }
        }
        return modified;
      }

      downloadBtn.addEventListener('click', () => {
        if (!originalBytes) return;
        const modified = injectDpi(originalBytes, targetDPI);
        const blob = new Blob([modified], { type: 'image/jpeg' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'photo-' + targetDPI + 'dpi.jpg';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("DPI / PPI Converter (300 DPI for UPSC/SSC)", "Change photo DPI to 200 or 300 DPI for Indian exam forms without recompression.", "dpi-converter.html", body)
    write_file("dpi-converter.html", html)

def build_png_to_jpg():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#fff7ed; color:#ea580c; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Clean Background Filling
      </div>
      <h1 class="tool-header-title">PNG to JPG Converter</h1>
      <p class="tool-header-desc">Convert transparent or solid PNG graphics to clean, compressed JPG format with custom background color filling.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/png" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🖼️</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose PNG File to Convert</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload PNG image</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.5rem;">Background Fill for Transparent Areas:</label>
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
            <button type="button" class="btn btn-primary btn-sm bg-fill-btn" data-color="#ffffff">Solid White</button>
            <button type="button" class="btn btn-secondary btn-sm bg-fill-btn" data-color="#000000">Solid Black</button>
          </div>
          <div>
            <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">JPG Quality:</label>
            <input type="range" id="quality-slider" min="10" max="100" value="90" style="width: 100%;">
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: hidden; border-radius: 8px; border: 1px solid var(--border-subtle, #e2e8f0); background: #f8fafc; padding: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
            <img id="preview-img" style="max-width: 100%; max-height: 400px;" alt="Converted JPG Preview">
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download JPG Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Convert Another
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;
      let fillColor = '#ffffff';
      let convertedBlob = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const previewImg = document.getElementById('preview-img');
      const qualitySlider = document.getElementById('quality-slider');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              process();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      document.querySelectorAll('.bg-fill-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.bg-fill-btn').forEach(b => { b.classList.remove('btn-primary'); b.classList.add('btn-secondary'); });
          btn.classList.add('btn-primary');
          btn.classList.remove('btn-secondary');
          fillColor = btn.dataset.color;
          process();
        });
      });

      qualitySlider.addEventListener('input', process);

      function process() {
        if (!originalImg) return;
        const canvas = document.createElement('canvas');
        canvas.width = originalImg.naturalWidth;
        canvas.height = originalImg.naturalHeight;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = fillColor;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(originalImg, 0, 0);

        const q = parseInt(qualitySlider.value, 10) / 100;
        canvas.toBlob((blob) => {
          convertedBlob = blob;
          previewImg.src = URL.createObjectURL(blob);
        }, 'image/jpeg', q);
      }

      downloadBtn.addEventListener('click', () => {
        if (!convertedBlob) return;
        const a = document.createElement('a');
        a.href = URL.createObjectURL(convertedBlob);
        a.download = 'converted.jpg';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("PNG to JPG Converter (Custom Background)", "Convert PNG to JPG online for free. Fill transparent background with solid white.", "png-to-jpg.html", body)
    write_file("png-to-jpg.html", html)

def build_jpg_to_png():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#f5f3ff; color:#8b5cf6; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Lossless Quality Conversion
      </div>
      <h1 class="tool-header-title">JPG to PNG Converter</h1>
      <p class="tool-header-desc">Convert standard JPEG photos to crisp, uncompressed lossless PNG format with zero degradation.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/jpeg,image/jpg" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🖼️</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose JPG Photo to Convert</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload JPG/JPEG photo</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: hidden; border-radius: 8px; border: 1px solid var(--border-subtle, #e2e8f0); background: #f8fafc; padding: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
            <img id="preview-img" style="max-width: 100%; max-height: 400px;" alt="Converted PNG Preview">
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download PNG Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Convert Another
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let convertedBlob = null;
      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const previewImg = document.getElementById('preview-img');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            const img = new Image();
            img.onload = () => {
              const canvas = document.createElement('canvas');
              canvas.width = img.naturalWidth;
              canvas.height = img.naturalHeight;
              const ctx = canvas.getContext('2d');
              ctx.drawImage(img, 0, 0);
              canvas.toBlob((blob) => {
                convertedBlob = blob;
                previewImg.src = URL.createObjectURL(blob);
                dropZone.style.display = 'none';
                controlsSection.style.display = 'block';
              }, 'image/png');
            };
            img.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      downloadBtn.addEventListener('click', () => {
        if (!convertedBlob) return;
        const a = document.createElement('a');
        a.href = URL.createObjectURL(convertedBlob);
        a.download = 'converted.png';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("JPG to PNG Converter (Lossless)", "Convert JPG to PNG online for free in full original quality.", "jpg-to-png.html", body)
    write_file("jpg-to-png.html", html)

def build_webp():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#ecfeff; color:#0891b2; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ⚡ Next-Gen Web Optimization
      </div>
      <h1 class="tool-header-title">WebP Converter</h1>
      <p class="tool-header-desc">Convert JPG/PNG to next-gen WebP format (70% smaller size) or convert WebP back to JPG/PNG.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose Image to Convert</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Upload JPG, PNG, or WebP</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; justify-content: space-between;">
            <div>
              <label style="font-size: 0.88rem; font-weight: 600; margin-right: 0.5rem;">Target Format:</label>
              <select id="target-format" style="padding: 0.45rem 0.75rem; border-radius: 6px; border: 1px solid #cbd5e1; font-weight: 600;">
                <option value="image/webp">WebP (Next-Gen Web)</option>
                <option value="image/jpeg">JPG / JPEG</option>
                <option value="image/png">PNG</option>
              </select>
            </div>
            <div>
              <label style="font-size: 0.88rem; font-weight: 600; margin-right: 0.5rem;">Quality:</label>
              <input type="range" id="q-range" min="10" max="98" value="80" style="vertical-align: middle;">
            </div>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="max-width: 100%; overflow: hidden; border-radius: 8px; border: 1px solid var(--border-subtle, #e2e8f0); background: #f8fafc; padding: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
            <img id="preview-img" style="max-width: 100%; max-height: 400px;" alt="WebP Preview">
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Converted Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Convert Another
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalImg = null;
      let convertedBlob = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const targetFormat = document.getElementById('target-format');
      const qRange = document.getElementById('q-range');
      const previewImg = document.getElementById('preview-img');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (ev) => {
            originalImg = new Image();
            originalImg.onload = () => {
              dropZone.style.display = 'none';
              controlsSection.style.display = 'block';
              process();
            };
            originalImg.src = ev.target.result;
          };
          reader.readAsDataURL(e.target.files[0]);
        }
      });

      targetFormat.addEventListener('change', process);
      qRange.addEventListener('input', process);

      function process() {
        if (!originalImg) return;
        const canvas = document.createElement('canvas');
        canvas.width = originalImg.naturalWidth;
        canvas.height = originalImg.naturalHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(originalImg, 0, 0);

        const format = targetFormat.value;
        const q = parseInt(qRange.value, 10) / 100;
        canvas.toBlob((blob) => {
          convertedBlob = blob;
          previewImg.src = URL.createObjectURL(blob);
        }, format, q);
      }

      downloadBtn.addEventListener('click', () => {
        if (!convertedBlob) return;
        const ext = targetFormat.value === 'image/webp' ? 'webp' : (targetFormat.value === 'image/png' ? 'png' : 'jpg');
        const a = document.createElement('a');
        a.href = URL.createObjectURL(convertedBlob);
        a.download = 'image.' + ext;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("WebP Converter (JPG/PNG to WebP)", "Convert images to WebP for faster website loading or WebP back to JPG/PNG.", "webp-converter.html", body)
    write_file("webp-converter.html", html)

def main():
    print("Building all 17 Image Tools...")
    build_compress()
    build_resize()
    build_crop()
    build_convert()
    build_jpg_to_pdf()
    build_remove_bg()
    build_blur_face()
    build_watermark()
    build_photo_enhancer()
    build_bulk_resize()
    build_rotate()
    build_color_picker()
    build_base64()
    build_dpi_converter()
    build_png_to_jpg()
    build_jpg_to_png()
    build_webp()
    print("🎉 All image tool pages built successfully!")

if __name__ == "__main__":
    main()
