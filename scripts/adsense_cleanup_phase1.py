#!/usr/bin/env python3
"""Phase 1 — AdSense cleanup (vytra.in).

Fixes applied to every HTML file in the repo:
  1. Remove Login / Sign up buttons (site has no accounts).
  2. Remove the dead auth overlay modal + its ilpAuthInit script.
  3. Replace misleading caption "100% free thanks to advertising" -> "Advertisement".
  4. Replace flash placeholder "0 Pages \u2022 0 KB" -> "Select a file to see details".
  5. Attribution: "Developed & Maintained by Vytra Team" -> "Developed & Designed by h1k0r"
     (avatar V -> H on the author bar).
  6. Strip internal "(iLovePDF-logic ...)" notes from HTML comments.
  7. Add "Blog & Guides" link to the footer Company column (all pages with a Contact link).
  8. Add "BLOG" link to desktop nav + mobile panel (pages with the full navbar).
  9. robots.txt: remove internal comment about competing with iLovePDF.

Idempotent: re-running produces no further changes.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AD_OLD = "100% free thanks to advertising"
AD_NEW = "Advertisement"
ZERO_OLD = "0 Pages \u2022 0 KB"
ZERO_NEW = "Select a file to see details"
ZERO2_OLD = "0 KB &bull; 0 Pages"
ZERO3_OLD = "0 Pages Total"
AUTHOR_OLD = "Developed &amp; Maintained by Vytra Team"
AUTHOR_NEW = "Developed &amp; Designed by h1k0r"
AVATAR_OLD = '<div class="vytra-author-avatar">V</div>'
AVATAR_NEW = '<div class="vytra-author-avatar">H</div>'

stats = {}
warnings = []


def bump(key, n=1):
    stats[key] = stats.get(key, 0) + n


def prefix_for(path):
    rel = os.path.relpath(os.path.dirname(path), ROOT)
    depth = 0 if rel == "." else len(rel.split(os.sep))
    return "../" * depth


def remove_auth_block(s, fname):
    """Remove <div class="ilp-auth-overlay"> ... (balanced divs) plus the
    immediately-following <script> that defines ilpAuthInit."""
    m = re.search(r"[ \t]*<div class=\"ilp-auth-overlay\" id=\"ilpAuthOverlay\"", s)
    if not m:
        return s
    start = m.start()
    pos = s.index("<div", start)
    depth = 0
    while True:
        nd = s.find("<div", pos)
        nc = s.find("</div>", pos)
        if nc == -1:
            warnings.append(f"{fname}: auth overlay closing </div> not found")
            return s
        if nd != -1 and nd < nc:
            depth += 1
            pos = nd + 4
        else:
            depth -= 1
            pos = nc + 6
            if depth == 0:
                break
    end = pos
    m2 = re.match(r"\s*<script>.*?ilpAuthInit.*?</script>", s[end:], re.S)
    if m2:
        end += m2.end()
    else:
        warnings.append(f"{fname}: auth script not directly after overlay")
    s = s[:start] + s[end:]
    bump("auth_overlay_removed")
    return s


def process(path):
    with open(path, "rb") as f:
        raw = f.read()
    try:
        s = raw.decode("utf-8")
    except UnicodeDecodeError:
        warnings.append(f"{path}: not utf-8, skipped")
        return
    orig = s
    fname = os.path.relpath(path, ROOT)

    # 1. Login / Sign up buttons (CRLF-safe)
    for cls in ("ilp-login", "ilp-signup"):
        pat = r"[ \t]*<button type=\"button\" class=\"" + cls + r" ilp-authbtn\"[^\n]*</button>\r?\n"
        s2 = re.sub(pat, "", s, count=1)
        if s2 != s:
            bump("authbtn_removed")
            s = s2

    # 2. Auth overlay + script
    s = remove_auth_block(s, fname)

    # 3. Ad caption
    s2 = re.sub(
        r"<div class=\"vytra-ad-notice\">\s*" + re.escape(AD_OLD) + r"\s*</div>",
        '<div class="vytra-ad-notice">' + AD_NEW + "</div>",
        s,
    )
    if s2 != s:
        bump("ad_notice_fixed")
        s = s2

    # 4. Placeholder flash (all known variants)
    for zold in (ZERO_OLD, ZERO2_OLD, ZERO3_OLD):
        n = s.count(zold)
        if n:
            s = s.replace(zold, ZERO_NEW)
            bump("zero_flash_fixed", n)

    # 5. Attribution
    if AUTHOR_OLD in s:
        s = s.replace(AUTHOR_OLD, AUTHOR_NEW)
        bump("author_text_fixed")
    if AVATAR_OLD in s:
        s = s.replace(AVATAR_OLD, AVATAR_NEW)
        bump("author_avatar_fixed")

    # 6. Internal iLovePDF comments
    s2 = re.sub(r" \(iLovePDF-logic[^)]*\)", "", s)
    if s2 != s:
        bump("ilovepdf_comments")
        s = s2

    p = prefix_for(path)
    eol = "\r\n" if "\r\n" in s[:4000] else "\n"

    # 7. Footer blog link
    m = re.search(r"([ \t]*)<li><a href=\"([^\"]*)contact\.html\">Contact</a></li>", s)
    if m:
        indent, p2 = m.group(1), m.group(2)
        line = m.group(0)
        add = (
            line
            + eol
            + indent
            + '<li><a href="'
            + p2
            + 'blog/">Blog &amp; Guides</a></li>'
        )
        if 'blog/">Blog' not in s:
            s = s.replace(line, add, 1)
            bump("footer_blog_link")
    else:
        if "ilp-topnav" in s or 'class="footer"' in s:
            warnings.append(f"{fname}: no footer Contact link found")

    # 8a. Desktop nav (before ALL PDF TOOLS mega)
    if 'data-mega="all"' in s:
        if p + 'blog/" class="ilp-link">BLOG</a>' not in s:
            m = re.search(r"([ \t]*)<div class=\"ilp-has-mega\" data-mega=\"all\">", s)
            if m:
                line = m.group(0)
                ins = (
                    m.group(1)
                    + '<a href="'
                    + p
                    + 'blog/" class="ilp-link">BLOG</a>'
                    + eol
                    + line
                )
                s = s.replace(line, ins, 1)
                bump("nav_blog_link")

    # 8b. Mobile panel (after mobile ALL PDF TOOLS anchor, svg width 12)
    if 'ALL PDF TOOLS<svg width="12"' in s:
        if 'class="ilp-link">BLOG</a>' not in s:
            m = re.search(
                r"[ \t]*<a href=\"[^\"]*\" class=\"ilp-link red\">ALL PDF TOOLS<svg width=\"12\".*?</a>(?P<eol>\r?\n)",
                s,
            )
            if m:
                line = m.group(0)
                ind = re.match(r"[ \t]*", line).group(0)
                ins = (
                    line
                    + ind
                    + '<a href="'
                    + p
                    + 'blog/" class="ilp-link">BLOG</a>'
                    + m.group("eol")
                )
                s = s.replace(line, ins, 1)
                bump("mobile_blog_link")

    if s != orig:
        with open(path, "wb") as f:
            f.write(s.encode("utf-8"))
        bump("files_changed")


def main():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "__pycache__")]
        for fn in filenames:
            if fn.endswith(".html"):
                process(os.path.join(dirpath, fn))

    # robots.txt
    rp = os.path.join(ROOT, "robots.txt")
    with open(rp, "rb") as f:
        rb = f.read().decode("utf-8")
    rb2 = rb.replace(
        "# Vytra.in Robots.txt \u2014 world-class crawl config to compete with iLovePDF",
        "# Vytra.in Robots.txt",
    )
    if rb2 != rb:
        with open(rp, "wb") as f:
            f.write(rb2.encode("utf-8"))
        bump("robots_fixed")

    print("=== Phase 1 cleanup report ===")
    for k in sorted(stats):
        print(f"  {k}: {stats[k]}")
    if warnings:
        print(f"--- warnings ({len(warnings)}) ---")
        for w in warnings:
            print("  " + w)


if __name__ == "__main__":
    sys.exit(main())
