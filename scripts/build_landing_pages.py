#!/usr/bin/env python3
"""Build exam/target-specific SEO landing pages (directory-style clean URLs).

Strategy: win long-tail, exam-specific queries ("ssc photo 20-50kb resize",
"compress pdf to 100kb for ssc") instead of head-on generic keywords.

Each page is written individually (NOT spun from one template): unique
editorial 600+ words, its own error blocks, its own FAQ with Hinglish
questions. Shared parts (nav shell, hero, author box) come from
build_form_kit so site chrome stays consistent.

Pages:
  /ssc-photo-resize-20kb-50kb/    (embedded Photo Resizer, SSC preset pre-set)
  /ibps-signature-resize-20kb/    (embedded Signature Resizer, IBPS preset)
  /rrb-photo-signature-size/      (embedded Photo Resizer, RRB preset)
  /compress-pdf-to-100kb/         (deep-link to Compress PDF, ?target=100 pre-sets Extreme)
  /compress-pdf-to-200kb/         (deep-link, ?target=200)
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_form_kit import (ADSENSE, TOOL_STYLE, author_related, breadcrumb,  # noqa: E402
                            dropzone, editorial_block, faq_block, head, hero,
                            load_shell, load_specs, tool_pages)

ROOT = os.path.dirname(HERE)
SITE = "https://vytra.in"
TODAY = "2026-10-27"
TODAY_HUMAN = "27 October 2026"


def errors_block(errors):
    out = ['    <div class="ik-card">',
           '      <h2 style="font-size:1.15rem;margin-top:0;">3 common rejections \u2014 and their fix</h2>']
    for msg, cause, fix in errors:
        out.append(f"""      <div style="border:1px solid #fecaca;background:#fff7f7;border-radius:10px;padding:12px 14px;margin:.7rem 0;">
        <div style="font-weight:800;color:#b91c1c;font-size:.92rem;">&ldquo;{html.escape(msg)}&rdquo;</div>
        <p style="margin:.35rem 0 0;font-size:.88rem;line-height:1.6;color:#374151;"><strong>Wajah:</strong> {cause}</p>
        <p style="margin:.3rem 0 0;font-size:.88rem;line-height:1.6;color:#374151;"><strong>Fix:</strong> {fix}</p>
      </div>""")
    out.append('    </div>')
    return "\n".join(out) + "\n"


def spec_table_for(exam, updated):
    p, s = exam["photo"], exam["signature"]
    return f"""    <div class="ik-card">
      <h2 style="font-size:1.15rem;margin-top:0;">{html.escape(exam['name'])} \u2014 official numbers (with source)</h2>
      <div class="editorial">
      <table>
        <tr><th>Field</th><th>Photo</th><th>Signature</th></tr>
        <tr><td>File size band</td><td><strong>{p['minKB']}\u2013{p['maxKB']} KB</strong></td><td><strong>{s['minKB']}\u2013{s['maxKB']} KB</strong></td></tr>
        <tr><td>Typical pixels</td><td>~{p['typicalPx']} px (ratio {p['ratioNum'][0]}:{p['ratioNum'][1]})</td><td>~{s['typicalPx']} px</td></tr>
        <tr><td>Format</td><td>{p['format']}</td><td>{s['format']}</td></tr>
        <tr><td>Official source</td><td colspan="2"><a href="{exam['source']}" target="_blank" rel="noopener">{exam['sourceLabel']}</a></td></tr>
        <tr><td>Last verified</td><td colspan="2"><strong>{updated}</strong> \u2014 limits change between notifications; the live form's instruction page is the final authority</td></tr>
      </table>
      <p class="ik-help">{html.escape(p.get('note',''))} {html.escape(s.get('note',''))}</p>
      </div>
    </div>
"""


def pdf_target_table(target):
    if target == 100:
        rows = """<tr><td>Single-page certificate (colour scan)</td><td>2\u20135 MB source</td><td><strong>80\u2013180 KB</strong> with Extreme + grayscale</td></tr>
        <tr><td>Signed declaration / undertaking PDF</td><td>0.3\u20131 MB</td><td>Comfortably under 100 KB with Extreme</td></tr>
        <tr><td>Photo + declaration combined</td><td>1\u20133 MB</td><td>Aim 70\u201390 KB for byte-rounding margin</td></tr>"""
        advice = "Type <strong>80</strong> as your working target, not 99 \u2014 file managers round KB differently than portals count bytes, and the middle of a cap survives both counting methods."
    else:
        rows = """<tr><td>Marksheet (single page, colour)</td><td>2\u20135 MB source</td><td><strong>80\u2013180 KB</strong> with Extreme + grayscale</td></tr>
        <tr><td>2\u20134 page document bundle</td><td>5\u201315 MB source</td><td>Compress parts first, then merge \u2014 lands near 150\u2013190 KB</td></tr>
        <tr><td>Certificate with seal + photo</td><td>3\u20138 MB source</td><td>100\u2013190 KB with Extreme + grayscale</td></tr>"""
        advice = "Type <strong>180</strong> as your working target: a file your file manager rounds to &ldquo;200KB&rdquo; can still exceed a portal's 200,000-byte cap. Ten percent of headroom removes that entire failure class."
    return f"""    <div class="ik-card">
      <h2 style="font-size:1.15rem;margin-top:0;">What to expect, by document type</h2>
      <div class="editorial">
      <table>
        <tr><th>Document</th><th>Typical source weight</th><th>After compression (honest ranges)</th></tr>
        {rows}
      </table>
      <p class="ik-help">{advice} Ranges, not guarantees \u2014 the number your tool reports after compressing <em>your</em> file is the only number that matters. Judge every upload by that display, then verify with your file manager.</p>
      </div>
    </div>
"""


def pdf_cta(target):
    return f"""    <div class="ik-card" style="border:2px solid #fecaca;background:#fffaf5;">
      <h2 style="font-size:1.15rem;margin-top:0;">Tool \u2014 opens pre-set for {target} KB</h2>
      <p class="ik-help" style="font-size:.9rem;">The button below opens Compress PDF with the <strong>Extreme preset already selected</strong> (loaded from this page's target). Add the grayscale checkbox for scanned or colour documents, then check the size the tool reports.</p>
      <div class="ik-cta">
        <a href="../pdf/compress.html?target={target}">Open Compress PDF \u2014 preset for {target} KB &rarr;</a>
      </div>
      <ol style="margin:.7rem 0 0;padding-left:1.3rem;font-size:.9rem;color:#374151;line-height:1.8;">
        <li>Drop your PDF (it stays in your browser).</li>
        <li>Preset arrives active \u2014 tick <strong>&ldquo;Convert scanned marksheets to grayscale&rdquo;</strong> for colour scans.</li>
        <li>Compress, read the before/after numbers, download.</li>
        <li>Still over the cap? See the three reasons below \u2014 usually it's a light preset, a colour scan, or a bundle that should be split.</li>
      </ol>
    </div>
"""


def embed_tool(specs, tool_slug, exam_id):
    tools = {t["slug"]: t for t in tool_pages(specs)}
    t = tools[tool_slug]
    preseed = f"""  <script>
  (function(){{
    var sel = document.getElementById('preset');
    if (!sel) return;
    for (var i = 0; i < sel.options.length; i++) {{
      if (sel.options[i].value.split('|')[0] === '{exam_id}') {{ sel.value = sel.options[i].value; break; }}
    }}
    sel.dispatchEvent(new Event('change'));
  }})();
  </script>
"""
    return t["body"] + t["script"] + preseed


def build_page(p, nav, footer, mega, specs):
    ld_graph = [
        {"@context": "https://schema.org", "@type": "WebApplication",
         "name": p["h1_plain"], "url": f"{SITE}/{p['slug']}/",
         "description": p["desc"], "applicationCategory": "MultimediaApplication",
         "operatingSystem": "Any", "browserRequirements": "Requires JavaScript",
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "author": {"@type": "Person", "name": "h1k0r"},
         "publisher": {"@type": "Organization", "name": "Vytra"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
             {"@type": "ListItem", "position": 2, "name": "Form-Kit", "item": f"{SITE}/forms/"},
             {"@type": "ListItem", "position": 3, "name": p["h1_plain"], "item": f"{SITE}/{p['slug']}/"}]},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer",
                                            "text": re.sub(r"<[^>]+>", " ", a).strip()}}
                        for q, a in p["faqs"]]},
    ]
    page = head(p["title"], p["desc"], f"{SITE}/{p['slug']}/",
                {"@context": "https://schema.org", "@graph": ld_graph})
    page += nav + "\n"
    page += breadcrumb([("../", "Home"), ("../forms/", "Form-Kit"), (None, p["crumb"])])
    page += hero(p["h1"], p["tagline"], p["steps"])
    page += p["top"]
    ed_html, ed_words = editorial_block(p["editorial"])
    page += ed_html
    page += errors_block(p["errors"])
    page += faq_block(p["faqs"])
    page += author_related(p["related_tools"], p["related_articles"])
    page += f"""  {footer}
  {mega}
  <script defer src="../data/tools.js"></script>
  <script defer src="../assets/js/common.js"></script>
</body>
</html>
"""
    outdir = os.path.join(ROOT, p["slug"])
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "index.html")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return path, ed_words


def ssc_page(specs):
    ex = next(e for e in specs["exams"] if e["id"] == "ssc")
    return {
        "slug": "ssc-photo-resize-20kb-50kb",
        "crumb": "SSC Photo Resize",
        "title": "SSC Photo Resize to 20\u201350 KB \u2014 Exact Pixels Tool | Vytra",
        "desc": "Resize SSC CGL/CHSL/MTS photo to 20\u201350 KB with exact pixels (200\u00d7230) in-browser. SSC preset pre-loaded, signature 10\u201320 KB band, official source links, common rejection fixes.",
        "h1": "SSC Photo Resize \u2014 20 KB to 50 KB, Exact Pixels",
        "h1_plain": "SSC Photo Resize to 20-50 KB",
        "tagline": "SSC ka photo band read kiya, tool preset pehle se set \u2014 drop, resize, upload.",
        "steps": ["Drop photo", "SSC preset pre-set", "Download at 35 KB"],
        "top": embed_tool(specs, "resize", "ssc") + spec_table_for(ex, specs["updated"]),
        "editorial": """
      <h2>SSC kya maangta hai \u2014 aur kya badalta rehta hai</h2>
      <p>Recent SSC notifications ask for a <strong>20\u201350 KB JPG</strong> photograph at roughly
      200&times;230 pixels (a 4:5-ish portrait), and a <strong>10\u201320 KB</strong> signature around
      4&times;2 cm. Two honest caveats belong in any trustworthy guide. First: an increasing number of
      SSC posts capture your photo <strong>live</strong> through webcam or phone during the form itself
      \u2014 if your form shows that flow, follow it and skip the upload entirely. Second: the exact band
      lives in <em>your</em> notification's instruction page; the table above is compiled from recent
      ones with the official source linked, last verified on the date shown.</p>
      <h2>Photo ka size 50KB se kam kaise karein</h2>
      <p>The tool above loads with the SSC preset already selected \u2014 target 35 KB (the middle of the
      band, safe from both rounding traps) and 200&times;230 pixels. Drop your photo, glance at the
      numbers, hit resize, download <em>Photo_35KB.jpg</em>. That is the whole job. Why the middle and
      not 49.9 KB? Because file managers round KB one way and portals count bytes another: a file your
      phone shows as &ldquo;49 KB&rdquo; can measure over a 50,000-byte cap. The band's middle passes
      both counting methods.</p>
      <h2>Why the ratio matters more than people think</h2>
      <p>Portals silently validate aspect ratio. A square 400&times;400 passport crop inside the correct
      KB band still fails forms that expect the taller 4:5 shape \u2014 and the error message rarely says
      &ldquo;wrong ratio&rdquo;; it says something vague like &ldquo;image specification not
      satisfied&rdquo;. The preset sets exact pixels that keep the expected shape. If your instruction
      page states its own pixel size, that number overrides the preset \u2014 type it into the width and
      height boxes directly.</p>
      <h2>The five-step workflow that never fails</h2>
      <ul>
      <li>Open your notification's instruction page beside this tool and note the exact band.</li>
      <li>Drop the photo, confirm the preset numbers match (or type your own).</li>
      <li>Resize, then verify the size in your file manager \u2014 not in your gallery app.</li>
      <li>Run the file through the <a href="../forms/preflight.html">Pre-flight Checker</a> for a second, independent verdict (size, ratio, background, format).</li>
      <li>Name it with its size (\u201CPhoto_35KB.jpg\u201D) so the deadline-hour upload is unambiguous.</li>
      </ul>
      <p>For the signature half of the same form, the band is 10\u201320 KB \u2014 use the
      <a href="../image/signature.html">Signature Resizer</a> preset and keep both files ready together.
      Originals stay untouched; you always upload the resized copy.</p>
      <h2>When to shoot vs when to reuse</h2>
      <p>SSC cycles accept the same recent photograph for multiple posts within a reasonable window
      \u2014 but "recent" here means current-looking, not last year's studio print. If your last photo
      predates a major appearance change (hair, beard, glasses), re-shoot; verification compares your
      form against your record, and a mismatched face is a worse problem than a mismatched KB. The
      capture itself: white or off-white plain wall, no patterned curtain behind you, phone at eye
      level, steady hands or a timer. One good capture, resized to 35 KB once, serves the entire
      registration form \u2014 photo upload, admission card, and any later document that asks for the
      same file. Keep the resized copy named <em>SSC_Photo_35KB.jpg</em> in a dedicated
      "exam files" folder on your phone and desktop; the next SSC notification reuses it without a
      single new edit.</p>
      <h2>What this page does not do</h2>
      <p>Honesty over hype: this page does not promise your form will be accepted. Portals validate
      dozens of fields \u2014 age, eligibility, category documents, centre choice \u2014 and no tool
      checks those. What the tool above does is eliminate the file-preparation failure class:
      correct band, correct pixels, correct format, correct background. Everything else is the
      form's own logic. And when the instruction page and this page disagree, the instruction page
      wins \u2014 always. The last-verified date in the table tells you when these numbers were
      last checked against official sources; if your notification arrived after that date, read
      its band and type those numbers into the tool directly.</p>
""",
        "errors": [
            ("Photograph / signature file size is not within the prescribed range",
             "The file sits outside 20\u201350 KB \u2014 usually a full-resolution camera photo (several MB) or an over-compressed file under 20 KB.",
             "Use the pre-set SSC target above (35 KB). Check the size in your file manager after download, not before."),
            ("Image dimensions do not match the required specification",
             "Pixels or aspect ratio differ from what the instruction page asks (common with square social-media crops).",
             "Set exact pixels in the tool (preset: 200&times;230) or type the numbers your notification states. Never crop to 1:1 for a 4:5 field."),
            ("Invalid file format / upload failed",
             "The portal accepts JPG only and the file is actually PNG (or a renamed extension that doesn't match the real bytes).",
             "Convert to JPG \u2014 any reliable converter, or resize here (output is always JPG). Upload the downloaded file, not the original from your gallery."),
        ],
        "faqs": [
            ("SSC photo ka size kitna hona chahiye?", "Recent notifications ask for a <strong>20\u201350 KB JPG</strong>, about 200&times;230 pixels. The preset above targets 35 KB \u2014 the safe middle. Verify the exact band in your notification (source: ssc.gov.in)."),
            ("Live photo capture wale SSC form me photo upload kyu nahi ho raha?", "Because there is no upload field \u2014 many recent SSC posts capture the photo live via webcam or phone during the form. Follow the form's on-screen flow; the file band applies only when a file upload is actually asked."),
            ("Photo 50KB se zyada aa rahi hai to kya karun?", "Drop the original into the tool above with the SSC preset: it sets 200&times;230 pixels and searches JPEG quality until the output lands at 35 KB. Several-megabyte phone photos routinely resize to 30\u201340 KB without visible quality loss."),
            ("Kya background white hona chahiye?", "Plain light backgrounds are the standard ask. Shoot against a white wall or sheet in even light; the <a href=\"../forms/preflight.html\">Pre-flight Checker</a> estimates background whiteness and flags shadowed edges."),
            ("Signature alag file me chahiye kya?", "Yes \u2014 SSC asks photo and signature as separate uploads with separate bands (signature 10\u201320 KB). Use the Signature Resizer preset for that file."),
            ("Resize ke baad photo blurry ho jayegi?", "At 200&times;230 an in-focus phone photo stays sharp \u2014 that is far below the camera's native resolution. Blur comes from the original shot, not from correct resizing; re-shoot if the source itself is soft."),
        ],
        "related_tools": [("image/resize.html", "Photo Resizer"), ("image/signature.html", "Signature Resizer"), ("forms/preflight.html", "Pre-flight Checker"), ("forms/specs.html", "Exam Specs Database")],
        "related_articles": [("ssc-photo-signature-size", "SSC photo & signature size guide"), ("file-size-too-large-error", "File size too large error fix"), ("compress-pdf-100kb", "Compress PDF under 100KB")],
    }


def ibps_page(specs):
    ex = next(e for e in specs["exams"] if e["id"] == "ibps")
    return {
        "slug": "ibps-signature-resize-20kb",
        "crumb": "IBPS Signature Resize",
        "title": "IBPS Signature Resize to 10\u201320 KB \u2014 Exact Size Tool | Vytra",
        "desc": "Resize IBPS PO/Clerk/RRB signature to 10\u201320 KB (about 140\u00d760) with white-background cleanup, in-browser. IBPS preset pre-loaded plus common rejection fixes.",
        "h1": "IBPS Signature Resize \u2014 10 KB to 20 KB",
        "h1_plain": "IBPS Signature Resize to 10-20 KB",
        "tagline": "IBPS ka signature band pre-set \u2014 white paper cleanup ke saath, browser me hi.",
        "steps": ["Upload signature", "IBPS preset pre-set", "Download at 15 KB"],
        "top": embed_tool(specs, "signature", "ibps") + spec_table_for(ex, specs["updated"]),
        "editorial": """
      <h2>Why the IBPS signature fails more than the photo</h2>
      <p>IBPS forms validate the signature in a narrow window: <strong>10 to 20 KB</strong>, a small
      wide image (roughly 140&times;60 pixels, the 7:3 shape of a 4&times;2 cm signature area), as JPG.
      Narrow windows fail more often \u2014 there is simply less room to land in. A 40 KB photo overshoots
      by 80%; a 25 KB signature overshoots by only 25%, but it fails exactly the same way. The fix is
      not effort, it is aiming: type 15 into the target above and let the encoder search.</p>
      <h2>Signature size 20KB se zyada hai? Ye karo</h2>
      <p>Three moves, in order. <strong>One:</strong> crop tight around the signature \u2014 most
      oversized signature files carry more white paper than ink, and paper is exactly what compression
      hates least. <strong>Two:</strong> keep the white-background cleanup switched on (it is on by
      default here): grey paper under window light becomes pure white, deep ink becomes crisper black,
      the middle tones of your strokes stay untouched. <strong>Three:</strong> let the preset's 15 KB
      target do the quality search. The result downloads as <em>Signature_15KB.jpg</em> \u2014 verify the
      number in your file manager and upload with confidence.</p>
      <h2>Shoot once, reuse for every IBPS cycle</h2>
      <p>The source photo matters more than any setting. Sign in dark ink on plain white paper; no
      lines, no grid, no date beside it. Photograph it straight-on in even indirect light \u2014 flash
      creates a hot spot on ballpoint ink and a shadow ridge at the paper edge. One clean capture
      resized per-form serves PO, Clerk and RRB cycles for years. If your style has drifted since an
      older signature, re-sign fresh rather than reusing the old scan: verification compares your form
      signature against your record, and consistency beats freshness.</p>
      <h2>Format and field gotchas</h2>
      <ul>
      <li><strong>JPG only in most cycles:</strong> PNG screenshots of a signature scan get rejected by fields expecting JPG. This tool outputs JPG always.</li>
      <li><strong>Separate from the photo:</strong> IBPS asks photo and signature as two different files with two different bands \u2014 never paste both into one image.</li>
      <li><strong>The declaration is not the signature:</strong> the handwritten declaration is its own upload, usually a longer text on its own page \u2014 the photo-to-PDF workflow in <a href="../blog/jpg-to-pdf-guide.html">JPG to PDF</a> covers that file.</li>
      <li><strong>Check before the deadline, not at it:</strong> run the final file through the <a href="../forms/preflight.html">Pre-flight Checker</a> \u2014 size, format, ratio and background in one pass.</li>
      </ul>
      <p>Numbers above are compiled from recent notifications (source linked in the table, last verified
      shown there). Different IBPS cycles word their bands slightly differently \u2014 when the live
      form's instruction disagrees, the form wins.</p>
      <h2>The night-before routine</h2>
      <p>Do not resize on submission day. The evening before the form opens (or the evening before you
      plan to fill it), prepare the full file set: photo at 20\u201350 KB, signature at 15 KB, both
      named with their sizes, both run through the Pre-flight Checker. This single habit converts the
      most stressful twenty minutes of the process \u2014 the deadline-hour scramble where people
      upload the wrong file into the wrong field \u2014 into a five-minute drag-and-drop of already-
      verified files. If something unexpected appears (a declaration upload, a left-thumb impression
      field), you still have calm hours left to handle it instead of minutes.</p>
      <p>One more pattern worth knowing: fields reject more often on the <em>second</em> attempt after
      a failed upload, because candidates re-upload the same wrong file or over-compress an already-
      compressed one. Always go back to the <strong>original</strong> and resize fresh. Compressing a
      compressed file compounds quality loss for zero size benefit \u2014 the encoder has nothing left
      to give. The tool above always starts from your original drop; keep it in front of you.</p>
""",
        "errors": [
            ("File size should be between 10 KB and 20 KB",
             "The signature is over 20 KB (untrimmed scan) or under 10 KB (over-compressed, ink eaten away).",
             "Target the middle: the preset above uses 15 KB. Re-download and confirm the size in your file manager before retrying."),
            ("Signature image dimensions are not as prescribed",
             "Wrong pixel shape \u2014 too tall, too square, or built from a full A4 scan instead of a tight crop.",
             "Crop tightly around the signature, then resize: the IBPS preset produces the wide ~140&times;60 shape the fields expect."),
            ("Signature is not clear / cannot be recognised",
             "Grey or shadowed paper, motion blur, or an ink tone that reads as light grey after earlier compression.",
             "Re-shoot flat in even light with dark ink; enable white-background cleanup here. Compression fixes background, not blur \u2014 if the strokes themselves are soft, recapture."),
        ],
        "faqs": [
            ("IBPS signature ka exact size kya hai?", "<strong>10\u201320 KB JPG</strong>, about 140&times;60 pixels (the shape of a 4&times;2 cm signature area). The preset above targets 15 KB \u2014 the safe middle of the band."),
            ("Signature banane ka sahi tarika kya hai?", "Plain white paper, dark pen, straight-on photo in even light. No lines or date beside the signature. Crop tight, then resize here with the white-background cleanup on."),
            ("Kya main PNG upload kar sakta hoon?", "Most IBPS cycles ask for JPG specifically. This tool outputs JPG always \u2014 drop any photo in and the download will be a correctly-sized JPG."),
            ("Photo aur signature ek hi file me daal sakte hain?", "No \u2014 IBPS asks them as separate files with separate bands (photo typically 20\u201350 KB, signature 10\u201320 KB). Keep two files, named with their sizes."),
            ("White background cleanup signature ko bigad to nahi degi?", "It only remaps near-white paper and deep ink tones; your strokes' mid-tones are preserved. It changes the paper, not what the signature says \u2014 and altering the signature itself is never acceptable."),
            ("Upload se pehle kaise verify karun?", "Run the file through the Pre-flight Checker: it shows size band, format, ratio and background whiteness as pass/fail with plain reasons \u2014 the same mechanical checks the portal performs."),
        ],
        "related_tools": [("image/resize.html", "Photo Resizer"), ("image/compress.html", "Exact-KB Compressor"), ("forms/preflight.html", "Pre-flight Checker"), ("forms/specs.html", "Exam Specs Database")],
        "related_articles": [("ssc-photo-signature-size", "SSC photo & signature size guide"), ("file-size-too-large-error", "File size too large error fix"), ("jpg-to-pdf-guide", "JPG to PDF for declarations")],
    }


def rrb_page(specs):
    ex = next(e for e in specs["exams"] if e["id"] == "rrb")
    return {
        "slug": "rrb-photo-signature-size",
        "crumb": "RRB Photo & Signature",
        "title": "RRB Photo & Signature Size 2026 \u2014 Pixels, KB Band, Resizer | Vytra",
        "desc": "RRB NTPC/Group D/ALP photo and signature size guide with typical KB bands, pixel values, official source links and an embedded resizer preset for RRB.",
        "h1": "RRB Photo & Signature Size \u2014 Check and Resize",
        "h1_plain": "RRB Photo & Signature Size Guide",
        "tagline": "Do files, ek page \u2014 RRB ka photo preset khula hua, signature ka band table me.",
        "steps": ["Check RRB bands", "Drop photo (preset set)", "Signature next"],
        "top": embed_tool(specs, "resize", "rrb") + spec_table_for(ex, specs["updated"]),
        "editorial": """
      <h2>RRB asks two files \u2014 and the bands move between notifications</h2>
      <p>Railway Recruitment Board forms (NTPC, Group D, ALP and others) take a
      <strong>recent photograph</strong> and a <strong>scanned signature</strong> as separate uploads.
      Typical bands seen across recent notifications: photos around <strong>15\u201340 KB</strong> and
      signatures at the familiar <strong>10\u201320 KB</strong>, with photo pixels around 200&times;230
      and a wide signature near 140&times;60. The important honesty note: RRB varies its numbers more
      than SSC or IBPS do \u2014 one cycle's advertisement may say 35 KB where another says 40 KB.
      Treat the table as your starting point and the instruction page of <em>your</em> form as the law.</p>
      <h2>The photo: recent, plain, right-sized</h2>
      <p>&ldquo;Recent&rdquo; in RRB language usually means a current-looking photograph (many
      notifications state a maximum age for the photo \u2014 check yours). Composition rules are stable
      across cycles: plain light background, face centred, no cap or dark glasses, even light without
      flash glare. The tool above loads with the RRB preset: mid-band target and typical pixels. Drop
      the photo, read the before/after numbers, download. If your notification states its own pixel
      values, type them over the preset \u2014 the notification always wins.</p>
      <h2>The signature: 10\u201320 KB, wide and clean</h2>
      <p>Switch to the <a href="../image/signature.html">Signature Resizer</a> for file two: the RRB
      band matches the standard 10\u201320 KB, target 15 KB with white-background cleanup on. Sign on
      plain white paper with dark ink, crop tight, no surrounding rules or dates. Both files should
      carry their sizes in the names (<em>RRB_Photo_32KB.jpg</em>, <em>RRB_Signature_15KB.jpg</em>) \u2014
      during a deadline hour, filenames are your checklist.</p>
      <h2>Verify as a pair, not one by one</h2>
      <p>After both files are resized, run each through the <a href="../forms/preflight.html">Pre-flight
      Checker</a> with the RRB exam selected: size band, ratio, pixels, format and background whiteness
      get one green line each, and any red line tells you which number to change. It takes ninety
      seconds and catches the class of errors that RRB portals report in the vaguest possible words.
      Keep the originals untouched \u2014 the next railway cycle reuses the same captures.</p>
      <h2>Which RRB form \u2014 and why it matters</h2>
      <p>NTPC, Group D, ALP and Ministerial posts run as separate notifications with separate
      instruction pages. This does not change the workflow (capture \u2192 resize \u2192 verify \u2192
      upload) but it does change the exact numbers, which is why this page links the official source
      instead of pretending one table rules them all. Open your notification PDF, search for the word
      "photograph" or "image", and read the two or three lines the recruitment body wrote. Compare
      them with the table above; where they match, use the preset with confidence; where they differ,
      type your notification's numbers into the tool and ignore the preset. That thirty-second check
      is the difference between a guide you can trust and a guide you must not.</p>
      <h2>Phone-capture tips that actually matter</h2>
      <ul>
      <li><strong>Steady beats fast:</strong> prop the phone or use a timer; motion blur is the number-one reason "not clear" errors appear.</li>
      <li><strong>Even light, no flash:</strong> indirect daylight; flash creates glare on ink and hard shadows on paper.</li>
      <li><strong>Fill the frame:</strong> the photo should be the photo \u2014 minimal wall, minimal paper margin \u2014 then crop tight in the tool.</li>
      <li><strong>One pass:</strong> resize once from the original; never compress an already-compressed file.</li>
      </ul>
      <p>That is the entire method \u2014 two files, one preset each, one verification pass. The
      railway form asks nothing exotic; it asks for exact numbers delivered cleanly, which is the
      one thing careful preparation can always guarantee. Do it the evening before, not at the last minute, and the
      upload itself becomes the easiest, calmest part of the whole application.</p>
""",
        "errors": [
            ("Photograph does not meet the required size / kindly upload recent photograph",
             "Outside the photo KB band (typically 15\u201340 KB across recent cycles) or an old/styled photo where a plain recent one is required.",
             "Resize with the RRB preset above (mid-band target), check the file manager size, and confirm your notification's exact band and photo-age clause."),
            ("Signature / photograph dimensions are incorrect",
             "Pixels or aspect ratio differ from the expected shape \u2014 square crops for photos, near-square crops for the wide signature field.",
             "Set exact pixels: photo preset ~200&times;230, signature ~140&times;60. If your form states its own values, type those instead."),
            ("Uploaded image is blurred / not visible",
             "Motion blur, flash glare, or heavy shadows \u2014 problems compression cannot fix, only masking can hide (and masking looks worse).",
             "Re-capture: steady phone, even indirect light, focus lock on the text/face, then resize once. The Pre-flight Checker's background test flags shadowed edges."),
        ],
        "faqs": [
            ("RRB photo ka size kitna hota hai?", "Recent cycles commonly ask around <strong>15\u201340 KB</strong> for the photograph (about 200&times;230 px) and <strong>10\u201320 KB</strong> for the signature. Bands differ per notification \u2014 verify on rrbapply.gov.in / your advertisement (source linked in the table)."),
            ("Dono files ek saath upload hoti hain?", "No \u2014 photo and signature are separate fields with separate bands. Prepare and name both files before opening the form."),
            ("Photo me date aur background ka kya rule?", "Composition rules (plain light background, no cap/glasses) are stable; any photo-age or date-statement rule is notification-specific. Read your cycle's instruction line and follow it."),
            ("Purani signature chalegi?", "As long as it is your signature and matches your records \u2014 but keep it consistent: same style across forms and verification. When in doubt, sign fresh on plain paper and re-scan."),
            ("Tool preset kaise kaam karta hai?", "The RRB preset fills a mid-band KB target and typical pixels automatically. Override any value by typing \u2014 the tool respects exact numbers you enter."),
            ("Upload se pehle check kaise karun?", "Pre-flight Checker with the RRB exam selected gives pass/fail on size, ratio, pixels, format and background with plain-language reasons \u2014 plus one-click auto-fix for images."),
        ],
        "related_tools": [("image/signature.html", "Signature Resizer"), ("image/compress.html", "Exact-KB Compressor"), ("forms/preflight.html", "Pre-flight Checker"), ("forms/specs.html", "Exam Specs Database")],
        "related_articles": [("ssc-photo-signature-size", "Photo & signature size guide"), ("file-size-too-large-error", "File size too large error fix"), ("jpg-to-pdf-guide", "Phone photos to PDF workflow")],
    }


def compress100_page(specs):
    return {
        "slug": "compress-pdf-to-100kb",
        "crumb": "Compress PDF to 100 KB",
        "title": "Compress PDF to Under 100 KB \u2014 SSC, UPSC Form Attachments | Vytra",
        "desc": "Compress a PDF to under 100 KB in your browser: target 80 KB, Extreme preset pre-set, grayscale for colour scans. Why 'file is 95KB but portal says too big' happens and how to fix it.",
        "h1": "Compress PDF to Under 100 KB",
        "h1_plain": "Compress PDF to Under 100 KB",
        "tagline": "100 KB cap wale forms ke liye \u2014 tool pre-set ke saath khulta hai, scan bhi grayscale tak.",
        "steps": ["Open tool (pre-set)", "Extreme + grayscale", "Check number, upload"],
        "top": pdf_cta(100) + pdf_target_table(100),
        "editorial": """
      <h2>Who actually asks for 100 KB</h2>
      <p>A 100 KB ceiling shows up where portals want a <strong>single scanned page</strong> as
      attachment: certificates, declarations, undertaking forms, sometimes photo-plus-declaration
      combinations. The number looks generous until you remember what phones produce \u2014 one colour
      certificate photo weighs 2\u20135 MB. Between that source and the cap sits exactly one tool
      category, and not all of them get you under <em>this</em> specific line. This page exists because
      &ldquo;compress PDF&rdquo; and &ldquo;compress PDF to 100 KB for a form&rdquo; are two very
      different jobs: the first is about quality, the second is about a number.</p>
      <h2>Aim below the line, not at it</h2>
      <p>Working rule: compress to <strong>80 KB</strong>, not 99 KB. Two counting systems are involved.
      Your file manager divides bytes by 1024 and rounds; portals often check raw byte counts (a
      &ldquo;100 KB&rdquo; cap can mean 100,000 bytes). A file showing exactly 100 KB on your side can
      measure over on theirs. Ten percent of headroom \u2014 the difference between 99 and 80 \u2014
      costs no visible quality and eliminates that entire failure class. Same logic, smaller scale, for
      the 200 KB world: <a href="../compress-pdf-to-200kb/">compress to 180 KB</a>.</p>
      <h2>PDF 100KB se kam nahi ho raha? Teen wajah, teen fix</h2>
      <p><strong>Light preset on a colour scan.</strong> Recommended preserves colour photography in
      your scan \u2014 which is precisely the weight you're fighting. Colour scans need
      <strong>Extreme + the grayscale checkbox</strong>; single text pages virtually always land in the
      80\u2013180 KB band there. <strong>Wrong tool path:</strong> image files (JPG/PNG of the document)
      need the <a href="../image/compress.html">Exact-KB Image Compressor</a> with a typed target, not
      the PDF pipeline. <strong>Too many pages:</strong> if the form wants only the certificate page,
      <a href="../pdf/split.html">extract that page</a> first \u2014 one page often clears 100 KB with
      no compression at all, and extraction beats compression by an order of magnitude.</p>
      <h2>Encrypted files fail before size even matters</h2>
      <p>Many institution-issued PDFs are password-restricted (often permissions-only). Portals reject
      those regardless of size. Remove the password from <em>your own</em> document first with
      <a href="../pdf/unlock.html">Unlock PDF</a> if it opens with just a permissions password, then
      compress. And judge everything by the tool's before/after display plus a file-manager check
      \u2014 two independent readings of the same bytes, both of which the portal will effectively
      perform.</p>
      <h2>Phone workflow, end to end</h2>
      <p>The full chain most candidates actually follow: photograph the certificate on a flat surface
      in even light (fill the frame, avoid flash glare) \u2192 open the pre-set tool above \u2192
      drop the photo or PDF \u2192 tick grayscale for colour documents \u2192 compress \u2192 read
      the reported size \u2192 download to a file named with its size (<em>Certificate_78KB.pdf</em>)
      \u2192 verify once in the file manager \u2192 upload. Five minutes the first time, two minutes
      every time after. The naming step is not decoration: during a deadline hour with twelve
      attachments, filenames are the only checklist that survives the chaos \u2014 "final",
      "final2", "final_correct" tell you nothing, "Certificate_78KB.pdf" tells you everything.</p>
      <h2>When 100 KB is genuinely not enough</h2>
      <p>Text-heavy multi-page documents compressed to 100 KB can become hard to read \u2014 and a
      legible 150 KB file is worth more than an unreadable one that passes the size gate. Read your
      instruction line carefully: some forms asking "100KB" mean it strictly for a single page, others
      are more flexible about multi-page bundles than their own wording suggests. If your document genuinely needs more room,
      re-read the requirement before mutilating the content \u2014 half the "100 KB" rejections we
      see are actually page-extraction problems wearing a size costume. Extract the one page that
      matters, compress that single page, and both problems disappear at once \u2014 no quality
      sacrificed, no cap negotiated.</p>
""",
        "errors": [
            ("File size exceeds 100 KB / attachment too large",
             "The file is over the cap \u2014 almost always a colour scan compressed with a light preset, or measured right at the boundary (99.7 KB rounds to '100' your side, over 100,000 bytes theirs).",
             "Re-compress with Extreme + grayscale, target 80 KB working margin. Open the pre-set tool above, tick grayscale, download, verify in file manager."),
            ("File could not be uploaded (size passes, upload still fails)",
             "Frequently a permissions-encrypted PDF, or an internal size check counting raw bytes differently than your file manager.",
             "Unlock the PDF first, then re-compress. Keep ~20% margin under the cap so both byte-counting conventions agree it passes."),
            ("Document rejected: pages missing / wrong content",
             "Compression wasn't the problem \u2014 the form wanted a single specific page and received a whole bundle (or vice versa).",
             "Extract the required page first (Split/Extract tool), compress the single page, then upload. Read the instruction line for 'page' vs 'document' wording."),
        ],
        "faqs": [
            ("PDF ko exactly 100KB ke under kaise karein?", "Open the pre-set tool above (Extreme loads automatically), tick the grayscale checkbox for colour scans, compress, then confirm the reported size. Aim for ~80 KB so byte-rounding cannot push you over."),
            ("Mera PDF 95KB hai phir bhi upload fail ho raha hai hai kyu?", "Byte counting: your file manager divides by 1024, portals often count 100 KB as 100,000 bytes \u2014 a '95KB' file can measure over the portal's line if it sits at the ceiling. Compress again to ~80 KB for margin."),
            ("Recommended preset se kyun nahi ho raha?", "Recommended protects colour fidelity \u2014 on colour scans that is the exact weight you're fighting. Single scanned pages need Extreme + grayscale to reach 100 KB; keep Recommended for text-born PDFs where it lands small anyway."),
            ("Grayscale se text clear rahega?", "Yes for text and stamps \u2014 grayscale removes colour channels, not detail. Signatures and seals stay legible; this is the standard move for marksheets and certificates under strict caps."),
            ("Kya mera document kahin upload hota hai?", "No \u2014 the whole pipeline runs in your browser tab. The privacy badge on the tool page counts file-upload requests in real time and stays at zero."),
            ("Photo JPG hai, PDF tool kyun nahi le raha?", "It's an image, not a PDF \u2014 use the Exact-KB Image Compressor (type 80 as your target), or convert JPG to PDF first if the portal insists on PDF."),
        ],
        "related_tools": [("pdf/compress.html", "Compress PDF"), ("image/compress.html", "Exact-KB Compressor"), ("pdf/split.html", "Split / Extract pages"), ("forms/preflight.html", "Pre-flight Checker")],
        "related_articles": [("compress-pdf-100kb", "Compress PDF under 100KB guide"), ("file-size-too-large-error", "File size too large error fix"), ("why-pdf-is-so-large", "Why your PDF is so large")],
    }


def compress200_page(specs):
    return {
        "slug": "compress-pdf-to-200kb",
        "crumb": "Compress PDF to 200 KB",
        "title": "Compress PDF to Under 200 KB \u2014 Marksheets & Certificates | Vytra",
        "desc": "Compress a PDF to under 200 KB for marksheet and certificate uploads: 180 KB working target, Extreme preset pre-set, grayscale for colour scans, bundle strategy.",
        "h1": "Compress PDF to Under 200 KB",
        "h1_plain": "Compress PDF to Under 200 KB",
        "tagline": "Marksheet/certificate 200KB caps ke liye \u2014 tool 200KB target ke saath pre-set.",
        "steps": ["Open tool (pre-set)", "Extreme + grayscale", "Aim 180 KB, verify"],
        "top": pdf_cta(200) + pdf_target_table(200),
        "editorial": """
      <h2>The 200 KB zone: single scans and small bundles</h2>
      <p>200 KB caps are the workhorse of Indian form attachments: marksheet scans, caste and income
      certificates, experience letters, two-to-four page bundles where the portal still draws one line
      in the sand. It feels like a roomy limit \u2014 until a colour marksheet arrives at 4 MB from the
      phone camera. The distance from 4 MB to 200 KB is about 95%, and it comes from two levers used
      together: <strong>pixel density</strong> (Extreme mode rasterises pages at web-appropriate
      resolution) and <strong>colour</strong> (the grayscale checkbox, which is where most of the
      remaining weight hides).</p>
      <h2>Work at 180, not 200</h2>
      <p>The same two-counting-systems problem as every cap: your file manager's &ldquo;200KB&rdquo; is
      bytes&divide;1024 rounded; the portal's 200 KB check may be 200,000 raw bytes. Files that sit on
      the ceiling fail intermittently \u2014 which is worse than failing loudly, because candidates
      re-upload the same file three times before suspecting the number itself. Compress to
      <strong>180 KB</strong> and the ambiguity disappears. The tool above opens with Extreme pre-set;
      set your attention on the grayscale checkbox for anything that was ever photographed.</p>
      <h2>Bundles: compress parts, then merge</h2>
      <p>If the form accepts one combined PDF of, say, marksheet plus certificate, sequence matters.
      Compress each document individually first (each gets its own quality pass, and one colour-heavy
      page cannot drag the others), then <a href="../pdf/merge.html">merge them</a> \u2014 merged size
      lands near the sum of the parts. Merge first, compress once, and the single heavy page decides
      everyone's fate. For forms asking <em>per-document</em> uploads, skip merging entirely and keep
      files separate and named by size (<em>Marksheet_168KB.pdf</em>).</p>
      <h2>Honest expectations</h2>
      <p>Text-born PDFs (created from Word, not scanned) shrink dramatically and stay razor sharp.
      Colour scans shrink to roughly the low-hundreds of KB with Extreme + grayscale; legibility of
      text, stamps and signatures holds at these sizes, but a heavily photographic page (a certificate
      with a large background image) has less to give. Read the tool's before/after display after each
      attempt \u2014 it reports real numbers for your file, which beat any range written on this page.
      Ranges here are typical outcomes, never promises; your file's number is the truth.</p>
      <h2>The grayscale question, answered honestly</h2>
      <p>Grayscale sounds destructive; for text documents it is close to free. A colour channel
      carries hue, not detail \u2014 a black-ink-on-white-paper scan has almost nothing in its colour
      channels except scanner noise and paper tint, both of which you want gone. Stamps and seals
      stay legible in grey (they were usually stamped in a dark ink that greyscales cleanly). The
      cases where grayscale <em>does</em> cost something: documents with colour-coded content \u2014
      a coloured table, a red "ORIGINAL" overprint, a multi-colour logo where colour carries meaning.
      For those, try Extreme without grayscale first; if the number still fails the cap, weigh
      whether the colour is information or decoration. In our experience, form-attachment scans are
      almost always the latter.</p>
      <h2>Batch day: many documents, one sitting</h2>
      <p>If you are preparing five attachments for one form, set them up like a production line:
      compress each to its own working target, name each file with its size, run each through the
      Pre-flight Checker (it flags PDF encryption and page count too, not just images), and drop the
      verified set into one folder. The mistake batch-day candidates make is mixing workflows \u2014
      resizing a photo between two PDF compressions, losing track of which file was compressed twice.
      One file type at a time, original to final, no re-compression ever. The portal's rejection
      message may be vague, but the cause is almost never mysterious: it is a number, a colour, or a
      page count.</p>
""",
        "errors": [
            ("File size larger than the permitted limit (200 KB)",
             "Colour scan compressed lightly, or the file sits exactly at the boundary where byte-counting conventions disagree (file manager says 200KB, portal counts 200,000 bytes).",
             "Extreme + grayscale to an ~180 KB working target. Verify the tool's reported size, then the file manager's reading, before re-uploading."),
            ("Combined attachment rejected / bundle too large",
             "The merged bundle's weight is the sum of its parts \u2014 merging does not compress, so three colour scans combine into one file over the cap.",
             "Compress each document separately first, then merge (merged lands near the sum of already-small parts). Or keep files separate if the form asks per-document."),
            ("Document opens blank / 'invalid PDF' after upload",
             "Portals re-parse uploads; heavily compressed colour pages can arrive where the portal's parser expects standard page structures \u2014 or the source PDF was already damaged.",
             "Re-compress from the original (not the compressed copy re-compressed); for broken sources run Repair PDF first. Avoid compressing twice in a row."),
        ],
        "faqs": [
            ("200KB wale form ke liye kitna compress karein?", "Work at <strong>180 KB</strong> \u2014 ten percent under the cap so file-manager rounding and portal byte counts both agree. The pre-set tool above loads Extreme automatically."),
            ("Marksheet ka size 200KB se kam nahi ho raha?", "Colour scans need Extreme + the grayscale checkbox together; Recommended alone usually stalls in the several-hundred-KB range because it protects colour \u2014 the exact weight you're fighting."),
            ("Do documents ko ek PDF me kaise banayein?", "Compress each first, then merge \u2014 merged size ≈ sum of the small parts. (Merge first, compress once, and the heaviest page sets the size for all of them.)"),
            ("Grayscale karne se marksheet invalid to nahi ho jayegi?", "No \u2014 grayscale changes colour channels, not content. Text, stamps and signatures remain legible; portals care about readability and size, not colour fidelity of a text document."),
            ("Kitne pages tak theek rahega?", "Single pages almost always fit; 2\u20134 page bundles fit after per-part compression. Larger bundles usually mean the form actually wanted only one page extracted \u2014 check the instruction line."),
            ("Mera file manager 198KB dikhata hai, phir bhi reject?", "The portal counts raw bytes its own way (often 1 KB = 1,000 bytes). Re-compress to ~180 KB: the margin absorbs the difference between the two counting systems."),
        ],
        "related_tools": [("pdf/compress.html", "Compress PDF"), ("pdf/merge.html", "Merge PDF"), ("pdf/split.html", "Split / Extract pages"), ("forms/preflight.html", "Pre-flight Checker")],
        "related_articles": [("compress-marksheet-under-200kb", "Marksheet under 200KB guide"), ("file-size-too-large-error", "File size too large error fix"), ("why-pdf-is-so-large", "Why your PDF is so large")],
    }


def update_sitemap(slugs):
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        s = f.read()
    add = []
    for slug in slugs:
        full = f"{SITE}/{slug}/"
        if f"<loc>{full}</loc>" not in s:
            add.append("  <url>\n"
                       f"    <loc>{full}</loc>\n"
                       f"    <lastmod>{TODAY}</lastmod>\n"
                       "    <changefreq>monthly</changefreq>\n"
                       "    <priority>0.9</priority>\n"
                       "  </url>\n")
    if add:
        s = s.replace("</urlset>", "".join(add) + "</urlset>")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
    return len(add)


def main():
    nav, footer, mega = load_shell()
    specs = load_specs()
    pages = [ssc_page(specs), ibps_page(specs), rrb_page(specs),
             compress100_page(specs), compress200_page(specs)]
    ok = True
    slugs = []
    for p in pages:
        path, words = build_page(p, nav, footer, mega, specs)
        slugs.append(p["slug"])
        flag = "OK " if words >= 600 else "LOW"
        if words < 600:
            ok = False
        print(f"  [{flag}] {p['slug']:<30} editorial {words} words")
    n = update_sitemap(slugs)
    print(f"sitemap entries added: {n}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
