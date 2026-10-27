#!/usr/bin/env python3
"""Build the vytra.in blog: index + article pages from content modules.

Reuses the real site navbar/footer (extracted from pdf/compress.html, which the
Phase-1 cleanup already updated: no Login buttons, BLOG link present) so blog
pages are visually identical to the rest of the site.

Also appends blog URLs to sitemap.xml (idempotent) and bumps lastmod for pages
edited during Phase 1.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from blog_content_a import ARTICLES_A  # noqa: E402
from blog_content_b import ARTICLES_B  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(ROOT, "blog")
SNIPPET_SRC = os.path.join(ROOT, "pdf", "compress.html")
TODAY = "2026-10-27"
TODAY_HUMAN = "27 October 2026"
SITE = "https://vytra.in"

ARTICLES = ARTICLES_A + ARTICLES_B
BY_SLUG = {a["slug"]: a for a in ARTICLES}

ADSENSE = ('  <script async defer src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
           '?client=ca-pub-7919122689237518" crossorigin="anonymous"></script>')

PAGE_STYLE = """
  <style>
    .legal-card dl { margin: 0; }
    .legal-card dt { font-weight: 700; margin-top: 16px; color: #111827; }
    .legal-card dd { margin: 6px 0 0 0; color: #374151; line-height: 1.65; }
    .blog-meta { font-size: .85rem; color: #64748b; margin: -.4rem 0 1.4rem; }
    .blog-meta a { color: #E5322D; text-decoration: none; font-weight: 600; }
    .blog-cta a { display: inline-block; background: #E5322D; color: #fff; padding: 11px 20px;
      border-radius: 8px; font-weight: 700; text-decoration: none; margin-top: 6px; }
    .blog-cta a:hover { background: #c8291f; }
    .blog-author { display: flex; gap: 14px; align-items: flex-start; background: #f9fafb;
      border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; margin-top: 2rem; }
    .blog-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 18px; margin: 1.5rem 0; }
    .blog-card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 18px;
      background: #fff; display: flex; flex-direction: column; gap: 8px; }
    .blog-card:hover { border-color: #fca5a5; box-shadow: 0 4px 14px rgba(0,0,0,.05); }
    .blog-card h2 { font-size: 1.05rem; margin: 0; line-height: 1.4; }
    .blog-card h2 a { color: #111827; text-decoration: none; }
    .blog-card h2 a:hover { color: #E5322D; }
    .blog-card p { font-size: .88rem; color: #4b5563; line-height: 1.6; margin: 0; flex: 1; }
    .blog-card .card-meta { font-size: .76rem; color: #9ca3af; text-transform: uppercase;
      letter-spacing: .04em; font-weight: 700; }
    .blog-card .read-more { font-size: .85rem; font-weight: 700; color: #E5322D; }
    .blog-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: .6rem 0 0; }
    .blog-chip { font-size: .8rem; font-weight: 700; background: #fef2f2; color: #b91c1c;
      border: 1px solid #fecaca; border-radius: 999px; padding: 5px 13px; }
    .blog-chip.muted { background: #f3f4f6; color: #6b7280; border-color: #e5e7eb; }
  </style>
"""


def extract_block(src, start_marker, end_marker, from_pos=0):
    i = src.index(start_marker, from_pos)
    j = src.index(end_marker, i) + len(end_marker)
    return src[i:j]


def load_shell():
    with open(SNIPPET_SRC, encoding="utf-8") as f:
        src = f.read()
    nav = extract_block(src, '<nav class="ilp-topnav"', "</nav>")
    footer = extract_block(src, '<footer class="footer">', "</footer>")
    # script that wires burger + mega menus
    k = src.index("(function ilpMegaInit()")
    s0 = src.rindex("<script>", 0, k)
    s1 = src.index("</script>", k) + len("</script>")
    mega = src[s0:s1]
    return nav, footer, mega


def head(title, desc, canonical, extra_ld, og_type="article"):
    esc_t, esc_d = html.escape(title), html.escape(desc)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R2EMRPEG70"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-R2EMRPEG70');
  </script>
  <meta charset="UTF-8">
  <meta http-equiv="x-dns-prefetch-control" content="on">
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com">
  <link rel="dns-prefetch" href="https://pagead2.googlesyndication.com">
  <link rel="dns-prefetch" href="https://www.googletagmanager.com">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://cdnjs.cloudflare.com" crossorigin>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/svg+xml" href="../assets/images/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="../assets/images/favicon-32x32.png">
  <link rel="apple-touch-icon" href="../assets/images/apple-touch-icon.png">
  <link rel="manifest" href="../site.webmanifest">
  <meta name="theme-color" content="#E5322D">
  <title>{esc_t}</title>
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="description" content="{esc_d}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Vytra">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{esc_t}">
  <meta property="og:description" content="{esc_d}">
  <meta property="og:image" content="{SITE}/assets/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc_t}">
  <meta name="twitter:description" content="{esc_d}">
  <meta name="twitter:image" content="{SITE}/assets/images/og-banner.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="stylesheet" href="../assets/css/ilp-workflow.css?v=20261009">
{PAGE_STYLE}
  <script type="application/ld+json">
{json.dumps(extra_ld, indent=2, ensure_ascii=False)}
  </script>
{ADSENSE}
</head>
<body>
"""


def breadcrumb(parts):
    out = ['  <div class="container">',
           '    <nav class="breadcrumb-nav" aria-label="Breadcrumb">']
    for i, (href, label) in enumerate(parts):
        if i:
            out.append('      <span class="breadcrumb-separator">/</span>')
        if href:
            out.append(f'      <a href="{href}">{label}</a>')
        else:
            out.append(f'      <span class="breadcrumb-current">{label}</span>')
    out += ['    </nav>', '  </div>']
    return "\n".join(out) + "\n"


def author_box():
    return """
      <div class="blog-author">
        <div class="vytra-author-avatar" style="flex:0 0 auto;">H</div>
        <div>
          <div style="font-weight:800;">h1k0r</div>
          <div style="font-size:.87rem;color:#64748b;line-height:1.65;margin-top:2px;">
            Independent developer who designs and builds Vytra's tools and writes these guides
            from hands-on testing on real application portals.
            <a href="../about.html" style="color:#E5322D;">About Vytra</a>
          </div>
        </div>
      </div>
"""


def faq_schema(faq_items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f["q"],
             "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
            for f in faq_items
        ],
    }


def article_schema(a):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["desc"],
        "datePublished": a["date"],
        "dateModified": a["date"],
        "author": {"@type": "Person", "name": "h1k0r"},
        "publisher": {"@type": "Organization", "name": "Vytra",
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/images/logo.svg"}},
        "mainEntityOfPage": {"@type": "WebPage",
                             "@id": f"{SITE}/blog/{a['slug']}.html"},
        "image": f"{SITE}/assets/images/og-banner.png",
    }


def breadcrumb_schema(a):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": a["cat"],
             "item": f"{SITE}/blog/{a['slug']}.html"},
        ],
    }


def build_article(a, nav, footer, mega):
    related_html = []
    for rs in a["related"]:
        r = BY_SLUG[rs]
        related_html.append(f'      <li><a href="{r["slug"]}.html">{html.escape(r["title"])}</a></li>')
    ld = {"@context": "https://schema.org", "@graph": [
        article_schema(a), breadcrumb_schema(a), faq_schema(a["faq"])]}
    page = head(f"{html.escape(a['title'])} | Vytra Blog", a["desc"],
                f"{SITE}/blog/{a['slug']}.html", ld)
    page += nav + "\n"
    page += breadcrumb([("../", "Home"), ("./", "Blog"), (None, a["cat"])])
    page += f"""
  <main class="container legal-content-wrap">
    <article class="legal-card">
      <h1>{html.escape(a['title'])}</h1>
      <div class="blog-meta">Last updated: {TODAY_HUMAN} &middot; By <a href="../about.html">h1k0r</a> &middot; Category: {html.escape(a['cat'])}</div>
{a['body']}
      <div class="highlight-box blog-cta">
        <p><strong>Try it yourself:</strong> {html.escape(a['tool']['label'])} &mdash; free,
        private, and it runs entirely in your browser.</p>
        <a href="{a['tool']['href']}">{html.escape(a['tool']['label'])} &rarr;</a>
      </div>
      <h2>Related guides</h2>
      <ul>
{chr(10).join(related_html)}
      </ul>
{author_box()}    </article>
  </main>

  {footer}
  {mega}
  <script defer src="../data/tools.js"></script>
  <script defer src="../assets/js/common.js"></script>
</body>
</html>
"""
    path = os.path.join(BLOG_DIR, a["slug"] + ".html")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return path, len(re.sub(r"<[^>]+>", " ", a["body"]).split())


def build_index(nav, footer, mega):
    cards = []
    for a in ARTICLES:
        cards.append(f"""      <div class="blog-card">
        <div class="card-meta">{html.escape(a['cat'])} &middot; {a['date']}</div>
        <h2><a href="{a['slug']}.html">{html.escape(a['title'])}</a></h2>
        <p>{html.escape(a['excerpt'])}</p>
        <a class="read-more" href="{a['slug']}.html">Read guide &rarr;</a>
      </div>""")
    chips = []
    for c in ("PDF Guides", "Govt Exam Forms"):
        chips.append(f'<span class="blog-chip">{c}</span>')
    for c in ("Image & Photo Tools", "Productivity & Office", "Developer Tips"):
        chips.append(f'<span class="blog-chip muted">{c} &middot; coming soon</span>')
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": f"{SITE}/blog/#blog", "name": "Vytra Blog",
         "description": "Free, practical guides for PDFs, government exam forms and document work.",
         "url": f"{SITE}/blog/", "author": {"@type": "Person", "name": "h1k0r"}},
        {"@type": "BreadcrumbList",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
             {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
         ]},
    ]}
    page = head("Vytra Blog \u2013 Free Guides for PDFs, Exam Forms & Document Work",
                "Practical, tested guides: compress PDFs for exam forms, photo and signature "
                "size rules, marksheet uploads, splitting, merging and more \u2014 written for "
                "Indian students and job applicants.", f"{SITE}/blog/", ld, og_type="website")
    page += nav + "\n"
    page += breadcrumb([("../", "Home"), (None, "Blog")])
    page += f"""
  <main class="container legal-content-wrap">
    <article class="legal-card">
      <h1>Vytra Blog &mdash; Guides That Make Forms Stop Rejecting You</h1>
      <p>
        Every guide here is written from hands-on testing: real file sizes, real portal
        behaviour, real fixes. The focus is the paperwork Indian students, job applicants and
        cyber caf&eacute; operators deal with every admission and exam season &mdash; photo
        and signature specs, marksheet compression, upload limits, bundles and conversions.
        Every article ends with the free browser tool it uses, so you can act while you read.
      </p>
      <div class="blog-chips">
{chr(10).join('        ' + c for c in chips)}
      </div>
      <div class="blog-grid">
{chr(10).join(cards)}
      </div>
      <p style="font-size:.88rem;color:#64748b;">
        New guides publish weekly. Need a topic covered? Tell us on the
        <a href="../contact.html" style="color:#E5322D;">contact page</a>.
      </p>
    </article>
  </main>

  {footer}
  {mega}
  <script defer src="../data/tools.js"></script>
  <script defer src="../assets/js/common.js"></script>
</body>
</html>
"""
    path = os.path.join(BLOG_DIR, "index.html")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return path


def update_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        s = f.read()

    entries = [("/", "0.9", "weekly"), ("/blog/", "0.8", "weekly")]
    entries += [(f"/blog/{a['slug']}.html", "0.7", "monthly") for a in ARTICLES]
    add = []
    for loc, prio, freq in entries:
        full = SITE + loc
        if f"<loc>{full}</loc>" not in s:
            add.append(
                "  <url>\n"
                f"    <loc>{full}</loc>\n"
                f"    <lastmod>{TODAY}</lastmod>\n"
                f"    <changefreq>{freq}</changefreq>\n"
                f"    <priority>{prio}</priority>\n"
                "  </url>\n"
            )
    if add:
        s = s.replace("</urlset>", "".join(add) + "</urlset>")

    # bump lastmod on pages edited during Phase 1
    for page in ("about.html", "contact.html", "privacy.html"):
        pat = re.compile(
            r"(<loc>" + re.escape(SITE + "/" + page) + r"</loc>\s*<lastmod>)[^<]+(</lastmod>)"
        )
        s = pat.sub(lambda m: m.group(1) + TODAY + m.group(2), s)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)
    return len(add)


def main():
    os.makedirs(BLOG_DIR, exist_ok=True)
    nav, footer, mega = load_shell()
    print(f"shell extracted: nav={len(nav)}B footer={len(footer)}B mega={len(mega)}B")
    total_words = 0
    for a in ARTICLES:
        path, words = build_article(a, nav, footer, mega)
        total_words += words
        flag = "OK " if words >= 900 else "LOW"
        print(f"  [{flag}] {a['slug']:<34} {words} words")
    ipath = build_index(nav, footer, mega)
    added = update_sitemap()
    print(f"index: {os.path.relpath(ipath, ROOT)}")
    print(f"sitemap entries added: {added}")
    print(f"TOTAL article words: {total_words}")
    if total_words < 9000:
        print("WARNING: average words/article below 900")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
