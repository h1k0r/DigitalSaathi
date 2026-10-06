import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Master clean SVG icons (24x24 viewBox vector icons styled with inline currentColor)
ICONS = {
    "merge": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-3"/><path d="M19 9l-5 5-4-4-3 3"/><path d="M14 9h5v5"/></svg>''',
    "split": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/></svg>''',
    "organize": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/></svg>''',
    "rotate": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6"/><path d="M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>''',
    "crop": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>''',
    "page_numbers": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M10 17h4"/><path d="M12 13v4"/></svg>''',
    "extract": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><polyline points="12 18 12 12 16 12"/></svg>''',
    "reorder": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg>''',
    "compress": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14h6v6"/><path d="M20 10h-6V4"/><path d="M14 10l7-7"/><path d="M3 21l7-7"/></svg>''',
    "repair": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>''',
    "word": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>''',
    "excel": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>''',
    "ppt": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>''',
    "jpg": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>''',
    "html": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>''',
    "pdfa": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="M4 9h16"/><path d="M9 4v16"/><path d="M15 4v16"/></svg>''',
    "edit": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>''',
    "sign": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 4.5l-3-3a1.5 1.5 0 0 0-2.12 0L3 13.88V18h4.12l12.38-12.38a1.5 1.5 0 0 0 0-2.12z"/><path d="M18.5 6.5l-3-3"/><path d="M3 21h18"/></svg>''',
    "watermark": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>''',
    "redact": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="12" rx="2" fill="currentColor"/></svg>''',
    "forms": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>''',
    "protect": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>''',
    "unlock": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>''',
    "scan": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>''',
    "ocr": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="8" y1="11" x2="14" y2="11"/><line x1="11" y1="8" x2="11" y2="14"/></svg>''',
    "compare": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>''',
    "info": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>''',
    "counter": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10"/><path d="M7 12h10"/><path d="M7 16h6"/></svg>''',
    "viewer": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>''',
    "ai": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4"/><path d="M12 18v4"/><path d="M4.93 4.93l2.83 2.83"/><path d="M16.24 16.24l2.83 2.83"/><path d="M2 12h4"/><path d="M18 12h4"/><path d="M4.93 19.07l2.83-2.83"/><path d="M16.24 7.76l2.83-2.83"/></svg>''',
    "translate": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8l6 6"/><path d="M4 14l6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="M22 22l-5-10-5 10"/><path d="M14 18h6"/></svg>''',
    "markdown": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><polyline points="7 15 9 9 11 15 13 9"/><polyline points="14 13 16 15 18 13"/></svg>''',
    "workflow": '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'''
}

# Complete tool catalog organized into specified categories and tags
TOOLS = [
    # Organize PDF (Coral/Orange Accent)
    {
        "name": "Merge PDF",
        "href": "merge.html",
        "cats": ["organize", "student", "cybercafe"],
        "icon_key": "merge",
        "color": "#ea580c",
        "bg": "#fff7ed",
        "desc": "Combine multiple PDF files into a single document in your desired order."
    },
    {
        "name": "Split PDF",
        "href": "split.html",
        "cats": ["organize", "student"],
        "icon_key": "split",
        "color": "#ea580c",
        "bg": "#fff7ed",
        "desc": "Separate one page or extract specific page ranges into independent PDFs."
    },
    {
        "name": "Organize PDF",
        "href": "organize.html",
        "cats": ["organize", "cybercafe"],
        "icon_key": "organize",
        "color": "#ea580c",
        "bg": "#fff7ed",
        "desc": "Rearrange, rotate, delete, or duplicate pages with visual drag-and-drop grid."
    },
    {
        "name": "Rotate PDF",
        "href": "rotate.html",
        "cats": ["organize", "cybercafe"],
        "icon_key": "rotate",
        "color": "#ea580c",
        "bg": "#fff7ed",
        "desc": "Rotate upside-down or sideways pages permanently in 90-degree steps."
    },
    {
        "name": "Crop PDF",
        "href": "crop.html",
        "cats": ["organize", "cybercafe"],
        "icon_key": "crop",
        "color": "#ea580c",
        "bg": "#fff7ed",
        "desc": "Trim unwanted margins, white borders, and adjust visible page dimensions."
    },
    {
        "name": "Page Numbers",
        "href": "page-numbers.html",
        "cats": ["organize", "student"],
        "icon_key": "page_numbers",
        "color": "#ea580c",
        "bg": "#fff7ed",
        "desc": "Add customizable page numbers (Page X of Y) with 6 position slots."
    },

    # Optimize PDF (Emerald Green Accent)
    {
        "name": "Compress PDF",
        "href": "compress.html",
        "cats": ["optimize", "student", "cybercafe"],
        "icon_key": "compress",
        "color": "#059669",
        "bg": "#ecfdf5",
        "desc": "Reduce PDF file size while maintaining quality. Presets for SSC/UPSC <100KB."
    },
    {
        "name": "Repair PDF",
        "href": "repair.html",
        "cats": ["optimize"],
        "icon_key": "repair",
        "color": "#059669",
        "bg": "#ecfdf5",
        "desc": "Recover corrupted, unopenable, or truncated PDF files by rebuilding xref tables."
    },

    # Convert PDF (Royal Blue Accent)
    {
        "name": "PDF to Word",
        "href": "pdf-to-word.html",
        "cats": ["convert", "student"],
        "icon_key": "word",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert PDF documents to editable Microsoft Word (.docx / .doc) files."
    },
    {
        "name": "PDF to Excel",
        "href": "pdf-to-excel.html",
        "cats": ["convert"],
        "icon_key": "excel",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Extract tabular data and bank statements from PDF into Excel (.xlsx) or CSV."
    },
    {
        "name": "PDF to PowerPoint",
        "href": "pdf-to-ppt.html",
        "cats": ["convert", "student"],
        "icon_key": "ppt",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert PDF pages into high-resolution PowerPoint presentation slide decks."
    },
    {
        "name": "Word to PDF",
        "href": "word-to-pdf.html",
        "cats": ["convert", "student"],
        "icon_key": "word",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert DOCX, DOC, and TXT documents into standard printable PDF files."
    },
    {
        "name": "Excel to PDF",
        "href": "excel-to-pdf.html",
        "cats": ["convert"],
        "icon_key": "excel",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert spreadsheets (.xlsx, .xls, .csv) into clean, printable table PDFs."
    },
    {
        "name": "PowerPoint to PDF",
        "href": "ppt-to-pdf.html",
        "cats": ["convert", "student"],
        "icon_key": "ppt",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert presentation slides into universal multi-page PDF documents."
    },
    {
        "name": "PDF to JPG",
        "href": "pdf-to-jpg.html",
        "cats": ["convert", "cybercafe"],
        "icon_key": "jpg",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert each PDF page into high-resolution JPG images or download as ZIP."
    },
    {
        "name": "JPG to PDF",
        "href": "jpg-to-pdf.html",
        "cats": ["convert", "cybercafe", "student"],
        "icon_key": "jpg",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert multiple JPG/PNG photos into a single formatted PDF document."
    },
    {
        "name": "HTML to PDF",
        "href": "html-to-pdf.html",
        "cats": ["convert"],
        "icon_key": "html",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Convert HTML code, GST invoices, and certificates into vector PDF."
    },
    {
        "name": "PDF/A Converter",
        "href": "pdf-a.html",
        "cats": ["convert"],
        "icon_key": "pdfa",
        "color": "#2563eb",
        "bg": "#eff6ff",
        "desc": "Standardize documents to ISO 19005 compliant PDF/A for legal archiving."
    },

    # Edit PDF (Blue / Violet Accent)
    {
        "name": "Edit PDF",
        "href": "edit.html",
        "cats": ["edit", "student"],
        "icon_key": "edit",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "desc": "Add text annotations, draw with pen, highlight lines, or erase with whiteout."
    },
    {
        "name": "Sign PDF",
        "href": "sign.html",
        "cats": ["edit", "cybercafe"],
        "icon_key": "sign",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "desc": "Draw, type cursive signature, or upload signature image to burn onto PDF."
    },
    {
        "name": "Watermark PDF",
        "href": "watermark.html",
        "cats": ["edit", "cybercafe"],
        "icon_key": "watermark",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "desc": "Stamp text or logo watermarks with custom rotation, opacity, and repeat grid."
    },
    {
        "name": "Redact PDF",
        "href": "redact.html",
        "cats": ["edit", "cybercafe"],
        "icon_key": "redact",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "desc": "Permanently blackout sensitive details like Aadhaar, PAN, and roll numbers."
    },
    {
        "name": "PDF Forms",
        "href": "forms.html",
        "cats": ["edit"],
        "icon_key": "forms",
        "color": "#3b82f6",
        "bg": "#eff6ff",
        "desc": "Detect, fill out interactive AcroForm fields, checkboxes, and flatten forms."
    },

    # PDF Security (Crimson / Violet Accent)
    {
        "name": "Protect PDF",
        "href": "protect.html",
        "cats": ["security"],
        "icon_key": "protect",
        "color": "#dc2626",
        "bg": "#fef2f2",
        "desc": "Encrypt PDF files with user passwords and restrict printing or copying."
    },
    {
        "name": "Unlock PDF",
        "href": "unlock.html",
        "cats": ["security"],
        "icon_key": "unlock",
        "color": "#dc2626",
        "bg": "#fef2f2",
        "desc": "Remove password protection and permission restrictions permanently."
    },

    # Scan & OCR (Indigo Accent)
    {
        "name": "Scan to PDF",
        "href": "scan-to-pdf.html",
        "cats": ["ocr", "cybercafe", "student"],
        "icon_key": "scan",
        "color": "#6366f1",
        "bg": "#eef2ff",
        "desc": "Scan document pages using your webcam or phone camera with B&W filters."
    },
    {
        "name": "OCR PDF",
        "href": "ocr.html",
        "cats": ["ocr", "student"],
        "icon_key": "ocr",
        "color": "#6366f1",
        "bg": "#eef2ff",
        "desc": "Extract searchable text layers from scanned documents with live word search."
    },

    # Analysis
    {
        "name": "Compare PDF",
        "href": "compare.html",
        "cats": ["advanced"],
        "icon_key": "compare",
        "color": "#4f46e5",
        "bg": "#eef2ff",
        "desc": "Compare two PDF documents side by side with synchronized scrolling."
    },
    {
        "name": "PDF Information",
        "href": "info.html",
        "cats": ["advanced"],
        "icon_key": "info",
        "color": "#4f46e5",
        "bg": "#eef2ff",
        "desc": "Inspect document metadata, page dimensions (mm/pt), version, and author info."
    },
    {
        "name": "Page Counter",
        "href": "page-counter.html",
        "cats": ["advanced", "cybercafe"],
        "icon_key": "counter",
        "color": "#4f46e5",
        "bg": "#eef2ff",
        "desc": "Instantly calculate page counts and inspect dimensions across PDF files."
    },
    {
        "name": "PDF Viewer",
        "href": "viewer.html",
        "cats": ["advanced", "student"],
        "icon_key": "viewer",
        "color": "#4f46e5",
        "bg": "#eef2ff",
        "desc": "Open and read PDF documents in browser with smooth navigation and zoom."
    },

    # Advanced / Intelligence (Purple Accent)
    {
        "name": "AI PDF Summarizer",
        "href": "ai-summarizer.html",
        "cats": ["advanced", "student"],
        "icon_key": "ai",
        "color": "#9333ea",
        "bg": "#fdf4ff",
        "desc": "Extract executive summaries, key bullet takeaways, and concept keywords."
    },
    {
        "name": "Translate PDF",
        "href": "translate.html",
        "cats": ["advanced", "student"],
        "icon_key": "translate",
        "color": "#9333ea",
        "bg": "#fdf4ff",
        "desc": "Translate PDF text into Hindi, Bengali, Tamil, Telugu, and 15+ languages."
    },
    {
        "name": "PDF to Markdown",
        "href": "pdf-to-markdown.html",
        "cats": ["advanced", "student"],
        "icon_key": "markdown",
        "color": "#9333ea",
        "bg": "#fdf4ff",
        "desc": "Convert PDF text into clean GitHub Markdown (# Headers, Tables) for LLMs."
    },

    # Workflow (Magenta Accent)
    {
        "name": "Create Workflow",
        "href": "workflow.html",
        "cats": ["advanced", "cybercafe"],
        "icon_key": "workflow",
        "color": "#d946ef",
        "bg": "#fdf4ff",
        "desc": "Build automated batch recipes: Numbering → Watermark → Protection in 1 click."
    }
]

# Generate Tool Cards HTML with clean SVG icons
cards_html = ""
for t in TOOLS:
    svg_icon = ICONS.get(t['icon_key'], ICONS['merge'])
    cat_classes = " ".join([f"cat-{c}" for c in t['cats']])
    cards_html += f'''
      <a href="{t['href']}" class="ds-tool-card {cat_classes}" data-name="{t['name'].lower()}" aria-label="{t['name']}">
        <div class="ds-card-icon" style="background:{t['bg']};color:{t['color']};">
          {svg_icon}
        </div>
        <h3 class="ds-card-title">{t['name']}</h3>
        <p class="ds-card-desc">{t['desc']}</p>
      </a>'''

# Compact Desktop & Mobile Navigation Header
HEADER_HTML = '''  <header class="ds-navbar" id="mainHeader">
    <div class="ds-nav-inner">
      <a href="../index.html" class="ds-brand" aria-label="DigitalSaathi Home">
        <span class="ds-brand-badge">DS</span>
        <span class="ds-brand-text">Digital<span class="ds-brand-hl">Saathi</span></span>
      </a>

      <!-- Desktop Nav Items -->
      <nav class="ds-nav-links" aria-label="Primary Navigation">
        <a href="../pdf/index.html" class="ds-nav-link active">PDF Tools</a>
        <a href="../image/resize.html" class="ds-nav-link">Image Tools</a>
        <a href="../cybercafe/passport-photo.html" class="ds-nav-link">Cyber Café</a>
        <a href="../student/resume.html" class="ds-nav-link">Students</a>
        <a href="../jobs/government.html" class="ds-nav-link">Jobs</a>
        <a href="../developer/json.html" class="ds-nav-link">Developer</a>
        <a href="../calculators/cgpa.html" class="ds-nav-link">Calculators</a>
      </nav>

      <!-- Search Trigger & Mobile Toggle -->
      <div class="ds-nav-actions">
        <button class="ds-search-toggle" id="headerSearchToggle" aria-label="Open Search">🔍</button>
        <button class="ds-menu-toggle" id="mobileMenuToggle" aria-label="Toggle navigation" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div class="ds-mobile-drawer" id="mobileDrawer">
      <a href="../pdf/index.html" class="ds-drawer-link active">📑 PDF Tools</a>
      <a href="../image/resize.html" class="ds-drawer-link">🖼️ Image Tools</a>
      <a href="../cybercafe/passport-photo.html" class="ds-drawer-link">🖥️ Cyber Café Tools</a>
      <a href="../student/resume.html" class="ds-drawer-link">🎓 Student Portal & Resume</a>
      <a href="../jobs/government.html" class="ds-drawer-link">🏛️ Government Jobs 2026</a>
      <a href="../developer/json.html" class="ds-drawer-link">💻 Developer Utilities</a>
      <a href="../calculators/cgpa.html" class="ds-drawer-link">🧮 Academic Calculators</a>
    </div>
  </header>'''

# Footer
FOOTER_HTML = '''  <footer class="ds-footer">
    <div class="ds-footer-container">
      <div class="ds-footer-grid">
        <div class="ds-footer-col ds-footer-main">
          <div class="ds-brand">
            <span class="ds-brand-badge">DS</span>
            <span class="ds-brand-text">Digital<span class="ds-brand-hl">Saathi</span></span>
          </div>
          <p class="ds-footer-p">Your all-in-one digital companion for Indian students, job seekers, and cyber cafés. 100% private, client-side, and free forever.</p>
          <div class="ds-privacy-chip">🔒 Zero Server Uploads • In-Browser Processing</div>
        </div>
        <div class="ds-footer-col">
          <h4 class="ds-footer-h">Popular PDF Tools</h4>
          <ul class="ds-footer-ul">
            <li><a href="merge.html">Merge PDF</a></li>
            <li><a href="split.html">Split PDF</a></li>
            <li><a href="compress.html">Compress PDF</a></li>
            <li><a href="pdf-to-word.html">PDF to Word</a></li>
            <li><a href="jpg-to-pdf.html">JPG to PDF</a></li>
          </ul>
        </div>
        <div class="ds-footer-col">
          <h4 class="ds-footer-h">Cyber Café & Students</h4>
          <ul class="ds-footer-ul">
            <li><a href="../cybercafe/passport-photo.html">Passport Photo Maker</a></li>
            <li><a href="../cybercafe/signature.html">Signature Resizer (<20KB)</a></li>
            <li><a href="../student/resume.html">Resume Builder</a></li>
            <li><a href="../calculators/cgpa.html">CGPA Calculator</a></li>
            <li><a href="../jobs/government.html">Government Jobs</a></li>
          </ul>
        </div>
        <div class="ds-footer-col">
          <h4 class="ds-footer-h">About & Policies</h4>
          <ul class="ds-footer-ul">
            <li><a href="../about.html">About DigitalSaathi</a></li>
            <li><a href="../privacy.html">Privacy Policy</a></li>
            <li><a href="../terms.html">Terms of Service</a></li>
            <li><a href="../contact.html">Contact Us</a></li>
          </ul>
        </div>
      </div>
      <div class="ds-footer-bottom">
        <p>&copy; 2026 DigitalSaathi. Built with privacy by design. All file operations occur entirely inside your browser.</p>
      </div>
    </div>
  </footer>'''

landing_page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PDF Tools for Every Digital Task — 100% Free & Private | DigitalSaathi</title>
  <meta name="description" content="Merge, split, compress, convert, edit and manage your PDF documents with simple browser-based tools. 100% free, private, with zero server uploads.">
  <meta name="keywords" content="pdf tools, merge pdf, split pdf, compress pdf, convert pdf, edit pdf, sign pdf, protect pdf, free online pdf tools, digitalsaathi">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">

  <!-- JSON-LD SEO Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "name": "DigitalSaathi PDF Tools Suite",
        "description": "Comprehensive browser-side PDF tools suite: Merge, Split, Compress, Convert, Edit, Sign, and Protect PDF files.",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All (Web Browser)",
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "INR"
        }}
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
            "name": "Are my PDF documents uploaded to your server?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "No. DigitalSaathi operates 100% locally in your web browser using WebAssembly and JavaScript. Your files never leave your computer."
            }}
          }},
          {{
            "@type": "Question",
            "name": "Is DigitalSaathi free to use without limits?",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "Yes, all 33+ PDF tools are completely free with no daily limits or subscription paywalls."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    /* ==========================================================================
       DIGITALSAATHI CLEAN COMPACT SAAS LANDING STYLES
       ========================================================================== */
    
    /* Header (Compact Desktop & Mobile) */
    .ds-navbar {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 1000;
      height: 60px;
      display: flex;
      align-items: center;
    }}
    .ds-nav-inner {{
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
      padding: 0 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }}
    .ds-brand {{
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      color: #0f172a;
      font-weight: 800;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }}
    .ds-brand-badge {{
      width: 28px;
      height: 28px;
      background: #2563eb;
      color: #ffffff;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 800;
    }}
    .ds-brand-hl {{
      color: #2563eb;
    }}
    .ds-nav-links {{
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    @media (max-width: 960px) {{
      .ds-nav-links {{ display: none; }}
    }}
    .ds-nav-link {{
      padding: 6px 12px;
      font-size: 0.875rem;
      font-weight: 600;
      color: #475569;
      text-decoration: none;
      border-radius: 6px;
      transition: all 0.15s ease;
    }}
    .ds-nav-link:hover {{
      color: #2563eb;
      background: #f1f5f9;
    }}
    .ds-nav-link.active {{
      color: #2563eb;
      background: #eff6ff;
    }}
    .ds-nav-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .ds-search-toggle {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 6px 10px;
      cursor: pointer;
      font-size: 0.9rem;
    }}
    .ds-menu-toggle {{
      display: none;
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px;
      flex-direction: column;
      gap: 4px;
    }}
    .ds-menu-toggle span {{
      width: 20px;
      height: 2px;
      background: #334155;
      border-radius: 2px;
    }}
    @media (max-width: 960px) {{
      .ds-menu-toggle {{ display: flex; }}
    }}
    .ds-mobile-drawer {{
      display: none;
      position: absolute;
      top: 60px;
      left: 0;
      right: 0;
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      padding: 12px 20px;
      box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
      flex-direction: column;
      gap: 8px;
    }}
    .ds-mobile-drawer.open {{
      display: flex;
    }}
    .ds-drawer-link {{
      padding: 10px 12px;
      font-size: 0.95rem;
      font-weight: 600;
      color: #334155;
      text-decoration: none;
      border-radius: 6px;
    }}
    .ds-drawer-link:hover, .ds-drawer-link.active {{
      background: #eff6ff;
      color: #2563eb;
    }}

    /* Compact Hero (50px-70px vertical spacing) */
    .ds-hero {{
      text-align: center;
      padding: 50px 1.25rem 24px;
      max-width: 800px;
      margin: 0 auto;
    }}
    .ds-hero-h1 {{
      font-size: 2.35rem;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.03em;
      line-height: 1.2;
      margin-bottom: 12px;
    }}
    @media (max-width: 640px) {{
      .ds-hero {{ padding: 36px 1rem 16px; }}
      .ds-hero-h1 {{ font-size: 1.75rem; }}
    }}
    .ds-hero-sub {{
      font-size: 1.05rem;
      color: #64748b;
      line-height: 1.55;
      max-width: 620px;
      margin: 0 auto 20px;
    }}

    /* Live Search Bar */
    .ds-search-bar-wrap {{
      max-width: 460px;
      margin: 0 auto 20px;
      position: relative;
    }}
    .ds-search-bar-input {{
      width: 100%;
      padding: 10px 16px 10px 40px;
      border: 1px solid #cbd5e1;
      border-radius: 30px;
      font-size: 0.9rem;
      background: #ffffff;
      outline: none;
      transition: all 0.2s;
    }}
    .ds-search-bar-input:focus {{
      border-color: #2563eb;
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }}
    .ds-search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: #94a3b8;
      font-size: 0.95rem;
      pointer-events: none;
    }}

    /* Category Filter Navigation (Horizontal scroll on mobile, no multi-line wrap) */
    .ds-filter-nav-wrap {{
      border-bottom: 1px solid #e2e8f0;
      margin-bottom: 28px;
    }}
    .ds-filter-nav {{
      display: flex;
      align-items: center;
      gap: 6px;
      overflow-x: auto;
      white-space: nowrap;
      padding: 0 1.25rem 12px;
      max-width: 1280px;
      margin: 0 auto;
      scrollbar-width: none;
      -webkit-overflow-scrolling: touch;
    }}
    .ds-filter-nav::-webkit-scrollbar {{
      display: none;
    }}
    .ds-pill {{
      padding: 7px 16px;
      font-size: 0.8125rem;
      font-weight: 600;
      border-radius: 20px;
      border: 1px solid #e2e8f0;
      background: #ffffff;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s ease;
      flex-shrink: 0;
    }}
    .ds-pill:hover {{
      border-color: #cbd5e1;
      color: #0f172a;
      background: #f8fafc;
    }}
    .ds-pill.active {{
      background: #0f172a;
      color: #ffffff;
      border-color: #0f172a;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}

    /* Tool Grid (Desktop 4-5 cols, Tablet 2-3 cols, Mobile 1 col) */
    .ds-grid-container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.25rem;
    }}
    .ds-tool-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 16px;
      margin-bottom: 48px;
    }}
    @media (min-width: 1280px) {{
      .ds-tool-grid {{
        grid-template-columns: repeat(5, 1fr);
      }}
    }}
    @media (max-width: 992px) and (min-width: 641px) {{
      .ds-tool-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}
    @media (max-width: 640px) {{
      .ds-tool-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Tool Cards */
    .ds-tool-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 20px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s ease;
      min-height: 140px;
      outline: none;
    }}
    .ds-tool-card:hover {{
      border-color: #cbd5e1;
      transform: translateY(-3px);
      box-shadow: 0 8px 16px -4px rgba(0, 0, 0, 0.08);
    }}
    .ds-tool-card:focus-visible {{
      border-color: #2563eb;
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.25);
    }}
    .ds-card-icon {{
      width: 40px;
      height: 40px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
      flex-shrink: 0;
    }}
    .ds-card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 4px 0;
      line-height: 1.3;
    }}
    .ds-card-desc {{
      font-size: 0.8125rem;
      color: #64748b;
      line-height: 1.45;
      margin: 0;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    /* Trust & Privacy Section */
    .ds-trust-section {{
      background: #f8fafc;
      border-top: 1px solid #e2e8f0;
      border-bottom: 1px solid #e2e8f0;
      padding: 40px 1.25rem;
      margin: 32px 0;
    }}
    .ds-trust-inner {{
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 24px;
    }}
    .ds-trust-item {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 20px;
    }}
    .ds-trust-icon {{
      font-size: 1.5rem;
      margin-bottom: 8px;
    }}
    .ds-trust-h {{
      font-size: 1rem;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 4px;
    }}
    .ds-trust-p {{
      font-size: 0.85rem;
      color: #64748b;
      line-height: 1.5;
      margin: 0;
    }}

    /* Clean Compact FAQ */
    .ds-faq-wrap {{
      max-width: 800px;
      margin: 0 auto 48px;
      padding: 0 1.25rem;
    }}
    .ds-faq-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      text-align: center;
      margin-bottom: 20px;
    }}
    .ds-faq-item {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      margin-bottom: 10px;
      overflow: hidden;
    }}
    .ds-faq-summary {{
      padding: 14px 18px;
      font-weight: 600;
      font-size: 0.95rem;
      color: #1e293b;
      cursor: pointer;
      user-select: none;
    }}
    .ds-faq-body {{
      padding: 0 18px 14px;
      font-size: 0.875rem;
      color: #64748b;
      line-height: 1.6;
    }}

    /* Footer */
    .ds-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 48px 1.25rem 24px;
      border-top: 1px solid #1e293b;
    }}
    .ds-footer-container {{
      max-width: 1280px;
      margin: 0 auto;
    }}
    .ds-footer-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 32px;
      margin-bottom: 36px;
    }}
    @media (max-width: 768px) {{
      .ds-footer-grid {{ grid-template-columns: 1fr; gap: 24px; }}
    }}
    .ds-footer-col .ds-brand-text {{
      color: #ffffff;
    }}
    .ds-footer-p {{
      font-size: 0.85rem;
      line-height: 1.6;
      margin: 12px 0;
      max-width: 320px;
    }}
    .ds-privacy-chip {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 600;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }}
    .ds-footer-h {{
      font-size: 0.9rem;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin: 0 0 14px;
    }}
    .ds-footer-ul {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .ds-footer-ul li {{
      margin-bottom: 8px;
    }}
    .ds-footer-ul a {{
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.15s;
    }}
    .ds-footer-ul a:hover {{
      color: #ffffff;
    }}
    .ds-footer-bottom {{
      border-top: 1px solid #1e293b;
      padding-top: 20px;
      text-align: center;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body class="tool-page">

{HEADER_HTML}

  <main>
    <!-- Centered Hero -->
    <section class="ds-hero">
      <h1 class="ds-hero-h1">PDF Tools for Every Digital Task</h1>
      <p class="ds-hero-sub">Merge, split, compress, convert, edit and manage your PDF documents with simple browser-based tools.</p>

      <!-- Instant Live Search Bar -->
      <div class="ds-search-bar-wrap">
        <span class="ds-search-icon">🔍</span>
        <input type="text" id="toolSearch" class="ds-search-bar-input" placeholder="Search any PDF tool (e.g. Merge, Compress, Word, Sign)..." aria-label="Search tools">
      </div>
    </section>

    <!-- Horizontal Category Filter Pills -->
    <div class="ds-filter-nav-wrap">
      <nav class="ds-filter-nav" aria-label="Tool Categories" id="categoryNav">
        <button class="ds-pill active" data-cat="all">All</button>
        <button class="ds-pill" data-cat="organize">Organize PDF</button>
        <button class="ds-pill" data-cat="optimize">Optimize PDF</button>
        <button class="ds-pill" data-cat="convert">Convert PDF</button>
        <button class="ds-pill" data-cat="edit">Edit PDF</button>
        <button class="ds-pill" data-cat="security">PDF Security</button>
        <button class="ds-pill" data-cat="ocr">OCR</button>
        <button class="ds-pill" data-cat="student">Student</button>
        <button class="ds-pill" data-cat="cybercafe">Cyber Café</button>
        <button class="ds-pill" data-cat="advanced">Advanced</button>
      </nav>
    </div>

    <!-- Responsive Tool Grid -->
    <section class="ds-grid-container" aria-label="PDF Tools Grid">
      <div class="ds-tool-grid" id="toolGrid">
        {cards_html}
      </div>
    </section>

    <!-- Trust / Privacy Section -->
    <section class="ds-trust-section" aria-label="Privacy and Trust">
      <div class="ds-trust-inner">
        <div class="ds-trust-item">
          <div class="ds-trust-icon">🔒</div>
          <h3 class="ds-trust-h">100% In-Browser Privacy</h3>
          <p class="ds-trust-p">All file operations run entirely in your local browser. Zero server uploads, zero data retention.</p>
        </div>
        <div class="ds-trust-item">
          <div class="ds-trust-icon">⚡</div>
          <h3 class="ds-trust-h">Instant & Unlimited</h3>
          <p class="ds-trust-p">No daily task limits, no queue wait times, and no paywalls. Instant processing at hardware speed.</p>
        </div>
        <div class="ds-trust-item">
          <div class="ds-trust-icon">🇮🇳</div>
          <h3 class="ds-trust-h">Built for Indian Forms</h3>
          <p class="ds-trust-p">Pre-configured dimension and size limit presets for SSC, UPSC, State PSC, and university portals.</p>
        </div>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section class="ds-faq-wrap" aria-label="Frequently Asked Questions">
      <h2 class="ds-faq-title">Frequently Asked Questions</h2>
      
      <details class="ds-faq-item" open>
        <summary class="ds-faq-summary">Are my PDF files uploaded to external servers?</summary>
        <div class="ds-faq-body">No. Unlike typical online tools, DigitalSaathi processes your files 100% inside your browser using WebAssembly and Web Workers. Your documents never touch any external server.</div>
      </details>

      <details class="ds-faq-item">
        <summary class="ds-faq-summary">How can I compress a PDF under 100KB for government job portals?</summary>
        <div class="ds-faq-body">Use the <b>Compress PDF</b> tool and choose the "SSC / UPSC (&lt;100KB)" preset. It strips heavy metadata and optimizes image streams to pass portal upload validations.</div>
      </details>

      <details class="ds-faq-item">
        <summary class="ds-faq-summary">Can I use DigitalSaathi on mobile phones and tablets?</summary>
        <div class="ds-faq-body">Yes, all tools are fully responsive and touch-friendly on Android, iOS, tablets, and desktop computers.</div>
      </details>

      <details class="ds-faq-item">
        <summary class="ds-faq-summary">Is there any fee or subscription required?</summary>
        <div class="ds-faq-body">No. All DigitalSaathi PDF tools are free to use with unlimited operations.</div>
      </details>
    </section>
  </main>

{FOOTER_HTML}

  <script>
    // Live Search & Category Filter Logic
    const searchInput = document.getElementById('toolSearch');
    const pillButtons = document.querySelectorAll('.ds-pill');
    const toolCards = document.querySelectorAll('.ds-tool-card');
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const headerSearchToggle = document.getElementById('headerSearchToggle');

    let activeCategory = 'all';

    // Filter pills click
    pillButtons.forEach(pill => {{
      pill.addEventListener('click', () => {{
        pillButtons.forEach(b => b.classList.remove('active'));
        pill.classList.add('active');
        activeCategory = pill.dataset.cat;
        applyFilter();
      }});
    }});

    // Search input
    searchInput.addEventListener('input', applyFilter);

    // Header search icon toggle
    if (headerSearchToggle) {{
      headerSearchToggle.addEventListener('click', () => {{
        searchInput.focus();
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});
    }}

    // Mobile menu toggle
    if (mobileMenuToggle && mobileDrawer) {{
      mobileMenuToggle.addEventListener('click', () => {{
        const isOpen = mobileDrawer.classList.toggle('open');
        mobileMenuToggle.setAttribute('aria-expanded', isOpen);
      }});
    }}

    function applyFilter() {{
      const query = searchInput.value.trim().toLowerCase();

      toolCards.forEach(card => {{
        const name = card.dataset.name || '';
        const matchesCategory = (activeCategory === 'all') || card.classList.contains(`cat-${{activeCategory}}`);
        const matchesSearch = !query || name.includes(query) || card.textContent.toLowerCase().includes(query);

        if (matchesCategory && matchesSearch) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>'''

write_file('pdf/index.html', landing_page_html)
print("Successfully generated clean, commercial-grade DigitalSaathi PDF Tools landing page.")
