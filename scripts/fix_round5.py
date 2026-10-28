# -*- coding: utf-8 -*-
"""Round-5: reviewer fixes.

1. About: name BOTH exceptions (Translate + Code Editor/Wandbox) so About,
   Privacy and the Code Editor page match.
2. Translate: remove the layout-preservation claim from my new guide (the FAQ
   says output is a clean paginated A4 rebuild — align), qualify 'unlimited'
   with the Google rate-limit reality.
3. Rewrite the pdf24-template 'Information' blocks (How to X / Easy to use /
   Supports your system / No installation required / Secure X) on 11 tool
   pages in our own words — removes the biggest copied-content risk.
4. Remove 'File protection is active' badge (meaningless, static, no JS).
5. Remove leftover 'Advertisement' label divs (CSS hides them, but remove the
   elements outright until ads are live).
6. Fix broken share text 'for free with free at Vytra' (4 pages).
7. SSC page: 'Wajah' -> 'Why'; drop the unverifiable 'Last verified 2026-10-27'
   claim (we did not check the official notice that day).
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []


def edit(rel, pairs):
    """Exact string replacements with count assertions."""
    path = os.path.join(ROOT, rel)
    s = io.open(path, encoding="utf-8").read()
    for old, new, cnt in pairs:
        n = s.count(old)
        if n != cnt:
            problems.append(f"{rel}: expected {cnt}, found {n}: {old[:70]!r}")
            continue
        s = s.replace(old, new)
    io.open(path, "w", encoding="utf-8", newline="\n").write(s)


# ---------------------------------------------------------------- 1. About
edit("about.html", [(
    "One honest exception: the Translate PDF tool parses your file locally but "
    "sends sentence text to Google's public translation service \u2014 its page "
    "states this plainly.",
    "Two honest exceptions, stated on their own pages: the Translate PDF tool "
    "parses your file locally but sends sentence text to Google's public "
    "translation service, and the Code Editor sends the code you write for C, "
    "C++, Java, PHP and Python to Wandbox's compiler (JavaScript itself runs "
    "locally). Everything else runs entirely in your browser.",
    1)])

# ------------------------------------------------------------- 2. Translate
edit("pdf/translate.html", [
    ("extracts the text from each page and returns a translated version while "
     "keeping the page layout in place.",
     "extracts the text from each page and compiles the translation into a "
     "clean, paginated A4 document for reading.", 1),
    ("The translated PDF keeps the original layout page by page, so figures, "
     "tables and dates stay exactly where they appear in the original \u2014 "
     "the main advantage over pasting paragraphs into a translator. Page "
     "numbers still match, which matters when you must refer back to a page in "
     "an application.",
     "The output is meant for reading, not for resubmission: translated text is "
     "re-flowed onto clean A4 pages rather than reproduced in the original's "
     "exact layout, so compare dates, amounts and tables against the original "
     "PDF whenever you act on them.", 1),
    ("Translate it, read the English beside the original layout, and confirm "
     "the closing date on the original page before you rely on it.",
     "Translate it, keep the original PDF open beside the translated one, and "
     "confirm the closing date on the original before you rely on it.", 1),
    ("<h3 class=\"vytra-info-cell-title\">Instant unlimited conversions</h3>\n"
     "          <p class=\"vytra-info-cell-desc\">No subscription fees, no "
     "artificial page caps, and no queue waiting times. Translate as many "
     "documents as you need completely free of charge.</p>",
     "<h3 class=\"vytra-info-cell-title\">No fixed cap from Vytra</h3>\n"
     "          <p class=\"vytra-info-cell-desc\">There is no Vytra-side page "
     "limit, subscription or queue. One honest note: translation runs through "
     "Google's endpoint, so very large batches can slow when that service "
     "rate-limits \u2014 translate very long documents in parts.</p>", 1),
])

# ------------------------------------------------- 6. Broken share texts
edit("pdf/edit.html", [
    ("Edit%20PDFs%20online%20for%20free%20with%20free%20at%20Vytra",
     "Edit%20a%20PDF%20in%20your%20browser%20-%20Vytra", 1)])
edit("pdf/jpg-to-pdf.html", [
    ("Convert%20JPG%20to%20PDF%20for%20free%20with%20free%20at%20Vytra",
     "Convert%20JPG%20to%20PDF%20in%20your%20browser%20-%20Vytra", 1)])
edit("pdf/merge.html", [
    ("Merge%20PDFs%20for%20free%20with%20free%20at%20Vytra",
     "Merge%20PDFs%20in%20your%20browser%20-%20Vytra", 1)])
edit("pdf/split.html", [
    ("Split%20PDF%20pages%20for%20free%20with%20free%20at%20Vytra",
     "Split%20a%20PDF%20in%20your%20browser%20-%20Vytra", 1)])

# ------------------------------------------------------------------ 7. SSC
ssc = open(os.path.join(ROOT, "ssc-photo-resize-20kb-50kb", "index.html"),
           encoding="utf-8").read()
edit("ssc-photo-resize-20kb-50kb/index.html", [
    ("<strong>Wajah:</strong>", "<strong>Why:</strong>", 3),
    ("<tr><td>Last verified</td><td colspan=\"2\"><strong>2026-10-27</strong> "
     "\u2014 limits change between notifications;",
     "<tr><td>Compiled</td><td colspan=\"2\">from recent SSC notifications "
     "\u2014 limits change between notifications;", 1),
])

# ------------------------------------- 3. Rewrite template info blocks
# per page: list of (old_title, new_title, new_desc)
CELLS = {
    "pdf/merge.html": [
        ("How to merge PDF files", "Combine documents in one pass",
         "Add every file you need, drag the page cards into the order the form "
         "asks for, and create a single PDF. The thumbnail strip shows exactly "
         "what the output will contain."),
        ("No quality loss", "Pages are copied, not re-taken",
         "Merging copies the original page objects into the new file. Vector "
         "text stays selectable, and a page that printed well before prints the "
         "same way after."),
        ("Easy to use", "Built for application forms",
         "The usual case is an exam or job form asking for photograph, "
         "signature and certificates as one upload. Arrange the cards to match "
         "the notification's order and merge once."),
        ("Supports your system", "Runs in the browser you already have",
         "No plug-ins, no downloads, no separate app. Open the page on a phone "
         "or laptop with a current browser and the tool is ready."),
        ("No installation required", "Nothing leaves the device",
         "Files are read and joined inside the browser tab. No upload, no "
         "server copy, no waiting queue \u2014 closing the tab discards "
         "everything."),
        ("Secure merging of PDFs", "Large files are fine",
         "Merging depends on your device's memory, not on an upload limit. "
         "Multi-hundred-page scans combine in seconds on a normal laptop."),
    ],
    "pdf/split.html": [
        ("How to split PDF files", "Extract only the pages you need",
         "Type a range such as 1-4,34 or pick pages from the thumbnail grid. "
         "The tool builds a new PDF containing just those pages, in the order "
         "you chose."),
        ("Visual page selection", "Ranges and clicks together",
         "Mix typed ranges with clicked thumbnails: select pages one by one, "
         "add a range, and the selection updates before you generate "
         "anything."),
        ("Easy to use", "Made for big study PDFs",
         "Coaching notes and previous-year papers often run to hundreds of "
         "pages. Split out one unit or one paper and keep just that file on "
         "your phone."),
        ("Supports your system", "Nothing to install",
         "The split runs in the current browser tab on Windows, macOS, Linux, "
         "Android or iPhone \u2014 no app-store visit, no plug-in."),
        ("No quality loss", "The output keeps original quality",
         "Selected pages are copied as-is: fonts, vector lines and embedded "
         "images keep their original resolution, and the page size does not "
         "change."),
        ("Secure PDF splitting", "Files stay on your device",
         "The PDF is opened and written inside the browser. No copy of the file "
         "is uploaded, so confidential documents remain with you."),
    ],
    "pdf/compress.html": [
        ("How to compress PDF files", "Shrink a PDF to a portal limit",
         "The file opens in the tab \u2014 choose Light, Balanced or Extreme "
         "and watch the size readout drop until it fits the KB cap your form "
         "demands."),
        ("Adjustable PDF compression", "Presets you can feel",
         "Light trims a little, Balanced handles ordinary documents, Extreme is "
         "for heavy scans. The grayscale switch removes colour data that "
         "scanned forms never need."),
        ("Easy to use", "Built around the 100 KB / 200 KB rule",
         "Indian portals love round numbers like 100 KB or 200 KB. Set the "
         "target from the form's instruction page, compress, and confirm the "
         "size before uploading."),
        ("Supports your system", "Works on old machines too",
         "Compression runs on the device, so even a low-RAM phone can handle a "
         "normal application PDF. A laptop simply finishes faster on very large "
         "files."),
        ("No installation required", "One tab, no setup",
         "Open the page, press the button. Nothing to install also means no "
         "admin rights are needed on a cyber-café computer."),
        ("Secure PDF compression", "Quality stays readable",
         "Text pages keep crisp text; scanned pages keep enough detail for "
         "photographs of marksheets. If Extreme looks too soft, step back to "
         "Balanced \u2014 the original file is never overwritten."),
    ],
    "pdf/edit.html": [
        ("How to edit PDF files", "Add text, signatures and shapes on top",
         "Open a PDF and place typed text, a drawn signature, rectangles, "
         "highlights or images onto any page, then save the annotated copy."),
        ("Insert text &amp; whiteout", "Fix small mistakes without re-printing",
         "Whiteout covers an old date or a wrong roll number; a fresh text box "
         "writes the correction. Useful when re-scanning the paper is not "
         "possible."),
        ("Easy to use", "Works where the form was filled",
         "Many applicants fill a printed form, scan it, then notice a typo. "
         "Editing the scanned PDF saves a fresh trip to the printer or the "
         "cyber café."),
        ("Supports your system", "Mouse or touch",
         "The same controls work with a finger on a phone and a mouse on a "
         "desktop, so a signature can be drawn on either."),
        ("No installation required", "Edits stay on the device",
         "The document is opened and saved inside the browser tab; the edited "
         "copy is downloaded directly to your device."),
        ("Secure PDF editing", "Original stays untouched",
         "Saving produces a new file. The edited version and the source PDF "
         "exist side by side, so nothing is lost if an edit goes wrong."),
    ],
    "pdf/jpg-to-pdf.html": [
        ("How to convert JPG to PDF", "Photographs in, single PDF out",
         "Add the JPG or PNG files, arrange the cards, pick A4, Letter or "
         "fit-to-image, and generate one PDF ready for an upload field."),
        ("A4, Letter &amp; Fit options", "Page size matches the notification",
         "A4 suits declaration pages, fit-to-image keeps a full-page scan "
         "uncropped. Check the instruction page once and choose "
         "accordingly."),
        ("Easy to use", "Made for photo-plus-signature forms",
         "Most forms want the photograph first and the signature second on one "
         "page. Order the cards that way and the portal accepts the file in "
         "one upload."),
        ("Supports your system", "Phone camera works",
         "Pictures taken on a phone are accepted directly \u2014 no transfer "
         "to a computer, no resizing in an editor first."),
        ("No watermarks or limits", "No watermark, no page cap",
         "The generated PDF carries only your images. There is no Vytra stamp, "
         "no page limit and no account to create."),
        ("Secure PDF compilation", "Images never leave the browser",
         "Conversion happens in the tab: the photos are read from your device "
         "and the PDF is written back to it, without any upload."),
    ],
    "pdf/sign.html": [
        ("How to sign PDF files", "Put your signature on a PDF",
         "Draw with a finger or mouse, type the name in a script style, or "
         "upload a photo of a written signature and place it on the page."),
        ("Draw, type, or upload", "Three ways to sign",
         "Drawing suits touch screens, typing suits quick declarations, and an "
         "uploaded signature photo matches the one already on your "
         "documents."),
        ("Easy to use", "Sign declarations without re-printing",
         "The handwritten declaration most forms ask for can be signed once, "
         "photographed, and reused as an image layer on future PDFs."),
        ("Supports your system", "Phone-friendly placement",
         "Dragging a signature into place works with a finger; zoom keeps "
         "small signature boxes accurate on a phone screen."),
        ("Legally recognized", "Know when a signature image is enough",
         "A placed signature works for declarations and application forms. "
         "Certificates and contracts that demand a certified digital signature "
         "still need the original process \u2014 this tool does not replace "
         "that."),
        ("Secure in-browser signing", "Signing stays private",
         "The document and the signature are handled inside the browser tab; "
         "neither is uploaded to Vytra."),
    ],
    "pdf/unlock.html": [
        ("How to unlock a PDF", "Remove a password you know",
         "Enter the password the file opens with, and the tool writes a copy "
         "without the restriction, ready to print or quote from."),
        ("Remove all restrictions", "Printing and copying bans lifted",
         "Documents that open but refuse to print or extract text lose those "
         "limits after unlocking; the content itself is unchanged."),
        ("Total data privacy", "The password is not stored",
         "It is used in the browser tab to open the file and then discarded. "
         "Vytra has no server that could keep it \u2014 or the document."),
        ("Perfect for government portals", "Portals reject locked files",
         "Many upload fields refuse password-protected PDFs. Unlock the copy "
         "you intend to submit, and keep the protected original for your own "
         "records."),
        ("No software needed", "It does not crack passwords",
         "If a document asks for a password you have genuinely never seen, no "
         "browser tool can legitimately open it. Ask the issuer for a fresh "
         "copy instead."),
        ("Fast &amp; high quality", "Output stays identical",
         "Unlocked pages are copied exactly \u2014 same fonts, same layout, "
         "same file quality. Only the restriction layer is dropped."),
    ],
    "pdf/watermark.html": [
        ("How to add a watermark", "Stamp text or a logo across pages",
         "Type words like SPECIMEN or pick an image, set opacity and angle, "
         "apply to all pages or a range, and save the watermarked copy."),
        ("Text or image logo stamps", "Built for sample documents",
         "Quotation drafts, internal handouts and 'not for submission' copies "
         "are the usual cases; a visible stamp prevents confusing a draft with "
         "the final file."),
        ("100% in-browser privacy", "Applied inside the tab",
         "The file is read and rewritten locally. The watermark is burned into "
         "the copy on your device, with nothing sent anywhere."),
        ("Angle and tile repeats", "Angle, spacing and repeat",
         "Diagonal repeats cover the full page; a single corner stamp suits "
         "letterheads. Opacity keeps the text underneath readable."),
        ("Lossless vector quality", "The document underneath stays sharp",
         "The stamp is added as vector text or a high-quality image, so the "
         "original content is not re-compressed into a blurry page."),
        ("Multi-device ready", "Same result on phone and laptop",
         "Settings carry over between devices because the tool is the same web "
         "page \u2014 start on a phone, finish on a desktop if needed."),
    ],
    "pdf/page-numbers.html": [
        ("How to number PDF pages", "Add page numbers in one pass",
         "Choose a position (corner or bottom centre), a style (plain, 'Page X "
         "of Y', Roman numerals), whether to skip the first page, and save."),
        ("Skip cover page", "Covers stay clean",
         "Application covers and title pages usually must not carry numbers; "
         "the skip-first switch keeps them unnumbered while the rest are "
         "stamped."),
        ("100% local privacy", "Numbering happens locally",
         "The PDF is opened, stamped and saved in the browser tab \u2014 "
         "suitable for documents with personal details."),
        ("Precision alignment", "Positions that look printed",
         "Margin and alignment controls place numbers where the examiner "
         "expects them, and the font size scales to the page."),
        ("Lossless vector text", "Numbers are real text",
         "The stamped number is vector text, not a picture \u2014 it stays "
         "sharp at any zoom and remains selectable."),
        ("Zero software install", "No office suite needed",
         "Numbering usually means a word-processor round-trip; here the PDF is "
         "stamped directly, with no conversion that could disturb the "
         "layout."),
    ],
    "pdf/rotate.html": [
        ("How to rotate PDF pages", "Turn pages that scanned sideways",
         "Scanners often save landscape pages rotated. Rotate single pages or "
         "all of them, preview, and save the corrected PDF."),
        ("Permanent orientation", "The rotation is saved into the file",
         "The new file opens upright in every reader without asking the viewer "
         "to rotate anything \u2014 important for printed submissions."),
        ("100% private &amp; secure", "Rotation without upload",
         "Pages are re-written inside the browser tab; the document never "
         "leaves the device."),
        ("Lossless quality", "Nothing is re-rendered",
         "Rotation changes the page orientation, not the content: text, "
         "vectors and images keep their original resolution."),
        ("Individual or bulk rotation", "Mix directions in one file",
         "Turn one wrong page by 90 degrees and the rest by 180 in the same "
         "pass \u2014 each page card carries its own rotation."),
        ("Works on every platform", "Touch controls included",
         "Buttons and drag controls work the same on a phone screen and a "
         "desktop, so a quick fix is possible from either."),
    ],
    "pdf/protect.html": [
        ("How to password protect a PDF", "Set an open password on a PDF",
         "Type a password, confirm it, and the tool writes an encrypted copy "
         "that asks for the password at open time."),
        ("Industry-standard encryption", "Standard PDF encryption",
         "The file uses the encryption every PDF reader understands \u2014 "
         "Adobe Reader, browser viewers and phone apps all prompt "
         "correctly."),
        ("100% in-browser privacy", "Password and file stay local",
         "Both are handled inside the tab; nothing about the document or the "
         "password is transmitted or stored."),
        ("Control permissions", "Share through a second channel",
         "Send the PDF by email and the password by message. Anyone who sees "
         "only one of the two gets nothing."),
        ("No software or installation", "Two minutes, no printer",
         "Protecting an identity proof used to mean scanning and re-printing "
         "routines; now it is a password box and a save click."),
        ("Universal reader compatibility", "Recipients need no special app",
         "Encrypted PDFs open in the standard readers people already have; the "
         "password prompt appears automatically."),
    ],
}

for rel, cells in CELLS.items():
    path = os.path.join(ROOT, rel)
    s = io.open(path, encoding="utf-8").read()
    for old_title, new_title, new_desc in cells:
        old_h = f'<h3 class="vytra-info-cell-title">{old_title}</h3>'
        if s.count(old_h) != 1:
            problems.append(f"{rel}: h3 count {s.count(old_h)}: {old_title!r}")
            continue
        s = s.replace(old_h, f'<h3 class="vytra-info-cell-title">{new_title}</h3>')
        pat = ('(' + re.escape(f'<h3 class="vytra-info-cell-title">{new_title}</h3>')
               + r'\s*<p class="vytra-info-cell-desc">)[^<]*(</p>)')
        s, n = re.subn(pat, lambda m: m.group(1) + new_desc + m.group(2), s,
                       count=1)
        if n != 1:
            problems.append(f"{rel}: desc replace failed for {new_title!r}")
    io.open(path, "w", encoding="utf-8", newline="\n").write(s)

# ------------------------ 4+5. Remove badge divs + ad-notice label divs
badge = re.compile(
    r'[ \t]*<div class="vytra-dz-secure-badge">[\s\S]*?</div>\n')
adlabel = re.compile(r'\s*<div class="vytra-ad-notice">Advertisement</div>')
removed = {"badge": 0, "adlabel": 0}
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in (".git", "seo", "templates",
                                            "__pycache__")]
    for fn in files:
        if not fn.endswith(".html"):
            continue
        path = os.path.join(dirpath, fn)
        s = io.open(path, encoding="utf-8").read()
        s2, nb = badge.subn("", s)
        s2, na = adlabel.subn("", s2)
        if nb or na:
            io.open(path, "w", encoding="utf-8", newline="\n").write(s2)
            removed["badge"] += nb
            removed["adlabel"] += na
print(f"removed: {removed['badge']} badges, {removed['adlabel']} ad labels")

if problems:
    print("=== PROBLEMS ===")
    for p in problems:
        print("  " + p)
    sys.exit(1)
print("all edits applied cleanly")
