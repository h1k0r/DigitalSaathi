import os
import glob
import re

TOOLS_SEO = {
    "merge.html": {
        "title": "Merge PDF Online Free — Combine Multiple PDF Files | DigitalSaathi",
        "h1": "Merge PDF",
        "desc": "Combine PDFs in the order you want with the easiest PDF merger available. 100% free and client-side secure.",
        "cta": "Select PDF files",
        "drop": "or drop PDFs here",
        "app_type": "PDF Merger",
        "steps": ["Select or drop your PDF files into the merger.", "Reorder files or pages into your desired sequence.", "Click 'Merge PDF' and download your combined document."]
    },
    "split.html": {
        "title": "Split PDF Online Free — Extract Custom PDF Pages | DigitalSaathi",
        "h1": "Split PDF",
        "desc": "Separate one page or a whole set for easy conversion into independent PDF files in seconds.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Splitter",
        "steps": ["Upload your multi-page PDF document.", "Select page range or individual pages to extract.", "Click 'Split PDF' to download individual pages or a ZIP archive."]
    },
    "compress.html": {
        "title": "Compress PDF to 100KB Online Free — Reduce PDF Size | DigitalSaathi",
        "h1": "Compress PDF",
        "desc": "Reduce PDF file size while optimizing for maximal quality. Dedicated presets for SSC, UPSC, and government form uploads.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Compressor",
        "steps": ["Choose the PDF document you want to compress.", "Select recommended, extreme, or custom compression preset.", "Download your optimized PDF instantly."]
    },
    "jpg-to-pdf.html": {
        "title": "Convert JPG to PDF Online Free — Images to PDF in Seconds | DigitalSaathi",
        "h1": "JPG to PDF",
        "desc": "Convert JPG images to PDF in seconds. Easily adjust orientation, margins, and page order.",
        "cta": "Select JPG images",
        "drop": "or drop JPG images here",
        "app_type": "JPG to PDF Converter",
        "steps": ["Upload one or more JPG, PNG, or WebP images.", "Rearrange image order, set page orientation and margin preferences.", "Click 'Convert to PDF' and download your compiled PDF."]
    },
    "pdf-to-jpg.html": {
        "title": "PDF to JPG Converter Online Free — High Quality Image Export | DigitalSaathi",
        "h1": "PDF to JPG",
        "desc": "Convert each PDF page into a high-resolution JPG image or extract all embedded images in seconds.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF to JPG Converter",
        "steps": ["Select the PDF you want to convert to images.", "Choose image quality (Standard / High Definition).", "Download single pages or a complete ZIP package."]
    },
    "organize.html": {
        "title": "Organize PDF Pages Online Free — Sort, Rotate & Delete | DigitalSaathi",
        "h1": "Organize PDF",
        "desc": "Sort, add, rotate and delete PDF pages with visual drag-and-drop thumbnails. 100% private in-browser.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Page Organizer",
        "steps": ["Upload your PDF document.", "Drag and drop cards to reorder, click rotate or delete on any page.", "Click 'Save Organized PDF' to download."]
    },
    "rotate.html": {
        "title": "Rotate PDF Pages Online Free — Permanent PDF Rotation | DigitalSaathi",
        "h1": "Rotate PDF",
        "desc": "Rotate your PDF pages upside-down or sideways. Save permanent rotation in seconds with visual preview.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Rotator",
        "steps": ["Select your PDF file.", "Click rotate icons (↺ ↻) on individual pages or rotate all at once.", "Download your permanently rotated PDF."]
    },
    "crop.html": {
        "title": "Crop PDF Margins Online Free — Trim White Borders | DigitalSaathi",
        "h1": "Crop PDF",
        "desc": "Trim document margins, remove white borders, and crop pages to custom dimensions with live visual preview.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Cropper",
        "steps": ["Upload your PDF document.", "Adjust visual crop box or percentage margin sliders.", "Click 'Crop PDF & Download'."]
    },
    "page-numbers.html": {
        "title": "Add Page Numbers to PDF Online Free | DigitalSaathi",
        "h1": "Page Numbers",
        "desc": "Add page numbers into PDFs with ease. Choose position, dimensions, format ('Page X of Y') and typography.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Page Numberer",
        "steps": ["Select your PDF file.", "Choose position slot, number format, and font styling.", "Click 'Add Page Numbers & Download'."]
    },
    "watermark.html": {
        "title": "Watermark PDF Online Free — Add Text & Logo Stamps | DigitalSaathi",
        "h1": "Watermark PDF",
        "desc": "Stamp custom text or official logo image over your PDF in seconds. Choose typography, transparency and angle.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Watermarker",
        "steps": ["Select your PDF document.", "Enter text or upload logo image, set angle and opacity.", "Click 'Apply Watermark & Download'."]
    },
    "edit.html": {
        "title": "Edit PDF Online Free — Add Text, Annotate & Draw | DigitalSaathi",
        "h1": "Edit PDF",
        "desc": "Add text, shapes, comments and highlights to your PDF document with freehand drawing tools.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Editor",
        "steps": ["Upload your PDF document.", "Select pen, highlighter, text box, or whiteout tool.", "Click 'Save & Download' to export your edited file."]
    },
    "sign.html": {
        "title": "Sign PDF Online Free — Draw, Type or Upload Signature | DigitalSaathi",
        "h1": "Sign PDF",
        "desc": "Draw your signature, type with cursive handwriting fonts, or upload signature image and place on PDF.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Signer",
        "steps": ["Upload the PDF document you need to sign.", "Draw signature with mouse/touch, type cursive name, or upload photo.", "Click document to place signature and download signed PDF."]
    },
    "redact.html": {
        "title": "Redact PDF Online Free — Permanently Blackout Sensitive Data | DigitalSaathi",
        "h1": "Redact PDF",
        "desc": "Permanently blackout sensitive text, Aadhaar numbers, PAN cards, and private data in your PDF.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Redactor",
        "steps": ["Select your PDF file.", "Click and drag to draw blackout rectangles over sensitive details.", "Click 'Permanently Redact & Download'."]
    },
    "forms.html": {
        "title": "Fill & Flatten PDF Forms Online Free | DigitalSaathi",
        "h1": "PDF Forms",
        "desc": "Fill out interactive AcroForm fields, checkboxes, dropdowns, and flatten PDF forms permanently.",
        "cta": "Select PDF Form",
        "drop": "or drop PDF Form here",
        "app_type": "PDF Form Filler",
        "steps": ["Upload your interactive PDF application form.", "Fill in text inputs, check boxes, and select dropdown values.", "Download your filled and flattened PDF."]
    },
    "protect.html": {
        "title": "Protect PDF with Password Online Free | DigitalSaathi",
        "h1": "Protect PDF",
        "desc": "Protect PDF files with a password. Encrypt PDF documents with military-grade security to prevent unauthorized access.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Password Encryptor",
        "steps": ["Select the PDF file you want to encrypt.", "Enter user password and configure security permissions.", "Download your password-protected PDF."]
    },
    "unlock.html": {
        "title": "Unlock PDF Online Free — Remove Password & Permissions | DigitalSaathi",
        "h1": "Unlock PDF",
        "desc": "Remove PDF password security and printing/copying restrictions giving you the freedom to use your PDFs.",
        "cta": "Select Locked PDF",
        "drop": "or drop locked PDF here",
        "app_type": "PDF Password Remover",
        "steps": ["Upload your password-protected PDF file.", "Enter the current document password.", "Download the unlocked, unrestricted PDF."]
    },
    "pdf-to-word.html": {
        "title": "PDF to Word Converter Online Free (.DOCX) | DigitalSaathi",
        "h1": "PDF to Word",
        "desc": "Easily convert your PDF files into easy to edit DOC and DOCX documents with preserved paragraphs and tables.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF to Word Converter",
        "steps": ["Select your PDF document.", "Our engine automatically extracts text, paragraphs, and lists.", "Download your editable Word (.doc / .docx) file."]
    },
    "pdf-to-excel.html": {
        "title": "PDF to Excel Converter Online Free (.XLSX / CSV) | DigitalSaathi",
        "h1": "PDF to Excel",
        "desc": "Pull data straight from PDFs into Excel spreadsheets and CSV files in a few short seconds.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF to Excel Converter",
        "steps": ["Upload statement, invoice, or PDF with tables.", "Our coordinate engine structures rows and columns.", "Download Excel (.xlsx) or CSV."]
    },
    "pdf-to-ppt.html": {
        "title": "PDF to PowerPoint Converter Online Free (.PPTX) | DigitalSaathi",
        "h1": "PDF to PowerPoint",
        "desc": "Turn your PDF files into easy to edit PPT and PPTX slideshow presentations with high-resolution slides.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF to PowerPoint Converter",
        "steps": ["Upload your presentation PDF document.", "Slides are extracted in high definition.", "Download presentation deck archive."]
    },
    "word-to-pdf.html": {
        "title": "Word to PDF Converter Online Free (.DOCX to PDF) | DigitalSaathi",
        "h1": "Word to PDF",
        "desc": "Make DOC and DOCX files easy to read by converting them to clean, universal PDF documents.",
        "cta": "Select Word file",
        "drop": "or drop Word file here",
        "app_type": "Word to PDF Converter",
        "steps": ["Upload DOCX, DOC, or TXT file.", "Preview formatted layout and typography.", "Click 'Convert to PDF' and download."]
    },
    "excel-to-pdf.html": {
        "title": "Excel to PDF Converter Online Free (.XLSX to PDF) | DigitalSaathi",
        "h1": "Excel to PDF",
        "desc": "Make Excel spreadsheets (.xlsx, .xls, .csv) easy to print and read by converting them to PDF with auto-fit tables.",
        "cta": "Select Excel file",
        "drop": "or drop Excel file here",
        "app_type": "Excel to PDF Converter",
        "steps": ["Select your Excel workbook.", "Choose active sheet to export.", "Download clean, styled table PDF."]
    },
    "ppt-to-pdf.html": {
        "title": "PowerPoint to PDF Converter Online Free (.PPTX to PDF) | DigitalSaathi",
        "h1": "PowerPoint to PDF",
        "desc": "Make PPT slideshows easy to view by converting slides into high-resolution multi-page PDF files.",
        "cta": "Select Slide files",
        "drop": "or drop slides here",
        "app_type": "PowerPoint to PDF Converter",
        "steps": ["Select slide exports or images.", "Choose 1-slide/page or handout layout.", "Download unified PDF document."]
    },
    "html-to-pdf.html": {
        "title": "HTML to PDF Converter Online Free | DigitalSaathi",
        "h1": "HTML to PDF",
        "desc": "Convert web pages or raw HTML code in seconds into clean, printable vector PDF documents.",
        "cta": "Convert HTML Code",
        "drop": "Paste code or choose template below",
        "app_type": "HTML to PDF Converter",
        "steps": ["Paste custom HTML/CSS code or choose GST invoice preset.", "Configure page orientation and margin settings.", "Click 'Convert to PDF & Download'."]
    },
    "pdf-a.html": {
        "title": "PDF/A Archival Converter Online Free (ISO 19005) | DigitalSaathi",
        "h1": "PDF/A Converter",
        "desc": "Convert standard PDF to ISO-standardized PDF/A for long-term archiving, court submissions, and legal compliance.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF/A Converter",
        "steps": ["Select standard PDF file.", "Choose PDF/A-1b or PDF/A-2b profile.", "Download ISO 19005 compliant archival PDF."]
    },
    "repair.html": {
        "title": "Repair Corrupt PDF Online Free — Fix Damaged PDFs | DigitalSaathi",
        "h1": "Repair PDF",
        "desc": "Repair damaged or corrupt PDFs and recover unreadable data from truncated files client-side.",
        "cta": "Select Corrupt PDF",
        "drop": "or drop damaged PDF here",
        "app_type": "PDF Repair Tool",
        "steps": ["Select broken or unopenable PDF file.", "Diagnostic scanner analyzes xref tables and stream headers.", "Download restored PDF document."]
    },
    "scan-to-pdf.html": {
        "title": "Scan to PDF Online Free — Camera Document Scanner | DigitalSaathi",
        "h1": "Scan to PDF",
        "desc": "Capture document pages with your camera, apply B&W enhancements, and compile to clean A4 PDF.",
        "cta": "Capture Document",
        "drop": "Use camera or upload photos",
        "app_type": "Camera Document Scanner",
        "steps": ["Position document inside camera frame.", "Capture snapshots and apply Magic Color or B&W filters.", "Compile and download multi-page PDF."]
    },
    "ocr.html": {
        "title": "OCR PDF Online Free — Extract Text & Searchable PDF | DigitalSaathi",
        "h1": "OCR PDF",
        "desc": "Easily convert scanned PDFs into searchable text layers with instant keyword search and copy.",
        "cta": "Select Scanned PDF",
        "drop": "or drop scanned PDF here",
        "app_type": "PDF OCR Extractor",
        "steps": ["Upload scanned PDF document.", "OCR engine extracts recognized text layers.", "Search words, copy text, or export TXT file."]
    },
    "compare.html": {
        "title": "Compare PDF Documents Online Free — Visual Diff Viewer | DigitalSaathi",
        "h1": "Compare PDF",
        "desc": "Display two PDF files side by side with synchronized scrolling to easily spot changes and revision differences.",
        "cta": "Select Both PDFs",
        "drop": "Upload Doc 1 & Doc 2 below",
        "app_type": "PDF Compare Tool",
        "steps": ["Upload original document and revised version.", "Navigate pages in synchronized side-by-side viewer.", "Spot modifications and text differences easily."]
    },
    "info.html": {
        "title": "PDF Information & Metadata Inspector Online Free | DigitalSaathi",
        "h1": "PDF Information",
        "desc": "Inspect page dimensions, PDF version, author metadata, and edit document properties client-side.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Metadata Inspector",
        "steps": ["Select your PDF file.", "Inspect page dimensions, version, author, and security status.", "Edit metadata and save updated PDF."]
    },
    "ai-summarizer.html": {
        "title": "AI PDF Summarizer Online Free — Instant Key Takeaways | DigitalSaathi",
        "h1": "AI PDF Summarizer",
        "desc": "Extract key takeaways, executive summaries, and action points from long PDFs with browser-side NLP.",
        "cta": "Select PDF to Summarize",
        "drop": "or drop PDF here",
        "app_type": "AI PDF Summarizer",
        "steps": ["Upload research paper, book, or report.", "NLP scoring ranks key conceptual sentences.", "Read executive summary and key bullet takeaways."]
    },
    "translate.html": {
        "title": "Translate PDF Online Free — Multilingual Translator | DigitalSaathi",
        "h1": "Translate PDF",
        "desc": "Translate PDF text into Hindi, Bengali, Tamil, Telugu, Marathi, and 15+ world languages with side-by-side view.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Translator",
        "steps": ["Upload PDF document.", "Choose target language (Hindi, Bengali, Telugu, etc.).", "Read side-by-side translation or export TXT."]
    },
    "pdf-to-markdown.html": {
        "title": "PDF to Markdown Converter Online Free (For ChatGPT & LLMs) | DigitalSaathi",
        "h1": "PDF to Markdown",
        "desc": "Convert PDF text into clean Markdown (# Headers, Lists, Tables) optimized for ChatGPT & LLM prompts.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF to Markdown Converter",
        "steps": ["Select your PDF document.", "Our parser formats headings, bullet points, and code.", "Copy clean Markdown directly for ChatGPT / Claude."]
    },
    "workflow.html": {
        "title": "Create PDF Workflow Online Free — Multi-Action Pipeline | DigitalSaathi",
        "h1": "Create Workflow",
        "desc": "Build automated multi-action PDF pipelines: Numbering → Watermark → Protection in 1 single click.",
        "cta": "Select PDF file",
        "drop": "or drop PDF here",
        "app_type": "PDF Workflow Pipeline",
        "steps": ["Upload your PDF document.", "Configure pipeline recipe (Page Numbers, Watermark, Password).", "Execute entire pipeline in one click."]
    }
}

for filename, meta in TOOLS_SEO.items():
    path = os.path.join("pdf", filename)
    if not os.path.exists(path):
        continue

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title & Meta Description
    content = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', content)
    content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']>', f'<meta name="description" content="{meta["desc"]}">', content)

    # 2. Inject JSON-LD Schema (WebApplication, HowTo, BreadcrumbList)
    schema_json = f'''  <!-- Top Ranking SEO Schema Markup (WebApplication, HowTo, BreadcrumbList) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "name": "{meta['title']}",
        "url": "https://digitalsaathi.in/pdf/{filename}",
        "description": "{meta['desc']}",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All (Web Browser)",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "INR"
        }}
      }},
      {{
        "@type": "HowTo",
        "name": "How to use {meta['h1']} on DigitalSaathi",
        "description": "{meta['desc']}",
        "step": [
          {{
            "@type": "HowToStep",
            "position": 1,
            "name": "{meta['steps'][0]}",
            "text": "{meta['steps'][0]}"
          }},
          {{
            "@type": "HowToStep",
            "position": 2,
            "name": "{meta['steps'][1]}",
            "text": "{meta['steps'][1]}"
          }},
          {{
            "@type": "HowToStep",
            "position": 3,
            "name": "{meta['steps'][2]}",
            "text": "{meta['steps'][2]}"
          }}
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
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{meta['h1']}",
            "item": "https://digitalsaathi.in/pdf/{filename}"
          }}
        ]
      }}
    ]
  }}
  </script>'''

    # Inject schema if not already present
    if "https://schema.org" not in content:
        content = content.replace("</head>", f"{schema_json}\n</head>")

    # 3. Upgrade Hero Section and Upload Button to iLovePDF Gold Standard
    # Replace tool-header with high-impact SaaS hero
    new_hero = f'''    <div class="tool-hero">
      <h1 class="tool-hero-title">{meta['h1']}</h1>
      <p class="tool-hero-subtitle">{meta['desc']}</p>
    </div>'''

    if '<div class="tool-header text-center">' in content:
        content = re.sub(r'<div class="tool-header text-center">[\s\S]*?</div>\s*</div>', new_hero, content, count=1)

    # Enhance Upload Zone Button with .btn-hero-cta
    content = content.replace('class="btn btn-primary" id="selectBtn"', 'class="btn-hero-cta" id="selectBtn"')
    if meta['cta']:
        content = re.sub(r'<button class="btn-hero-cta" id="selectBtn"[^>]*>.*?</button>', f'<button class="btn-hero-cta" id="selectBtn" type="button">{meta["cta"]}</button>', content)

    # Drop hint text
    content = content.replace('<p class="upload-subtitle">', '<p class="drop-hint-text">')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Injected High-Level SEO Schemas & Gold Standard Hero CTA buttons across all tool pages.")
