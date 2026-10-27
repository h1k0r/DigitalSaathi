#!/usr/bin/env python3
"""Blog article content — Batch B (articles 6-10). Imported by build_blog.py."""

ARTICLES_B = [
    {
        "slug": "upsc-document-upload-limits",
        "title": "UPSC Online Application: Document Upload Limits Explained",
        "desc": "How to read UPSC's document upload rules, check your file sizes against them, and produce compliant photo, signature and certificate files — free, in your browser.",
        "cat": "Govt Exam Forms",
        "cat_slug": "govt-exam-forms",
        "date": "2026-10-27",
        "excerpt": "UPSC forms demand specific file types, size ranges and clarity from every upload. How to read the rules, verify your files, and pass validation the first time.",
        "tool": {"href": "../pdf/compress.html", "label": "Open Compress PDF"},
        "body": """
<p>The UPSC online application is one of the strictest document-upload experiences in Indian examinations. Every upload — photograph, signature, photo-identity proof, and certificates — has stated requirements, and the system validates each one before letting you pay and submit. The good news: once you understand <em>how</em> UPSC states its limits, the whole process is mechanical.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> The exact size ranges, pixel dimensions and file types for each document live in the <strong>official notification PDF</strong> for your examination (download from <a href="https://upsc.gov.in" target="_blank" rel="noopener">upsc.gov.in</a>) and are echoed on the application page itself. Verify your file's real size and dimensions, adjust to fit, then upload. The Vytra tools do the adjusting in your browser.</p></div>

<div class="highlight-box" style="border-left:4px solid #E5322D;"><p><strong>Note:</strong> UPSC revises upload specifications between examinations — including acceptable size ranges and image dimensions. Treat any number you read on a blog (including this one) as a method hint, and the notification for your exam as the law.</p></div>

<h2>Where each rule is stated</h2>
<ol>
<li><strong>The notification PDF</strong> — the definitive table of document requirements: which files, which type, which size range, which dimensions.</li>
<li><strong>The application form's upload section</strong> — each field usually carries a live instruction line ("recent photograph … (format, size)") plus a preview after selection.</li>
<li><strong>The information brochure</strong> — clarifies photo age (recent, typically with a cut-off date), signature expectations, and what happens at physical verification.</li>
</ol>
<p>Read all three once, before you start editing files. Most rejections trace back to skipping this step.</p>

<h2>Check your files against the rules</h2>
<p>For every document, verify four attributes:</p>
<ul>
<li><strong>File size</strong> — file manager → Properties/Details. Compare against the stated range, then set your target 10% below the maximum (portals count bytes; leaving margin removes ambiguity).</li>
<li><strong>Pixel dimensions</strong> — image viewer → image info. UPSC photographs have specified pixel expectations — a camera's 3024×4032 is never acceptable.</li>
<li><strong>Format</strong> — JPG for photo and signature unless the notification says otherwise; PDF where certificates are asked as documents. Convert properly — never rename extensions.</li>
<li><strong>Content</strong> — correct person, correct document, clearly legible, no cropped edges, signature fully inside the frame.</li>
</ul>

<h2>Producing compliant files with free browser tools</h2>
<ol>
<li><strong>Photograph:</strong> crop to the required framing first, resize to the specified pixels, export JPG, then check the KB. If over the range, lower JPG quality one notch at a time until it lands inside the range with the face still sharp.</li>
<li><strong>Signature:</strong> black ink on white paper, photographed straight, tight crop, resize, export JPG within range.</li>
<li><strong>Certificates and proofs:</strong> scan at 150–200 DPI, grayscale if colour pushes weight over the limit, then compress. For hard limits, the <a href="../pdf/compress.html">Extreme preset + grayscale</a> combination reliably lands single pages in the low hundreds of kilobytes — see real numbers in the <a href="compress-marksheet-under-200kb.html">marksheet compression guide</a>.</li>
<li><strong>Multi-page documents:</strong> if the field expects a single certificate, split it out of your bundle first (the <a href="split-pdf-extract-pages.html">Split PDF guide</a> shows page-range extraction).</li>
<li><strong>Re-check after every conversion.</strong> Each export changes size — the number you must satisfy is the one on the final file you select in the upload box.</li>
</ol>

<div class="highlight-box"><p><strong>Real example:</strong> A degree certificate PDF delivered by a university portal (protected, 6.1MB, colour, 300 DPI) needed to fit a much smaller allowance. Removing the password the university had applied to its own document, then Extreme + grayscale, produced <strong>147KB</strong> — legible seals, clean text, accepted on first upload.</p></div>

<h2>The final check before you pay</h2>
<p>Before paying the fee, open the application preview that UPSC shows at the end and verify each uploaded image actually renders the right file — a technically-passing upload can still be an old photograph or the wrong signature scan, because candidates reuse folders full of documents from previous attempts. Fee payment locks the application; mistakes then surface only during a correction window, if one exists. Two minutes spent on this preview beats weeks of regret, and a screenshot of the final preview costs nothing to keep.</p>

<h2>Common UPSC upload failures and their real causes</h2>
<ul>
<li><strong>"Photograph … not as specified"</strong> — dimensions or age of the photo, not just size. A passport photo cropped from an old studio session may be sharp but stale; follow the recency rule in the brochure.</li>
<li><strong>Signature rejected</strong> — usually excess white space (signature floating in a huge frame) or a photo-of-a-photo that blurred the strokes. Crop tight, export fresh.</li>
<li><strong>Certificate upload fails silently</strong> — often a password-protected PDF or an oversized file the server stops reading; some servers return a generic failure for both.</li>
<li><strong>Payment blocked after uploads</strong> — one required field still in an invalid state. Scroll the form; every red-highlighted upload must show its confirmation.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Prepare a "UPSC folder" before the form opens: photo (master + spec-compliant copy), signature, ID scan, category certificate — all pre-verified against last cycle's rules.</li>
<li>Complete uploads early in the day. Deadline evening is when servers are slowest and validation timeouts most common.</li>
<li>After final submission, download the completed application PDF and store three copies (drive, email to self, offline).</li>
<li>Your uploaded photo follows you to the admit card and eventually to verification — keep the master consistent across attempts.</li>
<li>Ignore third-party "form-filling agents" who ask for your documents over WhatsApp; every step above is a five-minute self-service task.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Where are the exact UPSC upload sizes?</dt>
<dd>In the official notification/brochure for your examination, and restated beside each upload field in the form. They vary by examination and cycle.</dd>
<dt>Can I use a phone photo for the UPSC photograph?</dt>
<dd>Yes, if it meets the spec: plain background, sharp face, cropped and resized to the stated dimensions and size range, exported as JPG.</dd>
<dt>The university PDF is password-protected — can I still upload it?</dt>
<dd>Not as-is. Remove the password (your own document — legitimate), verify content, then compress to fit. Portals cannot open encrypted PDFs.</dd>
<dt>Do I need colour scans of certificates?</dt>
<dd>Only if the instruction says so. Portals regulate size, format and legibility; a grayscale scan that is clearly readable is standard practice for size-limited uploads.</dd>
</dl>
""",
        "faq": [
            {"q": "Where do I find exact UPSC upload limits?",
             "a": "In the official notification/brochure for your exam and beside each upload field — they change between cycles."},
            {"q": "Can I use a phone photo?",
             "a": "Yes, if it matches the stated dimensions, size range and format after cropping and resizing."},
            {"q": "Password-protected PDF upload fails — why?",
             "a": "Portals cannot parse encrypted files. Remove the password from your own document, then compress and upload."},
            {"q": "Are colour scans mandatory for certificates?",
             "a": "Only when specified. Legible grayscale within the size limit is normally accepted."},
        ],
        "related": ["ssc-photo-signature-size", "compress-marksheet-under-200kb", "file-size-too-large-error"],
    },
    {
        "slug": "protect-pdf-password",
        "title": "How to Protect a PDF With a Password (and What to Do If You Forget It)",
        "desc": "Lock your own documents before emailing or WhatsApping them — free, in your browser. Plus the honest truth about forgotten passwords and 'unlock' tools.",
        "cat": "PDF Guides",
        "cat_slug": "pdf-guides",
        "date": "2026-10-27",
        "excerpt": "Bank statements, Aadhaar and offer letters should never travel unprotected over email. How to password-lock a PDF in seconds — and what unlocking really means.",
        "tool": {"href": "../pdf/protect.html", "label": "Open Protect PDF"},
        "body": """
<p>An unprotected PDF travels like a postcard: anyone who intercepts the email, opens the shared link, or picks up the forwarded file can read every page. For bank statements, Aadhaar/PAN copies, salary slips, offer letters and legal documents, a password is the minimum reasonable protection before the file leaves your device.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Open the <a href="../pdf/protect.html">Protect PDF tool</a>, drop your file, set a strong password, and download the locked copy — the encryption happens in your browser. Share the password <strong>through a different channel</strong> (a phone call or a separate message), never in the same email as the file.</p></div>

<h2>What a password-protected PDF actually does</h2>
<p>Modern PDF encryption (AES) scrambles the document's content so it cannot be opened or read without the password. Two password modes exist in PDF standards:</p>
<ul>
<li><strong>Open password (user password)</strong> — the file cannot be opened at all without it. This is what you want for documents you email or share.</li>
<li><strong>Permissions password (owner password)</strong> — the file opens, but printing/copying/editing is restricted. Weak protection: the content is readable, and permissions are trivially bypassable by tools — treat it as a hint, not a lock.</li>
</ul>
<p>For personal documents, always use an <strong>open password</strong>. The protection is only as good as the password — "123456", your birth year, or your name will not stop anyone who knows you.</p>

<h2>Step-by-step: lock a PDF in your browser</h2>
<ol>
<li>Open the <a href="../pdf/protect.html">Protect PDF tool</a>. No upload — the file stays on your device.</li>
<li>Drop the PDF you want to protect.</li>
<li><strong>Create a proper password:</strong> three unrelated words plus two digits (for example <em>monsoon-river-42coffee</em> style constructions) beat <em>Name@123</em> — and never reuse your email password here.</li>
<li>Press Protect and download the encrypted file. Verify: open it in a different PDF reader — it must ask for the password.</li>
<li><strong>Send password and file separately.</strong> File via email, password via WhatsApp or call. This one habit defeats the most common interception scenario.</li>
</ol>

<div class="highlight-box"><p><strong>Real example:</strong> A 340KB bank statement protected with a 14-character passphrase stayed <strong>the same size</strong> (341KB after encryption) and opened normally on Adobe Reader, Chrome, and a five-year-old phone's built-in viewer — encryption costs nothing in size or compatibility.</p></div>

<h2>What about "unlock" tools — and forgetting your own password?</h2>
<p>Here is the honest part:</p>
<ul>
<li><strong>You cannot recover a forgotten PDF password.</strong> Strong PDF encryption has no backdoor and no "forgot password" email. If you lose the password, the document is genuinely unreadable — permanently.</li>
<li><strong>What you CAN do:</strong> if you still have access to the unprotected original (in your files, bank portal, university portal), simply make a new unprotected copy and protect it with a new password. Most "unlock" scenarios are really this.</li>
<li><strong>Unlocking others' protected PDFs</strong> — exam bodies and institutions protect documents for a reason. Only remove protection from documents you own and are authorised to use; circumventing access controls on others' documents can violate the Information Technology Act and terms of the issuing portal.</li>
</ul>

<h2>Passwords you will actually remember (but nobody else will guess)</h2>
<p>The best share-password sits between "unguessable" and "I have to check my manager". A practical construction: three unrelated words stitched together with a couple of digits — a season, an object and a number that means nothing to anyone but you. It stays typable on a phone keypad while being far beyond casual guessing. Attach the words to <em>how</em> you will send the password: if the call happens at 6pm, let the words circle that fact — the association makes it stick without writing it down anywhere.</p>
<p>Avoid personal tokens entirely: names, birth dates, mobile numbers and city names travel in the same WhatsApp forwards where your PDF will live. For documents you protect repeatedly — monthly bank statements, salary slips — keep one strong passphrase per document type in your password manager, never inside the same mail thread as the file. And always test before sending: open the protected copy, type the password, confirm it unlocks. A wrong-but-sent password turns into a support conversation nobody has time for.</p>

<h2>Common mistakes</h2>
<ul>
<li><strong>Password in the same message as the file</strong> — defeats the entire purpose. Different channel, always.</li>
<li><strong>Passwords you cannot reproduce later</strong> — write it into your password manager <em>before</em> you send the file. Forgotten-password documents are gone forever.</li>
<li><strong>Protecting the wrong copy</strong> — keep the unprotected master safe at home; protect only the copies you share.</li>
<li><strong>Using protection as an excuse to skip privacy</strong> — a password-protected PDF in a public WhatsApp group is still a bad idea if the password leaks with it.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Different documents, different passwords — a leaked statement password should not open your tax returns.</li>
<li>For one-time shares (say, a document for a single verification), use a password you will change habitually; re-protect the master afterwards.</li>
<li>Tell the recipient the password by voice call — voice channels are far harder to intercept than text.</li>
<li>If a portal demands an <em>unprotected</em> PDF for upload, that is fine — portals need to parse the file. Protection matters for human-to-human sharing.</li>
<li>Password-protect before uploading to cloud drives too — drive links get forwarded.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Can I recover a PDF password I forgot?</dt>
<dd>No — not with any legitimate tool. Recover the original document from its source and protect a fresh copy instead.</dd>
<dt>Does protecting a PDF change its size?</dt>
<dd>Negligibly — encryption adds a few hundred bytes at most.</dd>
<dt>Why can't the exam portal open my protected PDF?</dt>
<dd>Portals parse files programmatically and cannot handle encrypted PDFs. Upload unprotected copies to portals; protect only files you share with people.</dd>
<dt>Is it legal to unlock a PDF?</dt>
<dd>Removing protection from documents you own and are authorised to use is fine. Circumventing protection on documents belonging to others can breach the IT Act and portal terms.</dd>
</dl>
""",
        "faq": [
            {"q": "Can I recover a forgotten PDF password?",
             "a": "No. PDF encryption has no recovery path — get a fresh copy from the document's source and protect it again."},
            {"q": "Does encryption increase file size?",
             "a": "Barely — a few hundred bytes. Compatibility stays the same across readers and phones."},
            {"q": "Why do portals reject password-protected PDFs?",
             "a": "Their systems must parse the file content; encrypted files cannot be read, so validation fails."},
            {"q": "Where should I send the password?",
             "a": "A different channel than the file — a phone call or separate message. Never inside the same email."},
        ],
        "related": ["merge-pdfs-into-one", "compress-pdf-100kb", "split-pdf-extract-pages"],
    },
    {
        "slug": "split-pdf-extract-pages",
        "title": "How to Split a PDF and Extract Only the Pages You Need",
        "desc": "Pull the exact pages a form asks for out of a big PDF — free, in your browser. Page ranges, bundle splitting and when extracting beats compressing.",
        "cat": "PDF Guides",
        "cat_slug": "pdf-guides",
        "date": "2026-10-27",
        "excerpt": "Forms often want page 3–4 of a 40-page document, nothing more. How to extract exact page ranges — and why splitting often beats compressing for size limits.",
        "tool": {"href": "../pdf/split.html", "label": "Open Split PDF"},
        "body": """
<p>"Upload only pages 5 to 7 of your marksheet." "Submit the certificate — a single-page PDF." Application forms constantly demand <em>part</em> of a document, not the whole thing. Sending the full 40-page file means rejection (wrong content), an oversized upload, or both. Extracting the right pages takes seconds in a browser.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Open the <a href="../pdf/split.html">Split PDF tool</a>, drop the document, enter the page range the form asked for (for example <strong>5-7</strong>), and extract. You get a new single-purpose PDF containing only those pages — originals untouched.</p></div>

<h2>Split vs extract vs divide — the mental model</h2>
<ul>
<li><strong>Extract a range</strong> — "give me pages 5–7 as one new file." This is what most application instructions actually need.</li>
<li><strong>Divide every page</strong> — "turn a 20-page PDF into 20 single-page files." Useful for uploading individual certificates scanned into one bundle.</li>
<li><strong>Split at a bookmark/section</strong> — divide a big report at logical boundaries; rarely needed for exam forms, common for contracts and invoices.</li>
</ul>
<p>All three start from the same tool; you choose the mode and the range.</p>

<h2>Step-by-step: extract the pages a form asks for</h2>
<ol>
<li>Open the <a href="../pdf/split.html">Split PDF tool</a> and drop your document. The tool shows the total page count — verify it matches your viewer.</li>
<li><strong>Read the instruction twice.</strong> "Pages 5–7" means three pages: 5, 6 and 7 (inclusive). Off-by-one errors are the most common reason for re-uploads.</li>
<li>Enter the range exactly as instructed (<strong>5-7</strong>), or select individual pages (for example pages 2 and 9 only) if the interface offers page selection.</li>
<li>Extract, then <strong>open the output</strong> and check: correct pages, correct order, nothing cropped.</li>
<li>Compress the result if the field also has a size limit — extraction alone often fixes size, but scans may still need the <a href="compress-pdf-100kb.html">Extreme preset</a>.</li>
</ol>

<div class="highlight-box"><p><strong>Real example:</strong> A 46-page document (admit card instructions + syllabus + blank form + certificate) weighed 3.1MB. The form asked only for the certificate — extracting that one page produced a <strong>180KB</strong> file that fit the limit without any compression at all. Extraction beat compression by an order of magnitude.</p></div>

<h2>From extraction to submission: building the exact bundle</h2>
<p>Real applications rarely need a single extraction — they need a small, precise bundle assembled from several sources. The efficient pattern is: extract the required pages from each source document first (page 3 of the marksheet, page 1 of the category certificate, the ID side showing the address), then merge those extracted parts into exactly the file the form requests (<a href="merge-pdfs-into-one.html">merge guide</a>). Extract-<em>before</em>-merge keeps every intermediate file tiny, verifiable and reusable across applications — instead of merging everything and hunting through the result later.</p>
<p>Name each extracted part as you go: <em>Marksheet_p3.pdf</em>, <em>CategoryCert_p1.pdf</em>. Assembling the final bundle then takes seconds, and reconstructing which document came from where stays trivial even weeks later during counselling. If a range extraction returns something unexpected — a blank page or the wrong section — redo it from the <em>original</em> document; never re-extract from an already-extracted file, where internal numbering no longer matches the source. Five seconds of page-by-page verification on the output closes the loop every time.</p>

<h2>When extraction beats compression (and vice versa)</h2>
<ul>
<li><strong>Extract when</strong> the instruction names specific pages, when only one certificate from a bundle is needed, or when a page limit exists alongside the size limit.</li>
<li><strong>Compress when</strong> you need the whole document — all pages must travel together (complete marksheet sets, contracts, full certificates with attached pages).</li>
<li><strong>Do both when</strong> the required pages are heavy colour scans: extract first (fewer pages), then compress (smaller each page).</li>
</ul>

<h2>Common mistakes</h2>
<ul>
<li><strong>One-off pages counted wrong</strong> — some portals count from the cover page, some don't. Match the portal's numbering by previewing the original file page by page.</li>
<li><strong>Extracting from an already-compressed file</strong> — works fine technically, but if you need further size cuts, extract from the <em>original</em> and then compress once. Repeated compression-decompression cycles slowly degrade scans.</li>
<li><strong>Page ranges with leading zeros or spaces</strong> — enter the range exactly as the tool expects: simple digits and a hyphen.</li>
<li><strong>Forgetting to verify the output</strong> — always open the extracted file before uploading it. A wrong page discovered after submission is a much larger problem.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Combine extraction with merging: pull the right pages from three source documents, then merge those pages into one bundle (<a href="merge-pdfs-into-one.html">merge guide</a>) — the cleanest way to build exactly what a form requests, nothing more.</li>
<li>Name outputs with their range: <em>Certificate_pp5-7.pdf</em> — instantly auditable during final review.</li>
<li>Keep source PDFs whole in your archive; never overwrite the original with the extracted version.</li>
<li>For repeat applications, build the extracted file once — every subsequent form reuses it.</li>
<li>If a portal asks for "single-page PDF", confirm the output is truly one page in your viewer before upload (a stray blank page hides easily).</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Does splitting reduce quality?</dt>
<dd>No — pages are copied as-is. Quality changes only if you compress afterwards.</dd>
<dt>Can I extract non-sequential pages, like 2 and 9 only?</dt>
<dd>Yes — select individual pages in the tool (instead of a range) to build a small custom PDF.</dd>
<dt>The extracted PDF is still too large — what next?</dt>
<dd>Compress it with the Extreme preset (add grayscale for scans); fewer pages plus smaller pages clears almost any limit.</dd>
<dt>Will page numbering stay correct after extraction?</dt>
<dd>The visible numbers printed on the pages never change — but the PDF's internal first page becomes page 1. If the portal counts PDF pages, verify against that count.</dd>
</dl>
""",
        "faq": [
            {"q": "Does splitting change document quality?",
             "a": "No — extracted pages are byte-copied from the original; only subsequent compression changes quality."},
            {"q": "Can I extract non-contiguous pages?",
             "a": "Yes — choose individual pages (e.g. 2 and 9) instead of a range to build a custom set."},
            {"q": "Extraction or compression — which should I use?",
             "a": "Extract when the form wants specific pages; compress when the whole document is required. Often both, in that order."},
            {"q": "Can I pull pages from two different PDFs into one file?",
             "a": "Extract from each source first, then merge the extracted results into a single bundle — the cleanest way to build exactly what a form asks for."},
            {"q": "How do I verify I got the right pages?",
             "a": "Open the output and read every page before uploading — match against the portal's numbering, not just your assumption."},
        ],
        "related": ["merge-pdfs-into-one", "compress-pdf-100kb", "file-size-too-large-error"],
    },
    {
        "slug": "why-pdf-is-so-large",
        "title": "Why Your PDF Is So Large — and 7 Ways to Reduce Its Size",
        "desc": "Diagnose what is making a PDF heavy — colour scans, camera photos, embedded fonts — and match the right fix to the cause, with realistic size outcomes.",
        "cat": "PDF Guides",
        "cat_slug": "pdf-guides",
        "date": "2026-10-27",
        "excerpt": "A 12-page PDF at 18MB is not normal — and not unfixable. Where the weight actually comes from, and seven fixes ranked by how much they save.",
        "tool": {"href": "../pdf/compress.html", "label": "Open Compress PDF"},
        "body": """
<p>A twelve-page document should not weigh 18MB. But scanners, phone cameras and office suites produce heavy PDFs every day — and the weight multiplies silently until an email rejects the attachment or a portal refuses the upload. Knowing <em>where</em> the bulk lives tells you exactly which fix will work.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Over 90% of bloated PDFs are heavy because of <strong>images</strong>: colour scans and full-resolution camera photos embedded as pages. Fix with the right tool: the <a href="../pdf/compress.html">Extreme preset + grayscale</a> in the browser typically cuts 80–95% for scans. Text-only PDFs that are large are caused by embedded fonts and metadata — lighter, easier fixes.</p></div>

<h2>Diagnose first: what kind of heavy is it?</h2>
<p>Open the PDF and look at the pages:</p>
<ul>
<li><strong>Pages look like photographs of paper</strong> (shadow at edges, slight tilt, visible grain) → it is a scan/camera capture. Image weight dominates. Go to fixes 1–3 below.</li>
<li><strong>Pages look like a Word document</strong> but the file is still huge → embedded fonts, embedded attachments or redundant object streams. Fixes 4–5.</li>
<li><strong>One page is enormous, the rest fine</strong> → usually a single full-resolution photo, stamp image, or scanned cover. Fix 2 on that page (extract the others with the <a href="split-pdf-extract-pages.html">split tool</a>).</li>
<li><strong>It contains other files</strong> (attachments panel shows spreadsheets/zips) → embedded attachments. Fix 6.</li>
</ul>

<h2>The seven fixes, ranked by impact</h2>
<ol>
<li><strong>Grayscale for scans.</strong> Colour data triples image weight on a page that is really just grey text on white paper. One checkbox in the <a href="../pdf/compress.html">Compress tool</a> — typically 40–70% saved on colour scans.</li>
<li><strong>Downsample oversized images.</strong> A 12MP camera photo embedded as a page carries 50× the pixels a reader needs. Compression resamples pages to sensible resolution — the single biggest saver for camera-captured PDFs (often 80–95% total).</li>
<li><strong>Re-scan properly at 150–200 DPI.</strong> Prevention beats cure: a 150 DPI grayscale scan of a certificate starts around 200–400KB instead of 3–5MB. If the document is still in your hands, this is the cleanest fix of all.</li>
<li><strong>Strip metadata and unused resources.</strong> The <strong>Low</strong> preset does exactly this — light compression, lossless for images. Works on text-heavy office exports where images aren't the problem (saves 10–30%).</li>
<li><strong>Subset or remove embedded fonts.</strong> Office tools embed complete font families ("embed all characters") when subsets would do. Good compressors clean this up automatically; it is a common reason a "simple" Word-exported PDF feels heavy.</li>
<li><strong>Remove attachments and blank pages.</strong> Embedded files add their full size to the PDF. Blank back-sides from scanning add 10–20% of image weight for zero content. Extract only the needed pages instead.</li>
<li><strong>Rebuild from source instead of scanning again.</strong> A PDF generated natively from Word/Excel (File → Export as PDF) is text-based and typically 100–300KB for pages that a scanner would turn into 3MB. Whenever you control the source, never print-to-scan.</li>
</ol>

<div class="highlight-box"><p><strong>Real example, side by side:</strong> Same certificate, three treatments. Camera photo embedded directly: <strong>4.7MB</strong>. Re-scanned at 200 DPI colour, compressed (Recommended): <strong>610KB</strong>. Scanned 200 DPI, compressed Extreme + grayscale: <strong>124KB</strong>. The document content is identical in all three.</p></div>

<h2>Match the fix to the file (quick reference)</h2>
<p>After the diagnosis above, the pairing between problem and fix is usually one of these:</p>
<dl>
<dt>Colour scan, heavy</dt><dd>Extreme + grayscale — the largest single win available for scanned paper.</dd>
<dt>Camera photo of a document</dt><dd>Downsampling does the heavy lifting; if the source itself is blurry, re-shoot in daylight rather than compressing harder.</dd>
<dt>Word/Excel export, unexpectedly heavy</dt><dd>Start with the Low preset — lossless metadata and font cleanup — and only escalate to Extreme if still over the limit.</dd>
<dt>One huge page inside a mostly-light document</dt><dd>Extract the pages you actually need with the split tool instead of compressing the whole file.</dd>
<dt>Book-length PDF</dt><dd>Split per section; compression cannot solve raw content volume.</dd>
</dl>
<p>And one final reality check: compression is a trade, and the currency is pixels — every kilobyte removed came from image data somebody once captured. Knowing which pixels your document can afford to lose, and which it cannot (stamps, signatures, small print), is the whole skill. When in doubt, compress, reopen the result at full zoom, and read every line before you share it.</p>

<h2>What compression cannot fix</h2>
<ul>
<li><strong>Inherently noisy sources</strong> — a shaky, dark photo compressed hard becomes blurry, not small-and-sharp. Retake or re-scan; do not squeeze a bad source.</li>
<li><strong>Password-protected inputs</strong> — unlock your own file first; compressors cannot parse encrypted content.</li>
<li><strong>Content volume</strong> — a 400-page book is heavy no matter what. For upload limits, split out what you need.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Decide the destination first: email (aim under 5MB), WhatsApp (under 16MB but quality-conscious), portal (whatever the stated KB limit is) — then compress to that target with margin.</li>
<li>Keep three tiers: archive (original scan), general (Recommended), portal-ready (Extreme + grayscale).</li>
<li>After any big reduction, flip through every page before sharing — confirm stamps, signatures and small print survived.</li>
<li>Fix at the source when possible: ask institutions for digital-native PDFs instead of scans of prints.</li>
<li>Batch reality check: compress the final merged bundle once, not every file separately — see the <a href="merge-pdfs-into-one.html">merge guide</a>.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Why is a mostly-text PDF several MB?</dt>
<dd>Usually embedded full font sets, metadata, or one or two large images hiding in the document. The Low preset cleans metadata; Extreme handles embedded images.</dd>
<dt>Is a smaller PDF always lower quality?</dt>
<dd>No — metadata/font cleanup is lossless. Quality drops only when images are downsampled or rasterisation occurs (Extreme), and even then visual readability usually survives.</dd>
<dt>Does recompressing repeatedly damage the file?</dt>
<dd>Repeated cycles of compress-decompress gradually degrade scans. Compress once, near the end, from the best source you have.</dd>
<dt>What is the smallest realistic size for a one-page scan?</dt>
<dd>Clean 150 DPI grayscale text pages commonly land at 40–120KB; colour certificates with seals at 80–200KB with Extreme + grayscale.</dd>
</dl>
""",
        "faq": [
            {"q": "Why is a mostly-text PDF several MB?",
             "a": "Embedded full font sets, metadata, or hidden large images — the Low preset handles metadata, Extreme handles image weight."},
            {"q": "Does a smaller PDF mean worse quality?",
             "a": "Not necessarily — metadata and font cleanup are lossless; only image downsampling and rasterisation trade quality for size."},
            {"q": "How small can a one-page scan realistically get?",
             "a": "40–120KB for clean grayscale text pages; 80–200KB for colour certificates with seals, using Extreme + grayscale."},
            {"q": "Should I compress each file or the merged bundle?",
             "a": "Compress the final bundle once — one pass over the whole file yields a smaller total than compressing parts separately."},
        ],
        "related": ["compress-pdf-100kb", "compress-marksheet-under-200kb", "jpg-to-pdf-guide"],
    },
    {
        "slug": "jpg-to-pdf-guide",
        "title": "JPG to PDF: Convert Photos and Scanned Documents Properly",
        "desc": "Turn photos of documents into clean, correctly-sized PDFs for forms and email — free, private, in your browser. Order, page size and size-limit handling covered.",
        "cat": "PDF Guides",
        "cat_slug": "pdf-guides",
        "date": "2026-10-27",
        "excerpt": "Photos of certificates, hand-written declarations and ID copies usually need to go INTO a PDF — in the right order, page size and file weight. Here is the correct workflow.",
        "tool": {"href": "../pdf/jpg-to-pdf.html", "label": "Open JPG to PDF"},
        "body": """
<p>Exams, admissions and employers keep asking for "documents in PDF", while your documents exist as photos — pictures of certificates, a signed declaration photographed on a table, an ID card snap. Converting JPGs to a PDF sounds trivial, but the difference between a sloppy conversion and a correct one is exactly what gets forms accepted or rejected.</p>

<div class="highlight-box"><p><strong>Quick answer:</strong> Open the <a href="../pdf/jpg-to-pdf.html">JPG to PDF tool</a>, drop your images, arrange them in page order, convert — then check the result's size and compress with <a href="../pdf/compress.html">Extreme</a> if the portal has a limit. Crop images <em>before</em> converting; a PDF cannot fix a bad source photo.</p></div>

<h2>When JPG-to-PDF is the right move</h2>
<ul>
<li><strong>Application bundles:</strong> photo + signature + ID images combined into the one PDF the form demands.</li>
<li><strong>Declarations and receipts:</strong> signed sheets, payment screenshots and acknowledgements that must be submitted as one document.</li>
<li><strong>Certificates received as photos:</strong> someone photographed your certificate instead of scanning it — convert, then compress properly.</li>
<li><strong>Sharing multi-image documents:</strong> a PDF preserves order and prevents the "images got jumbled in WhatsApp" problem.</li>
</ul>

<h2>Step-by-step: photos to a clean PDF</h2>
<ol>
<li><strong>Crop first.</strong> Remove table backgrounds, fingers, shadows and neighbouring pages from each photo. Tight, straight crops are the single biggest quality lever — a PDF wraps your image as a page, good or bad as-is.</li>
<li><strong>Fix orientation</strong> before converting. A sideways page inside the PDF forces readers to rotate views — and some portals reject it.</li>
<li><strong>Order the pages.</strong> In the tool, arrange images in reading order: first page first. Verify after conversion by flipping through.</li>
<li><strong>Convert.</strong> Drop all images into <a href="../pdf/jpg-to-pdf.html">JPG to PDF</a>, arrange, press convert. Output is a standard PDF any reader opens.</li>
<li><strong>Check size against the portal's limit.</strong> Photos carry camera resolution — a 4-image PDF can reach 3–6MB instantly. Compress with Extreme (grayscale only if the documents are scans, not ID cards or photos where colour matters).</li>
</ol>

<div class="highlight-box"><p><strong>Real example:</strong> Four images — signed declaration (2.1MB), Aadhaar photo (1.4MB), marksheet snap (1.9MB), passport photo (820KB) — became a <strong>6.2MB</strong> PDF after conversion, then <strong>168KB</strong> after Extreme compression. Under a 200KB portal limit, from the same images, without retaking anything.</p></div>

<h2>Your source is a photo — now what?</h2>
<p>There is a difference between converting a well-made photo and salvaging a bad one. A well-lit photo shot parallel to the paper converts cleanly: crop, orient, convert, compress — done in a minute. A dark, angled photo with a hand shadow converts into exactly what it was: a poor image wrapped in PDF clothing. Quick triage before converting: is the text readable at full zoom on your phone? Are all four corners visible with margin? Is there glare across any stamp or signature? If any answer is no, reshoot — thirty seconds of retaking beats any amount of post-processing, because compression amplifies blur as much as it reduces size.</p>
<p>For documents you photograph repeatedly (IDs, licences, certificate folders), build a fixed setup once: window light, document flat on a dark table, phone held directly above. Consistent inputs make every downstream conversion boringly reliable — and every bundle you assemble afterwards fits its limits without heroics.</p>

<h2>Page size and layout realities</h2>
<ul>
<li><strong>Image dimensions ≠ page size.</strong> Your phone photo (3024×4032) does not become A4 automatically — tools map images to a page, and mismatched aspect ratios leave white margins or crop edges.</li>
<li><strong>Check margins after conversion.</strong> A signature cut off at the page edge is worse than a slightly smaller image. If edges clip, crop the source image with margin and reconvert.</li>
<li><strong>One document per file</strong> when the form has separate upload slots — photo here, signature there. Only bundle what the instruction says to bundle.</li>
</ul>

<h2>Common mistakes</h2>
<ul>
<li><strong>Converting before cropping</strong> — shadows, table texture and stray fingers become part of the permanent document.</li>
<li><strong>Leaving screenshots unedited</strong> — a phone screenshot with status-bar icons and notifications looks unprofessional at best; crop to the relevant region.</li>
<li><strong>PNG where JPG is expected</strong> (and vice versa) — some portals validate the <em>source</em> format even inside PDFs; know what the form asked for.</li>
<li><strong>Ignoring the final size</strong> — conversion is not compression. Always check KB after building the PDF; see the <a href="file-size-too-large-error.html">size-error guide</a> for what happens when you don't.</li>
<li><strong>Uploading without a page-by-page review</strong> — order mistakes and clipped edges are invisible until someone else opens it.</li>
</ul>

<h2>Pro tips</h2>
<ul>
<li>Shoot documents near a window in daylight, phone parallel to the paper — most "bad scans" are just poor light and angled cameras.</li>
<li>Keep master photos in a folder like <em>Docs_2026/</em> — you will reuse them across dozens of applications.</li>
<li>For repeat use, convert once into a "master PDF", then split/extract per form (<a href="split-pdf-extract-pages.html">split guide</a>).</li>
<li>Name the output formally: <em>Declaration_ShivamKumar.pdf</em>.</li>
<li>If the portal wants JPG images directly (not PDF), skip conversion — resize images to the KB range instead, as covered in the <a href="ssc-photo-signature-size.html">photo/signature guide</a>.</li>
</ul>

<h2>Frequently asked questions</h2>
<dl>
<dt>Will converting JPG to PDF lose quality?</dt>
<dd>The image is embedded as-is — no re-encoding loss at conversion time. Apparent quality issues come from the source photo itself (blur, bad light, tight resolution).</dd>
<dt>How do I keep the PDF under a portal's size limit?</dt>
<dd>After conversion, compress with the Extreme preset; for scanned text, add grayscale. Four typical form images compress from several MB to 100–200KB.</dd>
<dt>Can I merge images from different sources into one PDF?</dt>
<dd>Yes — phone photos, screenshots and exported images all convert together; just arrange the order before converting.</dd>
<dt>Do the images upload to a server during conversion?</dt>
<dd>No — browser-based conversion processes files on your device; they are not sent anywhere. For ID cards and signed declarations, that matters.</dd>
</dl>
""",
        "faq": [
            {"q": "Does JPG-to-PDF conversion reduce image quality?",
             "a": "No — the image embeds as-is. Any softness comes from the original photo's light, focus or resolution."},
            {"q": "How do I meet a size limit after converting?",
             "a": "Compress the converted PDF with Extreme (plus grayscale for scans); typical form bundles land at 100–200KB."},
            {"q": "Should I crop before or after conversion?",
             "a": "Before — cropping inside a PDF is not possible without re-editing; the source image defines the page."},
            {"q": "When should I upload JPGs directly instead of PDF?",
             "a": "When the form's photo/signature slots ask for images (JPG). PDF is for document and bundle slots."},
        ],
        "related": ["compress-pdf-100kb", "ssc-photo-signature-size", "merge-pdfs-into-one"],
    },
]
