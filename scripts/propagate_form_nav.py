#!/usr/bin/env python3
"""Propagate IMAGE TOOLS + FORM KIT nav entries into every page that carries the
site nav (all except pdf/compress.html — patched by hand — and blog/* which is
rebuilt from the shell). Idempotent: each insertion checks for itself.

Depth-aware: pages under a subfolder use ../ prefixes, root pages do not.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"templates", "__pycache__", ".github", "image", "forms", "blog", "node_modules"}
SKIP_FILES = {os.path.join("pdf", "compress.html")}

ARROW_SVG = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" '
             'style="display:inline;vertical-align:-1px;margin-left:5px;">'
             '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
CHEV_SVG = ('<svg width="9" height="6" viewBox="0 0 9 6" fill="none" '
            'style="display:inline;vertical-align:1px;margin-left:5px;">'
            '<path d="M1 1l3.5 3.5L8 1" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def desktop_drops(ind, d):
    return (
        f'{ind}<div class="ilp-has-mega" data-mega="img">\n'
        f'{ind}  <a href="{d}image/" class="ilp-link">IMAGE TOOLS{CHEV_SVG}</a>\n'
        f'{ind}  <div class="ilp-mega" style="width:min(360px,94vw);">\n'
        f'{ind}    <div><h4>Image Tools</h4><a href="{d}image/resize.html"><span class="ilp-badge" style="background:#DB2777;color:#fff;font-size:13px;">&#8596;</span>Photo Resizer</a><a href="{d}image/signature.html"><span class="ilp-badge" style="background:#7C3AED;color:#fff;font-size:13px;">S</span>Signature Resizer</a><a href="{d}image/compress.html"><span class="ilp-badge" style="background:#0D9488;color:#fff;font-size:10px;">KB</span>Exact-KB Compressor</a></div>\n'
        f'{ind}  </div>\n'
        f'{ind}</div>\n'
        f'{ind}<div class="ilp-has-mega" data-mega="forms">\n'
        f'{ind}  <a href="{d}forms/" class="ilp-link">FORM KIT{CHEV_SVG}</a>\n'
        f'{ind}  <div class="ilp-mega" style="width:min(360px,94vw);">\n'
        f'{ind}    <div><h4>Form-Ready Kit</h4><a href="{d}forms/preflight.html"><span class="ilp-badge" style="background:#E5322D;color:#fff;font-size:13px;">&#10003;</span>Pre-flight Checker</a><a href="{d}forms/specs.html"><span class="ilp-badge" style="background:#2563EB;color:#fff;font-size:13px;">&#9635;</span>Exam Specs Database</a></div>\n'
        f'{ind}  </div>\n'
        f'{ind}</div>\n'
    )


def mobile_links(ind, d):
    return (
        f'{ind}<a href="{d}image/" class="ilp-link">IMAGE TOOLS{ARROW_SVG}</a>\n'
        f'{ind}<a href="{d}forms/" class="ilp-link">FORM KIT{ARROW_SVG}</a>\n'
    )


def mega_cols(ind, d):
    return (
        f'{ind}<div><h4>Image Tools</h4><a href="{d}image/resize.html">Photo Resizer</a><a href="{d}image/signature.html">Signature Resizer</a><a href="{d}image/compress.html">Exact-KB Compressor</a></div>\n'
        f'{ind}<div><h4>Form-Ready Kit</h4><a href="{d}forms/preflight.html">Pre-flight Checker</a><a href="{d}forms/specs.html">Exam Specs Database</a></div>\n'
    )


FOOTER_COLS = """      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Image Tools</h4>
        <ul class="footer-links">
          <li><a href="{d}image/resize.html">Photo Resizer</a></li>
          <li><a href="{d}image/signature.html">Signature Resizer</a></li>
          <li><a href="{d}image/compress.html">Exact-KB Compressor</a></li>
        </ul>
      </div>
      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Form-Ready Kit</h4>
        <ul class="footer-links">
          <li><a href="{d}forms/preflight.html">Pre-flight Checker</a></li>
          <li><a href="{d}forms/specs.html">Exam Specs Database</a></li>
        </ul>
      </div>
"""


def process(path, rel):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    orig = s
    d = "../" if os.path.dirname(rel) else ""
    hits = {"desktop": 0, "mobile": 0, "mega": 0, "footer": 0}

    if 'data-mega="img"' not in s:
        m = re.search(r'([ \t]*)(<div class="ilp-has-mega" data-mega="all">)', s)
        if m:
            s = s[:m.start()] + desktop_drops(m.group(1), d) + s[m.start():]
            hits["desktop"] = 1

    if 'IMAGE TOOLS<svg width="12"' not in s:
        m = re.search(r'([ \t]*)(<a href="[^"]*tools/" class="ilp-link red">ALL PDF TOOLS<svg width="12")', s)
        if m:
            s = s[:m.start()] + mobile_links(m.group(1), d) + s[m.start():]
            hits["mobile"] = 1

    if not re.search(r'<h4>Image Tools</h4><a href="[^"]*">Photo Resizer</a>', s):
        m = re.search(r'([ \t]*)(<div><h4>PDF Security</h4>)', s)
        if m:
            s = s[:m.start()] + mega_cols(m.group(1), d) + s[m.start():]
            hits["mega"] = 1

    if 'margin-bottom:1rem;">Image Tools</h4>' not in s:
        m = re.search(r'<div>\s*<h4 style="color:#ffffff; font-size:0\.95rem; margin-bottom:1rem;">Company & Help</h4>', s)
        if m:
            s = s[:m.start()] + FOOTER_COLS.format(d=d) + m.group(0).replace(
                m.group(0), '<div>\n        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Company & Help</h4>') + s[m.end():]
            hits["footer"] = 1

    if s != orig:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
    return hits


def main():
    changed, missing = 0, []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT)
            if rel in SKIP_FILES:
                continue
            hits = process(full, rel)
            total = sum(hits.values())
            if total:
                changed += 1
            if total < 4:
                missing.append((rel, hits))
    print(f"pages updated: {changed}")
    for rel, hits in missing:
        print(f"  partial: {rel} -> {hits}")


if __name__ == "__main__":
    main()
