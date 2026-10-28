# -*- coding: utf-8 -*-
"""Reviewer round 3 — site-wide honesty sweep.

Fixes every absolute claim that isn't strictly true (Translate/Code-Editor
exceptions), removes fake entity credits ("Vytra Web Core Team", "Engineering
Team"), fake stats ("50k+ daily operations", "ISO Compliant" certification
style claims), and adds the Wandbox disclosure to the Code Editor.

Run from repo root: python scripts/fix_round3_claims.py
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (file, old, new, min_count)
FIXES = [
    # ---- about.html: title/OG/Twitter/schema + descriptions -----------------
    ("about.html",
     "About Vytra \u2013 Free, Private &amp; 100% Client-Side Online Tools",
     "About Vytra \u2013 Free, Private, Browser-Based Online Tools", 3),
    ("about.html",
     '"name": "About Vytra \u2013 Free, Private & 100% Client-Side Online Tools"',
     '"name": "About Vytra \u2013 Free, Private, Browser-Based Online Tools"', 1),
    ("about.html",
     "providing 100% free, private, client-side tools for Indian students, exam applicants, and cyber cafes. All processing happens in your browser.",
     "providing free, private, browser-based tools for Indian students, exam applicants, and cyber cafes. Processing happens in your browser.", 3),
    ("about.html",
     "and our 100% browser-based privacy architecture.",
     "and our browser-based privacy architecture.", 1),

    # ---- homepage JSON-LD ---------------------------------------------------
    ("index.html",
     '"Vytra is a free, 100% private, client-side digital utility toolkit for',
     '"Vytra is a free, browser-based digital utility toolkit for', 1),
    ("index.html",
     '"Free, 100% private in-browser utility toolkit for PDF editing',
     '"Free, in-browser utility toolkit for PDF editing', 1),

    # ---- privacy.html: meta x3, core guarantee, exceptions ------------------
    ("privacy.html",
     "Vytra Privacy Policy. Learn how your files are processed 100% locally in your web browser with zero server uploads, and how advertising cookies are managed.",
     "Vytra Privacy Policy. How your files are processed in your browser, the disclosed translation and code-compilation exceptions, and how advertising cookies work.", 3),
    ("privacy.html",
     "Core Guarantee: 100% In-Browser File Processing",
     "Core Principle: In-Browser File Processing", 1),
    ("privacy.html",
     "processed exclusively on your device.",
     "processed exclusively on your device, with two disclosed exceptions: the "
     "Translate PDF tool sends extracted sentence text to Google's translation "
     "service, and the Code Editor sends compiled-language code (C, C++, Java, "
     "PHP, Python) to Wandbox's compiler. In both cases the source file itself "
     "stays on your device.", 1),
    ("privacy.html",
     "We do not upload, transmit, store, or view your files on any remote server.",
     "Other than those two disclosures, we do not upload, transmit, store, or view your files on any remote server.", 1),
    ("privacy.html",
     "The document file itself stays on your device.",
     "The document file itself stays on your device. The Code Editor works the "
     "same way: JavaScript runs locally in an iframe, while source code written "
     "for C, C++, Java, PHP or Python is sent to Wandbox's public compiler "
     "(wandbox.org) to compile and run.", 1),

    # ---- 404 ----------------------------------------------------------------
    ("404.html",
     "All 33 Vytra PDF tools remain 100% free, browser-based, and private.",
     "All 33 Vytra PDF tools remain free and browser-based.", 1),

    # ---- design-system ------------------------------------------------------
    ("design-system.html",
     "Processed 100% locally in your browser",
     "Processed locally in your browser", 1),

    # ---- PDF hub ------------------------------------------------------------
    ("pdf/index.html",
     '"text": "No. Unlike traditional PDF websites, Vytra processes all documents 100% locally in your web browser using WebAssembly and PDF-lib. Your private documents never leave your computer."',
     '"text": "No. Unlike PDF websites that upload files to a server, Vytra '
     'processes documents in your web browser using WebAssembly and PDF-lib. '
     'Your documents stay on your computer \\u2014 the one exception is Translate '
     'PDF, which parses the file locally but sends sentence text to Google\'s '
     'translation service, as its page discloses."', 1),
    ("pdf/index.html",
     "100% private client-side processing with zero server uploads, no file size caps, and instant speed.",
     "Private, in-browser processing with zero file uploads, no file size caps, and instant speed.", 1),
    ("pdf/index.html",
     "Your sensitive marks sheets, financial statements, and job application forms are processed directly in your device RAM without uploading to external servers.",
     "Your sensitive marks sheets, financial statements, and job application forms are processed directly in your device RAM. One disclosed exception: Translate PDF parses the file in your browser but sends sentence text to Google for translation.", 1),
    ("pdf/index.html",
     "100% Free &bull; Zero Server Uploads &bull; ISO Compliant",
     "Free &bull; No File Uploads &bull; Standards-Based PDF Output", 1),
    ("pdf/index.html",
     "Engineered with precision by the Vytra Web Core Team. Certified 100% Client-Side WebAssembly Architecture.",
     "Built on WebAssembly and PDF-lib \u2014 every tool runs in your browser, with no app to install.", 1),
    ("pdf/index.html",
     "Check out this free 100%25 private PDF tools suite",
     "Check out free PDF tools that run in your browser", 1),
    ("pdf/index.html",
     "All PDF tools in one place with 100%25 in-browser privacy and zero server uploads",
     "All PDF tools in one place with in-browser privacy", 1),

    # ---- tools directory ----------------------------------------------------
    ("tools/index.html",
     "with 100% private in-browser processing.",
     "with private, in-browser processing.", 3),
    ("tools/index.html",
     "Fast, clean, 100% free client-side tools. Convert files, compress documents, calculate numbers, and format code with complete in-browser privacy.",
     "Fast, clean, free browser-based tools. Convert files, compress documents, calculate numbers, and format code \u2014 file processing happens in your browser.", 1),
    ("tools/index.html",
     "100% In-Browser Privacy Guarantee</h2>",
     "In-Browser Privacy by Default</h2>", 1),
    ("tools/index.html",
     "Unlike legacy converters that upload your confidential files to remote servers, Vytra runs directly inside your browser using HTML5 Canvas and WebAssembly. Your documents, photos, and personal data never leave your device.",
     "Unlike legacy converters that upload your confidential files to remote servers, Vytra processes documents directly inside your browser using HTML5 Canvas and WebAssembly. Your files are not uploaded to Vytra \u2014 two tools disclose their own exceptions on their pages: Translate PDF sends sentence text to Google for translation, and the Code Editor sends compiled code to Wandbox.", 1),

    # ---- html-to-pdf: Web Core Team + sample-doc fake stats -----------------
    ("pdf/html-to-pdf.html",
     "Engineered with precision by the Vytra Web Core Team. Compliant with ISO 32000 PDF standards and W3C HTML5 / CSS3 specifications.",
     "Built to the PDF specification (ISO 32000) and W3C HTML5 / CSS3 \u2014 conversion runs entirely in your browser.", 1),
    ("pdf/html-to-pdf.html",
     "Architected client-side PDF document manipulation tools handling 50k+ daily operations with zero server computing infrastructure.",
     "Built as client-side PDF document tools that run with no server computing infrastructure behind them.", 1),
    ("pdf/html-to-pdf.html",
     "Authored by: Web Core Engineering Team &bull; Published: Q4 2026",
     "Sample document &bull; Load and convert it to test the tool", 1),

    # ---- translate: Web Core Team -------------------------------------------
    ("pdf/translate.html",
     "Engineered with precision by the Vytra Web Core Team. Powered by Mozilla PDF.js text layer decoding and client-side vector pagination.",
     "Powered by Mozilla PDF.js text layer decoding \u2014 the file parses in your browser; sentence text goes to Google for translation.", 1),

    # ---- OCR false precision ------------------------------------------------
    ("pdf/ocr.html",
     "<td>100% exact text extraction</td>",
     "<td>Full text extraction</td>", 1),

    # ---- PDF/A overclaim ----------------------------------------------------
    ("pdf/pdf-a.html",
     "Guarantees 100% identical visual reproduction across all systems.",
     "Keeps the visual appearance stable across systems.", 1),

    # ---- Code Editor: honest meta + visible disclosure ----------------------
    ("developer/index.html",
     'meta name="description" content="Free online code editor and compiler for C, C++, Java, PHP, Python and JavaScript. Write, run and troubleshoot code in your browser. No signup."',
     'meta name="description" content="Free online code editor for C, C++, Java, PHP, Python and JavaScript. JavaScript runs in your browser; other languages compile via the free Wandbox service. No signup."', 1),
    ("developer/index.html",
     'meta property="og:description" content="Free online code editor and compiler for C, C++, Java, PHP, Python and JavaScript. No signup."',
     'meta property="og:description" content="Free online code editor: JavaScript runs locally in your browser; C, C++, Java, PHP and Python compile via Wandbox. No signup."', 1),
    ("developer/index.html",
     '<div class="vsc-shell" id="vscShell">',
     '<div class="exec-note" style="max-width:860px;margin:14px auto 0;padding:10px 16px;'
     'background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;font-size:.85rem;'
     'color:#475563;line-height:1.6;">'
     '<strong>How your code runs:</strong> JavaScript executes locally in your browser. '
     'C, C++, Java, PHP and Python are compiled and run by the free '
     '<a href="https://wandbox.org" target="_blank" rel="noopener">Wandbox</a> service '
     '\u2014 the code you write for those languages is sent there to execute.</div>\n'
     '        <div class="vsc-shell" id="vscShell">', 1),
]

# Fake-credit variants removed everywhere (except templates/)
CREDIT_RE = re.compile(
    r"(Created|Maintained) with care by the Vytra [A-Za-z ]*Engineering Team")


def main():
    changed = {}
    problems = []
    for rel, old, new, minc in FIXES:
        path = os.path.join(ROOT, rel)
        with io.open(path, encoding="utf-8") as f:
            s = f.read()
        n = s.count(old)
        if n < minc:
            problems.append(f"{rel}: expected>={minc}, found {n}: {old[:70]!r}")
            continue
        s = s.replace(old, new)
        changed[rel] = changed.get(rel, 0) + n
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)

    # sweep fake team credits site-wide
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "seo", "templates", "__pycache__")]
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(dirpath, fn)
            with io.open(path, encoding="utf-8") as f:
                s = f.read()
            s2, n = CREDIT_RE.subn(r"\1 with care on Vytra", s)
            if n:
                rel = os.path.relpath(path, ROOT).replace("\\", "/")
                changed[rel] = changed.get(rel, 0) + n
                with io.open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(s2)

    print("=== replacements applied ===")
    for k in sorted(changed):
        print(f"  {k}: {changed[k]}")
    if problems:
        print("=== PROBLEMS (not applied) ===")
        for p in problems:
            print("  " + p)
        return 1
    print(f"files touched: {len(changed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
