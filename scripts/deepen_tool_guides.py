# -*- coding: utf-8 -*-
"""Round-4b: deepen each injected guide past 300 words (reviewer threshold).
Inserts one more substantive paragraph after the first paragraph of each
vytra-editorial section, plus one more paragraph in the code-editor guide.
"""
import io
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

P = ('  <p style="font-size:0.95rem;line-height:1.75;'
     'color:var(--text-muted,#475569);margin:0 0 1.15rem;">{}</p>\n')

EXTRA = {
    "pdf/merge.html":
        "Merging does not recompress or rasterise anything: every page is copied into "
        "the new PDF at full quality, so text stays selectable and print quality is "
        "unchanged. There is no file-count limit beyond what your device can hold, and "
        "because nothing is uploaded, joining a 60 MB project report takes the same few "
        "seconds as joining a ten-page form.",
    "pdf/split.html":
        "Splitting is also a privacy habit: when an officer needs three pages, send "
        "three pages, not the whole 200-page file. The output is a normal PDF with the "
        "original page size and orientation preserved, and it can be compressed further "
        "if needed. For study workflow, separate a combined textbook into per-unit "
        "files and revise one unit at a time without carrying the whole book on your "
        "phone. Nothing is uploaded at any point.",
    "pdf/compress.html":
        "Compression works by re-encoding the images inside the PDF at lower resolution "
        "while keeping the text layer intact, which is why scanned documents shrink far "
        "more than text documents. If a file barely moves, it is already near the "
        "minimum for its content \u2014 reduce the pages themselves with Split instead "
        "of pushing quality lower. You can switch presets and preview repeatedly; the "
        "original file on your device is never modified until you save the copy.",
    "pdf/jpg-to-pdf.html":
        "A common exam-form pattern is one A4 page holding the photograph on top and "
        "the signature below it \u2014 many notifications ask for exactly this "
        "arrangement, and a single page avoids the portal rejecting two separate "
        "uploads. If your images are already sized to the notification's dimensions "
        "(for example a 200\u00d7230 px photo), use the fit option so nothing is "
        "cropped. The tool works the same on a phone as on a laptop, and the generated "
        "PDF is accepted anywhere a normal PDF is.",
    "pdf/pdf-to-jpg.html":
        "The images are ordinary JPGs \u2014 crop, rotate or rename them in any gallery "
        "app before sharing. Quality matters most on pages with small print: admit "
        "cards, seat numbers and date tables lose legibility first, so convert those at "
        "the highest setting. For casual sharing into a study group, a lower setting "
        "keeps the file small enough for WhatsApp. A single page converts in a second "
        "or two, and a large PDF never leaves your browser while it renders.",
    "pdf/word-to-pdf.html":
        "The conversion keeps the document structure rather than screenshotting it: "
        "headings remain headings, table borders stay crisp at any zoom, and page "
        "numbers stay where you placed them \u2014 which matters when the evaluator "
        "zooms in or prints the file. Before submitting, check the tables on the second "
        "or third page, any manual page breaks, and the page count against the "
        "assignment limit. If the PDF runs long, adjust the margins in the document and "
        "convert again rather than accepting an over-length submission.",
    "pdf/ocr.html":
        "Recognised text comes back as a separate, selectable layer \u2014 the original "
        "page images are untouched, so you keep both versions. Accuracy on clean "
        "printed scans is usually good for English, while old typewritten pages, faint "
        "photocopies and regional scripts vary more. A practical habit: OCR only the "
        "pages you need to quote, then proofread each quoted line against the image "
        "before pasting it into notes. Everything runs on your device, so a circular "
        "with personal details is never uploaded.",
    "pdf/translate.html":
        "The translated PDF keeps the original layout page by page, so figures, tables "
        "and dates stay exactly where they appear in the original \u2014 the main "
        "advantage over pasting paragraphs into a translator. Page numbers still match, "
        "which matters when you must refer back to a page in an application. "
        "Translation quality is good for plain administrative language and weaker for "
        "idioms and legal phrasing: treat the output as a reading aid and verify "
        "anything you intend to act on against the original page.",
    "pdf/protect.html":
        "Protection encrypts the whole file, not just the opening screen: without the "
        "password the content cannot be selected, copied or printed by ordinary "
        "readers, and the encryption is standard PDF security that any reader \u2014 "
        "phone, laptop, Adobe Reader, browser viewers \u2014 understands. Give each "
        "document type a different password (one for identity proofs, one for financial "
        "papers), and keep the original unprotected copy on your device for portals that "
        "reject encrypted uploads.",
    "pdf/unlock.html":
        "The unlocked file is a fresh copy \u2014 the original stays untouched, so you "
        "keep the protected version as a backup. Restrictions that get removed include "
        "printing bans, copy-and-extract bans and change limits. After unlocking, check "
        "the two things you actually needed: try printing page one, and try selecting a "
        "line of text. For study PDFs from coaching institutes or open websites this is "
        "often the whole fix: print the chapter you are working on instead of reading "
        "on screen.",
    "developer/index.html":
        "Beyond running code, the editor keeps a small file workspace: several files "
        "can sit side by side and be saved as one archive download. The console "
        "separates standard output from error text, the stdin box handles interactive "
        "input, and JavaScript runs post their messages back into the console from "
        "inside the isolated frame. Nothing you type is stored on Vytra's side; closing "
        "the tab clears the session.",
}


def main():
    for rel, para in EXTRA.items():
        path = os.path.join(ROOT, rel)
        s = io.open(path, encoding="utf-8").read()
        key = "vytra-editorial" if rel != "developer/index.html" else "How the Vytra Code Editor works"
        i = s.find(key)
        if i < 0:
            print(f"PROBLEM section not found: {rel}")
            return 1
        # first </p> after the section start = end of the first paragraph
        j = s.find("</p>", i)
        if j < 0:
            print(f"PROBLEM no paragraph end: {rel}")
            return 1
        insert_at = j + len("</p>\n")
        s = s[:insert_at] + P.format(para) + s[insert_at:]
        io.open(path, "w", encoding="utf-8", newline="\n").write(s)
        print(f"ok: {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
