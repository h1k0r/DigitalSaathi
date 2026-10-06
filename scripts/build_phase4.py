#!/usr/bin/env python3
"""
DigitalSaathi — Phase 4: Image Tools Complete Builder
"""
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"
IMAGE_DIR = os.path.join(BASE_DIR, "image")
os.makedirs(IMAGE_DIR, exist_ok=True)

from make_image_suite import wrap_page, write_file
from build_image_pages import (
    build_crop, build_convert, build_jpg_to_pdf, build_remove_bg,
    build_blur_face, build_watermark, build_photo_enhancer, build_bulk_resize,
    build_rotate, build_color_picker, build_base64, build_dpi_converter,
    build_png_to_jpg, build_jpg_to_png, build_webp
)

def build_compress():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#ecfdf5; color:#059669; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Client-Side Compression &bull; Zero Quality Loss
      </div>
      <h1 class="tool-header-title">Free Image Compressor</h1>
      <p class="tool-header-desc">Reduce JPG, PNG & WebP image sizes strictly under 20KB, 50KB, 100KB for Indian exam forms or customize quality.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/jpeg,image/png,image/webp" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🗜️</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose an Image or Drag & Drop Here</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Supports JPG, JPEG, PNG, WebP up to 25 MB</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; margin-bottom: 1rem; gap: 0.5rem;">
            <div style="font-weight: 700; color: var(--text-main, #0f172a);">Compression Settings</div>
            <div id="file-info-badge" class="badge badge-neutral">Photo Loaded</div>
          </div>

          <div style="margin-bottom: 1.25rem;">
            <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-main, #0f172a);">Exam & Portal Target Size Presets:</label>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-target="20">Under 20 KB (SSC/IBPS Sig)</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-target="50">Under 50 KB (SSC Photo)</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-target="100">Under 100 KB (UPSC/NTA)</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-target="200">Under 200 KB</button>
              <button type="button" class="btn btn-outline btn-sm preset-btn active" data-target="custom">Custom Quality Slider</button>
            </div>
          </div>

          <div id="slider-box" style="margin-bottom: 1.25rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.4rem; font-size: 0.9rem; font-weight: 600;">
              <span>Image Quality:</span>
              <span id="quality-val" style="color: #2563eb;">75%</span>
            </div>
            <input type="range" id="quality-range" min="5" max="98" value="75" style="width: 100%; cursor: pointer;">
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;">
            <label style="font-size: 0.88rem; font-weight: 600;">Output Format:</label>
            <select id="format-select" style="padding: 0.45rem 0.75rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-size: 0.9rem;">
              <option value="image/jpeg">JPG / JPEG (Best for Photos & Forms)</option>
              <option value="image/webp">WebP (Smallest File Size)</option>
              <option value="image/png">PNG (Lossless)</option>
            </select>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span class="tool-stat-badge badge-stat-orig" id="stat-original">Original: 0 KB</span>
            <span class="tool-stat-badge badge-stat-new" id="stat-compressed">Compressed: 0 KB</span>
            <span class="tool-stat-badge badge-stat-saved" id="stat-savings">Saved: 0%</span>
          </div>

          <div style="max-width: 100%; overflow: hidden; border-radius: 8px; border: 1px solid var(--border-subtle, #e2e8f0); background: #f1f5f9; padding: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
            <img id="preview-img" style="max-width: 100%; max-height: 380px; object-fit: contain; border-radius: 6px;" alt="Compressed Preview">
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Compressed Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Choose Another Image
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalFile = null;
      let originalImage = null;
      let compressedBlob = null;
      let targetKB = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const qualityRange = document.getElementById('quality-range');
      const qualityVal = document.getElementById('quality-val');
      const formatSelect = document.getElementById('format-select');
      const previewImg = document.getElementById('preview-img');
      const statOriginal = document.getElementById('stat-original');
      const statCompressed = document.getElementById('stat-compressed');
      const statSavings = document.getElementById('stat-savings');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');
      const presetBtns = document.querySelectorAll('.preset-btn');

      ['dragenter', 'dragover'].forEach(name => {
        dropZone.addEventListener(name, (e) => { e.preventDefault(); dropZone.classList.add('drag-over'); });
      });
      ['dragleave', 'drop'].forEach(name => {
        dropZone.addEventListener(name, (e) => { e.preventDefault(); dropZone.classList.remove('drag-over'); });
      });
      dropZone.addEventListener('drop', (e) => {
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
          handleFile(e.dataTransfer.files[0]);
        }
      });
      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
          handleFile(e.target.files[0]);
        }
      });

      function formatBytes(bytes) {
        if (bytes < 1024) return bytes + ' B';
        if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
        return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
      }

      function handleFile(file) {
        if (!file.type.startsWith('image/')) {
          alert('Please upload a valid image file (JPG, PNG, WebP).');
          return;
        }
        originalFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
          originalImage = new Image();
          originalImage.onload = () => {
            dropZone.style.display = 'none';
            controlsSection.style.display = 'block';
            document.getElementById('file-info-badge').textContent = file.name + ' (' + originalImage.naturalWidth + 'x' + originalImage.naturalHeight + 'px)';
            statOriginal.textContent = 'Original: ' + formatBytes(file.size);
            processImage();
          };
          originalImage.src = e.target.result;
        };
        reader.readAsDataURL(file);
      }

      presetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          presetBtns.forEach(b => { b.classList.remove('active', 'btn-primary'); b.classList.add('btn-secondary'); });
          btn.classList.remove('btn-secondary');
          btn.classList.add('active', 'btn-primary');
          const t = btn.dataset.target;
          targetKB = (t === 'custom') ? null : parseInt(t, 10);
          processImage();
        });
      });

      qualityRange.addEventListener('input', () => {
        qualityVal.textContent = qualityRange.value + '%';
        targetKB = null;
        presetBtns.forEach(b => {
          if (b.dataset.target === 'custom') {
            b.classList.add('active', 'btn-primary');
            b.classList.remove('btn-secondary');
          } else {
            b.classList.remove('active', 'btn-primary');
            b.classList.add('btn-secondary');
          }
        });
        processImage();
      });

      formatSelect.addEventListener('change', processImage);

      function processImage() {
        if (!originalImage) return;

        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        const format = formatSelect.value;

        let width = originalImage.naturalWidth;
        let height = originalImage.naturalHeight;

        if (targetKB) {
          let scale = 1.0;
          if (targetKB <= 20) {
            scale = Math.min(1.0, 400 / Math.max(width, height));
          } else if (targetKB <= 50) {
            scale = Math.min(1.0, 800 / Math.max(width, height));
          } else if (targetKB <= 100) {
            scale = Math.min(1.0, 1200 / Math.max(width, height));
          }
          canvas.width = Math.round(width * scale);
          canvas.height = Math.round(height * scale);
          ctx.drawImage(originalImage, 0, 0, canvas.width, canvas.height);

          let minQ = 0.05, maxQ = 0.95;
          function iterate(attempts) {
            const currentQ = (minQ + maxQ) / 2;
            canvas.toBlob((blob) => {
              if (!blob) return;
              const kb = blob.size / 1024;
              if (attempts > 0 && Math.abs(kb - targetKB) > (targetKB * 0.1)) {
                if (kb > targetKB) maxQ = currentQ;
                else minQ = currentQ;
                iterate(attempts - 1);
              } else {
                finishBlob(blob);
              }
            }, format, currentQ);
          }
          iterate(5);
        } else {
          canvas.width = width;
          canvas.height = height;
          ctx.drawImage(originalImage, 0, 0, width, height);
          const quality = parseInt(qualityRange.value, 10) / 100;
          canvas.toBlob(finishBlob, format, quality);
        }
      }

      function finishBlob(blob) {
        if (!blob) return;
        compressedBlob = blob;
        previewImg.src = URL.createObjectURL(blob);
        statCompressed.textContent = 'Compressed: ' + formatBytes(blob.size);

        const savedBytes = originalFile.size - blob.size;
        const savedPercent = Math.max(0, Math.round((savedBytes / originalFile.size) * 100));
        statSavings.textContent = 'Reduced by: ' + savedPercent + '% (' + formatBytes(Math.max(0, savedBytes)) + ')';
      }

      downloadBtn.addEventListener('click', () => {
        if (!compressedBlob) return;
        const ext = formatSelect.value === 'image/png' ? 'png' : (formatSelect.value === 'image/webp' ? 'webp' : 'jpg');
        const origBase = originalFile.name.substring(0, originalFile.name.lastIndexOf('.')) || originalFile.name;
        const filename = origBase + '-compressed.' + ext;
        const a = document.createElement('a');
        a.href = URL.createObjectURL(compressedBlob);
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
      });

      resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        originalFile = null;
        originalImage = null;
        compressedBlob = null;
        dropZone.style.display = 'block';
        controlsSection.style.display = 'none';
      });
    </script>"""
    html = wrap_page("Image Compressor (Under 20KB, 50KB, 100KB)", "Compress JPG, PNG, and WebP photos online for free. Dedicated presets for SSC, UPSC, and government exams.", "compress.html", body)
    write_file("compress.html", html)

def build_resize():
    body = """    <div class="tool-header-box">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:#eff6ff; color:#2563eb; padding:0.3rem 0.75rem; border-radius:9999px; font-size:0.8rem; font-weight:700; margin-bottom:0.75rem;">
        ✓ Exact Pixel & Exam Preset Scaling
      </div>
      <h1 class="tool-header-title">Image Resizer</h1>
      <p class="tool-header-desc">Resize image dimensions in pixels or percentage. Pre-configured presets for SSC (140x160px), UPSC, and passport photos.</p>
    </div>

    <div class="tool-main-card">
      <div class="tool-upload-box" id="drop-zone" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*" style="display: none;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📐</div>
        <h3 style="font-size: 1.2rem; font-weight: 700; color: var(--text-main, #0f172a); margin-bottom: 0.35rem;">Choose an Image to Resize</h3>
        <p style="color: var(--text-muted, #64748b); font-size: 0.9rem;">Supports JPG, PNG, WebP, GIF</p>
      </div>

      <div id="controls-section" style="display: none;">
        <div class="tool-controls-panel">
          <div style="margin-bottom: 1.25rem;">
            <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.5rem;">Quick Exam & Social Presets:</label>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-w="140" data-h="160">SSC Photo (140x160)</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-w="140" data-h="60">SSC/IBPS Sig (140x60)</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-w="350" data-h="350">UPSC Photo (350x350)</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-w="413" data-h="531">Passport 3.5x4.5cm</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-w="1280" data-h="720">YouTube 720p</button>
              <button type="button" class="btn btn-secondary btn-sm preset-btn" data-w="1080" data-h="1080">Instagram 1:1</button>
            </div>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Width (Pixels):</label>
              <input type="number" id="input-width" min="10" max="10000" style="width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-size: 1rem;">
            </div>
            <div>
              <label style="display: block; font-size: 0.88rem; font-weight: 600; margin-bottom: 0.35rem;">Height (Pixels):</label>
              <input type="number" id="input-height" min="10" max="10000" style="width: 100%; padding: 0.6rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-size: 1rem;">
            </div>
          </div>

          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.25rem;">
            <input type="checkbox" id="lock-aspect" checked style="width: 18px; height: 18px; cursor: pointer;">
            <label for="lock-aspect" style="font-size: 0.9rem; font-weight: 600; cursor: pointer;">Maintain Aspect Ratio (Proportions)</label>
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: center;">
            <label style="font-size: 0.88rem; font-weight: 600;">Format:</label>
            <select id="format-select" style="padding: 0.45rem 0.75rem; border-radius: 6px; border: 1px solid var(--border-default, #cbd5e1); font-size: 0.9rem;">
              <option value="image/jpeg">JPG / JPEG</option>
              <option value="image/png">PNG</option>
              <option value="image/webp">WebP</option>
            </select>
          </div>
        </div>

        <div class="tool-preview-panel">
          <div style="margin-bottom: 1rem;">
            <span class="tool-stat-badge badge-stat-orig" id="orig-dim-badge">Original: 0x0 px</span>
            <span class="tool-stat-badge badge-stat-new" id="new-dim-badge">New: 0x0 px</span>
          </div>

          <div style="max-width: 100%; overflow: hidden; border-radius: 8px; border: 1px solid var(--border-subtle, #e2e8f0); background: #f1f5f9; padding: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
            <img id="preview-img" style="max-width: 100%; max-height: 380px; object-fit: contain; border-radius: 6px;" alt="Resized Preview">
          </div>

          <div>
            <button id="download-btn" class="btn btn-primary" style="padding: 0.8rem 2rem; font-size: 1.05rem; font-weight: 700;">
              📥 Download Resized Image
            </button>
            <button id="reset-btn" class="btn btn-secondary" style="padding: 0.8rem 1.25rem; font-size: 0.95rem; margin-left: 0.5rem;">
              🔄 Change Photo
            </button>
          </div>
        </div>
      </div>
    </div>

    <script>
      let originalFile = null;
      let originalImg = null;
      let aspectRatio = 1.0;
      let resizedBlob = null;

      const fileInput = document.getElementById('file-input');
      const dropZone = document.getElementById('drop-zone');
      const controlsSection = document.getElementById('controls-section');
      const inputWidth = document.getElementById('input-width');
      const inputHeight = document.getElementById('input-height');
      const lockAspect = document.getElementById('lock-aspect');
      const formatSelect = document.getElementById('format-select');
      const previewImg = document.getElementById('preview-img');
      const origDimBadge = document.getElementById('orig-dim-badge');
      const newDimBadge = document.getElementById('new-dim-badge');
      const downloadBtn = document.getElementById('download-btn');
      const resetBtn = document.getElementById('reset-btn');
      const presetBtns = document.querySelectorAll('.preset-btn');

      fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) handleFile(e.target.files[0]);
      });

      function handleFile(file) {
        originalFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
          originalImg = new Image();
          originalImg.onload = () => {
            aspectRatio = originalImg.naturalWidth / originalImg.naturalHeight;
            inputWidth.value = originalImg.naturalWidth;
            inputHeight.value = originalImg.naturalHeight;
            origDimBadge.textContent = 'Original: ' + originalImg.naturalWidth + 'x' + originalImg.naturalHeight + ' px';
            dropZone.style.display = 'none';
            controlsSection.style.display = 'block';
            updateResize();
          };
          originalImg.src = e.target.result;
        };
        reader.readAsDataURL(file);
      }

      inputWidth.addEventListener('input', () => {
        if (lockAspect.checked && originalImg) {
          inputHeight.value = Math.round(parseInt(inputWidth.value || 0) / aspectRatio);
        }
        updateResize();
      });

      inputHeight.addEventListener('input', () => {
        if (lockAspect.checked && originalImg) {
          inputWidth.value = Math.round(parseInt(inputHeight.value || 0) * aspectRatio);
        }
        updateResize();
      });

      presetBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          lockAspect.checked = false;
          inputWidth.value = btn.dataset.w;
          inputHeight.value = btn.dataset.h;
          updateResize();
        });
      });

      formatSelect.addEventListener('change', updateResize);

      function updateResize() {
        if (!originalImg) return;
        const w = parseInt(inputWidth.value, 10) || 100;
        const h = parseInt(inputHeight.value, 10) || 100;
        newDimBadge.textContent = 'New: ' + w + 'x' + h + ' px';

        const canvas = document.createElement('canvas');
        canvas.width = w;
        canvas.height = h;
        const ctx = canvas.getContext('2d');
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(originalImg, 0, 0, w, h);

        const format = formatSelect.value;
        canvas.toBlob((blob) => {
          resizedBlob = blob;
          previewImg.src = URL.createObjectURL(blob);
        }, format, 0.92);
      }

      downloadBtn.addEventListener('click', () => {
        if (!resizedBlob) return;
        const ext = formatSelect.value === 'image/png' ? 'png' : (formatSelect.value === 'image/webp' ? 'webp' : 'jpg');
        const a = document.createElement('a');
        a.href = URL.createObjectURL(resizedBlob);
        a.download = 'resized-' + inputWidth.value + 'x' + inputHeight.value + '.' + ext;
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
    html = wrap_page("Image Resizer (Exact Pixels & Exam Presets)", "Resize image width and height online. Presets for SSC, UPSC, IBPS, and social media.", "resize.html", body)
    write_file("resize.html", html)

def main():
    print("Building entire DigitalSaathi Phase 4 Image Tools Suite...")
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
    print("🎉 ALL 17 Image Tools Successfully Generated!")

if __name__ == "__main__":
    main()
