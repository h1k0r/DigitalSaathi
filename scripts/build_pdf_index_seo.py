import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from build_batch_organize_edit import NAVBAR, FOOTER, write_file

# Master Tool List for Hub with category-specific colors
TOOLS_DATA = [
    # Organize PDF
    {"name": "Merge PDF", "href": "merge.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "📑", "color": "#ef4444", "bg": "#fef2f2", "desc": "Combine PDFs in the order you want with the easiest PDF merger available."},
    {"name": "Split PDF", "href": "split.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "✂️", "color": "#f97316", "bg": "#fff7ed", "desc": "Separate one page or a whole set for easy conversion into independent PDF files."},
    {"name": "Organize PDF", "href": "organize.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "📑", "color": "#0ea5e9", "bg": "#f0f9ff", "desc": "Sort, add, rotate and delete PDF pages. Drag and drop the page thumbnails easily."},
    {"name": "Rotate PDF", "href": "rotate.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "🔄", "color": "#8b5cf6", "bg": "#f5f3ff", "desc": "Rotate your PDF pages upside-down or sideways. Save permanent rotation in seconds."},
    {"name": "Crop PDF", "href": "crop.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "📐", "color": "#10b981", "bg": "#ecfdf5", "desc": "Trim document margins, remove white borders, and adjust page visible dimensions."},
    {"name": "Page Numbers", "href": "page-numbers.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "🔢", "color": "#ec4899", "bg": "#fdf2f8", "desc": "Add page numbers into PDFs with ease. Choose position, dimensions, format and typography."},
    {"name": "Extract Pages", "href": "extract.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "📥", "color": "#6366f1", "bg": "#eef2ff", "desc": "Extract specific pages from your PDF document into a new independent PDF."},
    {"name": "Reorder Pages", "href": "reorder.html", "cat": "organize", "cat_label": "Organize PDF", "icon": "🔀", "color": "#14b8a6", "bg": "#f0fdfa", "desc": "Rearrange and re-sequence the pages of your PDF document in visual order."},

    # Optimize PDF
    {"name": "Compress PDF", "href": "compress.html", "cat": "optimize", "cat_label": "Optimize PDF", "icon": "🗜️", "color": "#10b981", "bg": "#ecfdf5", "desc": "Reduce file size while optimizing for maximal PDF quality. Meet 100KB limits for SSC/UPSC."},
    {"name": "Repair PDF", "href": "repair.html", "cat": "optimize", "cat_label": "Optimize PDF", "icon": "🔧", "color": "#eab308", "bg": "#fefce8", "desc": "Repair damaged or corrupt PDFs and recover unreadable data from truncated files."},

    # Convert PDF
    {"name": "PDF to Word", "href": "pdf-to-word.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📄", "color": "#2563eb", "bg": "#eff6ff", "desc": "Easily convert your PDF files into easy to edit DOC and DOCX documents with 100% accuracy."},
    {"name": "PDF to PowerPoint", "href": "pdf-to-ppt.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📽️", "color": "#ea580c", "bg": "#fff7ed", "desc": "Turn your PDF files into easy to edit PPT and PPTX slideshow presentations."},
    {"name": "PDF to Excel", "href": "pdf-to-excel.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📊", "color": "#059669", "bg": "#ecfdf5", "desc": "Pull data straight from PDFs into Excel spreadsheets in a few short seconds."},
    {"name": "Word to PDF", "href": "word-to-pdf.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📝", "color": "#1d4ed8", "bg": "#eff6ff", "desc": "Make DOC and DOCX files easy to read by converting them to clean PDF documents."},
    {"name": "PowerPoint to PDF", "href": "ppt-to-pdf.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📽️", "color": "#c2410c", "bg": "#fff7ed", "desc": "Make PPT and PPTX slideshows easy to view by converting them to universal PDF."},
    {"name": "Excel to PDF", "href": "excel-to-pdf.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📈", "color": "#047857", "bg": "#ecfdf5", "desc": "Make EXCEL spreadsheets easy to print and read by converting them to PDF."},
    {"name": "PDF to JPG", "href": "pdf-to-jpg.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "🖼️", "color": "#d97706", "bg": "#fffbeb", "desc": "Convert each PDF page into a high-resolution JPG image or extract all images."},
    {"name": "JPG to PDF", "href": "jpg-to-pdf.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "📄", "color": "#dc2626", "bg": "#fef2f2", "desc": "Convert JPG images to PDF in seconds. Easily adjust orientation and margins."},
    {"name": "HTML to PDF", "href": "html-to-pdf.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "🌐", "color": "#0284c7", "bg": "#f0f9ff", "desc": "Convert web pages or raw HTML code in seconds into clean, printable vector PDF."},
    {"name": "PDF/A Converter", "href": "pdf-a.html", "cat": "convert", "cat_label": "Convert PDF", "icon": "🏛️", "color": "#475569", "bg": "#f8fafc", "desc": "Convert standard PDF to ISO-standardized PDF/A for long-term archiving and court use."},

    # Edit PDF
    {"name": "Edit PDF", "href": "edit.html", "cat": "edit", "cat_label": "Edit PDF", "icon": "✏️", "color": "#2563eb", "bg": "#eff6ff", "desc": "Add text, shapes, comments and highlights to your PDF document with freehand drawing."},
    {"name": "Sign PDF", "href": "sign.html", "cat": "edit", "cat_label": "Edit PDF", "icon": "✍️", "color": "#1e40af", "bg": "#dbeafe", "desc": "Sign yourself or request electronic signatures and burn digital signatures onto PDF."},
    {"name": "Watermark PDF", "href": "watermark.html", "cat": "edit", "cat_label": "Edit PDF", "icon": "💧", "color": "#059669", "bg": "#ecfdf5", "desc": "Stamp an image or text over your PDF in seconds. Choose typography, transparency and position."},
    {"name": "Redact PDF", "href": "redact.html", "cat": "edit", "cat_label": "Edit PDF", "icon": "⬛", "color": "#dc2626", "bg": "#fee2e2", "desc": "Permanently blackout sensitive text, Aadhaar numbers, and private data in your PDF."},
    {"name": "PDF Forms", "href": "forms.html", "cat": "edit", "cat_label": "Edit PDF", "icon": "📋", "color": "#0284c7", "bg": "#e0f2fe", "desc": "Fill out interactive AcroForm fields, checkboxes, and flatten PDF forms permanently."},

    # PDF Security
    {"name": "Protect PDF", "href": "protect.html", "cat": "security", "cat_label": "PDF Security", "icon": "🔒", "color": "#dc2626", "bg": "#fef2f2", "desc": "Protect PDF files with a password. Encrypt PDF documents to prevent unauthorized access."},
    {"name": "Unlock PDF", "href": "unlock.html", "cat": "security", "cat_label": "PDF Security", "icon": "🔓", "color": "#d97706", "bg": "#fef3c7", "desc": "Remove PDF password security and permissions giving you the freedom to use your PDFs."},

    # Scan & OCR
    {"name": "Scan to PDF", "href": "scan-to-pdf.html", "cat": "scan", "cat_label": "Scan & OCR", "icon": "📷", "color": "#0284c7", "bg": "#e0f2fe", "desc": "Capture document pages with your camera, apply B&W enhancements, and compile to PDF."},
    {"name": "OCR PDF", "href": "ocr.html", "cat": "scan", "cat_label": "Scan & OCR", "icon": "🔍", "color": "#2563eb", "bg": "#eff6ff", "desc": "Easily convert scanned PDFs into searchable text layers with instant keyword search."},

    # PDF Analysis
    {"name": "Compare PDF", "href": "compare.html", "cat": "analysis", "cat_label": "PDF Analysis", "icon": "⚖️", "color": "#4f46e5", "bg": "#eef2ff", "desc": "Display two PDF files side by side with synchronized scrolling to easily spot changes."},
    {"name": "PDF Information", "href": "info.html", "cat": "analysis", "cat_label": "PDF Analysis", "icon": "ℹ️", "color": "#2563eb", "bg": "#eff6ff", "desc": "Inspect page dimensions, PDF version, author metadata, and edit document properties."},
    {"name": "PDF Page Counter", "href": "page-counter.html", "cat": "analysis", "cat_label": "PDF Analysis", "icon": "🔢", "color": "#059669", "bg": "#ecfdf5", "desc": "Quickly count the exact number of pages and inspect page dimensions across PDF files."},
    {"name": "PDF Viewer", "href": "viewer.html", "cat": "analysis", "cat_label": "PDF Analysis", "icon": "👁️", "color": "#6366f1", "bg": "#eef2ff", "desc": "Open and read PDF files directly in your web browser with zoom and search controls."},

    # PDF Intelligence / Advanced
    {"name": "AI PDF Summarizer", "href": "ai-summarizer.html", "cat": "intelligence", "cat_label": "PDF Intelligence", "icon": "✨", "color": "#9333ea", "bg": "#fdf4ff", "desc": "Extract key takeaways, executive summaries, and action points from long PDFs with AI."},
    {"name": "Translate PDF", "href": "translate.html", "cat": "intelligence", "cat_label": "PDF Intelligence", "icon": "🌐", "color": "#0284c7", "bg": "#e0f2fe", "desc": "Translate PDF text into Hindi, Bengali, Tamil, Telugu, Marathi, and 15+ world languages."},
    {"name": "PDF to Markdown", "href": "pdf-to-markdown.html", "cat": "intelligence", "cat_label": "PDF Intelligence", "icon": "🤖", "color": "#7c3aed", "bg": "#f5f3ff", "desc": "Convert PDF text into clean Markdown (# Headers, Lists, Tables) for ChatGPT & LLMs."},

    # Workflow
    {"name": "Create Workflow", "href": "workflow.html", "cat": "workflow", "cat_label": "Workflow", "icon": "⚡", "color": "#9333ea", "bg": "#fdf4ff", "desc": "Build automated multi-action PDF pipelines: Numbering → Watermark → Protection in 1 click."}
]

# Generate Tool Cards HTML
cards_html = ""
for t in TOOLS_DATA:
    cards_html += f'''
      <a href="{t['href']}" class="saas-tool-card" data-cat="{t['cat']}" data-name="{t['name'].lower()}">
        <div class="saas-tool-icon-wrap" style="background:{t['bg']};color:{t['color']};">
          <span>{t['icon']}</span>
        </div>
        <h3 class="saas-tool-title">{t['name']}</h3>
        <p class="saas-tool-desc">{t['desc']}</p>
      </a>'''

index_seo_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>iLovePDF Alternative — 100% Free Online PDF Tools Suite | DigitalSaathi</title>
  <meta name="description" content="Every tool you need to work with PDFs in one place. 100% Free, Private & Secure. Merge, split, compress, convert, edit, sign, and protect PDF files right inside your browser with zero server uploads.">
  <meta name="keywords" content="pdf tools, merge pdf, split pdf, compress pdf, convert pdf to word, jpg to pdf, sign pdf, protect pdf, free pdf online, ilovepdf alternative, digitalsaathi">
  <link rel="canonical" href="https://digitalsaathi.in/pdf/">

  <!-- Open Graph / Social SEO -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="DigitalSaathi PDF Tools — 100% Free Client-Side PDF Suite">
  <meta property="og:description" content="Every tool you need to use PDFs at your fingertips. 100% free, private, and instant browser processing.">
  <meta property="og:url" content="https://digitalsaathi.in/pdf/">

  <!-- Fonts & Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">

  <!-- JSON-LD Structured Data Schema for Top Search Ranking -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "name": "DigitalSaathi PDF Tools Suite",
        "url": "https://digitalsaathi.in/pdf/",
        "description": "Complete free client-side PDF editor, converter, merger, compressor, and signer with zero server uploads.",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "All (Web Browser)",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "INR"
        }},
        "featureList": [
          "Merge PDF", "Split PDF", "Compress PDF to 100KB", "PDF to Word", "JPG to PDF", "Sign PDF", "Protect PDF", "OCR PDF"
        ]
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://digitalsaathi.in/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "PDF Tools",
            "item": "https://digitalsaathi.in/pdf/"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Is DigitalSaathi PDF Tools completely free to use?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Yes, all 33+ PDF tools on DigitalSaathi are 100% free with unlimited usage, no daily limits, and no registration required."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Are my PDF files uploaded to external servers?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "No. Unlike traditional PDF websites, DigitalSaathi processes all documents 100% locally in your web browser using WebAssembly and Web Workers. Your private documents never leave your computer."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Can I compress PDFs to under 100KB for government job portals?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Yes! Our PDF Compressor tool features dedicated presets for Indian government applications including SSC CGL, UPSC, State PSC, and university exam portals."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    .saas-grid-container {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
      margin-bottom: 3.5rem;
    }}
    .search-filter-wrap {{
      max-width: 500px;
      margin: 0 auto 1.5rem;
      position: relative;
    }}
    .search-filter-input {{
      width: 100%;
      padding: 12px 18px 12px 42px;
      border: 1px solid #cbd5e1;
      border-radius: 30px;
      font-size: 0.95rem;
      box-shadow: 0 2px 6px rgba(0,0,0,0.03);
      outline: none;
      transition: all 0.2s;
    }}
    .search-filter-input:focus {{
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }}
    .search-icon-pos {{
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: #94a3b8;
      font-size: 1.1rem;
    }}
  </style>
</head>
<body class="tool-page">

{NAVBAR}

  <div class="container page-content">
    <!-- Hero Section matching iLovePDF Gold Standard -->
    <div class="tool-hero">
      <h1 class="tool-hero-title">Every tool you need to work with PDFs in one place</h1>
      <p class="tool-hero-subtitle">Every tool you need to use PDFs, at your fingertips. All are 100% FREE and easy to use! Merge, split, compress, convert, rotate, unlock and watermark PDFs with just a few clicks.</p>

      <!-- Instant Search Filter -->
      <div class="search-filter-wrap">
        <span class="search-icon-pos">🔍</span>
        <input type="text" id="toolSearchInput" class="search-filter-input" placeholder="Search any PDF tool (e.g. Merge, Compress, Word, Sign)..." aria-label="Search PDF tools">
      </div>

      <!-- Category Filter Pills matching Reference -->
      <div class="saas-category-nav">
        <button class="saas-pill-btn active" data-filter="all">All</button>
        <button class="saas-pill-btn" data-filter="workflow">Workflows</button>
        <button class="saas-pill-btn" data-filter="organize">Organize PDF</button>
        <button class="saas-pill-btn" data-filter="optimize">Optimize PDF</button>
        <button class="saas-pill-btn" data-filter="convert">Convert PDF</button>
        <button class="saas-pill-btn" data-filter="edit">Edit PDF</button>
        <button class="saas-pill-btn" data-filter="security">PDF Security</button>
        <button class="saas-pill-btn" data-filter="scan">Scan & OCR</button>
        <button class="saas-pill-btn" data-filter="analysis">Analysis</button>
        <button class="saas-pill-btn" data-filter="intelligence">PDF Intelligence</button>
      </div>
    </div>

    <!-- 33+ Tool Cards Grid -->
    <div class="saas-grid-container" id="toolGrid">
      {cards_html}
    </div>

    <!-- SEO Content Section: Why DigitalSaathi -->
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;padding:36px;margin:40px 0;box-shadow:var(--shadow-sm);">
      <h2 style="font-size:1.6rem;font-weight:800;color:#0f172a;margin-bottom:12px;text-align:center;">Why Students, Job Seekers & Cyber Cafés Choose DigitalSaathi</h2>
      <p style="color:#64748b;text-align:center;max-width:700px;margin:0 auto 28px;line-height:1.6;">DigitalSaathi is built specifically for Indian needs with true 100% in-browser processing, zero server costs, and guaranteed document privacy.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:24px;">
        <div style="padding:16px;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
          <div style="font-size:1.6rem;margin-bottom:8px;">🔒</div>
          <h3 style="font-size:1.1rem;font-weight:700;color:#1e293b;margin-bottom:6px;">100% Client-Side Privacy</h3>
          <p style="font-size:0.875rem;color:#64748b;line-height:1.5;">Unlike other PDF sites, your sensitive Aadhaar cards, marks sheets, and bank statements are never uploaded to any remote server.</p>
        </div>

        <div style="padding:16px;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
          <div style="font-size:1.6rem;margin-bottom:8px;">⚡</div>
          <h3 style="font-size:1.1rem;font-weight:700;color:#1e293b;margin-bottom:6px;">Zero Wait Times & No Limits</h3>
          <p style="font-size:0.875rem;color:#64748b;line-height:1.5;">Process unlimited files without artificial daily limits, queues, or premium paywalls. Instant processing at hardware speed.</p>
        </div>

        <div style="padding:16px;background:#f8fafc;border-radius:8px;border:1px solid #e2e8f0;">
          <div style="font-size:1.6rem;margin-bottom:8px;">🇮🇳</div>
          <h3 style="font-size:1.1rem;font-weight:700;color:#1e293b;margin-bottom:6px;">Tailored for Indian Applications</h3>
          <p style="font-size:0.875rem;color:#64748b;line-height:1.5;">Exact presets for SSC CGL, UPSC, State PSC form uploads (&lt;100KB, &lt;50KB limits), photo background removal, and signature scaling.</p>
        </div>
      </div>
    </div>

    <!-- FAQ Accordion for Google PAA Rich Snippets -->
    <div class="faq-section" style="margin-bottom: 40px;">
      <h2 class="faq-heading" style="text-align:center;">Frequently Asked Questions</h2>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary class="faq-question">How is DigitalSaathi better than iLovePDF or Smallpdf?</summary>
          <div class="faq-answer">DigitalSaathi executes all PDF manipulations 100% inside your web browser via WebAssembly and JavaScript. There are zero upload times, no server queues, no daily file limits, no ads blocking your workflow, and your private documents never leave your computer.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Can I use these PDF tools on mobile phones?</summary>
          <div class="faq-answer">Yes, all DigitalSaathi tools are fully responsive and touch-optimized. You can merge, split, compress, or sign PDF files seamlessly on Android and iOS devices.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">How does the PDF Compressor reach under 100KB for government job forms?</summary>
          <div class="faq-answer">Our custom compressor strips unnecessary metadata, optimizes PDF stream fonts, and applies smart image downsampling to guarantee files pass portal upload checks on SSC, UPSC, and IBPS servers.</div>
        </details>
        <details class="faq-item">
          <summary class="faq-question">Are there any file size limits or paid subscriptions?</summary>
          <div class="faq-answer">No. All 33+ PDF tools are completely free to use with no subscription required.</div>
        </details>
      </div>
    </div>
  </div>

{FOOTER}

  <script src="../assets/js/common.js"></script>
  <script>
    const searchInput = document.getElementById('toolSearchInput');
    const pillButtons = document.querySelectorAll('.saas-pill-btn');
    const toolCards = document.querySelectorAll('.saas-tool-card');

    let currentFilter = 'all';

    pillButtons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        pillButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        filterCards();
      }});
    }});

    searchInput.addEventListener('input', filterCards);

    function filterCards() {{
      const query = searchInput.value.trim().toLowerCase();

      toolCards.forEach(card => {{
        const cat = card.dataset.cat;
        const name = card.dataset.name;
        const matchesCat = currentFilter === 'all' || cat === currentFilter;
        const matchesSearch = !query || name.includes(query) || card.textContent.toLowerCase().includes(query);

        if (matchesCat && matchesSearch) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>'''

write_file('pdf/index.html', index_seo_html)
print("Updated pdf/index.html with Gold Standard SaaS Design & SEO Schemas.")
