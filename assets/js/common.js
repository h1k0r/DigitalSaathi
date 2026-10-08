/* ==========================================================================
   VYTRA — MASTER JAVASCRIPT SYSTEM (v2.0 Production)
   "Your Digital Tools Suite for Everyone"
   ========================================================================== */

(function () {
  'use strict';

  // Automatically remove /index.html from URL bar for clean, professional URLs
  try {
    if (window.location.pathname.endsWith('/index.html')) {
      const cleanPath = window.location.pathname.replace(/\/index\.html$/, '/') + window.location.search + window.location.hash;
      window.history.replaceState(null, '', cleanPath);
    }
  } catch (e) {
    // Ignore in non-browser/restricted contexts
  }

  // ==========================================================================
  // 1. MASTER TOOL & ROUTE REGISTRY (Global Instant Search Database)
  // ==========================================================================
  const SEARCH_REGISTRY = [
    // PDF Tools - Organize
    { title: 'Merge PDF', category: 'PDF Tools', icon: '📑', url: 'pdf/merge.html', keywords: 'combine join merge multiple pdfs into one document' },
    { title: 'Split PDF', category: 'PDF Tools', icon: '✂️', url: 'pdf/split.html', keywords: 'split separate extract pages from pdf document' },
    { title: 'Organize PDF', category: 'PDF Tools', icon: '📑', url: 'pdf/organize.html', keywords: 'reorganize reorder delete add rotate pages in pdf' },
    { title: 'Rotate PDF', category: 'PDF Tools', icon: '🔄', url: 'pdf/rotate.html', keywords: 'rotate orientation landscape portrait 90 180 degrees' },
    { title: 'Crop PDF', category: 'PDF Tools', icon: '📐', url: 'pdf/crop.html', keywords: 'crop margins trim page size box bounding area' },
    { title: 'Page Numbers', category: 'PDF Tools', icon: '🔢', url: 'pdf/page-numbers.html', keywords: 'add page numbers footer header numbering roman' },
    { title: 'Extract Pages', category: 'PDF Tools', icon: '📥', url: 'pdf/extract.html', keywords: 'extract specific page range separate download' },
    { title: 'Reorder Pages', category: 'PDF Tools', icon: '🔀', url: 'pdf/reorder.html', keywords: 'drag reorder sort rearrange pdf pages' },

    // PDF Tools - Convert
    { title: 'PDF to Word Converter', category: 'PDF Tools', icon: '📝', url: 'pdf/pdf-to-word.html', keywords: 'convert pdf to docx word editable document pdf to word pdf to word converter pdf to word online convert pdf to word pdf to docx convert pdf to docx pdf to word editable extract text from pdf to docx pdf to word online free' },
    { title: 'PDF to PowerPoint', category: 'PDF Tools', icon: '📊', url: 'pdf/pdf-to-ppt.html', keywords: 'convert pdf to pptx powerpoint presentation slides pdf to powerpoint pdf to ppt pdf to pptx convert pdf to powerpoint pdf slides to pptx' },
    { title: 'PDF to Excel', category: 'PDF Tools', icon: '📈', url: 'pdf/pdf-to-excel.html', keywords: 'convert pdf table to xlsx excel spreadsheet csv pdf to excel pdf to excel converter pdf to xlsx convert pdf to excel pdf tables to excel' },
    { title: 'Word to PDF', category: 'PDF Tools', icon: '📄', url: 'pdf/word-to-pdf.html', keywords: 'convert docx word document to pdf format word to pdf word to pdf converter docx to pdf convert docx to pdf convert word to pdf online free' },
    { title: 'PowerPoint to PDF', category: 'PDF Tools', icon: '📽️', url: 'pdf/ppt-to-pdf.html', keywords: 'convert ppt pptx powerpoint slides to pdf document powerpoint to pdf ppt to pdf pptx to pdf convert powerpoint to pdf' },
    { title: 'Excel to PDF', category: 'PDF Tools', icon: '📊', url: 'pdf/excel-to-pdf.html', keywords: 'convert xls xlsx excel spreadsheet to pdf table excel to pdf xlsx to pdf convert xlsx to pdf convert excel to pdf online' },
    { title: 'PDF to JPG Converter', category: 'PDF Tools', icon: '🖼️', url: 'pdf/pdf-to-jpg.html', keywords: 'convert pdf pages images jpg png zip download pdf to jpg pdf to jpg converter pdf to jpg online pdf to jpg online free convert pdf to jpg pdf to jpeg pdf to jpeg converter pdf to png pdf to png converter pdf to png online convert pdf to png pdf to image pdf to image converter convert pdf to image pdf pages to jpg pdf pages to png extract images from pdf save pdf as jpg turn pdf into image convert pdf pages to images' },
    { title: 'JPG to PDF Converter', category: 'PDF Tools', icon: '📑', url: 'pdf/jpg-to-pdf.html', keywords: 'convert photos image jpg png to pdf document combine a4 image to pdf image to pdf converter convert image to pdf image to pdf online image to pdf online free image to pdf free photo to pdf photo to pdf converter picture to pdf picture to pdf converter convert picture to pdf images to pdf images to pdf converter convert images to pdf image converter to pdf make pdf from image make pdf from photos create pdf from images turn image into pdf turn photos into pdf' },
    { title: 'HTML to PDF Converter', category: 'PDF Tools', icon: '🌐', url: 'pdf/html-to-pdf.html', keywords: 'convert html web page code url to pdf document' },
    { title: 'PDF/A Converter', category: 'PDF Tools', icon: '🏛️', url: 'pdf/pdf-a.html', keywords: 'pdfa pdf a archive standard preservation iso long term' },
    { title: 'PDF to Markdown', category: 'PDF Tools', icon: '📑', url: 'pdf/pdf-to-markdown.html', keywords: 'extract markdown md formatting text headings code' },

    // PDF Tools - Optimize & Edit
    { title: 'PDF Compressor', category: 'PDF Tools', icon: '🗜️', url: 'pdf/compress.html', keywords: 'reduce size compress pdf kb mb 100kb shrink form upload' },
    { title: 'Repair PDF', category: 'PDF Tools', icon: '🔧', url: 'pdf/repair.html', keywords: 'fix corrupt broken damaged pdf header cross reference table' },
    { title: 'Edit PDF', category: 'PDF Tools', icon: '✏️', url: 'pdf/edit.html', keywords: 'edit pdf add text shapes images annotations highlight' },
    { title: 'Sign PDF', category: 'PDF Tools', icon: '✍️', url: 'pdf/sign.html', keywords: 'draw signature sign contract digital document' },
    { title: 'Watermark PDF', category: 'PDF Tools', icon: '💧', url: 'pdf/watermark.html', keywords: 'add watermark text confidential logo stamp angle opacity' },
    { title: 'Redact PDF', category: 'PDF Tools', icon: '⬛', url: 'pdf/redact.html', keywords: 'redact black out sensitive personal data hide privacy' },
    { title: 'PDF Forms', category: 'PDF Tools', icon: '📋', url: 'pdf/forms.html', keywords: 'fill pdf forms textfields checkboxes export form data' },

    // PDF Tools - Security, OCR & Analysis
    { title: 'Protect PDF', category: 'PDF Tools', icon: '🔒', url: 'pdf/protect.html', keywords: 'encrypt password protect secure restrict permissions' },
    { title: 'Unlock PDF', category: 'PDF Tools', icon: '🔓', url: 'pdf/unlock.html', keywords: 'remove password unlock decrypt open protected pdf' },
    { title: 'Scan to PDF', category: 'PDF Tools', icon: '📷', url: 'pdf/scan-to-pdf.html', keywords: 'camera scan document paper to pdf mobile web' },
    { title: 'OCR PDF (Text Recognition)', category: 'PDF Tools', icon: '👁️', url: 'pdf/ocr.html', keywords: 'ocr recognize text scanned image searchable extract' },
    { title: 'Compare PDF', category: 'PDF Tools', icon: '🔍', url: 'pdf/compare.html', keywords: 'compare two pdf documents side by side difference diff' },
    { title: 'PDF Information & Metadata', category: 'PDF Tools', icon: 'ℹ️', url: 'pdf/info.html', keywords: 'metadata author title subject fonts inspect page count' },
    { title: 'PDF Viewer & Reader', category: 'PDF Tools', icon: '👁️', url: 'pdf/viewer.html', keywords: 'view read inspect search zoom preview pdf online' },
    { title: 'PDF Page Counter & Stats', category: 'PDF Tools', icon: '🔢', url: 'pdf/page-counter.html', keywords: 'count pages words metadata fast analyze inspect' },
    { title: 'AI PDF Summarizer', category: 'PDF Tools', icon: '🤖', url: 'pdf/ai-summarizer.html', keywords: 'summarize key points insights client side ai extract overview' },
    { title: 'Translate PDF', category: 'PDF Tools', icon: '🌐', url: 'pdf/translate.html', keywords: 'translate language hindi english marathi bengali tamil' },
    { title: 'Create PDF Workflow', category: 'PDF Tools', icon: '⚡', url: 'pdf/workflow.html', keywords: 'automate chained pipeline merge compress convert batch' },
    { title: 'All PDF Tools Suite', category: 'PDF Tools', icon: '✨', url: 'pdf/index.html', keywords: 'all 38 pdf tools online free client side' },

    // Image Tools
    { title: 'Image HD Converter (4K & 1080p)', category: 'Image Tools', icon: '✨', url: 'image/hd-converter.html', keywords: 'image hd converter 1080p 2k 4k ultra hd upscale sharpen unsharp mask blur resolution' },
    { title: 'Image Compressor (Under 20KB/50KB/100KB)', category: 'Image Tools', icon: '🗜️', url: 'image/compress.html', keywords: 'compress photo reduce size quality slider webp jpg png ssc upsc kb' },
    { title: 'Image Resizer (Pixel & Exam Scale)', category: 'Image Tools', icon: '📐', url: 'image/resize.html', keywords: 'resize image dimensions width height aspect ratio ssc upsc custom' },
    { title: 'Image Cropper', category: 'Image Tools', icon: '✂️', url: 'image/crop.html', keywords: 'crop photo passport 3.5x4.5 ratio square 1:1 circular avatar landscape' },
    { title: 'Universal Image Converter', category: 'Image Tools', icon: '🔄', url: 'image/convert.html', keywords: 'convert image format batch zip jpg png webp gif bmp' },
    { title: 'JPG to PDF Converter', category: 'Image Tools', icon: '📄', url: 'image/jpg-to-pdf.html', keywords: 'convert jpg images to pdf combine multiple photos a4 document image to pdf image to pdf converter convert image to pdf image to pdf online image to pdf online free image to pdf free photo to pdf photo to pdf converter picture to pdf picture to pdf converter convert picture to pdf images to pdf images to pdf converter convert images to pdf image converter to pdf make pdf from image make pdf from photos create pdf from images turn image into pdf turn photos into pdf' },
    { title: 'Remove Background in HD Quality', category: 'Image Tools', icon: '✂️', url: 'image/remove-bg.html', keywords: 'remove background hd transparent png cutout photo eraser pure white passport seva exam remove background hd remove bg in hd quality transparent png maker photo background eraser white background photo maker passport background changer online free' },
    { title: 'Blur & Redact Censor Tool', category: 'Image Tools', icon: '🔒', url: 'image/blur-face.html', keywords: 'blur redact pixelate censor aadhaar pan card number face identity' },
    { title: 'Image Watermark Tool', category: 'Image Tools', icon: '💧', url: 'image/watermark.html', keywords: 'watermark stamp copyright protection diagonal tile logo text photo' },
    { title: 'Photo Enhancer & Scan Optimizer', category: 'Image Tools', icon: '✨', url: 'image/photo-enhancer.html', keywords: 'enhance clarify scan xerox marksheet text boost contrast filter' },
    { title: 'Bulk Image Resizer & Compressor', category: 'Image Tools', icon: '⚡', url: 'image/bulk-resize.html', keywords: 'bulk batch resize compress multiple 50 images zip download' },
    { title: 'Rotate & Flip Image', category: 'Image Tools', icon: '🔄', url: 'image/rotate.html', keywords: 'rotate 90 180 degrees flip horizontal mirror selfie vertical' },
    { title: 'Image Color Picker & Palette', category: 'Image Tools', icon: '🎨', url: 'image/color-picker.html', keywords: 'color picker eyedropper extract palette hex rgb hsl loupe' },
    { title: 'Image to Base64 Encoder', category: 'Image Tools', icon: '💻', url: 'image/base64.html', keywords: 'image to base64 data uri html img css background string decode' },
    { title: 'DPI / PPI Converter (300 DPI)', category: 'Image Tools', icon: '🖨️', url: 'image/dpi-converter.html', keywords: 'dpi converter 200 300 600 ppi upsc ssc exam print jfif header' },
    { title: 'PNG to JPG Converter', category: 'Image Tools', icon: '🖼️', url: 'image/png-to-jpg.html', keywords: 'png to jpg convert white background transparent fill quality png to jpg png to jpg converter convert png to jpg convert png with white background' },
    { title: 'JPG to PNG Converter', category: 'Image Tools', icon: '🖼️', url: 'image/jpg-to-png.html', keywords: 'jpg to png convert lossless original quality uncompressed jpg to png jpg to png converter jpg to png online convert jpg to png' },
    { title: 'WebP Converter', category: 'Image Tools', icon: '⚡', url: 'image/webp-converter.html', keywords: 'webp converter convert to webp 70 percent smaller size web optimization webp to jpg webp to png jpg to webp png to webp webp converter convert image to webp heic to jpg heic to png heic converter avif to jpg avif to png' },
    { title: 'Passport Photo Maker (A4 Grid)', category: 'Image Tools', icon: '📸', url: 'image/passport-photo.html', keywords: 'passport photo 3.5x4.5 ssc upsc visa 2x2 a4 print sheet grid' },
    { title: 'Signature Resizer (<20KB)', category: 'Image Tools', icon: '✍️', url: 'image/signature.html', keywords: 'resize signature under 20kb 50kb ibps ssc upsc dimension 140x60' },
    { title: 'All Image Tools Suite', category: 'Image Tools', icon: '✨', url: 'image/index.html', keywords: 'all 18 image photo tools free private browser' },

    // Invoice Tools Suite
    { title: 'Create Invoice (GST & Standard)', category: 'Invoices', icon: '🧾', url: 'pdf/create-invoice.html', keywords: 'create invoice gst bill billing tax invoice maker hsn sac cgst sgst igst' },
    { title: 'Create Invoice Visually (WYSIWYG)', category: 'Invoices', icon: '🎨', url: 'pdf/create-invoice-visually.html', keywords: 'visual invoice editor a4 wysiwyg live edit invoice print logo design' },
    { title: 'Create Electronic Invoice (ZUGFeRD / UBL)', category: 'Invoices', icon: '⚡', url: 'pdf/create-electronic-invoice.html', keywords: 'electronic invoice e-invoice zugferd factur-x ubl xml gst json b2b' },
    { title: 'PDF Invoice to E-Invoice Converter', category: 'Invoices', icon: '🔍', url: 'pdf/pdf-invoice-to-e-invoice.html', keywords: 'pdf to e-invoice extract invoice text parser xml json zugferd' },
    { title: 'XML E-Invoice to PDF Visualizer', category: 'Invoices', icon: '📄', url: 'pdf/xml-e-invoice-to-pdf.html', keywords: 'xml invoice to pdf render electronic invoice visualizer print' },
    { title: 'Validate E-Invoice Compliance', category: 'Invoices', icon: '🛡️', url: 'pdf/validate-e-invoice.html', keywords: 'validate e-invoice en 16931 rules audit syntax check certificate' },

    // Developer & Data Tools
            
    // Text & Utility Tools
    { title: 'Word Counter & Text Analyzer', category: 'Text Tools', icon: '📝', url: 'text/word-counter.html', keywords: 'word counter characters count reading time paragraphs sentences word counter character counter sentence counter case converter uppercase to lowercase lowercase to uppercase reading time calculator' },
    { title: 'QR Code Generator', category: 'Utility Tools', icon: '📱', url: 'utilities/qr-generator.html', keywords: 'qr code generator create custom qr wifi url vcard qr code generator make qr code free qr generator upi qr code generator wifi qr code maker' },
    { title: 'Password Generator', category: 'Utility Tools', icon: '🔐', url: 'utilities/password-generator.html', keywords: 'password generator secure random password strong passphrase password generator random password generator strong password maker secure password generator' }
  ];

  function getBasePrefix() {
    const hasParentRelative = document.querySelector('link[href^="../"], script[src^="../"]');
    return hasParentRelative ? '../' : '';
  }

  function resolveRelativeUrl(url) {
    if (!url) return '#';
    if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('#')) return url;
    const cleanPath = url.replace(/^\/+/, '');
    return getBasePrefix() + cleanPath;
  }

  // ==========================================================================
  // 2. TOAST NOTIFICATION SYSTEM
  // ==========================================================================
  class ToastManager {
    constructor() {
      this.container = null;
    }

    _ensureContainer() {
      if (!this.container || !document.body.contains(this.container)) {
        this.container = document.querySelector('.toast-container');
        if (!this.container) {
          this.container = document.createElement('div');
          this.container.className = 'toast-container';
          document.body.appendChild(this.container);
        }
      }
    }

    show(message, type = 'info', duration = 3500) {
      this._ensureContainer();

      const toast = document.createElement('div');
      toast.className = `toast toast-${type}`;

      const iconMap = {
        success: '✓',
        error: '✕',
        warning: '⚠',
        info: 'ℹ'
      };

      const icon = iconMap[type] || 'ℹ';
      toast.innerHTML = `
        <span class="toast-icon" style="font-weight:bold;margin-right:8px;">${icon}</span>
        <span class="toast-msg" style="flex:1;">${escapeHtml(message)}</span>
      `;

      this.container.appendChild(toast);

      // Trigger entrance
      requestAnimationFrame(() => {
        toast.classList.add('visible');
      });

      // Auto dismiss
      const timer = setTimeout(() => {
        this.dismiss(toast);
      }, duration);

      toast.addEventListener('click', () => {
        clearTimeout(timer);
        this.dismiss(toast);
      });

      return toast;
    }

    dismiss(toast) {
      if (!toast) return;
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(100%)';
      toast.style.transition = 'all 0.25s ease';
      setTimeout(() => {
        if (toast.parentElement) toast.parentElement.removeChild(toast);
      }, 260);
    }

    success(msg, duration) { return this.show(msg, 'success', duration); }
    error(msg, duration)   { return this.show(msg, 'error', duration || 4500); }
    warning(msg, duration) { return this.show(msg, 'warning', duration); }
    info(msg, duration)    { return this.show(msg, 'info', duration); }
  }

  window.dsToast = new ToastManager();
  window.showToast = (msg, type) => window.dsToast.show(msg, type);

  // ==========================================================================
  // 3. UPLOAD DROPZONE HELPER
  // ==========================================================================
  function initDropZone(zoneElement, options = {}) {
    if (!zoneElement) return;
    const fileInput = zoneElement.querySelector('input[type="file"]');
    if (!fileInput) return;

    const onFiles = options.onFiles || zoneElement.__onFiles || null;

    // Click to upload
    zoneElement.addEventListener('click', (e) => {
      if (e.target !== fileInput) {
        fileInput.click();
      }
    });

    // Drag & Drop events
    ['dragenter', 'dragover'].forEach(evtName => {
      zoneElement.addEventListener(evtName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        zoneElement.classList.add('drag-over');
      });
    });

    ['dragleave', 'dragend', 'drop'].forEach(evtName => {
      zoneElement.addEventListener(evtName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        zoneElement.classList.remove('drag-over');
      });
    });

    zoneElement.addEventListener('drop', (e) => {
      const dt = e.dataTransfer;
      if (dt && dt.files && dt.files.length > 0) {
        fileInput.files = dt.files;
        fileInput.dispatchEvent(new Event('change', { bubbles: true }));
        if (typeof onFiles === 'function') {
          onFiles(dt.files);
        }
      }
    });

    fileInput.addEventListener('change', () => {
      if (fileInput.files && fileInput.files.length > 0) {
        if (typeof onFiles === 'function') {
          onFiles(fileInput.files);
        }
      }
    });
  }

  window.initDropZone = initDropZone;

  // Auto-bind all `.upload-zone` on DOM ready
  function autoInitDropZones() {
    document.querySelectorAll('.upload-zone').forEach(zone => {
      initDropZone(zone);
    });
  }

  // ==========================================================================
  // 4. MODAL DIALOG CONTROLLER
  // ==========================================================================
  const dsModal = {
    open(modalId) {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    },
    close(modalId) {
      const modal = typeof modalId === 'string' ? document.getElementById(modalId) : modalId;
      if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
      }
    },
    init() {
      // Trigger open buttons
      document.querySelectorAll('[data-modal-target]').forEach(trigger => {
        trigger.addEventListener('click', (e) => {
          e.preventDefault();
          const targetId = trigger.getAttribute('data-modal-target');
          dsModal.open(targetId);
        });
      });

      // Trigger close buttons & backdrop click
      document.querySelectorAll('.modal-overlay').forEach(overlay => {
        overlay.addEventListener('click', (e) => {
          if (e.target === overlay || e.target.closest('[data-modal-close]')) {
            dsModal.close(overlay);
          }
        });
      });

      // ESC key dismiss
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          const activeModal = document.querySelector('.modal-overlay.active');
          if (activeModal) dsModal.close(activeModal);
        }
      });
    }
  };
  window.dsModal = dsModal;

  // ==========================================================================
  // 5. SMART INTENT & INTENT DETECTION ENGINE (Multi-lingual & Hinglish Ready)
  // ==========================================================================
  function matchSmartIntent(query) {
    const q = query.toLowerCase().trim().replace(/[-_]/g, ' ');
    if (!q || q.length < 2) return null;

    // 1. Passport Photo Intent (SSC, UPSC, 3.5x4.5, "passport size photo banana hai", etc.)
    if (/(passport\s*photo|passport\s*pic|3\.5\s*x\s*4\.5|ssc\s*photo|upsc\s*photo|exam\s*photo|visa\s*photo|2\s*x\s*2\s*inch|gov\w*\s*photo|photo\s*passport\s*size|passport\s*banana|passport\s*size)/i.test(q)) {
      let preset = '3.5x4.5';
      let titleExtra = ' (3.5×4.5cm Indian Exam Preset)';
      if (/visa|us|2\s*x\s*2/i.test(q)) {
        preset = '5.08x5.08';
        titleExtra = ' (2×2 inch US Visa Preset)';
      } else if (/college|3\s*x\s*4/i.test(q)) {
        preset = '3x4';
        titleExtra = ' (3×4cm College Form Preset)';
      }
      return {
        title: 'Passport Photo Maker' + titleExtra,
        category: 'Indian Form Tools',
        icon: '📸',
        url: `image/passport-photo.html?preset=${preset}`,
        isSmartMatch: true
      };
    }

    // 2. Signature Resizer Intent ("signature 20kb", "signature 50 kb se kam", "sign chhota karna", etc.)
    if (/(sign\w*\s*(20\s*kb|50\s*kb|10\s*kb|100\s*kb|resize|dimension|ssc|upsc|ibps|less|under|se\s*kam|chhota|banana|karna)|signature)/i.test(q)) {
      let target = '20';
      let preset = 'ssc';
      let titleExtra = ' (Under 20KB SSC/IBPS Preset)';
      if (/50\s*kb|upsc|psc/i.test(q)) {
        target = '50';
        preset = 'upsc';
        titleExtra = ' (Under 50KB UPSC Preset)';
      } else if (/10\s*kb/i.test(q)) {
        target = '10';
        preset = 'ssc';
        titleExtra = ' (Under 10KB Preset)';
      } else if (/100\s*kb/i.test(q)) {
        target = '100';
        preset = 'psc';
        titleExtra = ' (Under 100KB Preset)';
      }
      return {
        title: 'Signature Resizer' + titleExtra,
        category: 'Indian Form Tools',
        icon: '✍️',
        url: `image/signature.html?preset=${preset}&target=${target}`,
        isSmartMatch: true
      };
    }

    // 3. Image KB Compressor ("photo 20kb karna hai", "photo under 50 kb", "image 100kb", etc.)
    const kbMatch = q.match(/(?:photo|image|pic|picture|compress|reduce|shrink|make|karna|kam)\s*(?:under|to|in|se|less|ke\s*liye)?\s*(\d{2,3})\s*(?:kb|k)/i) ||
                    q.match(/(\d{2,3})\s*(?:kb|k)\s*(?:photo|image|pic|compress|karna|se\s*kam|under)/i);
    if (kbMatch && !q.includes('sign')) {
      const kb = parseInt(kbMatch[1], 10);
      return {
        title: `Image Compressor (${kb}KB Target Preset)`,
        category: 'Image Tools',
        icon: '🗜️',
        url: `image/compress.html?target=${kb}`,
        isSmartMatch: true
      };
    }

    // 4. DPI Converter Intent ("300 dpi", "convert to 200 dpi", "dpi change karna", etc.)
    const dpiMatch = q.match(/(\d{2,4})\s*dpi/i);
    if (dpiMatch || q.includes('dpi') || q.includes('ppi')) {
      const dpi = dpiMatch ? dpiMatch[1] : '300';
      return {
        title: `DPI Converter (${dpi} DPI Print Preset)`,
        category: 'Image Tools',
        icon: '🖨️',
        url: `image/dpi-converter.html?dpi=${dpi}`,
        isSmartMatch: true
      };
    }

    // 5. Combine / Join / Merge PDF ("pdf jodna hai", "combine two pdf", "join pdf", "do pdf ek sath", etc.)
    if (/combine\s*.*pdf|join\s*.*pdf|merge\s*.*pdf|put\s*pdf\s*together|concat\s*pdf|pdf\s*jodna|do\s*pdf|pdf\s*merge/i.test(q)) {
      return {
        title: 'Merge PDF (Combine Multiple Files)',
        category: 'PDF Tools',
        icon: '📑',
        url: 'pdf/merge.html',
        isSmartMatch: true
      };
    }

    // 6. Remove / Delete PDF Pages / Organize ("pdf ka page delete karna hai", "remove page from pdf", "pdf se page hatao", etc.)
    if (/pdf\s*.*page\w*\s*(remove|delete|extract|reorder|organize|hatao|hata|chahiye)|(remove|delete|hatao|extract)\s*.*page\w*.*pdf|pdf\s*ka\s*page/i.test(q)) {
      return {
        title: 'Organize PDF (Delete, Reorder & Rotate Pages)',
        category: 'PDF Tools',
        icon: '📑',
        url: 'pdf/organize.html',
        isSmartMatch: true
      };
    }

    // 7. Images into PDF ("images ko pdf banana hai", "photo to pdf", "photos ko pdf me badalna", etc.)
    if (/image\w*\s*(into|to|ko|se)\s*pdf|photo\w*\s*(into|to|ko|se)\s*pdf|make\s*pdf\s*from\s*(image|photo|pic)|turn\s*(image|photo|pic)\w*\s*into\s*pdf|pdf\s*banana\s*hai|photo\s*ko\s*pdf/i.test(q)) {
      return {
        title: 'JPG / Photos to PDF Converter',
        category: 'PDF Tools',
        icon: '📑',
        url: 'pdf/jpg-to-pdf.html',
        isSmartMatch: true
      };
    }

    // 8. PDF Pictures / Extract Images ("pdf se photo nikalna hai", "pdf se image nikalo", "pdf ko jpg mein convert karo", etc.)
    if (/pdf\s*(pictures|images|photo\w*)|extract\s*image\w*\s*from\s*pdf|save\s*pdf\s*as\s*(jpg|png|image)|turn\s*pdf\s*into\s*(image|jpg|png)|pdf\s*se\s*(photo|image|nikal)|pdf\s*ko\s*(jpg|image|png)/i.test(q)) {
      return {
        title: 'PDF to JPG Converter (Extract PDF Images)',
        category: 'PDF Tools',
        icon: '🖼️',
        url: 'pdf/pdf-to-jpg.html',
        isSmartMatch: true
      };
    }

    // 9. Remove Background ("photo ka bg hatana", "transparent background", "white bg photo", etc.)
    if (/remove\s*bg|remove\s*background|transparent\s*(bg|background|png)|white\s*background\s*photo|bg\s*(hata|change|remove|saaf)|background\s*hatana/i.test(q)) {
      return {
        title: 'Remove Background in HD Quality',
        category: 'Image Tools',
        icon: '✂️',
        url: 'image/remove-bg.html',
        isSmartMatch: true
      };
    }

    // 10. Marksheet / Xerox Scan Enhancer ("marksheet scan saaf karna", "xerox clean karna", etc.)
    if (/scan\s*(enhancer|clarify|clean|saaf)|marksheet\s*(enhanc\w*|saaf|clear)|xerox\s*(clean|boost|contrast|saaf)|enhance\s*(scan|document|xerox)|scan\s*saaf/i.test(q)) {
      return {
        title: 'Photo Enhancer & Scan Optimizer',
        category: 'Image Tools',
        icon: '✨',
        url: 'image/photo-enhancer.html',
        isSmartMatch: true
      };
    }

    // 11. Compress PDF Intent ("compress pdf", "pdf size kam karna", "make pdf smaller", "pdf under 200kb", etc.)
    if (/compress\s*pdf|pdf\s*compress|reduce\s*pdf|shrink\s*pdf|make\s*pdf\s*smaller|pdf\s*(size|mb|kb)\s*(kam|chhota|reduce|less|down)|pdf\s*2\s*mb|pdf\s*100\s*kb|pdf\s*200\s*kb|pdf\s*500\s*kb/i.test(q)) {
      return {
        title: 'Compress PDF (Reduce PDF File Size)',
        category: 'PDF Tools',
        icon: '🗜️',
        url: 'pdf/compress.html',
        isSmartMatch: true
      };
    }

    // 12. Split PDF Intent ("split pdf", "separate pdf pages", "pdf alag karna", etc.)
    if (/split\s*pdf|separate\s*pdf|cut\s*pdf|divide\s*pdf|pdf\s*split|pdf\s*(alag|tukde|divide)/i.test(q)) {
      return {
        title: 'Split PDF (Extract & Separate Pages)',
        category: 'PDF Tools',
        icon: '✂️',
        url: 'pdf/split.html',
        isSmartMatch: true
      };
    }

    // 13. PDF to Word / Word to PDF
    if (/pdf\s*(to|into|se|ko)\s*(word|doc|docx)|word\s*to\s*pdf|convert\s*pdf\s*word/i.test(q)) {
      if (/word\s*(to|into|se|ko)\s*pdf/i.test(q)) {
        return {
          title: 'Word to PDF Converter',
          category: 'PDF Tools',
          icon: '📄',
          url: 'pdf/word-to-pdf.html',
          isSmartMatch: true
        };
      }
      return {
        title: 'PDF to Word Converter',
        category: 'PDF Tools',
        icon: '📝',
        url: 'pdf/pdf-to-word.html',
        isSmartMatch: true
      };
    }

    // 14. Image Resizer Intent ("resize photo", "pixel dimensions", "1920x1080", "photo width height", etc.)
    if (/resize\s*(image|photo|pic)|change\s*(pixel|dimension|width|height)|image\s*resiz|photo\s*chhota|size\s*badalna/i.test(q)) {
      return {
        title: 'Image Resizer (Custom Dimensions & Pixels)',
        category: 'Image Tools',
        icon: '📐',
        url: 'image/resize.html',
        isSmartMatch: true
      };
    }

    return null;
  }

  // ==========================================================================
  // 6. GLOBAL SEARCH ENGINE & COMMAND PALETTE (Ctrl+K)
  // ==========================================================================
  function initCommandPalette() {
    let overlay = document.querySelector('.command-palette-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'command-palette-overlay';
      overlay.id = 'commandPaletteModal';
      overlay.innerHTML = `
        <div class="command-palette-modal" role="dialog" aria-modal="true" aria-label="Quick Search">
          <div class="palette-search-header">
            <span class="palette-search-icon">🔍</span>
            <input type="text" class="palette-search-input" id="paletteSearchInput" placeholder="Type a tool name, format, or task (e.g. ssc photo, signature 20kb)..." autocomplete="off" spellcheck="false">
            <button class="palette-close-btn" id="paletteCloseBtn" aria-label="Close search">ESC</button>
          </div>
          <div class="palette-results-list" id="paletteResultsList">
            <!-- Dynamically populated -->
          </div>
          <div class="palette-footer">
            <span><kbd style="background:#fff;border:1px solid #cbd5e1;padding:1px 4px;border-radius:4px;">↑</kbd> <kbd style="background:#fff;border:1px solid #cbd5e1;padding:1px 4px;border-radius:4px;">↓</kbd> to navigate</span>
            <span><kbd style="background:#fff;border:1px solid #cbd5e1;padding:1px 4px;border-radius:4px;">↵</kbd> to open</span>
            <span><kbd style="background:#fff;border:1px solid #cbd5e1;padding:1px 4px;border-radius:4px;">esc</kbd> to dismiss</span>
          </div>
        </div>
      `;
      document.body.appendChild(overlay);
    }

    const input = overlay.querySelector('#paletteSearchInput');
    const resultsList = overlay.querySelector('#paletteResultsList');
    const closeBtn = overlay.querySelector('#paletteCloseBtn');
    let selectedIndex = 0;

    function renderResults(query = '') {
      let filtered = [];
      const cleanQ = query.toLowerCase().trim();
      const smartMatch = cleanQ ? matchSmartIntent(cleanQ) : null;

      if (!cleanQ) {
        filtered = SEARCH_REGISTRY.slice(0, 10);
      } else {
        filtered = SEARCH_REGISTRY.filter(item => {
          return item.title.toLowerCase().includes(cleanQ) ||
                 item.category.toLowerCase().includes(cleanQ) ||
                 (item.keywords && item.keywords.toLowerCase().includes(cleanQ));
        });
        if (smartMatch) {
          filtered = [smartMatch, ...filtered.filter(it => it.url !== smartMatch.url.split('?')[0])];
        }
      }

      if (filtered.length === 0) {
        resultsList.innerHTML = `
          <div style="padding: 24px; text-align: center; color: var(--text-muted);">
            <div style="font-size: 1.6rem; margin-bottom: 6px;">🔍</div>
            No tools found for "<strong>${escapeHtml(query)}</strong>".
          </div>
        `;
        return;
      }

      selectedIndex = 0;
      resultsList.innerHTML = filtered.map((item, idx) => {
        const finalUrl = resolveRelativeUrl(item.url);
        const isSmart = item.isSmartMatch;
        return `
          <a href="${finalUrl}" class="palette-result-item ${idx === 0 ? 'selected' : ''}" data-idx="${idx}">
            <span class="palette-result-icon">${item.icon}</span>
            <div class="palette-result-info">
              <div class="palette-result-title">
                ${cleanQ ? highlightMatch(item.title, cleanQ) : escapeHtml(item.title)}
                ${isSmart ? '<span style="background:#eff6ff;color:#2563eb;font-size:0.72rem;font-weight:700;padding:2px 6px;border-radius:4px;border:1px solid #bfdbfe;margin-left:6px;">🎯 Smart Preset</span>' : ''}
              </div>
              <div class="palette-result-category">${escapeHtml(item.category)}</div>
            </div>
            <span class="palette-result-badge">Open →</span>
          </a>
        `;
      }).join('');
    }

    function openPalette() {
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
      input.value = '';
      renderResults('');
      setTimeout(() => input.focus(), 50);
    }

    function closePalette() {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }

    document.querySelectorAll('#headerSearchBtn, #mobileSearchBtn, .nav-search-btn, .mobile-search-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openPalette();
      });
    });

    if (closeBtn) {
      closeBtn.addEventListener('click', closePalette);
    }

    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closePalette();
    });

    input.addEventListener('input', (e) => {
      renderResults(e.target.value);
    });

    input.addEventListener('keydown', (e) => {
      const items = resultsList.querySelectorAll('.palette-result-item');
      if (items.length === 0) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        selectedIndex = (selectedIndex + 1) % items.length;
        items.forEach((it, idx) => it.classList.toggle('selected', idx === selectedIndex));
        if (items[selectedIndex]) items[selectedIndex].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        selectedIndex = (selectedIndex - 1 + items.length) % items.length;
        items.forEach((it, idx) => it.classList.toggle('selected', idx === selectedIndex));
        if (items[selectedIndex]) items[selectedIndex].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (items[selectedIndex]) {
          items[selectedIndex].click();
        }
      } else if (e.key === 'Escape') {
        closePalette();
      }
    });

    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (overlay.classList.contains('active')) {
          closePalette();
        } else {
          openPalette();
        }
      } else if (e.key === '/' && !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) {
        e.preventDefault();
        openPalette();
      }
    });
  }

  function initGlobalSearch() {
    initCommandPalette();

    const searchInputs = document.querySelectorAll('#homeSearchInput, #global-search, .search-bar, .hero-search-input, .nav-search-input, #toolSearchInput, #pdf-tool-search, #image-tool-search');
    if (searchInputs.length === 0) return;

    searchInputs.forEach(input => {
      const parent = input.closest('.hero-search-container, .hero-search-box, .search-container, .search-filter-wrap') || input.parentElement;
      let resultsContainer = parent ? parent.querySelector('#homeSearchResults, #search-results, .search-results-dropdown, .search-results') : null;

      if (!resultsContainer && parent) {
        resultsContainer = document.createElement('div');
        resultsContainer.className = 'search-results-dropdown hero-search-dropdown';
        resultsContainer.id = 'searchResults_' + Math.random().toString(36).substr(2, 6);
        parent.appendChild(resultsContainer);
      }

      if (!resultsContainer) return;

      let selectedIndex = -1;
      let currentMatches = [];

      function updateActiveSelection() {
        const items = resultsContainer.querySelectorAll('.search-result-item');
        items.forEach((item, idx) => {
          if (idx === selectedIndex) {
            item.classList.add('selected');
            item.scrollIntoView({ block: 'nearest' });
          } else {
            item.classList.remove('selected');
          }
        });
      }

      let lastQuery = null;

      function doSearch() {
        const query = input.value.toLowerCase().trim();
        if (query === lastQuery) return;
        lastQuery = query;

        if (query.length < 1) {
          resultsContainer.innerHTML = '';
          resultsContainer.classList.remove('active');
          resultsContainer.style.display = 'none';
          selectedIndex = -1;
          currentMatches = [];
          window.dispatchEvent(new CustomEvent('vytra:search', { detail: { query: '', count: SEARCH_REGISTRY.length } }));
          return;
        }

        const smartMatch = matchSmartIntent(query);

        currentMatches = SEARCH_REGISTRY.filter(item => {
          return item.title.toLowerCase().includes(query) ||
                 item.category.toLowerCase().includes(query) ||
                 (item.keywords && item.keywords.toLowerCase().includes(query));
        });

        if (smartMatch) {
          currentMatches = [smartMatch, ...currentMatches.filter(it => it.url !== smartMatch.url.split('?')[0])];
        }

        selectedIndex = currentMatches.length > 0 ? 0 : -1;

        if (currentMatches.length === 0) {
          resultsContainer.innerHTML = `
            <div style="padding: 16px; text-align: center; color: var(--text-muted, #64748b);">
              <span style="font-size: 1.4rem; display:block; margin-bottom:4px;">🔍</span>
              No tools matching "<strong>${escapeHtml(query)}</strong>"
            </div>
          `;
        } else {
          resultsContainer.innerHTML = currentMatches.slice(0, 8).map((item, idx) => {
            const finalUrl = resolveRelativeUrl(item.url);
            const isSmart = item.isSmartMatch;
            return `
              <a href="${finalUrl}" class="search-result-item ${idx === 0 ? 'selected' : ''}" data-idx="${idx}" style="display:flex;align-items:center;gap:12px;padding:11px 16px;border-bottom:1px solid var(--border-subtle, #f1f5f9);text-decoration:none;color:var(--text-main, #0f172a);transition:background 0.15s ease;">
                <span class="search-result-icon" style="font-size:1.3rem;width:34px;height:34px;display:flex;align-items:center;justify-content:center;background:var(--bg-surface-subtle, #f8fafc);border-radius:8px;border:1px solid var(--border-subtle, #e2e8f0);">${item.icon}</span>
                <div style="flex:1;min-width:0;">
                  <div style="font-weight:600;font-size:0.92rem;color:var(--text-main, #0f172a);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                    ${highlightMatch(item.title, query)}
                    ${isSmart ? '<span style="background:#eff6ff;color:#2563eb;font-size:0.72rem;font-weight:700;padding:2px 6px;border-radius:4px;border:1px solid #bfdbfe;margin-left:6px;">🎯 Smart Preset</span>' : ''}
                  </div>
                  <div style="font-size:0.75rem;color:var(--text-muted, #64748b);">${escapeHtml(item.category)}</div>
                </div>
                <span style="font-size:0.78rem;color:var(--primary, #2563eb);font-weight:700;display:inline-flex;align-items:center;gap:3px;">Open &rarr;</span>
              </a>
            `;
          }).join('');
        }

        resultsContainer.classList.add('active');
        resultsContainer.style.display = 'block';

        window.dispatchEvent(new CustomEvent('vytra:search', { detail: { query, count: currentMatches.length } }));
      }

      input.addEventListener('input', debounce(doSearch, 60));
      input.addEventListener('focus', () => {
        if (input.value.trim().length >= 1) {
          doSearch();
        }
      });

      // Full Keyboard Navigation: ArrowDown, ArrowUp, Enter, Escape
      input.addEventListener('keydown', (e) => {
        const items = resultsContainer.querySelectorAll('.search-result-item');
        if (!resultsContainer.classList.contains('active') || items.length === 0) return;

        if (e.key === 'ArrowDown') {
          e.preventDefault();
          selectedIndex = (selectedIndex + 1) % items.length;
          updateActiveSelection();
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          selectedIndex = (selectedIndex - 1 + items.length) % items.length;
          updateActiveSelection();
        } else if (e.key === 'Enter') {
          e.preventDefault();
          const targetIndex = selectedIndex >= 0 ? selectedIndex : 0;
          if (items[targetIndex]) {
            items[targetIndex].click();
          }
        } else if (e.key === 'Escape') {
          resultsContainer.classList.remove('active');
          resultsContainer.style.display = 'none';
        }
      });

      // Close on outside click
      document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !resultsContainer.contains(e.target)) {
          resultsContainer.classList.remove('active');
          resultsContainer.style.display = 'none';
        }
      });
    });
  }

  // ==========================================================================
  // 6. TABS SYSTEM
  // ==========================================================================
  function initTabs() {
    document.querySelectorAll('.tabs').forEach(tabGroup => {
      const buttons = tabGroup.querySelectorAll('.tab-btn');
      const container = tabGroup.closest('.tab-wrapper') || tabGroup.parentElement;

      buttons.forEach(btn => {
        btn.addEventListener('click', () => {
          buttons.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          const targetId = btn.getAttribute('data-tab');
          if (container && targetId) {
            container.querySelectorAll('.tab-content').forEach(panel => {
              panel.classList.remove('active');
            });
            const targetPanel = container.querySelector(`#${targetId}`);
            if (targetPanel) {
              targetPanel.classList.add('active');
            }
          }
        });
      });
    });
  }

  // ==========================================================================
  // 7. ACCORDION SYSTEM
  // ==========================================================================
  function initAccordions() {
    document.querySelectorAll('.accordion-header, .faq-question').forEach(header => {
      header.addEventListener('click', () => {
        const item = header.closest('.accordion-item, .faq-item');
        if (!item) return;

        const parent = item.parentElement;
        const isActive = item.classList.contains('active');

        // Close siblings if inside accordion container
        if (parent && parent.classList.contains('accordion-exclusive')) {
          parent.querySelectorAll('.accordion-item, .faq-item').forEach(sibling => {
            sibling.classList.remove('active');
          });
        }

        if (!isActive) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });
    });
  }

  // ==========================================================================
  // 8. MOBILE NAVIGATION DRAWER & SCROLL BEHAVIOR
  // ==========================================================================
  function initNavigation() {
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    const navbar = document.querySelector('.navbar');

    if (toggle && links) {
      toggle.addEventListener('click', () => {
        links.classList.toggle('active');
        const isOpen = links.classList.contains('active');
        toggle.textContent = isOpen ? '✕' : '☰';
        toggle.setAttribute('aria-expanded', isOpen);
      });

      // Mobile dropdown accordion handling (<= 1100px)
      const dropdownItems = links.querySelectorAll('.nav-item.has-dropdown');
      dropdownItems.forEach(item => {
        const topLink = item.querySelector('.nav-link');
        if (topLink) {
          topLink.addEventListener('click', (e) => {
            if (window.innerWidth <= 1100) {
              e.preventDefault();
              const wasOpen = item.classList.contains('open');
              dropdownItems.forEach(i => i.classList.remove('open'));
              if (!wasOpen) {
                item.classList.add('open');
              }
            }
          });
        }
      });

      // Close menu on tool / dropdown link click
      links.querySelectorAll('.dropdown-link, .nav-item:not(.has-dropdown) .nav-link').forEach(link => {
        link.addEventListener('click', () => {
          links.classList.remove('active');
          dropdownItems.forEach(i => i.classList.remove('open'));
          toggle.textContent = '☰';
          toggle.setAttribute('aria-expanded', 'false');
        });
      });

      // Close menu on outside click
      document.addEventListener('click', (e) => {
        if (!toggle.contains(e.target) && !links.contains(e.target)) {
          links.classList.remove('active');
          dropdownItems.forEach(i => i.classList.remove('open'));
          toggle.textContent = '☰';
          toggle.setAttribute('aria-expanded', 'false');
        }
      });

      // Automatically highlight active nav item based on current URL
      try {
        const currentPath = window.location.pathname.replace(/\\/g, '/');
        links.querySelectorAll('a').forEach(a => {
          const href = a.getAttribute('href');
          if (href && !href.startsWith('#') && !href.startsWith('http')) {
            const cleanHref = href.replace(/^\.\.\//, '').replace(/^\.\//, '');
            if (cleanHref && (currentPath.endsWith('/' + cleanHref) || currentPath.endsWith(cleanHref))) {
              a.classList.add('active');
              const parentItem = a.closest('.nav-item');
              if (parentItem) {
                const parentLink = parentItem.querySelector('.nav-link');
                if (parentLink) parentLink.classList.add('active');
              }
            }
          }
        });
      } catch (err) {}
    }

    // Navbar elevation on scroll (passive 60fps rAF throttle)
    if (navbar) {
      let isScrolled = false;
      let scrollTicking = false;
      window.addEventListener('scroll', () => {
        if (!scrollTicking) {
          window.requestAnimationFrame(() => {
            const shouldBeScrolled = window.scrollY > 20;
            if (shouldBeScrolled !== isScrolled) {
              isScrolled = shouldBeScrolled;
              navbar.classList.toggle('scrolled', isScrolled);
            }
            scrollTicking = false;
          });
          scrollTicking = true;
        }
      }, { passive: true });
    }
  }

  // ==========================================================================
  // 9. HELPER UTILITIES
  // ==========================================================================
  function formatFileSize(bytes) {
    if (!bytes || bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 100);
  }

  function downloadDataURL(dataUrl, filename) {
    const a = document.createElement('a');
    a.href = dataUrl;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
    }, 100);
  }

  async function copyToClipboard(text, successMsg = 'Copied to clipboard!') {
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
      } else {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
      }
      window.dsToast.success(successMsg);
      return true;
    } catch (err) {
      window.dsToast.error('Failed to copy text.');
      return false;
    }
  }

  function debounce(func, wait = 200) {
    let timeout;
    return function (...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function highlightMatch(text, query) {
    if (!query) return escapeHtml(text);
    const safeText = escapeHtml(text);
    const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return safeText.replace(regex, '<span style="background:var(--primary-100);color:var(--primary-800);border-radius:2px;padding:0 2px;">$1</span>');
  }

  // Expose global helpers
  window.formatFileSize = formatFileSize;
  window.downloadBlob = downloadBlob;
  window.downloadDataURL = downloadDataURL;
  window.copyToClipboard = copyToClipboard;
  window.debounce = debounce;
  window.escapeHtml = escapeHtml;
  window.resolveRelativeUrl = resolveRelativeUrl;

  // ==========================================================================
  // 10. AUTO-UPGRADE EMOJI ICONS TO PROFESSIONAL VECTOR SVG TILES (iLovePDF Standard)
  // ==========================================================================
  function upgradeEmojiIcons() {
    if (!window.getToolSvgIcon) return;
    const iconWraps = document.querySelectorAll('.saas-tool-icon-wrap, .tool-icon-box');
    if (!iconWraps || iconWraps.length === 0) return;
    iconWraps.forEach(wrap => {
      const card = wrap.closest('a');
      if (!card) return;
      const href = (card.getAttribute('href') || '').toLowerCase();
      
      let toolId = '';
      if (href.includes('merge')) toolId = 'merge-pdf';
      else if (href.includes('split')) toolId = 'split-pdf';
      else if (href.includes('compress') && href.includes('pdf')) toolId = 'compress-pdf';
      else if (href.includes('compress')) toolId = 'compress-image';
      else if (href.includes('pdf-to-word') || href.includes('word-to-pdf')) toolId = 'pdf-to-word';
      else if (href.includes('pdf-to-ppt') || href.includes('ppt-to-pdf')) toolId = 'pdf-to-ppt';
      else if (href.includes('pdf-to-excel') || href.includes('excel-to-pdf')) toolId = 'pdf-to-excel';
      else if (href.includes('edit')) toolId = 'edit-pdf';
      else if (href.includes('pdf-to-jpg')) toolId = 'pdf-to-jpg';
      else if (href.includes('jpg-to-pdf')) toolId = 'jpg-to-pdf';
      else if (href.includes('sign')) toolId = 'sign-pdf';
      else if (href.includes('rotate')) toolId = 'rotate-pdf';
      else if (href.includes('protect')) toolId = 'protect-pdf';
      else if (href.includes('unlock')) toolId = 'unlock-pdf';
      else if (href.includes('organize')) toolId = 'organize-pdf';
      else if (href.includes('crop')) toolId = 'crop-image';
      else if (href.includes('resize')) toolId = 'resize-image';
      else if (href.includes('convert')) toolId = 'convert-image';
      else if (href.includes('passport')) toolId = 'passport-photo';
      else if (href.includes('signature')) toolId = 'signature-resizer';
      else if (href.includes('json')) toolId = 'json-formatter';
      else if (href.includes('base64')) toolId = 'base64-converter';
      else if (href.includes('sql')) toolId = 'sql-formatter';
      else if (href.includes('emi')) toolId = 'emi-calculator';
      else if (href.includes('age')) toolId = 'age-calculator';
      else if (href.includes('percentage')) toolId = 'percentage-calculator';
      else if (href.includes('cgpa')) toolId = 'cgpa-calculator';
      else if (href.includes('attendance')) toolId = 'attendance-calculator';
      else if (href.includes('qr')) toolId = 'qr-generator';
      else if (href.includes('password')) toolId = 'password-generator';
      else if (href.includes('word-counter')) toolId = 'word-counter';

      if (toolId) {
        const svgTileHtml = window.getToolSvgIcon(toolId);
        if (svgTileHtml) {
          const temp = document.createElement('div');
          temp.innerHTML = svgTileHtml;
          const newTile = temp.firstElementChild;
          wrap.replaceWith(newTile);
        }
      }
    });
  }
  // ==========================================================================
  // 11. PRIVACY-COMPLIANT COOKIE CONSENT & ADSENSE CONTROLLER
  // ==========================================================================
  class ConsentController {
    constructor() {
      this.STORAGE_KEY = 'ds_consent_status';
      this.banner = null;
    }

    init() {
      let status = null;
      try {
        status = localStorage.getItem(this.STORAGE_KEY);
      } catch (e) {
        // localStorage blocked or private browsing
      }

      if (!status) {
        this.renderBanner();
      } else if (status === 'accepted') {
        const adsManager = window.VYTRA_ADS || window.DIGITALSAATHI_ADS;
        if (adsManager && typeof adsManager.init === 'function') {
          adsManager.init();
        }
      } else {
        const adsManager = window.VYTRA_ADS || window.DIGITALSAATHI_ADS;
        if (adsManager && typeof adsManager.collapse === 'function') {
          adsManager.collapse();
        }
      }
    }

    renderBanner() {
      if (document.getElementById('ds-consent-banner')) return;

      const cookiePolicyUrl = resolveRelativeUrl('cookie-policy.html');
      const privacyPolicyUrl = resolveRelativeUrl('privacy.html');

      const banner = document.createElement('aside');
      banner.id = 'ds-consent-banner';
      banner.className = 'ds-consent-banner';
      banner.setAttribute('role', 'region');
      banner.setAttribute('aria-label', 'Cookie Consent Preferences');

      banner.innerHTML = `
        <div class="ds-consent-container">
          <div class="ds-consent-content">
            <div class="ds-consent-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 10 10 1.5 1.5 0 0 1-1.5 1.5H19a2 2 0 0 0-2 2v1.5a1.5 1.5 0 0 1-1.5 1.5A10 10 0 0 1 12 2z"/><circle cx="8.5" cy="8.5" r="1.5"/><circle cx="16" cy="7.5" r="1"/><circle cx="10" cy="14" r="1"/><circle cx="15.5" cy="13" r="1.5"/></svg>
              Cookie Preferences &amp; Privacy
            </div>
            <p class="ds-consent-text">
              We use cookies to provide essential site functionality and analyze usage. When enabled, non-personalized or personalized advertising supports our free service. All tool processing occurs privately inside your browser. Read our <a href="${cookiePolicyUrl}">Cookie Policy</a> and <a href="${privacyPolicyUrl}">Privacy Policy</a>.
            </p>
          </div>
          <div class="ds-consent-actions">
            <button type="button" class="ds-consent-btn ds-consent-btn-reject" id="ds-consent-reject-btn">Essential Only</button>
            <button type="button" class="ds-consent-btn ds-consent-btn-accept" id="ds-consent-accept-btn">Accept All</button>
          </div>
        </div>
      `;

      document.body.appendChild(banner);
      banner.style.display = 'block';
      this.banner = banner;

      const acceptBtn = banner.querySelector('#ds-consent-accept-btn');
      const rejectBtn = banner.querySelector('#ds-consent-reject-btn');

      if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
          this.setConsent('accepted');
        });
      }

      if (rejectBtn) {
        rejectBtn.addEventListener('click', () => {
          this.setConsent('rejected');
        });
      }
    }

    setConsent(val) {
      try {
        localStorage.setItem(this.STORAGE_KEY, val);
      } catch (e) {
        // storage disabled
      }

      if (this.banner) {
        this.banner.style.display = 'none';
      }

      const adsManager = window.VYTRA_ADS || window.DIGITALSAATHI_ADS;
      if (val === 'accepted') {
        if (adsManager && typeof adsManager.init === 'function') {
          adsManager.init();
        }
      } else {
        if (adsManager && typeof adsManager.collapse === 'function') {
          adsManager.collapse();
        }
      }
    }

    openBanner() {
      if (!this.banner) {
        this.renderBanner();
      } else {
        this.banner.style.display = 'block';
      }
    }
  }

  const dsConsent = new ConsentController();
  window.VYTRA_CONSENT = dsConsent;
  window.DIGITALSAATHI_CONSENT = dsConsent;

  // ==========================================================================
  // 12. LIFECYCLE BOOTSTRAP
  // ==========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initGlobalSearch();
    autoInitDropZones();
    initTabs();
    initAccordions();
    dsModal.init();
    upgradeEmojiIcons();
    dsConsent.init();
  });

})();
