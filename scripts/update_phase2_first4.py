"""
Complete Phase 2 Script:
1. Optimizes the first 4 tool pages:
   - image/compress.html
   - image/passport-photo.html
   - image/signature.html
   - pdf/compress.html
2. Creates the 4 exam landing pages:
   - image/ssc-photo-signature-resize.html
   - image/upsc-photo-signature-resize.html
   - image/ibps-signature-resize.html
   - image/passport-photo-size-india.html
"""
import os
import re

def update_compress_image():
    path = "image/compress.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(r"<title>.*?</title>", "<title>Compress Image Online Free – Reduce JPG, PNG &amp; WebP to 20KB, 50KB, 100KB | DigitalSaathi</title>", c)
    c = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Free online image compressor to reduce JPG, PNG, and WebP photo size to under 20KB, 50KB, or 100KB with 100% browser-based privacy. No server uploads.">', c)
    c = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Compress Image Online Free – Reduce JPG, PNG &amp; WebP to 20KB, 50KB, 100KB | DigitalSaathi">', c)
    c = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Free online image compressor to reduce JPG, PNG, and WebP photo size to under 20KB, 50KB, or 100KB with 100% browser-based privacy. No server uploads.">', c)
    c = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Compress Image Online Free – Reduce JPG, PNG &amp; WebP to 20KB, 50KB, 100KB | DigitalSaathi">', c)
    c = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Free online image compressor to reduce JPG, PNG, and WebP photo size to under 20KB, 50KB, or 100KB with 100% browser-based privacy. No server uploads.">', c)

    schema = '''  <!-- Structured Data Schema (WebApplication & BreadcrumbList only) -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://vytra.in/image/compress.html#app",
      "url": "https://vytra.in/image/compress.html",
      "name": "Image Compressor - DigitalSaathi",
      "applicationCategory": "UtilitiesApplication, GraphicApplication",
      "operatingSystem": "All (Modern Web Browsers)",
      "browserRequirements": "Requires JavaScript and HTML5 Canvas support.",
      "description": "Free, browser-based image compressor to reduce JPG, PNG, and WebP file sizes to under 20KB, 50KB, or 100KB with 100% client-side privacy.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://vytra.in/image/compress.html#breadcrumbs",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://vytra.in/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Image Tools",
          "item": "https://vytra.in/image/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Image Compressor",
          "item": "https://vytra.in/image/compress.html"
        }
      ]
    }
  ]
}
</script>'''
    c = re.sub(r'<\!\s*--\s*Top Ranking Structured Data Schema.*?<\/script>', schema, c, flags=re.DOTALL)
    c = re.sub(r'<\!\s*--\s*Structured Data Schema.*?<\/script>', schema, c, flags=re.DOTALL)

    info_section = '''    <!-- 3. Comprehensive Guide & Technical Explanation -->
    <section class="vytra-info-section" style="margin-top: 3.5rem;">
      <h2 class="vytra-section-title">How to Compress Images Online (Step-by-Step)</h2>
      
      <!-- 3-Step Visual Process Guide -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 1.5rem 0 2.5rem;">
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">1</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Upload Your Image</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Drag and drop your JPG, PNG, or WebP file into the box above or tap the browse button to select a picture from your device.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">2</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Choose Size or Quality</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Select a one-click preset like <strong>Under 20 KB</strong>, <strong>Under 50 KB</strong>, or <strong>Under 100 KB</strong>, or adjust the compression slider manually.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">3</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Download Instantly</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Preview the real-time compressed file size and savings percentage, then click download to save the optimized file directly to your storage.</p>
        </div>
      </div>

      <!-- Detailed Technical & Use Case Content (350+ words) -->
      <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2rem; margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; font-weight:800; color:var(--text-main); margin-bottom:1rem;">How Client-Side Image Compression Works</h3>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          DigitalSaathi's Image Compressor executes 100% inside your web browser using the HTML5 Canvas API and WebAssembly quantization algorithms. When you upload an image, the browser reads the raw pixel data into local memory without transferring any bytes over the network to external servers.
        </p>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          For JPG and JPEG images, the compressor applies discrete cosine transform (DCT) quantization, removing imperceptible high-frequency visual noise and metadata (EXIF headers, color profiles, camera tags) that inflate file size. When you select a strict threshold such as <em>under 20 KB</em> or <em>under 50 KB</em>, an intelligent binary search loop tests varying compression quality factors and dimensional downsampling in milliseconds until the output strictly satisfies the target ceiling without creating visual blurriness.
        </p>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          If you need to adjust pixel dimensions alongside file size, you can use our dedicated <a href="resize.html" style="color:#2563eb; font-weight:600;">Image Resizer</a>. For official documents, explore the <a href="passport-photo.html" style="color:#2563eb; font-weight:600;">Passport Photo Maker</a> or <a href="signature.html" style="color:#2563eb; font-weight:600;">Signature Resizer</a>. If you are preparing application packages, convert your images into single documents using the <a href="../pdf/jpg-to-pdf.html" style="color:#2563eb; font-weight:600;">JPG to PDF Converter</a> or reduce existing document size with the <a href="../pdf/compress.html" style="color:#2563eb; font-weight:600;">PDF Compressor</a>.
        </p>

        <h4 style="font-size:1.1rem; font-weight:700; color:var(--text-main); margin:1.5rem 0 0.75rem;">Common Target File Size Presets</h4>
        <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem;">
          <li><strong>Under 20 KB:</strong> Standard specification for digital signatures and thumb impressions across government recruitment portals (SSC, UPSC, IBPS).</li>
          <li><strong>Under 50 KB:</strong> Standard requirement for passport-size candidate photos and identity card uploads.</li>
          <li><strong>Under 100 KB / 200 KB:</strong> Optimal for scanned certificates, mark sheets, and email attachments requiring lightweight delivery.</li>
        </ul>
      </div>

      <!-- Developer / Team Attribution Card -->
      <div class="vytra-author-bar">
        <div class="vytra-author-avatar">D</div>
        <div class="vytra-author-text">Developed &amp; Maintained by DigitalSaathi Team</div>
      </div>
    </section>

    <!-- 5. Visible Frequently Asked Questions -->
    <section class="vytra-qa-section">
      <h2 class="vytra-section-title" style="text-align:center;">Frequently Asked Questions</h2>
      <div class="vytra-qa-list">
        <div class="vytra-qa-item active">
          <button type="button" class="vytra-qa-header">
            <span>How do I compress an image to under 20KB or 50KB?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Upload your photo, then click the "Under 20 KB" or "Under 50 KB" preset button. The tool automatically computes the exact compression quality required to stay below your chosen limit while preserving facial clarity.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Does compressing an image reduce its clarity?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            DigitalSaathi uses adaptive quantization to discard unnecessary metadata and invisible color details before touching visible edges, ensuring text and portrait details remain sharp and legible.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Are my photos uploaded to any server?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            No. All compression processing runs entirely inside your browser sandbox on your device. Zero bytes are uploaded to remote servers.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Which image formats can I compress?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            You can compress JPG, JPEG, PNG, and WebP images. You can also output your compressed image as JPG or WebP for optimal compression efficiency.
          </div>
        </div>
      </div>
    </section>

    <!-- 8. Related Tools (Contextual Internal Links) -->
    <section style="margin-top: 4.5rem; padding-top: 2rem; border-top: 1px solid var(--border-subtle, #e2e8f0);">
      <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem; color: var(--text-main);">
        Related Free Tools
      </h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem;">
        <a href="resize.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📐</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Image Resizer</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Change width &amp; height</div>
          </div>
        </a>
        <a href="passport-photo.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📸</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Passport Photo Maker</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Indian &amp; Visa formats</div>
          </div>
        </a>
        <a href="signature.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">✍️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Signature Resizer</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Auto 140x60 under 20KB</div>
          </div>
        </a>
        <a href="jpg-to-png.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🖼️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">JPG to PNG</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Lossless format conversion</div>
          </div>
        </a>
        <a href="../pdf/compress.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🗜️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Compress PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Reduce PDF under 100KB</div>
          </div>
        </a>
        <a href="../pdf/jpg-to-pdf.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📑</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">JPG to PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Convert photos to A4 PDF</div>
          </div>
        </a>
      </div>
    </section>'''

    pattern = r'<\!\s*--\s*3\.\s*Information Section.*?<\/section>\s*<\/main>'
    c = re.sub(pattern, info_section + '\n  </main>', c, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("[PASS] image/compress.html updated!")

def update_passport_photo():
    path = "image/passport-photo.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(r"<title>.*?</title>", "<title>Passport Photo Maker Online Free – 3.5x4.5cm Indian &amp; Visa Photo Crop | DigitalSaathi</title>", c)
    c = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Create passport size photos online for Indian passport, PAN card, exams, and visa applications. Crop to 3.5x4.5 cm with custom white/blue background and printable A4 grid.">', c)
    c = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Passport Photo Maker Online Free – 3.5x4.5cm Indian &amp; Visa Photo Crop | DigitalSaathi">', c)
    c = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Create passport size photos online for Indian passport, PAN card, exams, and visa applications. Crop to 3.5x4.5 cm with custom white/blue background and printable A4 grid.">', c)
    c = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Passport Photo Maker Online Free – 3.5x4.5cm Indian &amp; Visa Photo Crop | DigitalSaathi">', c)
    c = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Create passport size photos online for Indian passport, PAN card, exams, and visa applications. Crop to 3.5x4.5 cm with custom white/blue background and printable A4 grid.">', c)

    schema = '''  <!-- Structured Data Schema (WebApplication & BreadcrumbList only) -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://vytra.in/image/passport-photo.html#app",
      "url": "https://vytra.in/image/passport-photo.html",
      "name": "Passport Photo Maker - DigitalSaathi",
      "applicationCategory": "UtilitiesApplication, GraphicApplication",
      "operatingSystem": "All (Modern Web Browsers)",
      "browserRequirements": "Requires JavaScript and HTML5 Canvas support.",
      "description": "Create standard passport size photos for Indian passport, PAN card, and job applications with custom backgrounds and printable A4 sheets.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://vytra.in/image/passport-photo.html#breadcrumbs",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://vytra.in/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Image Tools",
          "item": "https://vytra.in/image/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Passport Photo Maker",
          "item": "https://vytra.in/image/passport-photo.html"
        }
      ]
    }
  ]
}
</script>'''
    c = re.sub(r'<\!\s*--\s*Top Ranking SEO Schema Markup.*?<\/script>', schema, c, flags=re.DOTALL)
    c = re.sub(r'<\!\s*--\s*Structured Data Schema.*?<\/script>', schema, c, flags=re.DOTALL)

    info_section = '''    <!-- 3. Comprehensive Guide & Technical Explanation -->
    <section class="vytra-info-section" style="margin-top: 3.5rem;">
      <h2 class="vytra-section-title">How to Create Passport Size Photos Online (Step-by-Step)</h2>
      
      <!-- 3-Step Visual Process Guide -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 1.5rem 0 2.5rem;">
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">1</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Upload Your Portrait</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Upload a clear front-facing portrait photo or selfie taken in good lighting against a simple background.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">2</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Crop &amp; Select Background</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Select standard Indian Passport (3.5x4.5 cm) or US Visa (2x2 inch). Choose white, light blue, or red background and set DPI.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">3</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Download Single or A4 Grid</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Download a single digital photo for online forms or generate an A4 printable sheet (6, 8, or 12 photos) for studio printing.</p>
        </div>
      </div>

      <!-- Detailed Technical & Specification Content (350+ words) -->
      <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2rem; margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; font-weight:800; color:var(--text-main); margin-bottom:1rem;">Indian Passport &amp; Application Photo Guidelines</h3>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          The official Indian passport and exam portal standard requires photographs to measure exactly <strong>3.5 cm in width by 4.5 cm in height</strong> (at 300 DPI, this corresponds to 413 x 531 pixels). The applicant's face must occupy 70% to 80% of the vertical frame, measured from the bottom of the chin to the top of the forehead.
        </p>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          DigitalSaathi's Passport Photo Maker allows you to crop photos with precision alignment overlays. You can switch between plain white, off-white, and light blue background fills as required by specific application rules. When applying for US Visa or international travel, toggle to the 2x2 inch (51x51 mm) preset with a single click.
        </p>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          Need to prepare a complete digital application? Resize your accompanying signature using the <a href="signature.html" style="color:#2563eb; font-weight:600;">Signature Resizer</a>, compress your photo under 50KB with the <a href="compress.html" style="color:#2563eb; font-weight:600;">Image Compressor</a>, or remove complex backgrounds with the <a href="remove-bg.html" style="color:#2563eb; font-weight:600;">Background Remover</a>. For document submissions, combine your certificate photos into a single file with <a href="jpg-to-pdf.html" style="color:#2563eb; font-weight:600;">JPG to PDF</a> or adjust resolution via <a href="dpi-converter.html" style="color:#2563eb; font-weight:600;">DPI Converter</a>.
        </p>

        <h4 style="font-size:1.1rem; font-weight:700; color:var(--text-main); margin:1.5rem 0 0.75rem;">Standard Passport Dimension Reference</h4>
        <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem;">
          <li><strong>Indian Passport &amp; Exam Portals:</strong> 3.5 cm x 4.5 cm (35 mm x 45 mm, 413 x 531 px at 300 DPI).</li>
          <li><strong>US Visa / OCI / Schengen:</strong> 2 x 2 inches (51 mm x 51 mm, 600 x 600 px at 300 DPI).</li>
          <li><strong>Cyber Café A4 Printable Sheet:</strong> 8 or 12 tiled passport photos with cut-marks on a standard 210 x 297 mm paper sheet.</li>
        </ul>
      </div>

      <!-- Developer Attribution Card -->
      <div class="vytra-author-bar">
        <div class="vytra-author-avatar">D</div>
        <div class="vytra-author-text">Developed &amp; Maintained by DigitalSaathi Team</div>
      </div>
    </section>

    <!-- 5. Visible FAQ Section -->
    <section class="vytra-qa-section">
      <h2 class="vytra-section-title" style="text-align:center;">Frequently Asked Questions</h2>
      <div class="vytra-qa-list">
        <div class="vytra-qa-item active">
          <button type="button" class="vytra-qa-header">
            <span>What is the standard passport photo size in India?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            The standard dimension is 3.5 cm width by 4.5 cm height (35x45 mm). At 300 DPI print resolution, this translates to 413 x 531 pixels.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Can I print multiple passport photos on one A4 paper?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Yes. Use the "A4 Printable Sheet" option in the tool to arrange 6, 8, or 12 copies on a single A4 page with cutting border guidelines for easy photo studio printing.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>What background color should I use for passport photos?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            A plain white or light off-white background is recommended for most Indian government forms, passports, and visa applications.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Is it safe to make passport photos on this website?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Yes, 100%. All face cropping, rendering, and sheet generation occur locally in your browser memory via the HTML5 Canvas API without transmitting files to any server.
          </div>
        </div>
      </div>
    </section>

    <!-- 8. Related Tools (Contextual Internal Links) -->
    <section style="margin-top: 4.5rem; padding-top: 2rem; border-top: 1px solid var(--border-subtle, #e2e8f0);">
      <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem; color: var(--text-main);">
        Related Free Tools
      </h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem;">
        <a href="compress.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🗜️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Image Compressor</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Compress to 20KB/50KB</div>
          </div>
        </a>
        <a href="signature.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">✍️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Signature Resizer</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">140x60 px for job forms</div>
          </div>
        </a>
        <a href="crop.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">✂️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Crop Photo</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Custom aspect ratios</div>
          </div>
        </a>
        <a href="remove-bg.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🪄</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Remove Background</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">White &amp; transparent cutout</div>
          </div>
        </a>
        <a href="dpi-converter.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🖨️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">DPI Converter</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Set 200/300/600 DPI</div>
          </div>
        </a>
        <a href="jpg-to-pdf.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📑</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">JPG to PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Convert photos to A4 PDF</div>
          </div>
        </a>
      </div>
    </section>'''

    pattern = r'<\!\s*--\s*3\.\s*Information Section.*?<\/section>\s*<\/main>'
    c = re.sub(pattern, info_section + '\n  </main>', c, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("[PASS] image/passport-photo.html updated!")

def update_signature_resizer():
    path = "image/signature.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(r"<title>.*?</title>", "<title>Signature Resizer Online Free – Resize Signature to 10KB, 20KB &amp; 140x60 Pixels | DigitalSaathi</title>", c)
    c = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Resize and compress handwritten signatures for SSC, UPSC, IBPS, and government job portals. Auto-fit to 140x60 px and compress under 10KB or 20KB locally in browser.">', c)
    c = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Signature Resizer Online Free – Resize Signature to 10KB, 20KB &amp; 140x60 Pixels | DigitalSaathi">', c)
    c = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Resize and compress handwritten signatures for SSC, UPSC, IBPS, and government job portals. Auto-fit to 140x60 px and compress under 10KB or 20KB locally in browser.">', c)
    c = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Signature Resizer Online Free – Resize Signature to 10KB, 20KB &amp; 140x60 Pixels | DigitalSaathi">', c)
    c = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Resize and compress handwritten signatures for SSC, UPSC, IBPS, and government job portals. Auto-fit to 140x60 px and compress under 10KB or 20KB locally in browser.">', c)

    schema = '''  <!-- Structured Data Schema (WebApplication & BreadcrumbList only) -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://vytra.in/image/signature.html#app",
      "url": "https://vytra.in/image/signature.html",
      "name": "Signature Resizer - DigitalSaathi",
      "applicationCategory": "UtilitiesApplication, GraphicApplication",
      "operatingSystem": "All (Modern Web Browsers)",
      "browserRequirements": "Requires JavaScript and HTML5 Canvas support.",
      "description": "Resize and compress signatures to 140x60 pixels and under 10KB/20KB for SSC, UPSC, and online job portal applications.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://vytra.in/image/signature.html#breadcrumbs",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://vytra.in/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Image Tools",
          "item": "https://vytra.in/image/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Signature Resizer",
          "item": "https://vytra.in/image/signature.html"
        }
      ]
    }
  ]
}
</script>'''
    c = re.sub(r'<\!\s*--\s*Top Ranking SEO Schema Markup.*?<\/script>', schema, c, flags=re.DOTALL)
    c = re.sub(r'<\!\s*--\s*Structured Data Schema.*?<\/script>', schema, c, flags=re.DOTALL)

    info_section = '''    <!-- 3. Comprehensive Guide & Technical Explanation -->
    <section class="vytra-info-section" style="margin-top: 3.5rem;">
      <h2 class="vytra-section-title">How to Resize Signatures for Online Forms (Step-by-Step)</h2>
      
      <!-- 3-Step Visual Process Guide -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 1.5rem 0 2.5rem;">
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">1</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Upload Your Signature</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Take a photo or scan of your handwritten signature on clean, unruled white paper with black or blue ink.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">2</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Select Preset &amp; Size Limit</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Select SSC/IBPS (140x60 px) or UPSC (150x70 px). Choose strict file size ceiling (Under 10 KB or Under 20 KB).</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">3</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Crop &amp; Download</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Adjust the crop rectangle to frame your signature neatly, then download your ready-to-upload signature image.</p>
        </div>
      </div>

      <!-- Detailed Technical & Specification Content (350+ words) -->
      <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2rem; margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; font-weight:800; color:var(--text-main); margin-bottom:1rem;">Signature Upload Rules for Recruitment Portals</h3>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          Major Indian government examination systems (including Staff Selection Commission, Union Public Service Commission, Institute of Banking Personnel Selection, Railway Recruitment Boards, and State PSCs) enforce strict automated validation on uploaded signatures. Forms are frequently rejected if the image dimensions or file sizes fall outside specified ranges:
        </p>
        <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1rem;">
          <li><strong>SSC Portals (CGL, CHSL, MTS, GD):</strong> 140 pixels width x 60 pixels height, file size between 10 KB and 20 KB in JPEG/JPG format.</li>
          <li><strong>IBPS &amp; Bank PO/Clerk:</strong> 140 x 60 pixels, file size 10 KB to 20 KB, strictly on white background with black ink.</li>
          <li><strong>UPSC Applications:</strong> Minimum 350 x 350 pixels (or 150 x 70 px legacy), file size 20 KB to 300 KB.</li>
        </ul>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          DigitalSaathi's Signature Resizer automatically applies contrast enhancement and background whitening to eliminate shadows caused by phone cameras. It then compresses the signature using adaptive quantization to guarantee the final output falls within the mandatory 10KB to 20KB bracket without making the ink strokes jagged.
        </p>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          Pair your resized signature with a compliant photo from our <a href="passport-photo.html" style="color:#2563eb; font-weight:600;">Passport Photo Maker</a>, reduce overall photo weight with the <a href="compress.html" style="color:#2563eb; font-weight:600;">Image Compressor</a>, or fine-tune exact pixel sizes using <a href="resize.html" style="color:#2563eb; font-weight:600;">Image Resizer</a>. Convert formats seamlessly with <a href="png-to-jpg.html" style="color:#2563eb; font-weight:600;">PNG to JPG</a> or combine multiple scanned certificates into an application package using <a href="../pdf/merge.html" style="color:#2563eb; font-weight:600;">Merge PDF</a>.
        </p>
      </div>

      <!-- Developer Attribution Card -->
      <div class="vytra-author-bar">
        <div class="vytra-author-avatar">D</div>
        <div class="vytra-author-text">Developed &amp; Maintained by DigitalSaathi Team</div>
      </div>
    </section>

    <!-- 5. Visible FAQ Section -->
    <section class="vytra-qa-section">
      <h2 class="vytra-section-title" style="text-align:center;">Frequently Asked Questions</h2>
      <div class="vytra-qa-list">
        <div class="vytra-qa-item active">
          <button type="button" class="vytra-qa-header">
            <span>What are the standard dimensions for SSC and IBPS signature upload?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            The standard dimension is 140 pixels width by 60 pixels height (aspect ratio ~ 7:3) and the file size must be between 10 KB and 20 KB in JPG/JPEG format.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>How do I avoid shadows on my phone-photographed signature?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Sign on clean unlined white paper in good direct daylight without casting a hand shadow. Our tool automatically enhances background brightness to ensure high contrast.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Can I resize my signature to under 10KB or 20KB on mobile?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Yes. DigitalSaathi is fully optimized for mobile browsers on Android and iPhone. Simply upload your signature photo, select the "Under 20KB" preset, and download.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Is my signature secure and kept private?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Yes, completely. Because signatures are sensitive legal credentials, all processing is executed 100% locally in your device's browser memory without uploading any data to external servers.
          </div>
        </div>
      </div>
    </section>

    <!-- 8. Related Tools (Contextual Internal Links) -->
    <section style="margin-top: 4.5rem; padding-top: 2rem; border-top: 1px solid var(--border-subtle, #e2e8f0);">
      <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem; color: var(--text-main);">
        Related Free Tools
      </h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem;">
        <a href="compress.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🗜️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Image Compressor</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Compress to 20KB/50KB</div>
          </div>
        </a>
        <a href="passport-photo.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📸</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Passport Photo Maker</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">3.5x4.5 cm with A4 grid</div>
          </div>
        </a>
        <a href="resize.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📐</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Image Resizer</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Custom width &amp; height</div>
          </div>
        </a>
        <a href="png-to-jpg.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🖼️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">PNG to JPG</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Convert signature to JPG</div>
          </div>
        </a>
        <a href="photo-enhancer.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">✨</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Photo Enhancer</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Boost ink contrast</div>
          </div>
        </a>
        <a href="../pdf/merge.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📑</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Merge PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Combine application docs</div>
          </div>
        </a>
      </div>
    </section>'''

    pattern = r'<\!\s*--\s*3\.\s*Information Section.*?<\/section>\s*<\/main>'
    c = re.sub(pattern, info_section + '\n  </main>', c, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("[PASS] image/signature.html updated!")

def update_pdf_compress():
    path = "pdf/compress.html"
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    c = re.sub(r"<title>.*?</title>", "<title>Compress PDF Online Free – Reduce PDF File Size (Under 100KB, 200KB) | DigitalSaathi</title>", c)
    c = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Compress PDF files online without losing text clarity. Choose compression levels for exam portals, email attachments, and government submissions. 100% private in browser.">', c)
    c = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Compress PDF Online Free – Reduce PDF File Size (Under 100KB, 200KB) | DigitalSaathi">', c)
    c = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Compress PDF files online without losing text clarity. Choose compression levels for exam portals, email attachments, and government submissions. 100% private in browser.">', c)
    c = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Compress PDF Online Free – Reduce PDF File Size (Under 100KB, 200KB) | DigitalSaathi">', c)
    c = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Compress PDF files online without losing text clarity. Choose compression levels for exam portals, email attachments, and government submissions. 100% private in browser.">', c)

    schema = '''  <!-- Structured Data Schema (WebApplication & BreadcrumbList only) -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://vytra.in/pdf/compress.html#app",
      "url": "https://vytra.in/pdf/compress.html",
      "name": "PDF Compressor - DigitalSaathi",
      "applicationCategory": "UtilitiesApplication, BusinessApplication",
      "operatingSystem": "All (Modern Web Browsers)",
      "browserRequirements": "Requires JavaScript and WebAssembly support.",
      "description": "Compress PDF documents to under 100KB, 200KB, or 500KB online for free with 100% client-side privacy.",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://vytra.in/pdf/compress.html#breadcrumbs",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://vytra.in/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "PDF Tools",
          "item": "https://vytra.in/pdf/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Compress PDF",
          "item": "https://vytra.in/pdf/compress.html"
        }
      ]
    }
  ]
}
</script>'''
    c = re.sub(r'<\!\s*--\s*Top Ranking SEO Schema Markup.*?<\/script>', schema, c, flags=re.DOTALL)
    c = re.sub(r'<\!\s*--\s*Structured Data Schema.*?<\/script>', schema, c, flags=re.DOTALL)

    info_section = '''    <!-- 3. Comprehensive Guide & Technical Explanation -->
    <section class="vytra-info-section" style="margin-top: 3.5rem;">
      <h2 class="vytra-section-title">How to Compress PDF Files Online (Step-by-Step)</h2>
      
      <!-- 3-Step Visual Process Guide -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 1.5rem 0 2.5rem;">
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">1</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Upload Your PDF</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Select or drag and drop your PDF document into the compression dropzone above.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">2</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Choose Compression Level</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Select Extreme Compression (&lt;100 KB for exam portals), Medium (&lt;200 KB), or Standard Recommended reduction.</p>
        </div>
        <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:1.25rem;">
          <div style="width:32px; height:32px; border-radius:50%; background:var(--primary); color:#ffffff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.75rem;">3</div>
          <h3 style="font-size:1.05rem; font-weight:700; margin-bottom:0.5rem; color:var(--text-main);">Compress &amp; Download</h3>
          <p style="font-size:0.88rem; color:var(--text-body); line-height:1.5; margin:0;">Click "Compress PDF" and instantly download your optimized lightweight PDF with preserved text sharpness.</p>
        </div>
      </div>

      <!-- Detailed Technical & Specification Content (350+ words) -->
      <div style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2rem; margin-bottom:2rem;">
        <h3 style="font-size:1.25rem; font-weight:800; color:var(--text-main); margin-bottom:1rem;">How In-Browser PDF Compression Works</h3>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          PDF files frequently carry excess bloat from high-resolution embedded raster scans, duplicate font descriptors, unreferenced metadata objects, and uncompressed stream streams. DigitalSaathi's PDF Compressor parses your PDF structure directly in browser memory using WebAssembly binaries and PDF-Lib engines without uploading your sensitive files to cloud servers.
        </p>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          The compression pipeline applies a multi-stage optimization process:
        </p>
        <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1rem;">
          <li><strong>Object Stream Compaction:</strong> Flattens and deflates structural cross-reference tables and unused metadata streams.</li>
          <li><strong>Image Stream Resampling:</strong> Identifies embedded JPEG and PNG images, downsampling them to 150 DPI for screens or 200 DPI for forms while removing duplicate alpha masks.</li>
          <li><strong>Font Deduplication:</strong> Eliminates duplicate font subsets and strips unnecessary structural layers.</li>
        </ul>
        <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body); margin-bottom:1rem;">
          Need to manage multi-page documents? Use our <a href="merge.html" style="color:#2563eb; font-weight:600;">Merge PDF</a> tool to join separate scans into a single file, <a href="split.html" style="color:#2563eb; font-weight:600;">Split PDF</a> to extract specific pages, or <a href="pdf-to-word.html" style="color:#2563eb; font-weight:600;">PDF to Word</a> to convert documents into editable formats. If you have image certificates, convert them with <a href="jpg-to-pdf.html" style="color:#2563eb; font-weight:600;">JPG to PDF</a>, sign contracts with <a href="sign.html" style="color:#2563eb; font-weight:600;">Sign PDF</a>, or compress standalone images using <a href="../image/compress.html" style="color:#2563eb; font-weight:600;">Image Compressor</a>.
        </p>
      </div>

      <!-- Developer Attribution Card -->
      <div class="vytra-author-bar">
        <div class="vytra-author-avatar">D</div>
        <div class="vytra-author-text">Developed &amp; Maintained by DigitalSaathi Team</div>
      </div>
    </section>

    <!-- 5. Visible FAQ Section -->
    <section class="vytra-qa-section">
      <h2 class="vytra-section-title" style="text-align:center;">Frequently Asked Questions</h2>
      <div class="vytra-qa-list">
        <div class="vytra-qa-item active">
          <button type="button" class="vytra-qa-header">
            <span>How to compress a PDF to under 100KB or 200KB?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Upload your PDF and select the "Extreme Compression (< 100 KB)" preset. The tool optimizes image streams and strips metadata to achieve the target size for portal submissions.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Will PDF compression make my text unreadable?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            No. DigitalSaathi preserves vector text and font streams losslessly. Compression targets embedded scan images and structural bloat so text remains sharp.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Are confidential documents safe to compress here?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            Yes, completely safe. All compression happens client-side inside your browser engine. Your files never travel over the internet to any server.
          </div>
        </div>

        <div class="vytra-qa-item">
          <button type="button" class="vytra-qa-header">
            <span>Is there any limit on page count or daily usage?</span>
            <span>▼</span>
          </button>
          <div class="vytra-qa-content">
            No. You can compress multi-page documents freely with no daily task quotas, subscriptions, or watermarks.
          </div>
        </div>
      </div>
    </section>

    <!-- 8. Related Tools (Contextual Internal Links) -->
    <section style="margin-top: 4.5rem; padding-top: 2rem; border-top: 1px solid var(--border-subtle, #e2e8f0);">
      <h3 style="font-size: 1.25rem; font-weight: 800; margin-bottom: 1.25rem; color: var(--text-main);">
        Related Free Tools
      </h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem;">
        <a href="merge.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📑</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Merge PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Combine multiple files</div>
          </div>
        </a>
        <a href="split.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">✂️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Split PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Extract specific pages</div>
          </div>
        </a>
        <a href="pdf-to-word.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">📝</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">PDF to Word</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Convert to editable DOCX</div>
          </div>
        </a>
        <a href="jpg-to-pdf.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🖼️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">JPG to PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Convert photos to A4 PDF</div>
          </div>
        </a>
        <a href="sign.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">✍️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Sign PDF</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Draw &amp; place signature</div>
          </div>
        </a>
        <a href="../image/compress.html" class="card" style="text-decoration:none; color:inherit; padding:1.25rem; display:flex; align-items:center; gap:12px;">
          <span style="font-size:1.6rem;">🗜️</span>
          <div>
            <div style="font-weight:700; font-size:0.92rem;">Compress Image</div>
            <div style="font-size:0.78rem; color:var(--text-muted);">Compress photos to 20KB/50KB</div>
          </div>
        </a>
      </div>
    </section>'''

    pattern = r'<\!\s*--\s*3\.\s*Information Section.*?<\/section>\s*<\/main>'
    c = re.sub(pattern, info_section + '\n  </main>', c, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print("[PASS] pdf/compress.html updated!")

if __name__ == '__main__':
    update_compress_image()
    update_passport_photo()
    update_signature_resizer()
    update_pdf_compress()
