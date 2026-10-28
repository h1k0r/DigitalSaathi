# -*- coding: utf-8 -*-
"""Round-4: reviewer's item 2 (unique content on main tool pages) + fixes.

1. Replace literal \\uXXXX escapes in HTML with real characters (the visible
   "\u2014" glitch on About/Privacy/Translate).
2. Align Code Editor og/twitter titles + hidden h1 with <title>.
3. Soften pdf-a "100% compliance" wording.
4. Inject a unique ~330-word editorial section (when to use / common errors /
   example) before the FAQ section of the 10 main PDF tool pages.
5. Insert a "How the Vytra Code Editor works" guide below the editor app.

Run from repo root: python scripts/add_tool_guides.py
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SEC_OPEN = (
    '<section class="vytra-editorial" style="max-width:860px;margin:2.5rem auto;'
    'padding:0 1rem;">\n'
)
H2 = ('  <h2 style="font-size:1.3rem;font-weight:800;color:var(--text-main,#0f172a);'
      'margin:0 0 0.7rem;">{}</h2>\n')
P = ('  <p style="font-size:0.95rem;line-height:1.75;'
     'color:var(--text-muted,#475569);margin:0 0 1.15rem;">{}</p>\n')
UL_OPEN = '  <ul style="margin:0 0 1.15rem;padding-left:1.3rem;">\n'
LI = ('    <li style="font-size:0.95rem;line-height:1.7;'
      'color:var(--text-muted,#475569);margin-bottom:0.5rem;">{}</li>\n')
UL_CLOSE = '  </ul>\n'
SEC_CLOSE = '</section>\n\n'


def section(parts):
    return SEC_OPEN + "".join(parts) + SEC_CLOSE


def qa(h2t, paras, bullets=None, h2e="A quick example", pe=None):
    parts = [H2.format(h2t)]
    for p in paras:
        parts.append(P.format(p))
    if bullets:
        parts.append(H2.format("Common problems and how to fix them"))
        parts.append(UL_OPEN)
        for b in bullets:
            parts.append(LI.format(b))
        parts.append(UL_CLOSE)
    if pe:
        parts.append(H2.format(h2e))
        parts.append(P.format(pe))
    return section(parts)


GUIDES = {
    "pdf/merge.html": qa(
        "When to combine PDFs with Vytra Merge",
        ["Merging is the fastest way to satisfy an upload field that accepts a "
         "single PDF. Indian application portals &mdash; SSC, IBPS, UPSC, state PSCs "
         "and most university admissions &mdash; usually ask for one combined file: "
         "photograph, signature, handwritten declaration, education certificate, "
         "caste or income certificate and the identity proof, in that order. Students "
         "also use Merge to join scanned textbook chapters, recombine circulars that "
         "arrived as separate files, or assemble signed contract pages. Because "
         "merging happens in your browser, the order you set in the thumbnail list is "
         "exactly the order in the output file."],
        ["Wrong order in the output &mdash; fix the thumbnail order before pressing "
         "Merge; the first card becomes page one.",
         "One file is password-protected &mdash; remove its password with Unlock "
         "first (you need to know it), then merge.",
         "The combined file is too big for the portal &mdash; run Compress on the "
         "merged PDF and target the portal's KB limit.",
         "A file will not add &mdash; check that it is really a PDF; convert photos "
         "or phone scans to PDF with JPG to PDF first."],
        pe="An OSSC notification asks for a single PDF under 200 KB containing the "
           "photograph, signature and declaration. Put the three scans in that order, "
           "merge, then compress with the Extreme preset until your file manager shows "
           "under 200 KB. Upload once &mdash; done."),
    "pdf/split.html": qa(
        "When to split a PDF with Vytra Split",
        ["Split extracts the pages you need into a new, smaller PDF. Typical uses: "
         "pulling the admit-card page out of a large file, extracting one unit from a "
         "study PDF so it fits an email attachment limit, separating a combined "
         "circular into per-department copies, or cutting a 200-page handbook down to "
         "the five pages that mention your exam centre. The range box accepts patterns "
         "like 1-3,7,10-12, so you can grab scattered pages in one pass instead of "
         "cutting repeatedly."],
        ["'Invalid range' &mdash; use digits, hyphens and commas only, for example "
         "1-3,7. There is no '1 to 3' form.",
         "Pages are off by one &mdash; the numbering in the thumbnail view is what "
         "the tool uses, and it starts at the first page of the file.",
         "The PDF asks for a password &mdash; Unlock it first; Split cannot read "
         "encrypted files.",
         "You need every page as a separate file &mdash; extract one range at a time, "
         "or use PDF to JPG if you want images instead."],
        pe="A 36-page previous-year paper: you want only questions 1-8 (pages 1-4) and "
           "the answer key (page 34). Enter 1-4,34 and you get one 5-page PDF that is "
           "quick to print and easy to revise from."),
    "pdf/compress.html": qa(
        "When to compress a PDF with Vytra Compress",
        ["Almost every government and banking portal caps uploads &mdash; 100 KB, "
         "200 KB, 1 MB. Vytra Compress reduces a PDF inside your browser with three "
         "presets: Light for files that are close to the limit, Balanced for ordinary "
         "documents, and Extreme for scanned files that are far over. The grayscale "
         "toggle helps most with scanned marksheets and handwritten papers, where "
         "colour adds size but no information. The live size readout updates as you "
         "change presets, so you can stop as soon as the file drops under the portal's "
         "cap."],
        ["Barely any reduction &mdash; the file is probably text-based and already "
         "near its minimum; try Extreme, then grayscale.",
         "A scanned document stays large &mdash; scans are images; grayscale plus "
         "Extreme usually cuts them by 60-80%.",
         "Output looks blurry &mdash; use Light instead of Extreme when the document "
         "must stay clearly readable.",
         "Still over the limit &mdash; extract only the required pages with Split "
         "first, then compress."],
        pe="A 2.1 MB scanned marksheet must go under 200 KB. Choose Extreme, tick "
           "grayscale, wait for the readout to settle under 200 KB, save, and confirm "
           "the size in your file manager before uploading."),
    "pdf/jpg-to-pdf.html": qa(
        "When to convert photos to PDF with Vytra JPG to PDF",
        ["Exam forms rarely accept loose photographs &mdash; they want a single PDF "
         "containing the photo, the signature and often a handwritten declaration. "
         "Vytra JPG to PDF stacks JPG or PNG images into one PDF in the order you "
         "arrange them, on A4 pages or on pages sized to your images. Phone camera "
         "scans of marksheets, certificates and ID cards convert the same way. "
         "Everything runs in your browser, and you can reorder the cards before "
         "generating the file."],
        ["Pages appear in the wrong order &mdash; drag the thumbnail cards into order "
         "before pressing Convert.",
         "The photo looks too small on the page &mdash; choose the option that fits "
         "one image per A4 page for full-size scans.",
         "The PDF exceeds the portal limit &mdash; compress it afterwards, or start "
         "with lower-resolution photos.",
         "A converted screenshot looks soft &mdash; avoid enlarging small images; "
         "capture at a larger size instead."],
        pe="An IBPS form asks for the photograph and signature in one upload. Add the "
           "photo first, the signature second, generate the PDF, and check page one "
           "shows both clearly before submitting."),
    "pdf/pdf-to-jpg.html": qa(
        "When to convert a PDF page to an image with Vytra PDF to JPG",
        ["Some places refuse PDFs but accept images: WhatsApp and Telegram groups, "
         "email bodies, notice boards and a few application fields that only take JPG. "
         "Vytra PDF to JPG renders each page as an image at a quality level you "
         "choose, one page or a whole set. It is also handy for grabbing a single "
         "diagram, map or timetable page to paste into notes. Rendering happens in "
         "your browser, so a 100-page PDF converts without an upload wait."],
        ["Text looks soft in the image &mdash; raise the quality setting; higher "
         "quality means a bigger file.",
         "The image is too large to share &mdash; pick a lower quality, or convert "
         "only the page you need.",
         "Only one page is needed &mdash; convert just that page to save time and "
         "space.",
         "A page renders blank &mdash; it may be an image-only scan; run OCR if you "
         "need the text rather than a picture."],
        pe="You must send the admit-card page but the receiver wants an image. "
           "Convert page 1 at high quality and attach the JPG &mdash; the hall-ticket "
           "details stay readable."),
    "pdf/word-to-pdf.html": qa(
        "When to convert a document to PDF with Vytra Word to PDF",
        ["Assignments, project reports and application drafts are safer as PDFs: "
         "tables, headings and page breaks stay exactly where you put them, and the "
         "receiver cannot accidentally edit the text. Vytra Word to PDF converts .docx "
         "and .doc files inside your browser and keeps tables, headings, lists and "
         "basic styling. Converting before submitting also avoids the common problem of "
         "a document that looked correct on your machine rendering differently on the "
         "reviewer's older Word version."],
        ["An old .doc file will not convert &mdash; open it in any word processor and "
         "Save As .docx, then convert.",
         "Fonts shift slightly &mdash; common fonts are kept; very unusual custom "
         "fonts may fall back to a similar one.",
         "A very large document takes time &mdash; conversion runs on your device; "
         "wait for the progress bar rather than reloading.",
         "Images are missing in the output &mdash; check they are embedded in the "
         "document, not linked from a website."],
        pe="A project report with three tables and headings must be submitted as one "
           "PDF under 1 MB. Convert the .docx, check the tables on page two, and if "
           "the file is heavy, compress it once before uploading."),
    "pdf/ocr.html": qa(
        "When to run OCR on a PDF with Vytra OCR",
        ["Old scans, downloaded circulars and photographed pages are images of text: "
         "you can read them, but you cannot search, copy or quote from them. OCR "
         "(optical character recognition) reads the image and produces selectable "
         "text. Students use it to make a previous-year paper searchable, pull "
         "quotation lines out of a notification, or turn study material into notes "
         "they can edit. Recognition runs in your browser, so the scanned document "
         "stays on your device."],
        ["Blurred or tilted scans give the worst results &mdash; re-scan or "
         "re-photograph straight-on in good light; 300 DPI or better helps.",
         "Handwriting is recognised poorly &mdash; OCR works best on printed text.",
         "Special symbols and regional scripts may misread &mdash; check the output "
         "against the original before quoting.",
         "Small font sizes drop letters &mdash; crop to the text region and run "
         "recognition again."],
        pe="You need every mention of 'interview' from a scanned 60-page circular. Run "
           "OCR, wait for the text layer, and search the result &mdash; what took an "
           "hour of scrolling becomes a keyword search."),
    "pdf/translate.html": qa(
        "When to translate a PDF with Vytra Translate",
        ["Notifications, admission notices and study material often arrive in one "
         "language while you read comfortably in another. Vytra Translate extracts the "
         "text from each page and returns a translated version while keeping the page "
         "layout in place. One disclosure, stated plainly: the sentence text is sent to "
         "Google's translation service to be translated. The file itself never leaves "
         "your device, and pages without text (pure scans) need OCR first."],
        ["A scanned page comes back untranslated &mdash; it has no text layer; run OCR "
         "first, then translate.",
         "Technical terms read oddly &mdash; proper nouns, exam names and legal words "
         "often stay in the original; compare with the original page.",
         "Column order confuses the text &mdash; magazine-style layouts can "
         "interleave; check dates and numbers against the original.",
         "You need the exact wording for an application &mdash; use the original "
         "document; the translation is for understanding, not for submission."],
        pe="A Hindi admission notice lists dates in a table. Translate it, read the "
           "English beside the original layout, and confirm the closing date on the "
           "original page before you rely on it."),
    "pdf/protect.html": qa(
        "When to password-protect a PDF with Vytra Protect",
        ["You frequently need to email documents that should not be readable by anyone "
         "who intercepts or forwards the message &mdash; Aadhaar and PAN copies, bank "
         "statements, salary slips, marksheets and signed declarations. Vytra Protect "
         "adds an open password to the PDF using standard encryption, entirely in your "
         "browser: the file and the password never reach a server. Anyone opening the "
         "file must type the password you chose."],
        ["Choose a strong password &mdash; mix letters, numbers and a symbol, and do "
         "not reuse your portal or email password.",
         "Share the password separately &mdash; send it by message or call, not in "
         "the same email as the file.",
         "You cannot recover a forgotten password &mdash; Vytra does not store it; "
         "keep the record in a password manager.",
         "Some portals reject encrypted uploads &mdash; if the form refuses the file, "
         "submit the unprotected version to that portal instead."],
        pe="A landlord asks for your PAN and address proof. Protect the combined PDF "
           "with a password, send the password separately, and the documents stay "
           "private even if the email is forwarded."),
    "pdf/unlock.html": qa(
        "When to unlock a PDF with Vytra Unlock",
        ["PDFs you own sometimes carry restrictions: printing disabled, copying "
         "blocked, or an open password you set long ago. Vytra Unlock removes these "
         "restrictions when you know the password, in your browser. Typical situations: "
         "a freely-downloaded study PDF that refuses to print, a colleague-protected "
         "document you need to quote from, or your own file whose restriction password "
         "you no longer remember. One honest limit: the tool removes restrictions &mdash; "
         "it does not crack passwords. If a document asks for a password you genuinely "
         "do not know, there is no legitimate shortcut."],
        ["The file asks for a password before opening &mdash; you need the open "
         "password; enter it in the unlock box.",
         "'Incorrect password' though you are sure &mdash; check Caps Lock; passwords "
         "are case-sensitive.",
         "Print is still greyed out &mdash; open the new file the tool produced, not "
         "the original.",
         "A publisher watermark stays visible &mdash; unlocking does not remove "
         "watermarks or copyright marks."],
        pe="A downloaded practice PDF blocks printing. Unlock it with the password "
           "from the website you got it from, open the new file, and print the "
           "chapters you are revising."),
}

DEVELOPER_GUIDE = SEC_OPEN + (
    H2.format("How the Vytra Code Editor works") +
    P.format(
        "The editor gives you six languages in one screen: JavaScript, Python, C, "
        "C++, Java and PHP. JavaScript runs entirely inside your browser in an "
        "isolated frame &mdash; nothing is sent anywhere. The other languages "
        "(C, C++, Java, PHP, Python) are compiled and executed by Wandbox, a free "
        "public compiler service: when you press Run, the code you wrote is sent to "
        "wandbox.org, executed there, and the output comes back to the console pane. "
        "That is the same model most online IDEs use, and it is stated openly here so "
        "you know exactly what happens to your code. Do not paste passwords, keys or "
        "private data into code you run through those languages.") +
    H2.format("Common editor problems") + UL_OPEN +
    LI.format("Nothing appears in the console for C, C++, Java, PHP or Python &mdash; "
              "those languages need an internet connection because they run on "
              "Wandbox; check your network first.") +
    LI.format("The console shows a compilation error &mdash; read the first error "
              "line; it names the file and the line that failed.") +
    LI.format("Your program asks for input but seems stuck &mdash; type the input in "
              "the stdin box under the console and press Send.") +
    LI.format("JavaScript works but C does not &mdash; expected: JavaScript runs "
              "locally, the compiled languages need the compiler service.") +
    LI.format("You want to keep your code &mdash; use Save in the File menu; several "
              "files can live in one downloaded archive.") +
    UL_CLOSE +
    H2.format("A quick example") +
    P.format("Select Python, replace the template with a loop that prints the squares "
             "of 1 to 10, and press Run: the console prints ten lines in about a "
             "second. Switch the language to C and run again &mdash; the same window "
             "compiles and runs it through the service, and any compiler error "
             "appears in the same console.") +
    SEC_CLOSE
)


def main():
    changed = {}

    # 1. literal \uXXXX -> real chars, site-wide (safe in HTML, JS and JSON-LD)
    esc = re.compile(r"\\u([0-9a-fA-F]{4})")
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "seo", "templates",
                                                "__pycache__")]
        for fn in files:
            if not fn.endswith(".html"):
                continue
            path = os.path.join(dirpath, fn)
            s = io.open(path, encoding="utf-8").read()
            s2, n = esc.subn(lambda m: chr(int(m.group(1), 16)), s)
            if n:
                io.open(path, "w", encoding="utf-8", newline="\n").write(s2)
                rel = os.path.relpath(path, ROOT).replace("\\", "/")
                changed[rel] = changed.get(rel, 0) + n

    # 2. Code Editor title alignment
    d = os.path.join(ROOT, "developer", "index.html")
    s = io.open(d, encoding="utf-8").read()
    pairs = [
        ('og:title" content="Online Code Editor & Compiler — C, C++, Java, PHP, '
         'Python, JS | Vytra"',
         'og:title" content="Online Code Editor – Python, JavaScript, Java, '
         'C++ | Vytra"'),
        ('twitter:title" content="Online Code Editor & Compiler — C, C++, Java, '
         'PHP, Python, JS | Vytra"',
         'twitter:title" content="Online Code Editor – Python, JavaScript, Java, '
         'C++ | Vytra"'),
        ('Online Code Editor &amp; Compiler &mdash; C, C++, Java, PHP, Python, '
         'JavaScript | Vytra</h1>',
         'Online Code Editor &ndash; Python, JavaScript, Java, C++ | Vytra</h1>'),
    ]
    for old, new in pairs:
        if s.count(old) != 1:
            print(f"PROBLEM developer title: found {s.count(old)}: {old[:60]!r}")
            return 1
        s = s.replace(old, new)

    # 3. developer guide below the app (before the config script)
    anchor = "<script>\n/* VYTRA_IDE config"
    if s.count(anchor) != 1:
        print(f"PROBLEM developer guide anchor: found {s.count(anchor)}")
        return 1
    s = s.replace(anchor, DEVELOPER_GUIDE + anchor)
    io.open(d, "w", encoding="utf-8", newline="\n").write(s)
    changed["developer/index.html"] = changed.get("developer/index.html", 0) + 4

    # 4. pdf-a wording
    pa = os.path.join(ROOT, "pdf", "pdf-a.html")
    s = io.open(pa, encoding="utf-8").read()
    old = "ensuring 100% compliance with client confidentiality"
    if s.count(old) != 1:
        print(f"PROBLEM pdf-a: found {s.count(old)}")
        return 1
    io.open(pa, "w", encoding="utf-8", newline="\n").write(
        s.replace(old, "supporting client confidentiality"))
    changed["pdf/pdf-a.html"] = changed.get("pdf/pdf-a.html", 0) + 1

    # 5. tool guides before the first FAQ section
    faq = re.compile(r'<section class="vytra-(qa|faq)-section')
    for rel, html in GUIDES.items():
        path = os.path.join(ROOT, rel)
        s = io.open(path, encoding="utf-8").read()
        if "vytra-editorial" in s:
            print(f"skip (already has editorial): {rel}")
            continue
        m = faq.search(s)
        if not m:
            print(f"PROBLEM no FAQ anchor: {rel}")
            return 1
        s = s[:m.start()] + html + s[m.start():]
        io.open(path, "w", encoding="utf-8", newline="\n").write(s)
        changed[rel] = changed.get(rel, 0) + 1

    print("=== changed ===")
    for k in sorted(changed):
        print(f"  {k}: {changed[k]}")
    words = sum(len(re.sub(r'<[^>]+>', ' ', h).split()) for h in GUIDES.values())
    print(f"injected word count (10 tool guides): ~{words}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
