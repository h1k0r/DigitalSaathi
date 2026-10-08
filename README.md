# Vytra — Free Online Tools for Everyday Digital Work

> **100% Free, Client-Side Online Tools Suite.** Convert, compress, edit, calculate, and manage files securely in your web browser with zero server uploads.

[![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages-blue?logo=github)](https://vytra.in/)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Client--Side-emerald)](#privacy--security)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

---

## 🚀 Overview

**Vytra** is an enterprise-grade, privacy-first online tools platform designed as a modern alternative to traditional tools suites (like iLovePDF and Smallpdf). Unlike traditional platforms that require uploading private documents to external cloud servers with daily file quotas, Vytra runs **100% in your browser** using **WebAssembly, HTML5 Canvas, and modern Web APIs**.

- **Zero Server Uploads**: Your files never leave your device.
- **Truly Unlimited**: No daily usage caps, no artificial queues, no paywalls.
- **Hardware Acceleration**: Processes files at native hardware speeds.
- **Mobile-First & Touch Ready**: Tested across mobile, tablet, and desktop devices.
- **GitHub Pages Ready**: 100% static client-side architecture with zero backend server dependencies.

---

## 🧰 Comprehensive Tool Directory (76+ Tools)

### 📑 1. PDF Tools (`/pdf/`)
- **Organize**: Merge PDF, Split PDF, Reorder Pages, Extract Pages, Organize PDF, Rotate PDF, Crop PDF, Page Numbers.
- **Optimize**: Compress PDF (under 100KB, 200KB, 500KB), Repair PDF, OCR PDF, PDF/A Archival Converter.
- **Convert to PDF**: JPG to PDF, Word to PDF, Excel to PDF, PowerPoint to PDF, HTML to PDF, Scan to PDF.
- **Convert from PDF**: PDF to JPG, PDF to Word, PDF to Excel, PDF to PowerPoint, PDF to Markdown.
- **Edit & Security**: Edit PDF (Annotate, Draw, Text), Sign PDF, Watermark PDF, Redact PDF, Fill PDF Forms, Protect PDF, Unlock PDF.
- **Analysis**: Compare PDF, PDF Information Inspector, PDF Page Counter & Print Cost Estimator, PDF Viewer.
- **AI & Intelligence**: AI PDF Summarizer, Translate PDF.

### 🖼️ 2. Image Tools (`/image/`)
- **Compress & Resize**: Image Compressor (target under 20KB, 50KB, 100KB), Image Resizer, Bulk Image Resizer, DPI Converter (300 DPI).
- **Crop & Edit**: Crop Photo, Rotate & Flip, Photo Enhancer & Filters, Watermark Maker, Blur & Redact Faces / Sensitive Data.
- **Convert Formats**: JPG to PNG, PNG to JPG, WebP Converter (Two-way), Base64 Image Encoder/Decoder.
- **Government Exam & Passport Tools**: Passport BG Color Replacer, Passport Photo Sheet Maker (A4 / 4x6" grid), Signature Resizer (under 20KB).

### 💻 3. Developer Tools (`/developer/`)
- **JSON Formatter & Validator**: Beautify, minify, validate syntax errors, and expandable tree view.
- **Base64 Converter**: Two-way encode/decode text and binary strings.
- **SQL Formatter**: Standardize, uppercase keywords, and format queries.

### 🧮 4. Financial & Educational Calculators (`/calculators/`)
- **Loan EMI Calculator**: Monthly EMI calculation, principal vs. interest breakdown, and amortization schedule.
- **Percentage Calculator**: 4-mode calculation (obtained marks, CGPA to %, % to CGPA, grading).
- **Age Calculator**: Precise calculation in years, months, days, hours, and next birthday countdown.
- **CGPA Calculator**: Multi-semester credit-weighted grade calculation.
- **Attendance Calculator**: 75% minimum eligibility planner with required classes calculation.

### ⚡ 5. Text & Utility Tools (`/text/` & `/utilities/`)
- **Word Counter**: Real-time word, character, sentence, paragraph count, and reading time estimation.
- **QR Code Generator**: Generate crisp downloadable QR codes for URLs, WiFi credentials, UPI payments, and plain text.
- **Password Generator**: Cryptographically secure client-side password creation with entropy strength analysis.

---

## 🔒 Privacy & Security

All document manipulations happen inside your browser sandbox:
1. When you drop a PDF or photo, the browser loads the binary data into local memory.
2. WebAssembly/JavaScript executes the requested operations (compression, conversion, merging).
3. The resulting file is generated as a local Blob and saved directly to your Downloads folder.
4. **No network requests containing your file bytes are ever made.**

---

## 📁 Repository Structure

```
Vytra/
│
├── index.html                   # High-converting tools directory homepage
├── about.html                   # About Vytra
├── contact.html                 # Contact & support page
├── privacy.html                 # Client-side privacy guarantee
├── terms.html                   # Terms of service
├── design-system.html           # Design tokens, UI components, typography
├── robots.txt                   # Search crawler directives
├── sitemap.xml                  # 76-URL XML sitemap with daily/weekly changefreq
│
├── assets/
│   ├── css/
│   │   └── style.css            # Complete design system, animations, responsive layout
│   └── js/
│       └── common.js            # Global command palette (Ctrl+K), tabs, dropzones, modals
│
├── data/
│   └── tools.js                 # Master tools registry powering dynamic directory & SVG icons
│
├── tools/
│   └── index.html               # Searchable, filterable 76+ tools directory
│
├── pdf/                         # 33+ Complete PDF tools
├── image/                       # 18+ Image and photo tools
├── calculators/                 # Financial and academic calculators
├── developer/                   # JSON, Base64, and SQL developer tools
├── text/                        # Word counter and text processing
├── utilities/                   # QR code and secure password generators
└── tests/                       # Automated QA, relative link audits, and health tests
```

---

## 🛠️ Local Development

To run Vytra locally:

```bash
# Clone the repository
git clone https://github.com/h1k0r/DigitalSaathi.git

# Navigate to project folder
cd Vytra

# Start any static HTTP server (e.g., Python 3)
python -m http.server 8080

# Open in your web browser:
# http://localhost:8080/
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
