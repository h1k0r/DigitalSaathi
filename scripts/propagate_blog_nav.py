#!/usr/bin/env python3
"""Add a BLOG link to the mobile burger panel on every page that has the panel.

The desktop mega-nav and footer already link blog/; the mobile panel did not.
Idempotent: skips files whose panel already contains a blog link.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The mobile panel's COMPRESS PDF entry (uppercase, ilp-link) is the anchor.
# Desktop nav uses "Compress PDF" in mega menus, so the uppercase text inside
# the mobile panel is the reliable marker.
ANCHOR = '<a href="{p}pdf/compress.html" class="ilp-link">COMPRESS PDF</a>'
INSERT = ANCHOR + '\n        <a href="{p}blog/" class="ilp-link">BLOG</a>'


def process(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    if "ilp-mobile-panel" not in s:
        return None
    if re.search(r'ilp-mobile-panel.{0,1200}?blog/', s, re.S):
        return "skip"
    depth = os.path.dirname(os.path.relpath(path, ROOT))
    prefix = "" if depth == "" else "../"
    anchor = ANCHOR.format(p=prefix)
    if anchor not in s:
        return "no-anchor"
    s = s.replace(anchor, INSERT.format(p=prefix), 1)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)
    return "ok"


def main():
    added = skipped = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "templates")]
        for name in filenames:
            if not name.endswith(".html"):
                continue
            r = process(os.path.join(dirpath, name))
            if r == "ok":
                added += 1
            elif r == "skip":
                skipped += 1
            elif r == "no-anchor":
                print(f"  no anchor: {os.path.relpath(os.path.join(dirpath, name), ROOT)}")
    print(f"blog link added to mobile panel: {added} files (skipped {skipped})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
