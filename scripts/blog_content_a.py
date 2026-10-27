#!/usr/bin/env python3
"""Blog article content — Batch A (articles 1-5). Imported by build_blog.py."""

ARTICLES_A = [
    {
        "slug": "compress-pdf-100kb",
        "title": "How to Compress a PDF to Under 100KB Without Losing Readability",
        "desc": "Shrink a PDF below 100KB for SSC, UPSC, IBPS and job portals — step by step, free, in your browser. Real before/after sizes, preset choice and blur fixes.",
        "cat": "PDF Guides",
        "cat_slug": "pdf-guides",
        "date": "2026-10-27",
        "excerpt": "A 4 MB marksheet PDF, a 100KB portal limit, and one hour left before the deadline? Here is the exact workflow to get under 100KB without unreadable text.",
        "tool": {"href": "../pdf/compress.html", "label": "Open Compress PDF"},
        "body": """
<p>Government exam portals, scholarship forms and job applications rarely accept a PDF bigger than 100KB or 200KB. You upload a perfectly fine-looking document, hit Submit, and get <strong>"File size exceeds the permitted limit"</strong>. Minutes before the deadline, this is the most stressful error on Indian application forms.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Open the <a href="../pdf/compress.html">Compress PDF tool</a>, drop your file, select the <strong>Extreme</strong> preset, tick the grayscale option if the document is a colour scan, and press Compress. A typical 2–4MB marksheet lands between 60KB and 150KB — comfortably under the 100KB mark.</p></div>

<h2>Why does your PDF weigh so much in the first place?</h2>
<p>Before compressing, it helps to understand where the weight comes from. Almost always it is one of these:</p>
<ul>
<li><strong>Scanned pages captured in colour.</strong> A phone scan of a marksheet stores full colour data for a page that is mostly white paper and black text. Colour scans are usually 3–8× heavier than the same page in grayscale.</li>
<li><strong>Captured at high camera resolution.</strong> Modern phones shoot 12MP photos. Embedded into a PDF, a single page can become 1–3MB on its own.</li>
<li><strong>Embedded fonts and metadata.</strong> Word and scanner apps embed complete font tables, colour profiles and hidden metadata that add weight nobody can see.</li>
<li><strong>Images inside a document.</strong> Logos, stamps, scanned signatures and photographs all add up quickly.</li>
</ul>

<h2>Step-by-step: compress any PDF below 100KB</h2>
<ol>
<li><strong>Open the tool.</strong> Go to the <a href="../pdf/compress.html">Vytra Compress PDF page</a>. Nothing installs and no account is needed — the file stays inside your browser.</li>
<li><strong>Drop your PDF</strong> into the file box. The page shows the current size so you know your starting point (for example, <em>4.2 MB</em>).</li>
<li><strong>Choose the preset.</strong> Pick <strong>Extreme</strong> when a portal has a hard 100KB or 200KB limit. Stick with <strong>Recommended</strong> if you only need a lighter file for email or WhatsApp.</li>
<li><strong>For scanned documents, tick "Convert scanned marksheets to grayscale".</strong> This is the single biggest size lever for scans — it drops the colour channels while keeping text crisp.</li>
<li><strong>Name the output and press Compress PDF Now.</strong> Download the result and check the size before uploading to the portal.</li>
</ol>

<div class="highlight-box"><p><strong>What to expect:</strong> A colour phone scan of a single certificate usually starts between <strong>2 and 4MB</strong>. With Extreme + grayscale, single pages commonly land in the <strong>90–150KB</strong> band — comfortably under a 100KB or 200KB limit. Light presets alone rarely cross that finish line on colour scans. The tool displays your exact before/after sizes — always judge by that number, not by estimates.</p></div>

<h2>Which preset should you actually pick?</h2>
<ul>
<li><strong>Recommended</strong> — best balance of size and readability; start here for 95% of documents (emails, sharing, general uploads).</li>
<li><strong>Extreme</strong> — smallest possible file for hard portal limits. Be honest about the trade-off: Extreme rasterises pages, which means <strong>text becomes an image</strong> — it can no longer be selected, searched or copy-pasted. For exam uploads nobody reads text digitally, so this is usually fine.</li>
<li><strong>Low</strong> — light compression that strips metadata while keeping image fidelity. Use it when the file is slightly over a generous limit (say, 2MB) and quality matters most.</li>
<li><strong>Grayscale checkbox</strong> — always combine with Extreme for scans, photographs of documents, and marksheet bundles.</li>
</ul>

<h2>Common problems and quick fixes</h2>
<h3>"The output is still above 100KB"</h3>
<p>Check how many pages the PDF has. A 15-page document has far more image data than a single-page certificate. Options: split out only the pages the portal asks for (the <a href="split-pdf-extract-pages.html">Split PDF guide</a> explains how), then compress that smaller file. Also confirm you actually selected Extreme — Recommended will not always cross the finish line.</p>
<h3>"The text looks blurry after compressing"</h3>
<p>Blur after compression means the preset went too aggressive for that particular file. Two fixes: switch to <strong>Recommended</strong> if the limit allows a slightly larger file, or re-scan the document at 150–200 DPI in grayscale first. A clean grayscale scan usually compresses small <em>and</em> stays sharp — blurry results almost always start as low-quality, over-compressed camera photos.</p>
<h3>"The portal still rejects the file"</h3>
<p>Some portals check more than size — page count, PDF version, or whether the PDF has a password. Confirm the limit is really about kilobytes, and make sure the file is not password-protected (portals cannot open encrypted PDFs; the <a href="protect-pdf-password.html">password guide</a> covers what to do).</p>

<h2>Pro tips</h2>
<ul>
<li>Always compress <strong>before</strong> the last day of registration — you want time to verify readability.</li>
<li>Check the final size in your phone's file manager before uploading; don't trust your memory of the limit.</li>
<li>Keep the original large PDF safe. You will need it for later rounds, counselling and document verification.</li>
<li>One document, one file: portals usually reject a bundle that mixes several certificates unless the notification says otherwise.</li>
<li>For repeated forms, compress once and reuse the file across applications that share the same 100KB rule.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Is compressing a PDF for an exam form allowed?</dt>
<dd>Yes. Portals publish size limits precisely because they expect you to compress or rescan documents to fit them. You are not altering the document's content — only its file size.</dd>
<dt>Will Extreme compression make my text unreadable?</dt>
<dd>On documents with clean, high-contrast scans, text stays perfectly readable to the eye — but it becomes an image, so selection and search stop working. If the portal limit allows, Recommended keeps text selectable.</dd>
<dt>Do I need to install any software?</dt>
<dd>No. The compression runs entirely in your browser. Your file is not uploaded to any server, which matters for marksheets, certificates and ID proofs.</dd>
<dt>How many PDFs can I compress at once?</dt>
<dd>Compress each document separately when a portal asks for individual uploads — that also gives you per-file control over the final size.</dd>
</dl>
""",
        "faq": [
            {"q": "Is compressing a PDF for an exam form allowed?",
             "a": "Yes — portals publish size limits precisely because they expect you to compress documents to fit them. You are only changing file size, not content."},
            {"q": "Does Extreme compression make text unreadable?",
             "a": "Text stays visually readable but becomes an image (no selection or search). If the limit allows, Recommended keeps text selectable."},
            {"q": "Do I need to install software?",
             "a": "No. Compression runs in your browser and the file never leaves your device."},
            {"q": "My output is still over the limit. What now?",
             "a": "Split out only the required pages, select the Extreme preset, and enable grayscale for scanned documents."},
        ],
        "related": ["split-pdf-extract-pages", "compress-marksheet-under-200kb", "file-size-too-large-error"],
    },
    {
        "slug": "merge-pdfs-into-one",
        "title": "How to Merge Multiple PDFs Into One (Free, in Your Browser)",
        "desc": "Combine marksheet, certificate and ID PDFs into a single file for online applications — free, no software, no uploads. Order control and quality notes included.",
        "cat": "PDF Guides",
        "cat_slug": "pdf-guides",
        "date": "2026-10-27",
        "excerpt": "Application forms often want ONE PDF containing marksheet + certificate + ID. Here is how to merge them in the right order without losing quality — free and private.",
        "tool": {"href": "../pdf/merge.html", "label": "Open Merge PDF"},
        "body": """
<p>Most online applications — university admissions, government exams, scholarships, tender submissions — ask for <strong>one single PDF</strong> containing your marksheet, certificate, category proof and ID. Uploading four separate files gets you a rejection; merging them into one bundle is the fix.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Open the <a href="../pdf/merge.html">Merge PDF tool</a>, drop every file you need, drag them into the order the form asks for (usually marksheet first, ID last), press Merge, and download one combined PDF — no software, no upload, free.</p></div>

<h2>Before you merge: get the order right</h2>
<p>Examiners and admission officers scan bundles in a fixed sequence, and many notifications spell out an order. A sensible default used across Indian application forms:</p>
<ol>
<li>Application acknowledgement / Aadhaar-linked form page</li>
<li>10th / matriculation marksheet</li>
<li>12th / inter marksheet</li>
<li>Degree or diploma certificates</li>
<li>Category / caste certificate (if applicable)</li>
<li>Photo ID proof</li>
</ol>
<p>Reordering a merged file means redoing the merge — so arrange the sequence <em>before</em> you press the button. The tool lets you drag files into position in the grid.</p>

<h2>Step-by-step: merge your PDFs</h2>
<ol>
<li>Open the <a href="../pdf/merge.html">Merge PDF tool</a> in any browser — desktop or phone.</li>
<li><strong>Drop all your PDFs at once</strong> (hold Ctrl/Cmd while selecting, or pick multiple files on mobile). Each file appears as a card with its size and page count.</li>
<li><strong>Arrange the order</strong> by dragging the cards. Read the order above — or the exact order from your exam notification.</li>
<li>Press <strong>Merge</strong>. The combined file is built inside your browser, typically in a second or two for documents under 50 pages.</li>
<li>Download the result and <strong>rename it</strong> to something formal: <em>Documents_ShivamKumar.pdf</em>, not <em>merged_final_v3.pdf</em>.</li>
</ol>

<div class="highlight-box"><p><strong>What to expect:</strong> Merged size ≈ sum of the parts — a bundle of four documents weighing 210KB, 240KB, 180KB and 95KB lands around <strong>700–730KB</strong> as one file. Merging takes seconds and copies pages structurally: the originals are never modified, and page order is preserved exactly as arranged. Judge the result by the size the tool reports after merging.</p></div>

<h2>Does merging reduce quality?</h2>
<p>No — merging is a <strong>structural operation</strong>, not a re-encoding. Text, vectors and fonts are copied page-for-page, so page 1 of your marksheet after merging is byte-equivalent in quality to the original. Two exceptions worth knowing:</p>
<ul>
<li><strong>File size:</strong> the merged file is roughly the sum of the parts (minus a little shared overhead). If the bundle crosses a portal's size limit, compress it afterwards with the <a href="compress-pdf-100kb.html">100KB compression workflow</a>.</li>
<li><strong>Mixed page sizes:</strong> if one document is A4 and another is a smaller scan, all pages keep their own size inside the merged PDF. Most portals accept this; if yours insists on uniform A4, note it and we will cover the resize path in a future guide.</li>
</ul>

<h2>Merging on a phone (the cyber-café workflow)</h2>
<p>Most form-filling happens on phones now, and merging works the same way there: open the tool in Chrome, tap the file box, choose Browse, then long-press to multi-select documents from Files or Downloads. Arrange the cards by dragging, merge, and verify page order before leaving the page. One mobile-specific warning: phones with "storage optimisation" (iPhone's Files app, some Android galleries) keep a smaller placeholder locally while the full file lives in the cloud — if the merge fails or the sizes look wrong, make the originals available offline first and retry. And while verifying the result, raise screen brightness: phone screens hide faint scans and light-grey seals that a monitor shows clearly.</p>
<p>The phone route has one advantage of its own: your camera captures documents directly, so a common café pattern is scan → convert (JPG to PDF) → merge → compress, all in one session on one device without a single file leaving it. That end-to-end flow assembles the complete document bundle for most applications in under five minutes.</p>

<h2>Common mistakes</h2>
<ul>
<li><strong>Merging in the wrong order.</strong> The most common redo. Arrange before merging; there is no "swap pages" shortcut without splitting again.</li>
<li><strong>Merging password-protected PDFs.</strong> Protected files cannot be merged until unlocked. Remove the password first (see the <a href="protect-pdf-password.html">password guide</a> for what is legitimate — your own documents, always).</li>
<li><strong>One giant bundle instead of what the form asked for.</strong> Some forms want separate uploads for photo and signature. Merge only what the instruction says to merge.</li>
<li><strong>Forgetting a document.</strong> Download and open the final file once, page by page, before submitting. A missing certificate discovered after submission is a much bigger problem.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Compress <em>after</em> merging, not before — one compression pass on the final bundle gives a smaller total than compressing each file separately.</li>
<li>Keep a "master bundle" updated as you add new certificates; clone it per application.</li>
<li>Check the merged page count against the sum of the individual files — it takes five seconds and catches ordering bugs instantly.</li>
<li>For email submissions under 1MB, merge first, then use the Recommended compression preset.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Is there a limit to how many PDFs I can merge?</dt>
<dd>Practical limits come from your device's memory, not the tool. Bundles of 20–30 files merge fine in a normal browser.</dd>
<dt>Can I merge files from different devices?</dt>
<dd>Yes — the files do not travel anywhere, so as long as all documents are on the device you are using, they can be merged regardless of where they originally came from.</dd>
<dt>Will the merged PDF work on phones and cyber-café systems?</dt>
<dd>Yes. The output is a standard PDF that opens in any PDF reader, including older readers installed on café systems.</dd>
<dt>What if I merged the wrong order?</dt>
<dd>Simply re-merge with the correct arrangement — the original files are never modified, so nothing is lost by repeating the process.</dd>
</dl>
""",
        "faq": [
            {"q": "Is there a limit to how many PDFs I can merge?",
             "a": "Only your device's memory matters — normal bundles of 20–30 files merge fine."},
            {"q": "Does merging reduce document quality?",
             "a": "No. Merging copies pages structurally; text and images keep their original quality."},
            {"q": "Can I merge scanned images (JPG) along with PDFs?",
             "a": "Convert the images to PDF first with JPG to PDF, then merge the results — combining raw images directly with PDFs is not supported."},
            {"q": "What if I merged files in the wrong order?",
             "a": "Re-merge with the correct arrangement — original files are never changed."},
            {"q": "Merged file is over the portal limit — what now?",
             "a": "Compress the final bundle once using the Extreme preset; see our 100KB compression guide."},
        ],
        "related": ["compress-pdf-100kb", "split-pdf-extract-pages", "protect-pdf-password"],
    },
    {
        "slug": "ssc-photo-signature-size",
        "title": "SSC Form Photo and Signature Size: Limits, Pixels and How to Get Them Right",
        "desc": "Photo KB range, signature KB range, pixel dimensions and common rejection reasons for SSC and similar exam forms — plus the free workflow to hit the limits exactly.",
        "cat": "Govt Exam Forms",
        "cat_slug": "govt-exam-forms",
        "date": "2026-10-27",
        "excerpt": "SSC forms reject more candidates on photo/signature specs than on anything else. KB ranges, pixel sizes, formats and the exact workflow to get it right the first time.",
        "tool": {"href": "../image/resize.html", "label": "Open Photo Resizer"},
        "body": """
<p>"Photo signature size galat hai." If there is one error that stalls SSC and allied exam applications more than any other, it is the photograph and signature upload. The rules are strict — a minimum <em>and</em> maximum file size, pixel dimensions, background colour, and a file format — and the portal validates every single one of them before letting you proceed.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Your exam's <strong>official notification PDF</strong> is the only source of truth for exact numbers. Recent SSC cycles have typically asked for a passport photo roughly in the <strong>20–50KB</strong> range and a signature roughly in the <strong>10–20KB</strong> range, as JPG, on a white background, with specific pixel dimensions. Read the limit from your notification, check your file's current size, then resize and convert in the browser.</p></div>

<div class="highlight-box" style="border-left:4px solid #E5322D;"><p><strong>Important:</strong> Size limits and pixel dimensions change between exams and even between years. Always verify the exact numbers in the official notification on <a href="https://ssc.nic.in" target="_blank" rel="noopener">ssc.nic.in</a> (or your exam body's site) — this guide teaches the method, the notification gives the numbers.</p></div>

<h2>The four rules the portal actually checks</h2>
<ol>
<li><strong>File size range.</strong> Not "under 100KB" — a <em>range</em>. A 5KB photo is rejected as too small just like a 90KB one is rejected as too large, because too-small files are usually blurry thumbnails. Aim for the middle of the range.</li>
<li><strong>Pixel dimensions.</strong> The photo's width × height in pixels matters as much as its KB. A common passport-photo size family is around 200×230 pixels, but your notification may specify something else.</li>
<li><strong>Format.</strong> Photos are usually <strong>JPG</strong>; signatures are <strong>JPG</strong> too. A PNG or a PDF will be rejected by uploaders expecting JPG.</li>
<li><strong>Background and framing.</strong> Plain white or light background, face clearly visible, no selfies with filters. Signatures must be on white paper, shot straight, without extra surrounding space.</li>
</ol>

<h2>Check what your current files look like to the portal</h2>
<ul>
<li><strong>Size in KB:</strong> on Windows, right-click → Properties → Size. On Android, long-press the file → Details. On iPhone, open the photo in Files and check info. The portal sees the same number you do.</li>
<li><strong>Dimensions:</strong> open the image in any viewer that shows properties, or upload the file to a photo app and check "image size". If your viewer says 3024×4032, that is a full-resolution camera photo — nowhere near a form-spec file.</li>
</ul>

<h2>The free browser workflow to hit the spec exactly</h2>
<ol>
<li><strong>Crop first, resize second.</strong> Crop the photo to the required aspect (passport framing) — cropping after resizing distorts the face.</li>
<li><strong>Resize to the exact pixel dimensions</strong> your notification asks for. This does most of the size reduction automatically.</li>
<li><strong>Export as JPG</strong> with white background. Keep the quality high enough that the face is sharp — this is the one image you do not want artefacts on.</li>
<li><strong>Check the KB again.</strong> Still over the range? Lower JPG quality one step at a time (90 → 85 → 80) and re-check after each change. You are hunting for the value that lands inside the range while the face still looks clean.</li>
<li><strong>For signatures:</strong> photograph or scan the signature on plain white paper, crop tight to the signature (but keep a small margin), resize to the specified dimensions, and export JPG. Signatures compress hard — they will comfortably fit typical limits.</li>
<li><strong>If the portal asks for a combined PDF</strong> (photo + signature in one file), build it with <a href="../pdf/jpg-to-pdf.html">JPG to PDF</a> and then compress with the <a href="compress-pdf-100kb.html">Extreme preset</a>.</li>
</ol>

<div class="highlight-box"><p><strong>What to expect:</strong> Camera photos start huge — a full-resolution phone photo is commonly 1–4MB at 3000+ pixels. Cropping to passport framing and resizing to the notification's pixel spec removes most of that weight; exported at 85% JPG quality, such photos typically land in the <strong>20–60KB</strong> band, and signatures (white paper, tight crop) rarely exceed <strong>10–25KB</strong>. The number that matters is what your file manager shows on the final export — check it every time.</p></div>

<h2>Why photos get rejected (and the fixes)</h2>
<ul>
<li><strong>"File size not in range"</strong> — you are either under the minimum (too-small = blurry file) or over the maximum. Re-export at a different JPG quality; do not just keep compressing blindly.</li>
<li><strong>"Dimensions not as specified"</strong> — resize to exact pixels. Note: a file inside the KB range can still have wrong dimensions.</li>
<li><strong>Blurry or cropped face</strong> — caused by downscaling an already-soft photo. Crop first, and if the source photo itself is soft, retake it in good light rather than upscaling.</li>
<li><strong>Background not white</strong> — the classic home-photo problem. Stand against a plain wall, or use a background-replacement feature in your phone's gallery editor before resizing.</li>
<li><strong>Signature spanning extra space</strong> — tight crop, but not so tight that the last stroke is cut off. Check the preview the portal shows after upload.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Make ONE perfect master photo and reuse it across SSC, IBPS, RRB and state forms — only the KB/px target changes.</li>
<li>Keep masters in a folder named with their spec: <em>SSC_photo_31KB_200x230.jpg</em>.</li>
<li>Upload from a computer when possible — the portal's live preview is easier to verify on a big screen.</li>
<li>Take a screenshot of the successful upload confirmation. Servers crash during deadline hours.</li>
<li>Never share your photograph and signature scans publicly (WhatsApp groups, forums) — they are enough for identity misuse.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>My photo is inside the KB range but still rejected. Why?</dt>
<dd>Most often pixel dimensions, format (PNG instead of JPG), or background. The error message usually names the exact check that failed.</dd>
<dt>Can I use the same photo for signature upload?</dt>
<dd>No — the signature slot needs an image of your signature. Portals verify them as separate files with separate specs.</dd>
<dt>Does the portal count file size in KB or bytes?</dt>
<dd>It uses bytes internally; the KB you see is the same number divided by 1024. Trust what your file manager shows.</dd>
<dt>Is a scanned hardcopy signature better than a digital one?</dt>
<dd>Either works if it meets the spec. Many candidates photograph a signature made with black ink on white paper — that matches what examiners expect to see later.</dd>
</dl>
""",
        "faq": [
            {"q": "Why is my photo rejected even though it is inside the KB range?",
             "a": "Usually pixel dimensions, the wrong file format (PNG vs JPG), or a non-white background — the error message names the failed check."},
            {"q": "Where do I find the exact size limits?",
             "a": "In your exam's official notification PDF (ssc.nic.in and similar sites). Limits change between exams and years."},
            {"q": "Can I reuse one photo across SSC, IBPS and RRB forms?",
             "a": "Yes — create one clean master meeting the strictest spec you have seen, then re-export to each form's exact range."},
            {"q": "Do signature files need a white background?",
             "a": "Typically yes: black ink on plain white paper, cropped tight, exported as JPG within the stated size range."},
        ],
        "related": ["compress-marksheet-under-200kb", "jpg-to-pdf-guide", "file-size-too-large-error"],
    },
    {
        "slug": "compress-marksheet-under-200kb",
        "title": "How to Compress a Marksheet PDF to Under 200KB for Government Portals",
        "desc": "Colour scan to under 200KB in under a minute — Extreme preset + grayscale, real before/after sizes, and how to keep marks and seals readable.",
        "cat": "Govt Exam Forms",
        "cat_slug": "govt-exam-forms",
        "date": "2026-10-27",
        "excerpt": "Marksheets are the heaviest documents in any application bundle — colour paper, stamps and seals. Here is how to reliably get them under 200KB or 100KB.",
        "tool": {"href": "../pdf/compress.html", "label": "Open Compress PDF"},
        "body": """
<p>A marksheet is the worst-case document for file size: full-page colour scans, rubber stamps, holographic seals, and off-white paper that refuses to compress like clean white text. Government portals — scholarships, admissions, exam forms — routinely cap such documents at <strong>200KB or even 100KB</strong>, and a colour scan of a single marksheet can easily weigh 2–5MB.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> In the <a href="../pdf/compress.html">Compress PDF tool</a>, select the <strong>Extreme</strong> preset and enable <strong>"Convert scanned marksheets to grayscale"</strong>. That combination is built for exactly this job: a 3MB colour scan typically lands at 80–180KB — under the 200KB line with a readable result. Always confirm the exact cap in your exam's official notification (<a href="https://ssc.nic.in" target="_blank" rel="noopener">ssc.nic.in</a>, <a href="https://upsc.gov.in" target="_blank" rel="noopener">upsc.gov.in</a>, <a href="https://ibps.in" target="_blank" rel="noopener">ibps.in</a>).</p></div>

<h2>Why marksheets resist compression</h2>
<ul>
<li><strong>Colour data everywhere.</strong> Even "white" paper carries warm tones and scanner noise; colour data triples the image weight of every page.</li>
<li><strong>Stamps and seals.</strong> Red and blue inks, holograms and guilloché patterns are high-frequency detail that encoders must preserve.</li>
<li><strong>Camera photos instead of scans.</strong> Photographs of marksheets bring shadows, perspective distortion and megapixels of unnecessary resolution.</li>
<li><strong>High default DPI.</strong> Scanners defaulting to 300–600 DPI produce huge pages that no portal needs — 150–200 DPI is plenty for reading marks and grades.</li>
</ul>

<h2>Step-by-step: get under 200KB</h2>
<ol>
<li>Open the <a href="../pdf/compress.html">Compress PDF tool</a> and drop your marksheet PDF. Note the starting size shown next to the file.</li>
<li>Select the <strong>Extreme</strong> preset — it is designed for hard portal limits like 100KB/200KB.</li>
<li>Tick <strong>"Convert scanned marksheets to grayscale"</strong>. Grayscale removes the colour channel that dominates scan weight while keeping text and seals visible in shades of grey.</li>
<li>Press <strong>Compress PDF Now</strong> and check the result size.</li>
<li>Under 200KB? Open the file and inspect it: every mark, the seal, the roll number and your name must be clearly legible. If it missed the limit, run it once more — or split multi-page bundles first (see below).</li>
</ol>

<div class="highlight-box"><p><strong>What to expect:</strong> Colour scans of a single marksheet typically start at <strong>2–5MB</strong>. Extreme + grayscale usually lands them around <strong>80–180KB</strong> — under most 100KB/200KB caps. With Recommended alone, colour scans often stall in the several-hundred-KB range, because light compression cannot undo a full-colour capture — which is exactly why the grayscale checkbox exists.</p></div>

<h2>Multi-document bundles: compress smart, not hard</h2>
<p>When one PDF contains four certificates and the limit is 200KB total, compression alone may not save you. In that case:</p>
<ul>
<li><strong>Split</strong> the bundle into individual documents (the <a href="split-pdf-extract-pages.html">Split PDF guide</a> covers page ranges) if the portal allows separate uploads — per-file limits are easier to satisfy.</li>
<li>If it must stay one file, <strong>compress the bundle once as a whole</strong> with Extreme + grayscale. Fewer pixels per page (grayscale + downsampling) matters more than page count.</li>
<li>As a last resort, <strong>re-scan at 150 DPI grayscale</strong> yourself and compress again. A fresh 150 DPI scan often starts at 300–400KB instead of 3MB.</li>
</ul>

<h2>When the form specifically demands colour</h2>
<p>Some notifications ask for a "colour copy of the marksheet". In that case leave the grayscale checkbox off and lean on the Extreme preset alone — image downsampling still delivers the biggest cut, just without the colour-channel saving. If you land a few kilobytes over the limit, try re-scanning at 150 DPI in colour instead of a higher resolution: lower-resolution colour scans frequently fit where full-resolution ones fail, and stamps keep their colour. Where the instruction says only "legible copy" — as most do — grayscale remains fair game, because portals regulate size and format, not colour.</p>

<h2>Common problems</h2>
<h3>"Under the limit but text is hard to read"</h3>
<p>Blur at small sizes usually traces back to a poor source photo — shaky camera, small text, shadows. Fix the source: scan or photograph straight-on, in even light, at 150–200 DPI. Then compress. Do not try to recover a bad source by choosing a gentler preset and blowing the size limit.</p>
<h3>"The seal disappeared / turned dark"</h3>
<p>Grayscale keeps seals visible, but a very light pastel seal can lose contrast. Check the preview carefully. If a seal genuinely becomes illegible, leave grayscale off for that one document and accept a slightly larger file — then meet the limit by splitting the bundle instead.</p>
<h3>"Portal says size limit exceeded but my file is under 200KB"</h3>
<p>Check the units. 200KB ≠ 200,000 bytes in some portals (they compare against 204,800 bytes; others against 200,000). Also re-check whether the limit applies to the PDF only or to each attachment. When close to the boundary, aim ~10% under to be safe.</p>

<h2>Pro tips</h2>
<ul>
<li>Scan once, archive right: immediately after receiving a marksheet, scan it at 200 DPI and save both colour and grayscale versions — you will use them for years.</li>
<li>Name files by content and size: <em>10th_Marksheet_112KB.pdf</em> — you will thank yourself during the final submission scramble.</li>
<li>Verify readability on a phone screen, not just a 24-inch monitor — that is how most officers will view it.</li>
<li>Keep the original high-resolution scan somewhere safe; portals sometimes ask for "clear colour copies" in later rounds.</li>
<li>Certificates with gold foils photograph badly — use diffuse light (near a window, not flash) to avoid glare before scanning.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Is grayscale acceptable for official document uploads?</dt>
<dd>Yes — portals specify size and format, not colour. Marksheets in grayscale remain fully valid documents, and many notifications explicitly accept black-and-white copies.</dd>
<dt>Should I compress before or after merging documents?</dt>
<dd>After. One compression pass on the final bundle produces a smaller total than compressing each file separately.</dd>
<dt>Extreme turned my text into an image — is that a problem?</dt>
<dd>Not for portal uploads: officers read the rendered page, they do not search inside it. Keep a selectable-text version for your own records.</dd>
<dt>Can I compress a password-protected marksheet PDF?</dt>
<dd>Remove the password first (banks and institutions sometimes deliver PDFs protected). If it is your own document, unlocking it is fine — see the password guide.</dd>
</dl>
""",
        "faq": [
            {"q": "Is grayscale acceptable for official uploads?",
             "a": "Yes — portals regulate size and format, not colour, and grayscale scans stay fully legible."},
            {"q": "Should I compress before or after merging?",
             "a": "After merging — one pass over the final bundle yields the smallest total size."},
            {"q": "What starting size should I expect from a phone scan?",
             "a": "Phone photographs commonly start at 2–5MB per page; Extreme + grayscale typically lands single pages at 80–180KB."},
            {"q": "My portal rejected a file that was under the limit — why?",
             "a": "Re-check KB vs bytes counting, whether the limit covers all attachments, and whether the PDF is password-protected."},
        ],
        "related": ["compress-pdf-100kb", "file-size-too-large-error", "split-pdf-extract-pages"],
    },
    {
        "slug": "file-size-too-large-error",
        "title": "\"File Size Too Large\" Error on Exam Portals: Causes and Fixes",
        "desc": "Why the upload keeps failing even when the file 'looks small' — KB vs bytes, hidden weight, and a reliable fix order that works on SSC, UPSC, IBPS portals.",
        "cat": "Govt Exam Forms",
        "cat_slug": "govt-exam-forms",
        "date": "2026-10-27",
        "excerpt": "You are sure the file is small — the portal disagrees. The real causes of 'file size too large' on Indian exam portals, ranked, with a fix order that works.",
        "tool": {"href": "../pdf/compress.html", "label": "Open Compress PDF"},
        "body": """
<p>You pick the file, hit Upload, and the form throws back: <strong>"File size is larger than the permitted limit"</strong> or <strong>"Invalid file size"</strong>. You check — the file is 180KB, the limit is 200KB. It still fails. During deadline hours, this single error costs candidates real time.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Almost every "size too large" failure comes down to one of four things: the limit is smaller than you remember, KB is being counted differently, the file has hidden weight you cannot see (colour scan, embedded fonts, extra pages), or the portal is checking something else (format/password) and reporting size generically. Fix in order: re-read the limit → check the real size → compress with Extreme → check format and password.</p></div>

<h2>Cause 1: the limit is not where you think it is</h2>
<p>Notifications state limits per document type — photograph, signature, marksheet, acknowledgement — and they differ. A form may allow 200KB for marksheets but only 50KB for photos, or cap the <em>total</em> of all uploads. Re-open the notification (or the instruction line right above the upload field) and read the number the portal is actually enforcing for THAT field. Note: near-boundary files also fail — if the limit is 200KB and your file is 199KB, you are inside tolerance but leaving nothing for portals that count 1 KB = 1,000 bytes instead of 1,024.</p>

<h2>Cause 2: KB counted two ways</h2>
<p>Your file manager says 200KB; the portal counts bytes. Tools that count in "decimal KB" treat 200KB as 200,000 bytes, while "binary KB" means 204,800 bytes. A file at 203,000 bytes passes one check and fails the other. <strong>Rule of thumb: stay 10% under any limit.</strong> A "200KB" target should mean 180KB or less in your file manager.</p>

<h2>Cause 3: hidden weight inside the PDF</h2>
<ul>
<li><strong>Colour scan of a mostly-white page</strong> — the most common offender; grayscale alone can cut 40–70%.</li>
<li><strong>Full camera resolution</strong> — 12MP photos embedded as pages. Downsampling to 150–200 DPI drops this dramatically.</li>
<li><strong>Extra pages you forgot about</strong> — scanned bundles often carry blank back-sides, covers, or duplicate pages. Check the page count.</li>
<li><strong>Embedded fonts and metadata</strong> — Word/scanner exports embed complete font tables; compression strips the unused parts.</li>
<li><strong>Attachments inside the PDF</strong> — PDFs can embed files (a spreadsheet inside a form PDF adds its full size). Rare but shocking when it happens.</li>
</ul>

<h2>Cause 4: it is not really about size</h2>
<p>Some portals show a size-related message when the actual problem is:</p>
<ul>
<li><strong>Wrong format:</strong> .jpeg vs .jpg usually fine, but .png where JPG is demanded, or a PDF where an image is demanded.</li>
<li><strong>Password-protected PDF:</strong> the portal cannot parse it, so the upload validation fails — sometimes with a misleading error.</li>
<li><strong>Renamed extensions:</strong> a JPEG renamed to <em>.pdf</em> passes the filename check and then fails content validation. Export genuinely, do not rename.</li>
<li><strong>Browser upload limits:</strong> outdated browsers or flaky extensions occasionally mangle uploads near the limit — try another browser before blaming the file.</li>
</ul>

<h2>Different portals, different strictness</h2>
<p>Every portal enforces a little differently, and knowing the pattern prevents surprises. Some validate size client-side — the error is instant, the moment you pick the file. Others check after upload: the error arrives seconds later, so wait for it before re-selecting the file. A few display the limit in MB in the instructions but report failure in KB; some cap each attachment individually, others cap the total of everything you attach. The 10%-under-margin rule works across all of them. When a form states no limit anywhere in text, tap or hover the file input itself — the hint is usually baked into the field — and check it before your first upload attempt.</p>

<h2>The reliable fix order (do these top to bottom)</h2>
<ol>
<li><strong>Re-read the exact limit</strong> for that specific field in the notification or the form's instruction line — official sources: <a href="https://ssc.nic.in" target="_blank" rel="noopener">ssc.nic.in</a>, <a href="https://upsc.gov.in" target="_blank" rel="noopener">upsc.gov.in</a> and <a href="https://ibps.in" target="_blank" rel="noopener">ibps.in</a>.</li>
<li><strong>Check the true size</strong> in file properties — and take 10% off the limit as your target.</li>
<li><strong>Open the <a href="../pdf/compress.html">Compress PDF tool</a>, pick Extreme, tick grayscale for scans, compress.</strong> Single pages land well under strict limits; see the <a href="compress-marksheet-under-200kb.html">marksheet workflow</a> for real numbers.</li>
<li><strong>Still too big?</strong> Split out only the required pages (the <a href="split-pdf-extract-pages.html">split guide</a> shows how) and compress again.</li>
<li><strong>Verify format and password.</strong> Correct extension, no encryption, correct image type for photos/signatures.</li>
<li><strong>Retry in another browser</strong> if everything above passes — and do this well before the deadline, not in the last ten minutes.</li>
</ol>

<div class="highlight-box"><p><strong>What to expect:</strong> A classic near-boundary failure: a file your file manager rounds to "200KB" can still measure over the portal's byte-level cap — "200KB" as 200,000 bytes and "200KB" as 204,800 bytes are two different targets. The fix is arithmetic, not luck: compress to roughly <strong>10% below</strong> the stated limit (a "200KB" target becomes ~180KB) and that entire category of failures disappears. The content never changes — only the byte count.</p></div>

<h2>Pro tips</h2>
<ul>
<li>Set a personal rule: target 90% of any stated limit. It eliminates this entire category of failures.</li>
<li>Screenshot every successful upload (confirmation message + file name).</li>
<li>Keep three versions of every document: original scan (colour, high-res), portal-ready (compressed), and an all-purpose mid-size copy.</li>
<li>Test uploads during off-peak hours — some portals corrupt uploads under load and return generic errors.</li>
<li>Never zip files to "fix" size errors — portals read the raw file, not your archive.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>The file is clearly under the limit but upload fails. Why?</dt>
<dd>Check how the portal counts KB (decimal vs binary), whether the limit applies per-file or total, and whether the real issue is format or password protection.</dd>
<dt>Does compressing change my document's content?</dt>
<dd>No — compression reduces how the same pages are stored. Text, marks and seals remain exactly as they are.</dd>
<dt>Why does the Extreme preset make text unselectable?</dt>
<dd>Extreme rasterises pages — text is rendered as an image. That is the size-for-selectability trade-off; it does not affect visual reading.</dd>
<dt>Which file should I compress: photo, signature or marksheet?</dt>
<dd>Whichever one fails the check. Each field has its own limit — fix the specific field the error points at.</dd>
</dl>
""",
        "faq": [
            {"q": "Why does the portal reject a file that is under the limit?",
             "a": "Portals count KB differently (1,000 vs 1,024 bytes), may apply per-file vs total limits, or may really be failing on format/password."},
            {"q": "Does compressing alter my document?",
             "a": "No — only the file's storage size changes; marks, text and seals stay identical."},
            {"q": "What if splitting is not allowed by the form?",
             "a": "Compress the whole document with Extreme + grayscale; for bundles, re-scan at 150 DPI grayscale as a last resort."},
            {"q": "Is renaming a file's extension a valid fix?",
             "a": "No — portals validate file content. Convert properly (PDF stays PDF, images stay JPG) instead of renaming."},
        ],
        "related": ["compress-pdf-100kb", "compress-marksheet-under-200kb", "split-pdf-extract-pages"],
    },
]
