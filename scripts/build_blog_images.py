#!/usr/bin/env python3
"""Generate one original 1200x630 WebP feature image per blog article.

Each image is drawn from scratch with PIL (brand background, red accent
shapes, category label, wrapped article title, vytra.in mark) - no stock
photos, no competitor assets. Output: assets/images/blog/<slug>.webp

Re-run after changing article titles or adding articles. Idempotent.
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(ROOT, "assets", "images", "blog")

W, H = 1200, 630
BG = (17, 24, 39)        # #111827 charcoal
BG2 = (31, 41, 55)       # #1f2937
RED = (229, 50, 45)      # #E5322D brand red
WHITE = (243, 244, 246)
GREY = (156, 163, 175)

FONT_DIRS = [r"C:\Windows\Fonts", "/usr/share/fonts/truetype/dejavu",
             "/usr/share/fonts/truetype/liberation"]


def find_font(*names):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    return None


BOLD = find_font("arialbd.ttf", "verdanab.ttf", "DejaVuSans-Bold.ttf",
                 "LiberationSans-Bold.ttf")
REG = find_font("arial.ttf", "verdana.ttf", "DejaVuSans.ttf",
                "LiberationSans-Regular.ttf")


def load(size, bold=True):
    path = (BOLD if bold else REG)
    if path:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def rounded(draw, box, radius, fill):
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def make(slug, title, cat, out_path):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Subtle diagonal band (background variation)
    d.polygon([(0, H), (W, H - 210), (W, H), (0, H)], fill=BG2)
    # Brand red accent: corner block + rule
    d.rectangle([0, 0, 14, H], fill=RED)
    rounded(d, [70, 66, 70 + 190, 66 + 46], 23, RED)
    f_cat = load(24)
    d.text((90, 74), cat.upper()[:18], font=f_cat, fill=WHITE)

    # Title, wrapped to fit
    f_title = load(64)
    lines = wrap(d, title, f_title, W - 160)
    while len(lines) > 4:
        f_title = load(54)
        lines = wrap(d, title, f_title, W - 160)
        if len(lines) <= 4:
            break
    line_h = int(f_title.size * 1.18)
    y = 150
    for ln in lines:
        d.text((76, y), ln, font=f_title, fill=WHITE)
        y += line_h

    # Red underline under the title block
    d.rectangle([76, y + 8, 76 + 300, y + 14], fill=RED)

    # Decorative "document" motif bottom-right
    ox, oy = W - 250, H - 250
    rounded(d, [ox, oy, ox + 150, oy + 190], 12, (55, 65, 81))
    for i in range(5):
        wln = 110 if i % 2 == 0 else 84
        d.rectangle([ox + 24, oy + 34 + i * 30, ox + 24 + wln, oy + 44 + i * 30],
                    fill=GREY if i else RED)
    # Folded corner
    d.polygon([(ox + 118, oy), (ox + 150, oy), (ox + 150, oy + 32)], fill=BG)

    # Footer mark
    f_foot = load(26, bold=False)
    d.text((76, H - 62), "vytra.in  ·  Free browser-based document tools",
           font=f_foot, fill=GREY)
    # small red dot
    d.ellipse([48, H - 58, 62, H - 44], fill=RED)

    out_path_png = out_path  # webp path
    img.save(out_path_png, "WEBP", quality=82, method=6)
    return os.path.getsize(out_path_png)


def main():
    sys.path.insert(0, HERE)
    from build_blog import ARTICLES  # noqa: E402  (builder defines the data)
    os.makedirs(OUT_DIR, exist_ok=True)
    total = 0
    for a in ARTICLES:
        out = os.path.join(OUT_DIR, a["slug"] + ".webp")
        kb = make(a["slug"], a["title"], a["cat"], out) / 1024
        flag = "OK " if kb < 100 else "BIG"
        if kb >= 100:
            total += 1
        print(f"  [{flag}] {a['slug']:<36} {kb:6.1f} KB")
    print(f"images over 100KB: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
