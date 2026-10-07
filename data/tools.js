/**
 * VYTRA — MASTER TOOLS REGISTRY (data/tools.js)
 * Central structured data registry powering directory, search, category filters, and related tools.
 * Complete 67 Functional Client-Side Tools.
 */

(function () {
  'use strict';

  const TOOLS_DATA = [
    {
        "id": "merge-pdf",
        "name": "Merge PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Combine multiple PDF files into one single organized document in your chosen order.",
        "url": "pdf/merge.html",
        "tags": [
            "merge",
            "combine",
            "join",
            "pdf",
            "binder",
            "pages",
            "organize",
            "merge pdf",
            "merge pdf online",
            "merge pdf free",
            "combine pdf",
            "combine pdf online",
            "join pdf files",
            "merge multiple pdf files",
            "combine pdf pages into one document",
            "pdf joiner online free"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "split-pdf",
        "name": "Split PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Extract specific pages or separate a PDF into individual one-page documents.",
        "url": "pdf/split.html",
        "tags": [
            "split",
            "extract",
            "separate",
            "pages",
            "cut",
            "pdf",
            "split pdf",
            "split pdf online",
            "split pdf pages",
            "extract pdf pages",
            "separate pdf pages",
            "delete pages from pdf",
            "remove pages from pdf",
            "reorder pdf pages",
            "cut pdf document"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "compress-pdf",
        "name": "Compress PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Reduce PDF file size to under 100KB, 200KB or 500KB while maintaining optimal quality.",
        "url": "pdf/compress.html",
        "tags": [
            "compress",
            "reduce",
            "size",
            "kb",
            "mb",
            "shrink",
            "optimize",
            "pdf",
            "compress pdf",
            "compress pdf online",
            "compress pdf free",
            "reduce pdf size",
            "reduce pdf file size",
            "pdf compressor",
            "compress pdf to 100kb",
            "compress pdf to 200kb",
            "compress pdf to 500kb",
            "shrink pdf online"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "jpg-to-pdf",
        "name": "JPG to PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert JPG, PNG, and WebP images into a single professional A4 PDF document.",
        "url": "pdf/jpg-to-pdf.html",
        "tags": [
            "jpg to pdf",
            "images to pdf",
            "png to pdf",
            "convert",
            "a4",
            "photos to pdf",
            "image to pdf",
            "image to pdf converter",
            "convert image to pdf",
            "image to pdf online",
            "image to pdf online free",
            "image to pdf free",
            "photo to pdf",
            "photo to pdf converter",
            "picture to pdf",
            "picture to pdf converter",
            "convert picture to pdf",
            "images to pdf converter",
            "convert images to pdf",
            "image converter to pdf",
            "make pdf from image",
            "make pdf from photos",
            "create pdf from images",
            "turn image into pdf",
            "turn photos into pdf",
            "jpg to pdf converter",
            "jpg to pdf online",
            "jpg to pdf online free",
            "jpg to pdf free",
            "convert jpg to pdf",
            "convert jpg to pdf online",
            "convert jpg to pdf free",
            "jpg image to pdf",
            "jpg image to pdf converter",
            "jpeg to pdf",
            "jpeg to pdf converter",
            "jpeg to pdf online",
            "jpeg to pdf free",
            "convert jpeg to pdf",
            "jpg pictures to pdf",
            "jpg images to pdf",
            "multiple jpg to pdf",
            "multiple jpg images to pdf",
            "jpg files to pdf",
            "jpg photos to pdf",
            "combine jpg into pdf",
            "merge jpg into pdf",
            "jpg to one pdf",
            "convert multiple jpg to one pdf",
            "jpg to pdf without losing quality",
            "jpg to pdf high quality",
            "jpg to pdf without registration",
            "jpg to pdf without software",
            "jpg to pdf on mobile",
            "png to pdf converter",
            "png to pdf online",
            "png to pdf online free",
            "png to pdf free",
            "convert png to pdf",
            "convert png to pdf online",
            "png image to pdf",
            "png images to pdf",
            "multiple png to pdf",
            "multiple png images to pdf",
            "png files to pdf",
            "png picture to pdf",
            "png photo to pdf",
            "combine png into pdf",
            "merge png into pdf",
            "png to one pdf",
            "png to pdf high quality",
            "png to pdf without software",
            "png to pdf on mobile",
            "multiple images to pdf",
            "multiple images to one pdf",
            "multiple photos to pdf",
            "multiple pictures to pdf",
            "multiple image pdf maker",
            "combine images into pdf",
            "combine photos into pdf",
            "combine pictures into pdf",
            "merge images into pdf",
            "merge photos into pdf",
            "merge pictures into pdf",
            "images into one pdf",
            "photos into one pdf",
            "pictures into one pdf",
            "create pdf from multiple images",
            "create pdf from multiple photos",
            "make pdf from multiple pictures",
            "convert multiple images to pdf",
            "convert multiple photos to pdf",
            "convert multiple pictures to pdf"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "pdf-to-jpg",
        "name": "PDF to JPG",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert PDF document pages into high-resolution JPG or PNG images with ZIP download.",
        "url": "pdf/pdf-to-jpg.html",
        "tags": [
            "pdf to jpg",
            "pdf to image",
            "pdf to images",
            "pdf to png",
            "pdf to webp",
            "pdf24 alternative",
            "convert",
            "pages to jpg",
            "extract images",
            "png",
            "pdf to jpg converter",
            "pdf to jpg online",
            "pdf to jpg online free",
            "convert pdf to jpg",
            "pdf to jpeg",
            "pdf to jpeg converter",
            "pdf to png converter",
            "pdf to png online",
            "convert pdf to png",
            "pdf to image converter",
            "convert pdf to image",
            "pdf pages to jpg",
            "pdf pages to png",
            "extract images from pdf",
            "save pdf as jpg",
            "turn pdf into image",
            "convert pdf pages to images",
            "pdf to images converter",
            "export pdf to picture",
            "pdf to high quality jpg",
            "pdf to picture online"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "edit-pdf",
        "name": "Edit PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Add text, signatures, shapes, annotations, and images directly onto any PDF document.",
        "url": "pdf/edit.html",
        "tags": [
            "edit",
            "annotate",
            "text",
            "shapes",
            "draw",
            "markup",
            "pdf",
            "pdf editor online",
            "edit pdf online",
            "annotate pdf",
            "add text to pdf",
            "draw on pdf",
            "fill pdf online"
        ],
        "popular": false,
        "badge": "New"
    },
    {
        "id": "sign-pdf",
        "name": "Sign PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Draw, type, or upload your electronic signature and place it securely on PDF contracts.",
        "url": "pdf/sign.html",
        "tags": [
            "sign",
            "signature",
            "esign",
            "draw",
            "contract",
            "pdf",
            "sign pdf online",
            "digital signature pdf",
            "sign contract pdf free"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "protect-pdf",
        "name": "Protect PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Encrypt your PDF with strong AES passwords to prevent unauthorized access and copying.",
        "url": "pdf/protect.html",
        "tags": [
            "protect",
            "encrypt",
            "password",
            "lock",
            "secure",
            "pdf",
            "protect pdf",
            "password protect pdf",
            "encrypt pdf",
            "lock pdf file with password"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "unlock-pdf",
        "name": "Unlock PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Remove password security and usage restrictions from your encrypted PDF documents.",
        "url": "pdf/unlock.html",
        "tags": [
            "unlock",
            "remove password",
            "decrypt",
            "open",
            "permissions",
            "pdf",
            "unlock pdf",
            "remove pdf password",
            "decrypt pdf",
            "unlock protected pdf online"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "rotate-pdf",
        "name": "Rotate PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Rotate individual or all pages in your PDF document clockwise or counterclockwise.",
        "url": "pdf/rotate.html",
        "tags": [
            "rotate",
            "turn",
            "orientation",
            "landscape",
            "portrait",
            "degrees",
            "pdf",
            "rotate pdf",
            "rotate pdf online",
            "rotate pdf 90 degrees",
            "rotate pdf pages permanently"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "organize-pdf",
        "name": "Organize PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Visually rearrange, reorder, duplicate, or delete pages in your PDF document.",
        "url": "pdf/organize.html",
        "tags": [
            "organize",
            "reorder",
            "pages",
            "delete",
            "sort",
            "arrange",
            "pdf"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-to-word",
        "name": "PDF to Word",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert PDF documents into editable Microsoft Word (.docx) files with formatting intact.",
        "url": "pdf/pdf-to-word.html",
        "tags": [
            "pdf to word",
            "pdf to docx",
            "convert",
            "editable",
            "document",
            "pdf to word converter",
            "pdf to word online",
            "convert pdf to word",
            "convert pdf to docx",
            "pdf to word editable",
            "extract text from pdf to docx",
            "pdf to word online free"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "word-to-pdf",
        "name": "Word to PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert DOC and DOCX Word documents into standard high-fidelity PDF files.",
        "url": "pdf/word-to-pdf.html",
        "tags": [
            "word to pdf",
            "docx to pdf",
            "convert",
            "document",
            "save pdf",
            "word to pdf converter",
            "convert docx to pdf",
            "convert word to pdf online free"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-to-excel",
        "name": "PDF to Excel",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Extract tables and structured financial data from PDF documents into Excel spreadsheets (.xlsx).",
        "url": "pdf/pdf-to-excel.html",
        "tags": [
            "pdf to excel",
            "pdf to xlsx",
            "tables",
            "spreadsheet",
            "data extract",
            "pdf to excel converter",
            "convert pdf to excel",
            "pdf tables to excel"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "excel-to-pdf",
        "name": "Excel to PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert Excel workbooks and sheets into cleanly formatted printable PDF documents.",
        "url": "pdf/excel-to-pdf.html",
        "tags": [
            "excel to pdf",
            "xlsx to pdf",
            "convert",
            "spreadsheet",
            "print",
            "convert xlsx to pdf",
            "convert excel to pdf online"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-to-ppt",
        "name": "PDF to PowerPoint",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert PDF slides into editable Microsoft PowerPoint presentation decks (.pptx).",
        "url": "pdf/pdf-to-ppt.html",
        "tags": [
            "pdf to ppt",
            "pdf to powerpoint",
            "slides",
            "presentation",
            "pdf to pptx",
            "convert pdf to powerpoint",
            "pdf slides to pptx"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "ppt-to-pdf",
        "name": "PowerPoint to PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert PowerPoint presentation slides into non-editable, shareable PDF documents.",
        "url": "pdf/ppt-to-pdf.html",
        "tags": [
            "ppt to pdf",
            "powerpoint to pdf",
            "presentation",
            "slides",
            "pptx to pdf",
            "convert powerpoint to pdf"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-a",
        "name": "PDF/A Converter",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert PDF files to ISO standardized PDF/A format for long-term document archival.",
        "url": "pdf/pdf-a.html",
        "tags": [
            "pdfa",
            "pdf a",
            "archive",
            "iso standard",
            "compliance"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "repair-pdf",
        "name": "Repair PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Recover and repair damaged, corrupted, or unreadable PDF files in your browser.",
        "url": "pdf/repair.html",
        "tags": [
            "repair",
            "fix",
            "corrupt",
            "damaged",
            "recover",
            "pdf"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "page-numbers",
        "name": "Add Page Numbers",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Insert custom page numbers, headers, and footers with customizable font and position.",
        "url": "pdf/page-numbers.html",
        "tags": [
            "page numbers",
            "header",
            "footer",
            "numbering",
            "pagination"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "scan-to-pdf",
        "name": "Scan to PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Capture documents using your mobile or webcam and save them directly as a crisp PDF.",
        "url": "pdf/scan-to-pdf.html",
        "tags": [
            "scan",
            "scanner",
            "camera",
            "photo to pdf",
            "capture"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "ocr-pdf",
        "name": "OCR PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Extract selectable text from scanned paper PDFs using client-side Optical Character Recognition.",
        "url": "pdf/ocr.html",
        "tags": [
            "ocr",
            "text recognition",
            "scanned",
            "searchable",
            "extract text"
        ],
        "popular": true,
        "badge": "AI"
    },
    {
        "id": "compare-pdf",
        "name": "Compare PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Visually compare two PDF documents side-by-side to highlight text and layout differences.",
        "url": "pdf/compare.html",
        "tags": [
            "compare",
            "diff",
            "side by side",
            "changes",
            "revisions"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "redact-pdf",
        "name": "Redact PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Permanently blackout and erase sensitive personal data, Aadhaar, and confidential text from PDF.",
        "url": "pdf/redact.html",
        "tags": [
            "redact",
            "blackout",
            "censor",
            "privacy",
            "erase",
            "sensitive"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "crop-pdf",
        "name": "Crop PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Trim unwanted margins and crop PDF page dimensions to fit specific paper sizes.",
        "url": "pdf/crop.html",
        "tags": [
            "crop",
            "trim",
            "margins",
            "cut",
            "box",
            "dimensions"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "forms-pdf",
        "name": "PDF Form Filler",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Fill out interactive PDF form fields, check checkboxes, and flatten form data.",
        "url": "pdf/forms.html",
        "tags": [
            "forms",
            "fill",
            "form filler",
            "flatten",
            "acroforms"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "ai-summarizer",
        "name": "AI PDF Summarizer",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Generate instant key insights, summaries, and bullet points from lengthy PDF documents.",
        "url": "pdf/ai-summarizer.html",
        "tags": [
            "ai",
            "summarize",
            "summary",
            "key points",
            "insights"
        ],
        "popular": true,
        "badge": "AI"
    },
    {
        "id": "translate-pdf",
        "name": "Translate PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Translate PDF text into Hindi, English, and major regional languages privately.",
        "url": "pdf/translate.html",
        "tags": [
            "translate",
            "language",
            "hindi",
            "english",
            "regional"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-to-markdown",
        "name": "PDF to Markdown",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Extract headings, code blocks, lists, and formatted text from PDF into clean Markdown (.md).",
        "url": "pdf/pdf-to-markdown.html",
        "tags": [
            "markdown",
            "pdf to md",
            "extract",
            "documentation"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-info",
        "name": "PDF Metadata & Info",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Inspect PDF author, title, creation date, fonts, security permissions, and page metrics.",
        "url": "pdf/info.html",
        "tags": [
            "metadata",
            "info",
            "inspect",
            "fonts",
            "author",
            "pages"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "page-counter",
        "name": "PDF Page Counter",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Instantly calculate total page counts, color breakdown, and estimated cyber caf\u00e9 print costs.",
        "url": "pdf/page-counter.html",
        "tags": [
            "page count",
            "counter",
            "print cost",
            "cyber cafe",
            "pages"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-viewer",
        "name": "In-Browser PDF Viewer",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Fast, secure client-side PDF reader with zoom, page navigation, and text search.",
        "url": "pdf/viewer.html",
        "tags": [
            "viewer",
            "reader",
            "view",
            "read",
            "open pdf"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "extract-pdf",
        "name": "Extract PDF Pages",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Selectively extract specific pages or page ranges into a separate new PDF document.",
        "url": "pdf/extract.html",
        "tags": [
            "extract",
            "pages",
            "select",
            "export",
            "range"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "reorder-pdf",
        "name": "Reorder PDF Pages",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Drag and drop PDF page thumbnails to change their sequential order effortlessly.",
        "url": "pdf/reorder.html",
        "tags": [
            "reorder",
            "drag",
            "drop",
            "sort",
            "sequence"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "watermark-pdf",
        "name": "Watermark PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Add custom text stamps, confidential watermarks, or company logos across PDF pages.",
        "url": "pdf/watermark.html",
        "tags": [
            "watermark",
            "stamp",
            "logo",
            "confidential",
            "draft",
            "watermark pdf",
            "add watermark to pdf",
            "stamp pdf",
            "text watermark on pdf"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "pdf-workflow",
        "name": "PDF Workflow Automation",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Chain multiple PDF actions (merge, compress, and sign) into one automated sequence.",
        "url": "pdf/workflow.html",
        "tags": [
            "workflow",
            "automation",
            "batch",
            "pipeline",
            "chain"
        ],
        "popular": false,
        "badge": "Pro"
    },
    {
        "id": "html-to-pdf",
        "name": "HTML to PDF",
        "category": "pdf",
        "categoryName": "PDF Tools",
        "description": "Convert HTML code, webpages, or styled snippets into high-quality printable PDF files.",
        "url": "pdf/html-to-pdf.html",
        "tags": [
            "html to pdf",
            "webpage to pdf",
            "code to pdf",
            "convert"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "image-compressor",
        "name": "Image Compressor",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Compress JPG, PNG, and WebP images to under 20KB, 50KB, or 100KB for government forms.",
        "url": "image/compress.html",
        "tags": [
            "compress",
            "reduce size",
            "kb",
            "20kb",
            "50kb",
            "100kb",
            "ssc",
            "upsc",
            "image compressor",
            "image compressor online",
            "compress image",
            "compress image online",
            "compress jpg",
            "compress png",
            "compress webp",
            "reduce image size",
            "reduce jpg size",
            "reduce png size",
            "compress photo under 20kb",
            "compress photo under 50kb",
            "compress photo under 100kb",
            "photo compressor",
            "india",
            "indian form",
            "ssc",
            "upsc",
            "ibps",
            "govt exam",
            "passport size",
            "20kb",
            "50kb",
            "100kb"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "image-resizer",
        "name": "Image Resizer",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Resize photos to exact pixel dimensions, centimeters, and aspect ratios with aspect lock.",
        "url": "image/resize.html",
        "tags": [
            "resize",
            "dimensions",
            "width",
            "height",
            "pixels",
            "aspect ratio",
            "image resizer",
            "image resize online",
            "resize image",
            "resize jpg",
            "resize png",
            "photo resizer",
            "resize image in pixels",
            "resize photo in cm",
            "passport size photo resizer"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "image-cropper",
        "name": "Photo Cropper",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Crop photos with precision preset ratios including 1:1 square, 3.5x4.5cm passport, and 16:9.",
        "url": "image/crop.html",
        "tags": [
            "crop",
            "cut",
            "trim",
            "ratio",
            "square",
            "avatar",
            "image cropper",
            "crop image online",
            "crop photo",
            "square crop",
            "circle crop avatar"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "image-converter",
        "name": "Universal Image Converter",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Convert images between JPG, PNG, WebP, GIF, BMP, and SVG formats in batch.",
        "url": "image/convert.html",
        "tags": [
            "convert",
            "format",
            "jpg to png",
            "png to jpg",
            "webp",
            "batch"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "passport-photo",
        "name": "Passport Photo Maker",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Generate 3.5x4.5cm Indian passport and exam photo sheets formatted for A4 photo printouts.",
        "url": "image/passport-photo.html",
        "tags": [
            "passport",
            "photo",
            "3.5x4.5",
            "a4",
            "sheet",
            "ssc",
            "upsc",
            "print",
            "india",
            "indian form",
            "ssc",
            "upsc",
            "ibps",
            "govt exam",
            "passport size",
            "20kb",
            "50kb",
            "100kb"
        ],
        "popular": true,
        "badge": "Essential"
    },
    {
        "id": "signature-resizer",
        "name": "Signature Resizer",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Resize candidate signatures to SSC/IBPS/UPSC specifications (140x60px, under 20KB).",
        "url": "image/signature.html",
        "tags": [
            "signature",
            "resizer",
            "ssc",
            "ibps",
            "upsc",
            "20kb",
            "140x60",
            "india",
            "indian form",
            "ssc",
            "upsc",
            "ibps",
            "govt exam",
            "passport size",
            "20kb",
            "50kb",
            "100kb"
        ],
        "popular": true,
        "badge": "Essential"
    },
    {
        "id": "remove-bg",
        "name": "Passport BG Color Replacer",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Replace passport photo backgrounds with official plain white, light blue, or red backdrop.",
        "url": "image/remove-bg.html",
        "tags": [
            "background",
            "remove bg",
            "white background",
            "passport",
            "photo",
            "remove background hd",
            "remove bg in hd quality",
            "transparent png maker",
            "photo background eraser",
            "white background photo maker",
            "passport background changer online free"
        ],
        "popular": false,
        "badge": "New"
    },
    {
        "id": "blur-face",
        "name": "Face Blur & Redact Privacy Tool",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Pixelate or blackout faces, Aadhaar numbers, and sensitive details for privacy protection.",
        "url": "image/blur-face.html",
        "tags": [
            "blur",
            "face",
            "redact",
            "censor",
            "aadhaar",
            "privacy",
            "pixelate"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "bulk-resize",
        "name": "Bulk Image Resizer",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Resize and compress dozens of photos simultaneously with single ZIP batch download.",
        "url": "image/bulk-resize.html",
        "tags": [
            "bulk",
            "batch",
            "multiple",
            "resize",
            "compress",
            "zip"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "color-picker",
        "name": "Image Color Picker & Palette",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Pick exact Hex and RGB colors from photos with high-precision magnifier loupe.",
        "url": "image/color-picker.html",
        "tags": [
            "color picker",
            "eyedropper",
            "palette",
            "hex",
            "rgb"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "dpi-converter",
        "name": "300 DPI Converter",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Convert image resolution to 200, 300, or 600 DPI for official government printing standards.",
        "url": "image/dpi-converter.html",
        "tags": [
            "dpi",
            "ppi",
            "300 dpi",
            "print quality",
            "resolution",
            "india",
            "indian form",
            "ssc",
            "upsc",
            "ibps",
            "govt exam",
            "passport size",
            "20kb",
            "50kb",
            "100kb"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "jpg-to-png",
        "name": "JPG to PNG Converter",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Convert lossy JPG images to clean, lossless PNG format with transparent background support.",
        "url": "image/jpg-to-png.html",
        "tags": [
            "jpg to png",
            "convert",
            "lossless",
            "transparent",
            "jpg to png converter",
            "jpg to png online",
            "convert jpg to png"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "png-to-jpg",
        "name": "PNG to JPG Converter",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Convert PNG images to lightweight JPG format with custom background color fill.",
        "url": "image/png-to-jpg.html",
        "tags": [
            "png to jpg",
            "convert",
            "jpeg",
            "white background",
            "png to jpg converter",
            "convert png to jpg",
            "convert png with white background"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "webp-converter",
        "name": "WebP Converter",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Convert images to ultra-lightweight Google WebP format or decode WebP to JPG/PNG.",
        "url": "image/webp-converter.html",
        "tags": [
            "webp",
            "convert to webp",
            "modern image",
            "speed",
            "webp to jpg",
            "webp to png",
            "jpg to webp",
            "png to webp",
            "webp converter",
            "convert image to webp",
            "heic to jpg",
            "heic to png",
            "heic converter",
            "avif to jpg",
            "avif to png"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "rotate-image",
        "name": "Rotate & Flip Image",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Rotate photos 90 or 180 degrees, flip horizontally for mirrored selfies, or flip vertically.",
        "url": "image/rotate.html",
        "tags": [
            "rotate",
            "flip",
            "mirror",
            "degrees",
            "turn"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "image-watermark",
        "name": "Photo Watermark Tool",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Add copyright text stamps, repeated diagonal tiles, or image logos to your photography.",
        "url": "image/watermark.html",
        "tags": [
            "watermark",
            "stamp",
            "logo",
            "copyright",
            "protection"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "photo-enhancer",
        "name": "Scan & Xerox Enhancer",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Boost contrast, clarify faded scans, and apply clean black-and-white Xerox photocopy filters.",
        "url": "image/photo-enhancer.html",
        "tags": [
            "enhance",
            "scan",
            "xerox",
            "contrast",
            "clarify",
            "marksheet",
            "india",
            "indian form",
            "ssc",
            "upsc",
            "ibps",
            "govt exam",
            "passport size",
            "20kb",
            "50kb",
            "100kb"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "image-base64",
        "name": "Image to Base64",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Convert image files into Base64 Data URI strings for inline CSS, HTML, and web embedding.",
        "url": "image/base64.html",
        "tags": [
            "base64",
            "data uri",
            "inline image",
            "css",
            "html"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "image-jpg-to-pdf",
        "name": "Image to PDF Converter",
        "category": "image",
        "categoryName": "Image Tools",
        "description": "Combine multiple photo files into a single A4 PDF document directly from image tools.",
        "url": "image/jpg-to-pdf.html",
        "tags": [
            "jpg to pdf",
            "photos to pdf",
            "images to pdf",
            "a4",
            "image to pdf",
            "image to pdf converter",
            "convert image to pdf",
            "image to pdf online",
            "image to pdf online free",
            "image to pdf free",
            "photo to pdf",
            "photo to pdf converter",
            "picture to pdf",
            "picture to pdf converter",
            "convert picture to pdf",
            "images to pdf converter",
            "convert images to pdf",
            "image converter to pdf",
            "make pdf from image",
            "make pdf from photos",
            "create pdf from images",
            "turn image into pdf",
            "turn photos into pdf",
            "jpg to pdf converter",
            "jpg to pdf online",
            "jpg to pdf online free",
            "jpg to pdf free",
            "convert jpg to pdf",
            "convert jpg to pdf online",
            "convert jpg to pdf free",
            "jpg image to pdf",
            "jpg image to pdf converter",
            "jpeg to pdf",
            "jpeg to pdf converter",
            "jpeg to pdf online",
            "jpeg to pdf free",
            "convert jpeg to pdf",
            "jpg pictures to pdf",
            "jpg images to pdf",
            "multiple jpg to pdf",
            "multiple jpg images to pdf",
            "jpg files to pdf",
            "jpg photos to pdf",
            "combine jpg into pdf",
            "merge jpg into pdf",
            "jpg to one pdf",
            "convert multiple jpg to one pdf",
            "jpg to pdf without losing quality",
            "jpg to pdf high quality",
            "jpg to pdf without registration",
            "jpg to pdf without software",
            "jpg to pdf on mobile",
            "png to pdf",
            "png to pdf converter",
            "png to pdf online",
            "png to pdf online free",
            "png to pdf free",
            "convert png to pdf",
            "convert png to pdf online",
            "png image to pdf",
            "png images to pdf",
            "multiple png to pdf",
            "multiple png images to pdf",
            "png files to pdf",
            "png picture to pdf",
            "png photo to pdf",
            "combine png into pdf",
            "merge png into pdf",
            "png to one pdf",
            "png to pdf high quality",
            "png to pdf without software",
            "png to pdf on mobile",
            "multiple images to pdf",
            "multiple images to one pdf",
            "multiple photos to pdf",
            "multiple pictures to pdf",
            "multiple image pdf maker",
            "combine images into pdf",
            "combine photos into pdf",
            "combine pictures into pdf",
            "merge images into pdf",
            "merge photos into pdf",
            "merge pictures into pdf",
            "images into one pdf",
            "photos into one pdf",
            "pictures into one pdf",
            "create pdf from multiple images",
            "create pdf from multiple photos",
            "make pdf from multiple pictures",
            "convert multiple images to pdf",
            "convert multiple photos to pdf",
            "convert multiple pictures to pdf"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "word-counter",
        "name": "Word Counter & Text Analyzer",
        "category": "text",
        "categoryName": "Text Tools",
        "description": "Real-time word count, character counter (with/without spaces), reading speed, and keyword density.",
        "url": "text/word-counter.html",
        "tags": [
            "word counter",
            "characters",
            "reading time",
            "paragraphs",
            "sentences",
            "seo",
            "character counter",
            "sentence counter",
            "case converter",
            "uppercase to lowercase",
            "lowercase to uppercase",
            "reading time calculator"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "qr-generator",
        "name": "QR Code Generator",
        "category": "utilities",
        "categoryName": "Utility Tools",
        "description": "Generate static vector QR codes for UPI payments, WiFi networks, URLs, and vCards.",
        "url": "utilities/qr-generator.html",
        "tags": [
            "qr code",
            "upi qr",
            "wifi qr",
            "vcard",
            "url qr",
            "generator",
            "qr code generator",
            "make qr code",
            "free qr generator",
            "upi qr code generator",
            "wifi qr code maker"
        ],
        "popular": true,
        "badge": "Popular"
    },
    {
        "id": "password-generator",
        "name": "Secure Password Generator",
        "category": "utilities",
        "categoryName": "Utility Tools",
        "description": "Generate high-entropy cryptographically strong passwords and passphrases in your browser.",
        "url": "utilities/password-generator.html",
        "tags": [
            "password",
            "generator",
            "secure",
            "crypto",
            "random",
            "strong",
            "password generator",
            "random password generator",
            "strong password maker",
            "secure password generator"
        ],
        "popular": false,
        "badge": ""
    },
    {
        "id": "create-invoice",
        "name": "Create Invoice",
        "category": "invoices",
        "categoryName": "Invoices",
        "description": "Create professional GST-compliant tax invoices with automatic CGST, SGST, IGST, and instant PDF download.",
        "url": "pdf/create-invoice.html",
        "tags": [
            "invoice",
            "create invoice",
            "gst invoice",
            "tax invoice",
            "billing",
            "bill",
            "receipt",
            "pdf invoice"
        ],
        "popular": true,
        "badge": "GST Ready"
    },
    {
        "id": "create-invoice-visually",
        "name": "Create Invoice Visually",
        "category": "invoices",
        "categoryName": "Invoices",
        "description": "WYSIWYG visual invoice editor with live editable A4 paper sheet, custom logo upload, and 1-click vector PDF.",
        "url": "pdf/create-invoice-visually.html",
        "tags": [
            "visual invoice",
            "wysiwyg invoice",
            "live editor",
            "a4 sheet",
            "printable invoice",
            "invoice designer"
        ],
        "popular": true,
        "badge": "WYSIWYG"
    },
    {
        "id": "create-electronic-invoice",
        "name": "Create Electronic Invoice",
        "category": "invoices",
        "categoryName": "Invoices",
        "description": "Generate European standard ZUGFeRD 2.2 / Factur-X XML, UBL 2.1 OASIS XML, and Indian GST e-Invoice JSON.",
        "url": "pdf/create-electronic-invoice.html",
        "tags": [
            "electronic invoice",
            "e-invoice",
            "zugferd",
            "factur-x",
            "ubl",
            "xml",
            "gst json",
            "b2b"
        ],
        "popular": false,
        "badge": "ZUGFeRD / UBL"
    },
    {
        "id": "pdf-invoice-to-e-invoice",
        "name": "PDF Invoice to E-Invoice",
        "category": "invoices",
        "categoryName": "Invoices",
        "description": "Extract structured data from standard PDF invoices and convert to ZUGFeRD XML and Indian GST e-Invoice JSON.",
        "url": "pdf/pdf-invoice-to-e-invoice.html",
        "tags": [
            "pdf to e-invoice",
            "extract invoice",
            "invoice parser",
            "pdf.js",
            "xml converter",
            "zugferd"
        ],
        "popular": false,
        "badge": "Smart Parser"
    },
    {
        "id": "xml-e-invoice-to-pdf",
        "name": "XML E-Invoice to PDF",
        "category": "invoices",
        "categoryName": "Invoices",
        "description": "Upload any ZUGFeRD, XRechnung, UBL XML, or GST JSON electronic invoice and render into a beautiful printable PDF.",
        "url": "pdf/xml-e-invoice-to-pdf.html",
        "tags": [
            "xml to pdf",
            "e-invoice visualizer",
            "xrechnung to pdf",
            "ubl visualizer",
            "zugferd to pdf"
        ],
        "popular": false,
        "badge": "Visualizer"
    },
    {
        "id": "validate-e-invoice",
        "name": "Validate E-Invoice",
        "category": "invoices",
        "categoryName": "Invoices",
        "description": "Validate electronic invoice compliance against EN 16931 rules, syntax schema, and tax math with compliance certificate.",
        "url": "pdf/validate-e-invoice.html",
        "tags": [
            "validate invoice",
            "e-invoice validator",
            "en 16931",
            "audit invoice",
            "compliance certificate"
        ],
        "popular": false,
        "badge": "Compliance"
    },
    {
        "id": "image-hd-converter",
        "name": "Image HD Converter",
        "category": "images",
        "categoryName": "Image Tools",
        "description": "Upscale low-resolution blurry photos to Full HD (1080p), 2K, or 4K Ultra HD with edge sharpening and 300 DPI support.",
        "url": "image/hd-converter.html",
        "tags": [
            "image hd",
            "hd converter",
            "upscale",
            "4k converter",
            "1080p",
            "sharpen",
            "clarify",
            "unsharp mask",
            "image hd converter",
            "upscale image to 4k",
            "convert low quality photo to hd",
            "photo enhancer 4k",
            "sharpen blurry image",
            "enhance photo clarity online free"
        ],
        "popular": true,
        "badge": "4K Ultra HD"
    }
];

  // Path resolution utility for nested directories
  function resolveToolUrl(url) {
    if (!url) return '#';
    if (url.startsWith('http://') || url.startsWith('https://') || url.startsWith('#')) return url;
    
    // Check nesting level of current document
    const path = window.location.pathname.replace(/\\/g, '/');
    let prefix = '';
    
    if (path.includes('/tools/') || path.includes('/pdf/') || path.includes('/image/') || 
        path.includes('/developer/') || path.includes('/calculators/') || 
        path.includes('/text/') || path.includes('/utilities/')) {
      prefix = '../';
    }
    
    const cleanUrl = url.replace(/^\/+/, '');
    return prefix + cleanUrl;
  }

  // =========================================================================
  // Professional Vector SVG Icon Tile Generator (Like iLovePDF SaaS standard)
  // =========================================================================
  const SVG_ICONS = {
    'merge-pdf': {
      bg: '#ffefe8', color: '#ea580c',
      svg: '<svg viewBox="0 0 24 24"><path d="M4 4l6 6M4 10h6V4M20 20l-6-6M20 14h-6v6"/><line x1="12" y1="2" x2="12" y2="22" stroke-dasharray="3 3"/></svg>'
    },
    'split-pdf': {
      bg: '#ffefe8', color: '#ea580c',
      svg: '<svg viewBox="0 0 24 24"><path d="M10 4L4 10M4 4h6M4 4v6M14 20l6-6M20 20h-6M20 20v-6"/><line x1="12" y1="2" x2="12" y2="22" stroke-dasharray="3 3"/></svg>'
    },
    'compress-pdf': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><path d="M4 14h6v6M4 20l6-6M20 10h-6V4M20 4l-6 6M14 14h6v6M14 20l6-6M10 10H4V4M4 4l6 6"/></svg>'
    },
    'jpg-to-pdf': {
      bg: '#fef2f2', color: '#dc2626',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>'
    },
    'pdf-to-jpg': {
      bg: '#fffbeb', color: '#d97706',
      svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><circle cx="10" cy="13" r="1.5"/><path d="m18 18-3.5-3.5a1.4 1.4 0 0 0-2 0L8 19"/></svg>'
    },
    'edit-pdf': {
      bg: '#fdf4ff', color: '#9333ea',
      svg: '<svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>'
    },
    'sign-pdf': {
      bg: '#fff1f2', color: '#e11d48',
      svg: '<svg viewBox="0 0 24 24"><path d="m3 21 1.9-5.7a8.5 8.5 0 1 1 3.8 3.8z"/><path d="M8 12c2 0 3-1 3-2s-1-2-2.5-2C7 8 7 10 8 12c1 2 3 3 5 3s4-1 4-2"/></svg>'
    },
    'protect-pdf': {
      bg: '#faf5ff', color: '#7c3aed',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
    },
    'unlock-pdf': {
      bg: '#ecfeff', color: '#0891b2',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>'
    },
    'rotate-pdf': {
      bg: '#eff6ff', color: '#3b82f6',
      svg: '<svg viewBox="0 0 24 24"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>'
    },
    'organize-pdf': {
      bg: '#f0fdf4', color: '#16a34a',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>'
    },
    'ocr-pdf': {
      bg: '#fdf2f8', color: '#db2777',
      svg: '<svg viewBox="0 0 24 24"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'
    },
    'ai-summarizer': {
      bg: '#eef2ff', color: '#4f46e5',
      svg: '<svg viewBox="0 0 24 24"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>'
    },
    'image-compressor': {
      bg: '#f5f3ff', color: '#6366f1',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><polyline points="8 12 12 16 16 12"/><line x1="12" y1="8" x2="12" y2="16"/></svg>'
    },
    'image-resizer': {
      bg: '#f5f3ff', color: '#6366f1',
      svg: '<svg viewBox="0 0 24 24"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>'
    },
    'image-cropper': {
      bg: '#f5f3ff', color: '#6366f1',
      svg: '<svg viewBox="0 0 24 24"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>'
    },
    'image-converter': {
      bg: '#ecfeff', color: '#0891b2',
      svg: '<svg viewBox="0 0 24 24"><path d="M17 1l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 23l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>'
    },
    'passport-photo': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 19a5 5 0 0 1 10 0"/></svg>'
    },
    'signature-resizer': {
      bg: '#fff1f2', color: '#e11d48',
      svg: '<svg viewBox="0 0 24 24"><path d="M3 18c3-4 6 2 9-1s6-4 9-1"/><line x1="3" y1="21" x2="21" y2="21"/></svg>'
    },
    'remove-bg': {
      bg: '#fdf2f8', color: '#db2777',
      svg: '<svg viewBox="0 0 24 24"><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"/></svg>'
    },
    'blur-face': {
      bg: '#f1f5f9', color: '#475569',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>'
    },
    'json-formatter': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><polyline points="8 3 4 8 4 12 2 12 4 12 4 16 8 21"/><polyline points="16 3 20 8 20 12 22 12 20 12 20 16 16 21"/></svg>'
    },
    'base64-converter': {
      bg: '#eef2ff', color: '#4f46e5',
      svg: '<svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
    },
    'sql-formatter': {
      bg: '#eff6ff', color: '#0284c7',
      svg: '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>'
    },
    'emi-calculator': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>'
    },
    'percentage-calculator': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>'
    },
    'age-calculator': {
      bg: '#fffbeb', color: '#d97706',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><circle cx="12" cy="16" r="3"/><polyline points="12 15 12 16 13 16"/></svg>'
    },
    'cgpa-calculator': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
    },
    'attendance-calculator': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><polyline points="9 14 11 16 15 11"/></svg>'
    },
    'word-counter': {
      bg: '#fdf4ff', color: '#9333ea',
      svg: '<svg viewBox="0 0 24 24"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="14" y2="12"/><line x1="4" y1="18" x2="18" y2="18"/><polyline points="17 11 19 13 22 10"/></svg>'
    },
    'qr-generator': {
      bg: '#ecfeff', color: '#0891b2',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="3" height="3"/><rect x="18" y="14" width="3" height="3"/><rect x="14" y="18" width="3" height="3"/><rect x="18" y="18" width="3" height="3"/></svg>'
    },
    'password-generator': {
      bg: '#faf5ff', color: '#7c3aed',
      svg: '<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><circle cx="12" cy="16" r="1"/></svg>'
    },
    'create-invoice': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'
    },
    'create-invoice-visually': {
      bg: '#fdf4ff', color: '#a855f7',
      svg: '<svg viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>'
    },
    'create-electronic-invoice': {
      bg: '#ecfdf5', color: '#059669',
      svg: '<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
    },
    'pdf-invoice-to-e-invoice': {
      bg: '#fffbeb', color: '#d97706',
      svg: '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'
    },
    'xml-e-invoice-to-pdf': {
      bg: '#eef2ff', color: '#4f46e5',
      svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><line x1="9" y1="15" x2="15" y2="15"/></svg>'
    },
    'validate-e-invoice': {
      bg: '#f0fdf4', color: '#16a34a',
      svg: '<svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>'
    },
    'image-hd-converter': {
      bg: '#eff6ff', color: '#2563eb',
      svg: '<svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
    }
  };

  function getToolSvgIcon(toolId, category) {
    if (SVG_ICONS[toolId]) {
      const item = SVG_ICONS[toolId];
      return `<div class="tool-icon-tile" style="background:${item.bg};color:${item.color};">${item.svg}</div>`;
    }
    
    // Category Fallbacks with crisp vector SVGs
    const catFallbacks = {
      pdf: { bg: '#ffefe8', color: '#ea580c', svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>' },
      invoices: { bg: '#eff6ff', color: '#2563eb', svg: '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>' },
      image: { bg: '#f5f3ff', color: '#6366f1', svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>' },
      images: { bg: '#f5f3ff', color: '#6366f1', svg: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>' },
      developer: { bg: '#eff6ff', color: '#2563eb', svg: '<svg viewBox="0 0 24 24"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>' },
      calculators: { bg: '#ecfdf5', color: '#059669', svg: '<svg viewBox="0 0 24 24"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>' },
      text: { bg: '#fdf4ff', color: '#9333ea', svg: '<svg viewBox="0 0 24 24"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="14" y2="12"/><line x1="4" y1="18" x2="18" y2="18"/></svg>' },
      utilities: { bg: '#ecfeff', color: '#0891b2', svg: '<svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>' }
    };
    
    const c = (category || 'pdf').toLowerCase();
    const fallback = catFallbacks[c] || catFallbacks.pdf;
    return `<div class="tool-icon-tile" style="background:${fallback.bg};color:${fallback.color};">${fallback.svg}</div>`;
  }

  // Global object export (Vytra primary + backward compatible alias)
  window.VYTRA_TOOLS = TOOLS_DATA;
  window.DIGITALSAATHI_TOOLS = TOOLS_DATA;
  window.resolveToolUrl = resolveToolUrl;
  window.getToolSvgIcon = getToolSvgIcon;

})();
