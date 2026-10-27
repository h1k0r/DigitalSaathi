# -*- coding: utf-8 -*-
"""Vytra blog — BATCH 2 (staggered release).

Release structure (durable, no env vars needed to keep live posts live):
  ARTICLES_C1 — live now (published 2026-10-27)
  ARTICLES_C2 — drafts; release 2-3 per week. To release one: move it into
                ARTICLES_C1 and set its "date" to the ACTUAL publish day
                (never a planned/fake date). Do not dump all at once.
PUBLISH_BATCH2=1 publishes everything still in C2 (bulk fallback only).
Content rules: honest claims only (typical ranges, no invented test numbers),
tool CTA must point to a page that exists on the site.
"""

ARTICLES_C = [
    {
        "slug": "remove-rearrange-pages-pdf-mobile",
        "title": "How to Remove or Rearrange Pages in a PDF on Your Phone",
        "desc": "Reorder, rotate or delete pages inside a PDF from a phone browser — no app, no signup. Vytra's Organize PDF tool does it privately.",
        "excerpt": "Reorder, rotate or delete pages inside a PDF from a phone browser — no app, no signup. Vytra's Organize PDF tool does it privately.",
        "cat": "PDF Guides",
        "date": "2026-10-31",
        "body": """
<div class="highlight-box"><p><strong>Quick answer:</strong> Open the <a href="../pdf/organize.html">Organize PDF tool</a>, load the file, then drag thumbnails to reorder pages, tick the pages you don't need to delete them, rotate any sideways scan, and download. Everything runs in your phone's browser — no app install, no account, and the file never leaves the device.</p></div>

<h2>The situation: your PDF has the right document, the wrong pages</h2>
<p>You scanned your certificate together with the admit card instructions. The form asks only for the certificate — but the PDF has eighteen pages, and the certificate sits somewhere in the middle, upside down, after two blank sheets. Or: you merged three documents in the wrong order and the marksheet now comes after the Aadhaar page. On a laptop you would fix this in a desktop editor. On a phone — where most form filling actually happens these days — you need something that works in the browser, at the last minute, without installing anything.</p>
<p>That is exactly what a thumbnail organizer is for: it treats your PDF as a row of page cards you can shuffle, tick and rotate, then reassemble into a new file. No re-scanning, no re-taking photos, no losing the original.</p>

<h2>Reorder pages by dragging thumbnails</h2>
<p>Load the PDF and every page appears as a numbered thumbnail. On a phone, press and hold a thumbnail, then drag it to its new position — the others shift to make room. Typical uses:</p>
<ul>
<li><strong>Correct scan order:</strong> pages photographed out of sequence (page 3 before page 1) go back in reading order.</li>
<li><strong>Form-required order:</strong> many government attachments must appear in a fixed sequence — declaration first, then certificate, then marksheet. Drag them into that exact sequence once, download once, upload once.</li>
<li><strong>Certificate-first bundles:</strong> put the page the officer will actually look for at position one instead of page nine.</li>
</ul>
<p>Zoom in on a thumbnail if you are unsure which page is which — a tiny "12" in the corner is easy to misread at arm's length.</p>

<h2>Delete the pages the form never asked for</h2>
<p>Tick the checkboxes on pages you don't need and remove them in one pass. Instructions sheets, blank separators, the wrong document that got swept into the same scan — all gone from the exported file.</p>
<p>But pause before you delete: if the extra pages belong to <em>another</em> form and you will need them separately later, extraction is the safer move — it gives you the chosen pages as a brand-new file while keeping the original bundle untouched (see <a href="split-pdf-extract-pages.html">Split &amp; extract pages</a> for that workflow). Delete when the pages are genuinely waste; extract when they are still needed elsewhere.</p>

<h2>Rotate before you export</h2>
<p>Phone cameras love to add sideways pages to otherwise upright documents. Rotate any thumbnail that is lying on its side before downloading — a form reviewer should never have to tilt their head, and some auto-checkers complain about orientation too. Rotate, glance through the whole strip once, then export.</p>

<h2>What this tool does not do</h2>
<p>Honesty first: the organizer reorders, deletes and rotates pages. It does not compress the file (use <a href="compress-pdf-100kb.html">Extreme compression</a> if a size cap applies) and it does not recognise text in scanned images (scanned files are pictures of pages — OCR is a separate job). If your file must pass a 200KB limit, organise first, then compress — the order matters because compression should see the final page set.</p>

<h2>A workflow that works on a phone</h2>
<ul>
<li>Open the form's instruction page first and note the exact requirement: which pages, what order, any size cap.</li>
<li>Organise once: reorder, tick-delete waste, rotate, download.</li>
<li>If a size cap exists, run the organised file through compression and check the new size.</li>
<li>Open the result on the phone and swipe through every page before uploading — the check that takes fifteen seconds prevents the resubmission that costs an hour.</li>
<li>Keep the original scan safe; work only on copies.</li>
</ul>

<h2>When reordering is not enough: rebuild the bundle</h2>
<p>Sometimes the pages are right but the file is a mess of three documents scanned in one sitting. The organizer handles that too: delete everything that doesn't belong, then <a href="merge-pdfs-into-one.html">merge</a> the cleaned file with the other required documents in the prescribed order. Applications that ask for one combined attachment — declaration, certificate, marksheet, in that sequence — are assembled exactly this way: organise each part, merge once, compress once, upload once.</p>
<p>One habit prevents most rework: organise on a copy, never on the master scan. If the merged bundle turns out to be missing a page, the master still contains everything and no re-shooting is needed — you simply extract the right page from the original and merge again.</p>

<h2>Common questions</h2>
<dl>
<dt>Does organising a PDF change the original file?</dt>
<dd>No. The tool reads your file and produces a new, rearranged copy. The file on your phone is never modified.</dd>
<dt>Do pages lose quality when I reorder or rotate them?</dt>
<dd>No. Reordering copies page objects; rotation records an orientation flag. Text stays text, scanned pages stay at their original resolution.</dd>
<dt>Will it work with a 50-page scanned PDF?</dt>
<dd>Yes — scanned files are image-heavy, so thumbnails may take a few seconds to appear, but reordering works the same way.</dd>
<dt>Can I organise two PDFs in one session?</dt>
<dd>The tool works on one PDF at a time — organise each file separately, then merge the results into the final bundle. Two passes, no quality loss.</dd>
<dt>Is my document uploaded to a server?</dt>
<dd>No. The pages are processed inside your browser's memory. Close the tab and it is gone.</dd>
</dl>
""",
        "faq": [
            {"q": "Can I rearrange pages in a scanned PDF?", "a": "Yes. Scanned PDFs are pages like any other — thumbnails show each scan and you can drag, delete and rotate them freely."},
            {"q": "Does deleting pages reduce the PDF size?", "a": "Usually yes, since each removed page also removes its content — but scanned pages are heavy, so a size-limited upload may still need a compression pass afterwards."},
            {"q": "Do I need to install an app?", "a": "No. The tool runs in the browser on phones and desktops alike — nothing to install, no account to create."},
        ],
        "related": ["split-pdf-extract-pages", "compress-pdf-100kb", "jpg-to-pdf-guide", "merge-pdfs-into-one"],
        "tool": {"href": "../pdf/organize.html", "label": "Open Organize PDF"},
    },
    {
        "slug": "ibps-form-upload-errors",
        "title": "IBPS Form Upload Errors: Photo & Signature Fixes",
        "desc": "Why IBPS photo/signature uploads fail — size bands, pixel dimensions, backgrounds — and how to fix each file before the deadline.",
        "excerpt": "Why IBPS photo/signature uploads fail — size bands, pixel dimensions, backgrounds — and how to fix each file before the deadline.",
        "cat": "Govt Exam Forms",
        "date": "2026-11-02",
        "body": """
<div class="highlight-box"><p><strong>Quick answer:</strong> Most IBPS upload failures come from three causes — the file sits above the KB band, the pixel dimensions differ from the notification, or the wrong file got picked. Fix the size with <a href="../pdf/compress.html">Extreme compression</a>, re-export the photo at the exact pixel spec, and always re-read the band from the official notification on <a href="https://ibps.in" target="_blank" rel="noopener">ibps.in</a> before uploading — the numbers change between recruitments.</p></div>

<h2>The error is generic; the cause is specific</h2>
<p>IBPS forms rarely tell you <em>why</em> an upload failed. You get a one-line message — "file upload failed", "invalid file size", "image dimensions not as prescribed" — and a countdown timer. The underlying causes, however, are always one of a handful, and each has a mechanical fix you can do in a phone browser at 11 PM.</p>

<h2>Cause 1: the file is over the KB band</h2>
<p>Recruitment notifications state a band — commonly a 20–50KB window for photos and 10–20KB for signatures, with both a floor and a ceiling. Two traps live here. First, the ceiling: a phone camera photo weighs megabytes, so it must be compressed. Second, the floor: a file compressed <em>too</em> far lands under the minimum and fails just as hard. Aim for the middle of the band and verify the actual byte count in your file manager, because "45KB" as your phone rounds it may be 47,000 bytes to the portal.</p>
<p>Workflow that works: open <a href="../pdf/compress.html">Compress PDF</a> for document files, or export the photo through the converter with the quality slider set low; check the resulting size; re-export once more if it missed the band. Photos and signatures are small files — one or two passes usually land them.</p>

<h2>Cause 2: wrong pixel dimensions</h2>
<p>The band mentions pixels as well as kilobytes — a photo might be asked at roughly 200×230 pixels, a signature at a wider, shorter ratio. A file inside the KB band but at the wrong dimensions still fails. Crop to the ratio first (fill the frame with the face for photos; the signature should touch neither edge nor float in white space), then export at the specified pixel size. Cropping removes weight too, which helps the KB band on the way by.</p>

<h2>Cause 3: background and content rules</h2>
<p>Notifications specify backgrounds — commonly a plain light background for photos. Photograph the document against a white wall or white sheet in even light; avoid shadows across the face and avoid busy backgrounds. For the signature, sign on plain white paper with a dark pen, tight crop, no fingers in frame. These are content rules, not technical ones — but portals reject on them.</p>

<h2>Cause 4: the declaration file</h2>
<p>Many IBPS forms ask for a scanned declaration — a signed statement on paper — as its own upload, often as a PDF with its own size band. Photograph the declaration page flat, convert the photo to PDF with the <a href="jpg-to-pdf-guide.html">JPG-to-PDF workflow</a>, then compress the result into its band. Keep the wording exactly as the notification prescribes — declarations are checked against the required text.</p>

<h2>An error-message decoder</h2>
<p>Portal messages are vague, but they map to a short list of causes:</p>
<ul>
<li><strong>"File size exceeds the prescribed limit"</strong> — the file is over the ceiling of the KB band; compress it or re-export at lower quality.</li>
<li><strong>"File size is below the minimum"</strong> — it was over-compressed; re-export from the original with less aggressive settings.</li>
<li><strong>"Invalid image dimensions"</strong> — pixel width/height differ from the notification; crop and resize to the exact spec.</li>
<li><strong>"File format not supported"</strong> — the upload expects JPG where you have PNG, or PDF where you have a photo; convert with the matching tool.</li>
<li><strong>"Upload failed" with no reason given</strong> — often a timeout during peak deadline hours; rename the file and retry once calmly.</li>
</ul>
<p>None of these messages accuse you of anything — they are mechanical checks with mechanical fixes, each worth two calm minutes rather than ten panicked retries. Screenshot the error before retrying: if it persists, the picture is what support staff will ask for.</p>

<h2>Before you hit submit</h2>
<ul>
<li>Open each uploaded file on the phone and confirm it is the right document, right way up, legible at thumbnail size.</li>
<li>Cross-check every number against the notification PDF from ibps.in — not against a coaching-site screenshot.</li>
<li>Keep masters: original photo, original signature scan, compressed copies. You will reuse them for the next application.</li>
<li>Never alter a document's content — editing a marksheet or ageing a photo is malpractice with consequences far beyond one form.</li>
</ul>

<h2>Common questions</h2>
<dl>
<dt>Which exact KB limits does IBPS use?</dt>
<dd>They differ per recruitment and per post. Only the notification you are applying under is authoritative — read it on ibps.in, don't copy numbers from old forms or YouTube comments.</dd>
<dt>My photo is inside the band but still fails. Why?</dt>
<dd>Usually pixel dimensions or background. Check the px spec in the notification and re-export at that exact size on a plain background.</dd>
<dt>Can I compress a JPG photo?</dt>
<dd>Yes — image tools and the converter's quality slider both reduce weight; PDF compression handles signature/declaration files that must be PDFs.</dd>
<dt>Does compressing reduce legibility?</dt>
<dd>At these small file sizes, a properly cropped photo stays perfectly legible — the compression cost is invisible at thumbnail scale, which is what the portal checks.</dd>
<dt>Do the photo and signature bands differ?</dt>
<dd>Yes — they usually have different KB ranges and different pixel ratios. Read both rows of the notification's upload table separately; copying one file's treatment onto the other is a classic failure during retests.</dd>
</dl>
""",
        "faq": [
            {"q": "Why does my IBPS photo upload keep failing?", "a": "Almost always one of three reasons: the file is over the KB band, the pixel dimensions differ from the notification, or the background doesn't match the spec. Verify all three before retrying."},
            {"q": "Should I compress below the limit or stay near it?", "a": "Land in the middle of the stated band — files pushed to the extreme minimum can fail floor checks, and files a hair under the ceiling can fail byte-rounding checks."},
            {"q": "Is it safe to edit the photo background?", "a": "A plain background for the photo itself is the notification's requirement. Altering document content — marks, dates, signatures — is malpractice and never acceptable."},
        ],
        "related": ["file-size-too-large-error", "compress-marksheet-under-200kb", "jpg-to-pdf-guide", "compress-pdf-100kb"],
        "tool": {"href": "../pdf/compress.html", "label": "Open Compress PDF"},
    },
    {
        "slug": "scan-documents-mobile-upload-checks",
        "title": "How to Scan Documents With Your Phone for Uploads",
        "desc": "Phone scanning done right: lighting, angles, page framing and export settings that produce upload-ready PDFs for exam and job forms.",
        "excerpt": "Phone scanning done right: lighting, angles, page framing and export settings that produce upload-ready PDFs for exam and job forms.",
        "cat": "Govt Exam Forms",
        "date": "2026-11-05",
        "body": """
<div class="highlight-box"><p><strong>Quick answer:</strong> Shoot flat on a dark surface in bright, even light; keep the whole page in frame with a small margin; take one clear photo per page; then use the <a href="../pdf/scan-to-pdf.html">Scan to PDF tool</a> to assemble pages and <a href="../pdf/compress.html">compress</a> the result into the portal's KB band. A good scan rarely needs a second attempt — a bad one can never be rescued by compression.</p></div>

<h2>Most rejected scans fail before the upload</h2>
<p>Portals reject scans for reasons compression cannot fix: a finger over the text, a shadow across half the page, a page curled at the corner, three pages squeezed into one photo. Compression is the last step of the workflow, not the first — it can shrink a good scan, but it can only make a bad scan smaller, not better. So the shooting habits matter most.</p>

<h2>Lighting: even and indirect</h2>
<p>Window light beats the phone flash. Flash creates a hot glare spot over laminated marksheets and a hard shadow along the page edge. Stand the page near a window on a bright day, or under a broad ceiling light; make sure no shadow of your own head or hand falls across the page. Even lighting is also what keeps the background recognisably white instead of grey-blotchy.</p>

<h2>Surface and angle: flat, dark, square</h2>
<p>Lay the document on a plain dark surface — a dark folder, a tablecloth — so the white page edge is unambiguous. Kneel or stand so the camera is directly above the centre of the page, not shooting from an angle: angled shots produce trapezoids that form reviewers distrust and that waste pixels on perspective distortion. Most phone camera apps show a level guide — use it, and hold still for a beat after the focus locks.</p>

<h2>Framing: whole page, small margin</h2>
<p>Capture the entire page with a thin margin around it — enough that no text touches the frame edge, no more. Filling the frame with the document (cropping edges off) risks losing the serial number at the bottom; leaving huge margins wastes the resolution that legibility depends on. One page per photo, always — multi-page cramming is the single most common cause of unreadable scans.</p>

<h2>Assemble and compress</h2>
<p>With pages shot, open <a href="../pdf/scan-to-pdf.html">Scan to PDF</a>: it combines the photos into one PDF in page order. Check the order, rotate anything sideways, and download. Then, if the portal has a KB cap, run the file through <a href="compress-marksheet-under-200kb.html">Extreme + grayscale</a> — grayscale is legitimate for marksheets and certificates; it typically saves a large share of the weight with no legibility loss at these file sizes.</p>

<h2>Multi-page documents: shoot like a machine</h2>
<p>For a five-page certificate booklet, consistency beats brilliance. Lay page one down, frame it, shoot; turn the page in place without moving the folder or the light; shoot again. Because the surface and light stay fixed, all five photos come out with the same background tone and the same margin — the assembled PDF then looks like one scan session rather than five random snapshots, and reviewers notice that. Check the thumbnails as you go: the tool shows pages in assembly order, so a mis-ordered page is immediately visible and fixable by reordering.</p>
<p>Two small habits matter more than any setting. First, use the rear camera — it resolves text far better than the selfie lens — and wipe the lens with a cloth; pocket lint is the hidden cause of hazy, low-contrast scans. Second, tap the screen on the document's text to lock focus and exposure, and shoot in the half-second after the focus settles: blur cannot be fixed by compression, only by re-shooting, and the document may be far away by then.</p>

<h2>Verify before you upload — the 30-second audit</h2>
<ul>
<li>Open the final PDF on the phone and swipe through every page: complete page, no fingers, no shadows, correct orientation, readable at 100% zoom.</li>
<li>Check the file size in your file manager against the portal's stated cap — with a margin, because portals count bytes strictly.</li>
<li>Confirm the right file got selected — a form that accepted "marksheet.pdf" and then received "marksheet_old.pdf" is a story every submission season repeats.</li>
<li>Keep the original photos until the application is confirmed accepted; retakes are impossible after the deadline.</li>
</ul>

<h2>Common questions</h2>
<dl>
<dt>Is a phone scan accepted by exam portals?</dt>
<dd>Yes — the overwhelming majority of uploaded documents today are phone photographs, provided they are complete, legible, flat and inside the size band.</dd>
<dt>Should I use the flash?</dt>
<dd>Avoid it when possible. Flash creates glare on glossy paper and hard shadows at page edges; indirect daylight or a broad lamp gives cleaner results.</dd>
<dt>Does scanning in colour matter?</dt>
<dd>Usually not for text documents — portals care about legibility. Compressing in grayscale afterwards typically keeps text perfectly readable while cutting size.</dd>
<dt>How many megapixels do I need?</dt>
<dd>Far fewer than any modern phone has. A page shot at full resolution and then resized to a sensible dimension ends up both legible and small — excess resolution is what makes files heavy in the first place.</dd>
<dt>Should I delete blurry photos before converting?</dt>
<dd>Yes — convert only sharp, complete frames. A blurry page inside the PDF means re-shooting the document, which may not be possible later; ten seconds of judgement at shooting time beats an unusable scan at upload time.</dd>
<dt>Can I mix phone photos and old PDF files in one bundle?</dt>
<dd>Yes — the Scan to PDF tool accepts both, so an existing PDF certificate and fresh phone photos can sit together in one ordered document.</dd>
</dl>
""",
        "faq": [
            {"q": "What DPI should a phone scan be?", "a": "Phones don't shoot in DPI — they shoot in pixels. Aim for a full, square, in-focus capture of the page; the export and resize step sets the final dimensions and weight."},
            {"q": "Why do my scans look grey instead of white?", "a": "Uneven or dim lighting. Brighter indirect light fixes the background at the source; compression then preserves that whiteness better."},
            {"q": "Can I combine photos from different documents into one PDF?", "a": "Yes, if the form asks for one combined file — keep pages in the required order and name the download clearly so you know what it contains at upload time."},
        ],
        "related": ["compress-marksheet-under-200kb", "file-size-too-large-error", "documents-checklist-govt-application", "jpg-to-pdf-guide"],
        "tool": {"href": "../pdf/scan-to-pdf.html", "label": "Open Scan to PDF"},
    },
    {
        "slug": "documents-checklist-govt-application",
        "title": "Document Checklist for a Government Job Application",
        "desc": "Every certificate, scan and file-size rule a govt application typically demands — plus the digital prep workflow that prevents last-day disasters.",
        "excerpt": "Every certificate, scan and file-size rule a govt application typically demands — plus the digital prep workflow that prevents last-day disasters.",
        "cat": "Govt Exam Forms",
        "date": "2026-11-08",
        "body": """
<div class="highlight-box"><p><strong>Quick answer:</strong> Before opening any form, assemble: 10th and 12th marksheets, degree/post-graduation certificates, category certificate (if applicable), Aadhaar, a recent photo, a signature scan, and the prescribed declaration. Scan each one separately, compress per the notification's KB caps (see <a href="file-size-too-large-error.html">size-limit guide</a>), and store them in a folder named with each file's size — the notification PDF is the only authority on what exactly is required.</p></div>

<h2>Why a checklist first</h2>
<p>Application deadlines don't move, and the two things that ruin form-filling are never the form itself: it's discovering at 10:40 PM that your category certificate is at your cousin's house, and discovering that the photo you scanned last year weighs 2.8MB against a 50KB cap. Both failures are preventable with an inventory done days before, not hours.</p>

<h2>The typical document set</h2>
<p>Recruitments vary — the notification is always the authority — but the recurring core looks like this:</p>
<ul>
<li><strong>10th and 12th marksheets</strong> (date-of-birth proof and the basic qualification record).</li>
<li><strong>Graduation certificates</strong> or marksheets for graduate-level posts; a post-graduation certificate where asked.</li>
<li><strong>Category certificate</strong> — SC/ST/OBC-NCL/EWS — issued within the validity window the notification prescribes.</li>
<li><strong>Aadhaar</strong> (or the alternate ID the form accepts).</li>
<li><strong>Passport-size photograph</strong> — recent, on the prescribed background, within the KB band.</li>
<li><strong>Signature scan</strong> — signed on plain white paper, tight crop, its own KB band.</li>
<li><strong>Declaration</strong> — the exact wording the notification prescribes, signed and scanned.</li>
<li><strong>Disability or ex-serviceman documents</strong> where applicable — validity dates matter here too.</li>
</ul>

<h2>Validity dates: the quiet trap</h2>
<p>Certificates carry validity — OBC-NCL declarations are typically issued within a stated window before the application cut-off; EWS certificates too. A perfectly scanned certificate that had expired before the cut-off date is still a rejection. Read the validity clause in the notification and, if yours is stale, get a fresh one now rather than during the form window.</p>

<h2>The digital prep workflow</h2>
<ol>
<li><strong>Scan each document separately</strong> — flat, evenly lit, one page per shot (see <a href="scan-documents-mobile-upload-checks.html">the scanning guide</a>).</li>
<li><strong>Name files by content and size:</strong> <em>10th_Marksheet_112KB.pdf</em>, <em>Photo_31KB.jpg</em>. During submission hour, that naming saves the guessing that causes wrong-file uploads.</li>
<li><strong>Compress per cap:</strong> documents to each portal limit with <a href="compress-marksheet-under-200kb.html">Extreme + grayscale</a> (that link's guide covers the 100/200KB world); photos and signatures into their bands via the converter's quality control.</li>
<li><strong>Audit each file once:</strong> open it, swipe it, confirm legibility and orientation.</li>
<li><strong>Store two copies</strong> — the phone and a cloud drive or second device. Phones get lost and wiped in precisely the weeks before deadlines.</li>
</ol>

<h2>Validity windows, in plain language</h2>
<p>Every "issued within X months of the cut-off date" clause in a notification is a hard filter, not a formality. Check the issue dates on your category, income and disability certificates against the application cut-off on the day the notification appears — not on the last day of the form. Renewal offices run their own queues, and a certificate applied for during the form week frequently arrives after the document-verification stage instead.</p>

<h2>When a document is genuinely missing</h2>
<p>Panic is the wrong response; sequencing is the right one. For a missing category or income certificate, apply for issuance immediately — most are applyable online — and note the acknowledgement number. Many recruitments accept the acknowledgement at provisional submission; where they don't, you will at least know this days ahead instead of hours. For a lost marksheet, the issuing board's duplicate-copy process is the only honest path — no photocopy improvisation, no editing of anything, ever. A forged or altered paper is checked against originals at verification, and its cost is permanent.</p>

<h2>A naming convention that survives deadline hour</h2>
<p>Consistency beats cleverness: <em>DocType_Size.pdf</em> — <em>10th_Marksheet_112KB.pdf</em>, <em>CategoryCert_148KB.pdf</em>, <em>Photo_31KB.jpg</em>, <em>Signature_14KB.jpg</em>. When the upload dialog opens at 11:47 PM, the size written in the name confirms you are picking the compressed copy, not the 2.6MB master. Prefix numbers (<em>01_</em>, <em>02_</em>…) if the form wants documents in a specific upload order — the file picker sorts alphabetically, and so will your fingers.</p>

<h2>On form day</h2>
<p>Open the notification PDF first and keep it beside the form tab. Upload in the order the form asks, watch each success message, and — after payment — save the confirmation page and PDF as the permanent record. Fifteen minutes of this discipline beats any amount of last-minute compression heroics.</p>

<h2>Common questions</h2>
<dl>
<dt>Do I need original certificates at any stage?</dt>
<dd>Yes — document verification happens in person at later stages with originals. The digital copies are for the online form only.</dd>
<dt>Can one PDF contain several certificates?</dt>
<dd>When the form asks for a combined attachment, yes — <a href="merge-pdfs-into-one.html">merge in the prescribed order</a>. When it asks per-document uploads, keep them separate.</dd>
<dt>My scan is too big for every cap. What now?</dt>
<dd>Extreme preset plus grayscale, then check the size. Single text pages virtually always land well inside 100–200KB bands; the greyscale step is what gets colour scans there.</dd>
<dt>How early should prep start?</dt>
<dd>As soon as the notification is out — ideally the same week. Validity renewals and re-scans have lead times; deadlines have none.</dd>
<dt>Where should I store the scanned copies?</dt>
<dd>Two places minimum — the phone and a cloud drive or a second device. Phones get lost and wiped in precisely the weeks before deadlines, and re-scanning relatives' documents at the last moment is entirely avoidable.</dd>
<dt>Can I reuse last year's scanned set?</dt>
<dd>For unchanged documents, yes — but re-check every file's size and legibility against this year's caps, and refresh certificates whose validity windows have lapsed.</dd>
</dl>
""",
        "faq": [
            {"q": "Which documents does a govt application always need?", "a": "The recurring set is 10th and 12th marksheets, graduation proof, category certificate where applicable, Aadhaar, photo, signature and declaration — but the notification you are applying under is the only authority."},
            {"q": "How long does a category certificate stay valid?", "a": "Validity windows are prescribed per recruitment and per scheme in the notification — check the cut-off date clause rather than assuming last year's certificate still qualifies."},
            {"q": "Should scanned documents be colour or black-and-white?", "a": "Either works for legibility; compressing to grayscale usually preserves text clarity while cutting file size substantially for portals with strict caps."},
        ],
        "related": ["file-size-too-large-error", "compress-marksheet-under-200kb", "merge-pdfs-into-one", "scan-documents-mobile-upload-checks"],
        "tool": {"href": "../tools/", "label": "Open All Vytra Tools"},
    },
    {
        "slug": "word-excel-ppt-to-pdf",
        "title": "Word, Excel & PowerPoint to PDF Without Losing Format",
        "desc": "Convert DOCX, XLSX and PPTX to clean PDFs in your browser — fonts, tables and slide layouts locked exactly as designed, no software install.",
        "excerpt": "Convert DOCX, XLSX and PPTX to clean PDFs in your browser — fonts, tables and slide layouts locked exactly as designed, no software install.",
        "cat": "PDF Guides",
        "date": "2026-11-11",
        "body": """
<div class="highlight-box"><p><strong>Quick answer:</strong> Use the <a href="../pdf/word-to-pdf.html">Word to PDF</a>, <a href="../pdf/excel-to-pdf.html">Excel to PDF</a> or <a href="../pdf/powerpoint-to-pdf.html">PowerPoint to PDF</a> converter: load the file, convert in the browser, download the PDF. The layout, fonts and pagination stay exactly where the author put them — and the recipient needs no Office licence to read it.</p></div>

<h2>Why PDF is the delivery format</h2>
<p>A résumé that opens as a slightly different document on the reviewer's machine is a résumé that lost the interview slot. Word, Excel and PowerPoint files are <em>editable instructions</em> — the receiving program decides how to interpret fonts, margins, column widths and slide breaks, and every machine interprets them a little differently. A PDF is a <em>finished page</em>: what you see is byte-for-byte what the examiner, the client or the college office sees, on any device, with no licence, no font pack and no "which version is this?" phone call.</p>
<p>That is why application forms, assignments, quotations and handouts are asked as PDFs — not because the author used a paid tool, but because the format ends the conversation about formatting.</p>

<h2>Word to PDF: the document that must not shift</h2>
<p>Typical cases: résumés and CVs, project reports, application letters, assignment submissions. The conversion walks through the document's pagination and freezes each page — headers, footers, page numbers, tables and images in place. Two pre-flight checks save most trouble:</p>
<ul>
<li><strong>Accept or hide tracked changes.</strong> Conversion includes whatever is visible — comments and tracked edits ride along into the PDF if they're showing. Switch to the final view before converting a document meant for someone else's eyes.</li>
<li><strong>Embed the font choice.</strong> If the document substitutes an unusual font your machine lacks, the PDF freezes the substituted look — check the first page after converting.</li>
</ul>

<h2>Excel to PDF: tables that stop moving</h2>
<p>Spreadsheets are grids that expand to whatever screen they open on; PDFs are pages. The conversion fixes print-ready pages — which means print settings decide the result. Before converting, set the print area and scale-to-page options in the spreadsheet itself: a 40-column sheet squeezed into a portrait A4 produces an unreadable grid. Landscape orientation and a sensible scale produce a table a human can actually read. Salary sheets, budget summaries and mark-entry tables almost always benefit from this one minute of setup.</p>

<h2>PowerPoint to PDF: the handout that travels</h2>
<p>Slide decks converted to PDF keep colours, graphics and animation-free layouts intact, and they open instantly on projectors and phones alike — no font substitutions, no missing transitions, no "can you email it in a format my tablet reads". If the deck carries speaker notes you don't want to share, export the handout view instead of the full presentation. The converter preserves whatever pages the deck produces.</p>

<h2>After conversion: check, then compress if needed</h2>
<p>Open the PDF and swipe through it — this thirty-second audit catches the two realistic failure modes: a font substitution on page one, and an unexpected page break in a long table. If the file must fit a portal's KB cap (assignments and application attachments frequently carry one), run it through <a href="compress-pdf-100kb.html">Extreme compression</a> — text-heavy Office exports compress extremely well, because their weight is usually embedded images, not text.</p>

<h2>Converting from a phone</h2>
<p>The same tools work in a mobile browser — useful when the file lives in Drive, WhatsApp or an email attachment. Open the converter, load the file from the phone's storage, convert, download. The phone's "share → save to files" gesture moves a WhatsApp-received résumé into the converter's reach in two taps. For a multi-file application bundle, convert each file in one session and download them in order — the phone's download list then mirrors the order you will upload them in.</p>

<h2>Why portals insist on PDF specifically</h2>
<p>Beyond layout stability, PDFs are checkable: the text stays selectable and searchable, page counts are exact, and the file opens identically in a reviewer's browser without them installing anything. An editable DOCX invites the question "is this the final version?" — a PDF answers it. That is also why completed forms, signed declarations and fee-receipt confirmations are archived as PDFs: they are finished records, and finished records deserve a format that cannot drift.</p>
<p>A note on honesty of content: converting freezes what the document <em>says</em> — including tracked changes you forgot to accept and old figures in an unsent draft. Glance through the converted pages before sending; the format guarantees fidelity, not judgement.</p>

<h2>Common questions</h2>
<dl>
<dt>Does the conversion require Microsoft Office?</dt>
<dd>No. The files are parsed in the browser — no Office installation, no account, no subscription involved on either side.</dd>
<dt>Will images inside my document survive?</dt>
<dd>Yes — images, tables and vector graphics convert with the pages. Very image-heavy decks are simply larger PDFs, which the compression pass can address afterwards.</dd>
<dt>Are my files uploaded anywhere?</dt>
<dd>The conversion runs inside the browser tab. Your document stays on your machine — close the tab and nothing lingers anywhere.</dd>
<dt>Can I convert multiple files at once?</dt>
<dd>Yes — load several files and convert them in one run, then download each result. Converting a whole report folder takes one pass instead of five.</dd>
<dt>Can I convert a scanned PDF back into editable Word?</dt>
<dd>That is the reverse direction — OCR extraction, not conversion. Plain conversion only freezes pages exactly as they are; turning scans into editable text is a separate job for an OCR workflow.</dd>
<dt>What if the converter refuses my file?</dt>
<dd>Damaged or password-protected Office files fail conversion — remove the protection the document owner applied to your own file first, and re-download the source from email or Drive if the copy seems corrupted.</dd>
</dl>
""",
        "faq": [
            {"q": "Does Word to PDF conversion keep the exact formatting?", "a": "Yes — the conversion freezes the rendered pages: fonts, tables, headers and pagination all stay where the document placed them, and the reader needs no Office licence."},
            {"q": "Why is my Excel PDF unreadably small?", "a": "Usually print settings: a wide sheet squeezed into portrait A4. Set the print area, switch to landscape and scale to page width before converting."},
            {"q": "Can I convert a file without installing Office?", "a": "Yes — the converters run entirely in the browser, so no Microsoft Office installation or account is required on your device."},
            {"q": "Converted PDF too big for the upload cap?", "a": "Run one Extreme compression pass — Office exports are text-heavy and typically shrink dramatically with the embedded images re-encoded."},
        ],
        "related": ["compress-pdf-100kb", "merge-pdfs-into-one", "why-pdf-is-so-large", "protect-pdf-password"],
        "tool": {"href": "../pdf/word-to-pdf.html", "label": "Open Word to PDF"},
    },
]

# ---------------------------------------------------------------------------
# Staggered-release split — live set is data, not an env var, so plain
# rebuilds never unpublish an article.
ARTICLES_C1 = ARTICLES_C[:2]   # live now
ARTICLES_C2 = ARTICLES_C[2:]   # drafts: release 2-3/week, real dates only

for _a in ARTICLES_C1:
    _a["date"] = "2026-10-27"  # actual publish day (was planned 10-31 / 11-02)
