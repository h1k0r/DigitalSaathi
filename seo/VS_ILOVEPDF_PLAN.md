# Vytra.in vs iLovePDF — Honest SEO Battle Plan (No #1 Guarantee)

> No one can promise Google rank #1. This is the white-hat system to *earn* clicks vs iLovePDF.

## 1. Where we now match iLovePDF logic
- Mega-menu on 82 pages: `MERGE / SPLIT / COMPRESS / CONVERT ▾ / ALL PDF TOOLS ▾` with 6 columns
  (Organize, Optimize, Convert to/from, Edit, Security + Intelligence).
- Tool workflow: `Select (big red button) → grid + sidebar + sticky action bar → spinner overlay → success
  (stats + Download)`. Implemented on `pdf/merge.html`, `pdf/split.html`, `pdf/compress.html`.
- Brand A–Z for `vytra.in`: `assets/images/logo.svg`, `favicon.svg`, `favicon-*.png`,
  `apple-touch-icon.png`, `android-chrome-*.png`, `og-banner.png (1200×630)`, `site.webmanifest`,
  `theme-color #E5322D`, nav/footer rebranded Vytra.

## 2. Keyword system (honest, no stuffing)
- Primary pattern per tool: `{Task} Online Free — {Benefit} | Vytra`
  e.g. `Merge PDF Online Free — Combine PDFs in Seconds | Vytra`.
- Descriptions 150–160 chars, always: `free, online, private in-browser, no signup, no watermark`.
- Never target `calculators/*` / `developer/*` until files exist — `seo/keyword-map.json`
  currently points to missing `/calculators/age.html`. Either build those 5+3 pages or prune the map,
  else crawl waste.
- Don’t copy iLovePDF text. Our edge to state truthfully: **private client-side, no uploads,
  no queues, no accounts** (their funnel needs accounts/queues).

## 3. Technical checklist (done)
- [x] `sitemap.xml`: 82 URLs, priorities (home 1.0, merge/split/compress 0.9, hubs 0.85), `lastmod` today
- [x] `robots.txt`: Allow /, disallow `/design-system.html`, `/seo/`, sitemap absolute
- [x] Canonical absolute `https://vytra.in/...` per page, single H1, OG/Twitter large image
- [x] JSON-LD `WebApplication + Breadcrumb + HowTo + FAQ` — NO fake `aggregateRating`
      (fake stars = penalty risk)
- [x] `defer` for pdf-lib/pdf.js, `display=swap` fonts, `theme-color`, manifest, apple icon
- [x] Internal links: mega-menu + related tools + hubs `pdf/`, `image/`, `tools/`

## 4. To outrank on merit (next)
1. Unique 200-word intro + 3 steps + 4 FAQs per top-10 tool (merge/split/compress done visually,
   text still thin/generic).
2. DONE (PDF-only): removed `image/`, `calculators/`, `developer/`, `text/`, `utilities/` and 11 extra PDF pages (invoices, viewer, info, page-counter, workflow, reorder). Registry, search, sitemap, footers, directory and keyword data are PDF-only (32 tools).
3. Page speed: keep each tool <200KB HTML, lazy pdf.js until file chosen, `fetchpriority=high` on logo.
4. Measure: Search Console (index, CTR per `merge pdf` / `split pdf` / `compress pdf`),
   beat them on CTR with honest `Free • No signup • Private` suffixes, not on copied copy.
