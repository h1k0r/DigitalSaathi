"""
Generates 4 exam-specific landing pages:
1. image/ssc-photo-signature-resize.html
2. image/upsc-photo-signature-resize.html
3. image/ibps-signature-resize.html
4. image/passport-photo-size-india.html
"""

HEADER_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-R2EMRPEG70"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
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
  <title>{TITLE}</title>
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="description" content="{DESC}">
  <link rel="canonical" href="https://vytra.in/image/{SLUG}.html">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="DigitalSaathi">
  <meta property="og:url" content="https://vytra.in/image/{SLUG}.html">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="{DESC}">
  <meta property="og:image" content="https://vytra.in/assets/images/og-banner.png">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{TITLE}">
  <meta name="twitter:description" content="{DESC}">
  <meta name="twitter:image" content="https://vytra.in/assets/images/og-banner.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">

  <!-- Structured Data Schema (WebApplication & BreadcrumbList only) -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "@id": "https://vytra.in/image/{SLUG}.html#app",
      "url": "https://vytra.in/image/{SLUG}.html",
      "name": "{TOOL_NAME} - DigitalSaathi",
      "applicationCategory": "UtilitiesApplication, GraphicApplication",
      "operatingSystem": "All (Modern Web Browsers)",
      "browserRequirements": "Requires JavaScript and HTML5 Canvas support.",
      "description": "{DESC}",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://vytra.in/image/{SLUG}.html#breadcrumbs",
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
          "name": "{BREADCRUMB}",
          "item": "https://vytra.in/image/{SLUG}.html"
        }
      ]
    }
  ]
}
</script>

  <style>
    .guide-wrap {
      max-width: 880px;
      margin: 0 auto;
      padding: 2rem 1rem 5rem;
    }
    .spec-table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border-default);
    }
    .spec-table th, .spec-table td {
      padding: 12px 16px;
      text-align: left;
      border-bottom: 1px solid var(--border-subtle);
      font-size: 0.92rem;
    }
    .spec-table th {
      background: #f8fafc;
      font-weight: 700;
      color: var(--text-main);
    }
    .action-cta-card {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      color: #ffffff;
      padding: 2rem;
      border-radius: var(--radius-lg);
      margin: 2rem 0;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .action-cta-card h3 {
      font-size: 1.35rem;
      font-weight: 800;
      margin: 0;
      color: #ffffff;
    }
    .cta-btn-group {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }
  </style>
  <script async defer src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7919122689237518" crossorigin="anonymous"></script>
</head>
<body class="tool-page">

  <!-- Universal Navigation -->
  <nav class="navbar" id="main-nav">
    <div class="container nav-container">
      <a href="../" class="logo">
        <span class="logo-text" style="letter-spacing: -0.05em; font-weight: 800;">DIGITALSAATHI</span>
      </a>

      <ul class="nav-links" id="navLinks">
        <li class="nav-item">
          <a href="../" class="nav-link">Home</a>
        </li>
        <li class="nav-item has-dropdown">
          <a href="../tools/" class="nav-link">
            Tools
            <svg class="nav-chevron" width="9" height="6" viewBox="0 0 9 6" fill="none"><path d="M1 1L4.5 4.5L8 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <div class="nav-dropdown">
            <a href="../pdf/" class="dropdown-link">PDF Tools <span>&rarr;</span></a>
            <a href="../image/" class="dropdown-link">Image Tools <span>&rarr;</span></a>
            <a href="../text/" class="dropdown-link">Text Tools <span>&rarr;</span></a>
            <a href="../utilities/" class="dropdown-link">Utility Tools <span>&rarr;</span></a>
            <a href="../tools/" class="dropdown-link dropdown-view-all">All Tools Directory &rarr;</a>
          </div>
        </li>
        <li class="nav-item">
          <a href="../#categories" class="nav-link">Categories</a>
        </li>
        <li class="nav-item">
          <a href="../#popular" class="nav-link">Popular Tools</a>
        </li>
        <li class="nav-item">
          <a href="../about.html" class="nav-link">About</a>
        </li>
        <li class="nav-item">
          <a href="../contact.html" class="nav-link">Contact</a>
        </li>
      </ul>

      <div class="nav-actions">
        <button class="nav-search-btn" id="headerSearchBtn" title="Search all tools (Ctrl+K)" aria-label="Search tools">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <span class="search-placeholder">Search tools...</span>
          <kbd class="nav-search-key">Ctrl K</kbd>
        </button>
        <button class="mobile-search-btn" id="mobileSearchBtn" title="Search tools" aria-label="Search tools">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </button>
        <button class="nav-toggle" id="navToggleBtn" aria-label="Toggle navigation" aria-expanded="false">&#9776;</button>
        <a href="../tools/" class="btn btn-primary btn-sm" style="margin-left: 8px;">Explore Tools</a>
      </div>
    </div>
  </nav>

  <!-- Breadcrumb -->
  <div class="container" style="padding-top: 1.5rem;">
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
      <a href="../">Home</a>
      <span>/</span>
      <a href="./">Image Tools</a>
      <span>/</span>
      <span style="color:var(--text-main); font-weight:600;">{BREADCRUMB}</span>
    </nav>
  </div>
'''

FOOTER_HTML = '''  <!-- Universal Footer -->
  <footer class="footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="../" class="logo" style="color:#ffffff;">
          <span class="logo-text" style="letter-spacing: -0.05em; font-weight: 800;">DIGITALSAATHI</span>
        </a>
        <p style="color:#94a3b8; font-size:0.875rem; margin-top:1rem; line-height:1.6;">
          Free online tools for everyday digital work. Convert, compress, edit, and manage files securely in your browser.
        </p>
      </div>

      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Tools & Categories</h4>
        <ul class="footer-links">
          <li><a href="../pdf/">PDF Tools</a></li>
          <li><a href="../image/">Image Tools</a></li>
          <li><a href="../text/">Text Tools</a></li>
          <li><a href="../utilities/">Utility Tools</a></li>
        </ul>
      </div>
      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Company & Help</h4>
        <ul class="footer-links">
          <li><a href="../about.html">About</a></li>
          <li><a href="../contact.html">Contact</a></li>
          <li><a href="../tools/">All Tools Directory</a></li>
        </ul>
      </div>
      <div>
        <h4 style="color:#ffffff; font-size:0.95rem; margin-bottom:1rem;">Legal</h4>
        <ul class="footer-links">
          <li><a href="../privacy.html">Privacy Policy</a></li>
          <li><a href="../terms.html">Terms of Service</a></li>
          <li><a href="../cookie-policy.html">Cookie Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <div>&copy; 2026 DigitalSaathi by Vytra &middot; 100% Client-Side Free Tools. All rights reserved.</div>
    </div>
  </footer>

  <script defer src="../assets/js/common.js"></script>
</body>
</html>'''

PAGES = [
    {
        "slug": "ssc-photo-signature-resize",
        "title": "SSC Photo & Signature Resizer Online Free – CGL, CHSL, MTS & GD Specifications | DigitalSaathi",
        "tool_name": "SSC Photo and Signature Resizer",
        "breadcrumb": "SSC Photo & Signature Resizer",
        "desc": "Resize and compress photograph and signature for SSC CGL, CHSL, MTS, and GD Constable online application forms. 20KB to 50KB photo and 10KB to 20KB signature.",
        "content": '''  <main class="container guide-wrap">
    <article style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-sm);">
      <h1 style="font-size:2rem; font-weight:800; color:var(--text-main); margin-bottom:0.75rem; letter-spacing:-0.02em;">SSC Photo &amp; Signature Resizer Online</h1>
      <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:2rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem;">
        Complete official guidelines and free browser tools to resize, crop, and compress your photograph and signature for SSC CGL, CHSL, MTS, Stenographer, and GD Constable recruitment portals.
      </p>

      <!-- Action CTA Box -->
      <div class="action-cta-card">
        <h3>Direct Tool Shortcuts</h3>
        <p style="margin:0; font-size:0.95rem; color:#cbd5e1;">Click below to launch the free in-browser resizer with pre-configured SSC dimensions and file size limits:</p>
        <div class="cta-btn-group">
          <a href="passport-photo.html" class="btn btn-primary" style="background:#2563eb; color:#ffffff; padding:10px 20px;">Open Passport Photo Maker</a>
          <a href="signature.html" class="btn btn-primary" style="background:#059669; color:#ffffff; padding:10px 20px;">Open Signature Resizer (140x60)</a>
          <a href="compress.html" class="btn btn-outline" style="background:#ffffff; color:#0f172a; padding:10px 20px;">Image Compressor (&lt;50KB)</a>
        </div>
      </div>

      <h2>Official SSC Image &amp; Signature Requirements</h2>
      <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body);">
        According to the official Staff Selection Commission (SSC) recruitment notifications, candidate files must strictly comply with the following technical parameters:
      </p>

      <table class="spec-table">
        <thead>
          <tr>
            <th>Document Type</th>
            <th>Required Dimensions</th>
            <th>File Size Limit</th>
            <th>Format</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>SSC Photograph</strong></td>
            <td>3.5 cm (width) x 4.5 cm (height)</td>
            <td>20 KB to 50 KB</td>
            <td>JPEG / JPG</td>
          </tr>
          <tr>
            <td><strong>SSC Signature</strong></td>
            <td>4.0 cm (width) x 2.0 cm (height) / 140 x 60 px</td>
            <td>10 KB to 20 KB</td>
            <td>JPEG / JPG</td>
          </tr>
        </tbody>
      </table>

      <h2>Step-by-Step Guide for SSC Portal</h2>
      <ol style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1.5rem;">
        <li><strong>Photo Preparation:</strong> Use the <a href="passport-photo.html" style="color:#2563eb; font-weight:600;">Passport Photo Maker</a>. Crop your picture so your face takes up 70% to 80% of the frame with a light or white background. Ensure no caps, spectacles, or masks are worn.</li>
        <li><strong>Signature Formatting:</strong> Use the <a href="signature.html" style="color:#2563eb; font-weight:600;">Signature Resizer</a>. Sign on clean white paper with black or blue ballpoint pen, upload the photo, and select the 140x60 px preset. The tool compresses it to strictly under 20KB.</li>
        <li><strong>Verify Size:</strong> If your photo is larger than 50KB, use the <a href="compress.html" style="color:#2563eb; font-weight:600;">Image Compressor</a> with the "Under 50 KB" preset.</li>
      </ol>

      <h2>Important Common Reasons for SSC Rejection</h2>
      <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1.5rem;">
        <li>Blurry or tilted photo where facial features are not clearly distinguishable.</li>
        <li>Signature uploaded on lined or colored notebook paper causing shadow artifacts.</li>
        <li>File size below 20KB for photo or below 10KB for signature.</li>
        <li>Uploading PNG or PDF format instead of mandatory JPG/JPEG. You can convert PNGs with <a href="png-to-jpg.html" style="color:#2563eb; font-weight:600;">PNG to JPG Converter</a>.</li>
      </ul>

      <!-- Visible FAQ -->
      <h2 style="margin-top:2.5rem;">Frequently Asked Questions</h2>
      <div style="display:flex; flex-direction:column; gap:12px; margin-top:1rem;">
        <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:8px; padding:1.25rem;">
          <h4 style="font-size:1rem; font-weight:700; color:var(--text-main); margin-bottom:0.5rem;">Can I resize my SSC photo and signature on my mobile phone?</h4>
          <p style="font-size:0.9rem; color:var(--text-body); line-height:1.6; margin:0;">Yes. All DigitalSaathi tools run locally in mobile web browsers without requiring any app installations or desktop software.</p>
        </div>
        <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:8px; padding:1.25rem;">
          <h4 style="font-size:1rem; font-weight:700; color:var(--text-main); margin-bottom:0.5rem;">Are my photo and signature private on DigitalSaathi?</h4>
          <p style="font-size:0.9rem; color:var(--text-body); line-height:1.6; margin:0;">Yes. All cropping and resizing happen inside your browser memory on your device. Zero bytes are uploaded to remote servers.</p>
        </div>
      </div>
    </article>
  </main>'''
    },
    {
        "slug": "upsc-photo-signature-resize",
        "title": "UPSC Photo & Signature Resizer Online Free – Civil Services, NDA & CDS Specifications | DigitalSaathi",
        "tool_name": "UPSC Photo and Signature Resizer",
        "breadcrumb": "UPSC Photo & Signature Resizer",
        "desc": "Resize and format photo and signature for UPSC Civil Services IAS, NDA, CDS, and OTR portal. Minimum 350x350 to 1000x1000 pixels and 20KB to 300KB file size.",
        "content": '''  <main class="container guide-wrap">
    <article style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-sm);">
      <h1 style="font-size:2rem; font-weight:800; color:var(--text-main); margin-bottom:0.75rem; letter-spacing:-0.02em;">UPSC Photo &amp; Signature Resizer Online</h1>
      <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:2rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem;">
        Accurate dimensional guidelines and free browser utilities for Union Public Service Commission (UPSC Civil Services, NDA, CDS, CAPF, and OTR One Time Registration) application forms.
      </p>

      <div class="action-cta-card">
        <h3>Direct Tool Shortcuts</h3>
        <p style="margin:0; font-size:0.95rem; color:#cbd5e1;">Launch dedicated tools to format and crop your files to exact UPSC specifications:</p>
        <div class="cta-btn-group">
          <a href="passport-photo.html" class="btn btn-primary" style="background:#2563eb; color:#ffffff; padding:10px 20px;">Passport Photo Maker (350x350 px)</a>
          <a href="signature.html" class="btn btn-primary" style="background:#059669; color:#ffffff; padding:10px 20px;">Signature Resizer</a>
          <a href="resize.html" class="btn btn-outline" style="background:#ffffff; color:#0f172a; padding:10px 20px;">Custom Image Resizer</a>
        </div>
      </div>

      <h2>Official UPSC Image &amp; Signature Guidelines</h2>
      <p style="font-size:0.95rem; line-height:1.75; color:var(--text-body);">
        UPSC enforces strict square aspect ratio guidelines on its online portal:
      </p>

      <table class="spec-table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Minimum Requirement</th>
            <th>Maximum Allowed</th>
            <th>Aspect Ratio</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Photo Dimensions</strong></td>
            <td>350 x 350 pixels</td>
            <td>1000 x 1000 pixels</td>
            <td>Square (1:1)</td>
          </tr>
          <tr>
            <td><strong>Signature Dimensions</strong></td>
            <td>350 x 350 pixels (or 150x70)</td>
            <td>1000 x 1000 pixels</td>
            <td>1:1 or 2:1</td>
          </tr>
          <tr>
            <td><strong>File Size</strong></td>
            <td>20 KB</td>
            <td>300 KB</td>
            <td>JPG / JPEG</td>
          </tr>
        </tbody>
      </table>

      <h2>How to Prepare Your Files for UPSC Portal</h2>
      <ol style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1.5rem;">
        <li><strong>Photo Resize:</strong> Use the <a href="resize.html" style="color:#2563eb; font-weight:600;">Image Resizer</a> and set width and height to 500x500 pixels. Ensure your name and photo date are clearly visible if requested in the notification.</li>
        <li><strong>Signature Crop:</strong> Use the <a href="signature.html" style="color:#2563eb; font-weight:600;">Signature Resizer</a> to crop signature cleanly on a pure white background.</li>
        <li><strong>Document Merging:</strong> If uploading certificates, combine them into a single PDF under 300KB using <a href="../pdf/merge.html" style="color:#2563eb; font-weight:600;">Merge PDF</a> and <a href="../pdf/compress.html" style="color:#2563eb; font-weight:600;">PDF Compressor</a>.</li>
      </ol>

      <!-- Visible FAQ -->
      <h2 style="margin-top:2.5rem;">Frequently Asked Questions</h2>
      <div style="display:flex; flex-direction:column; gap:12px; margin-top:1rem;">
        <div style="background:#f8fafc; border:1px solid var(--border-subtle); border-radius:8px; padding:1.25rem;">
          <h4 style="font-size:1rem; font-weight:700; color:var(--text-main); margin-bottom:0.5rem;">What is the minimum pixel resolution for UPSC photo upload?</h4>
          <p style="font-size:0.9rem; color:var(--text-body); line-height:1.6; margin:0;">UPSC requires at least 350 pixels in width and 350 pixels in height, with a file size between 20 KB and 300 KB.</p>
        </div>
      </div>
    </article>
  </main>'''
    },
    {
        "slug": "ibps-signature-resize",
        "title": "IBPS Signature & Thumb Impression Resizer Online Free – PO, Clerk & RRB Guidelines | DigitalSaathi",
        "tool_name": "IBPS Signature and Thumb Impression Resizer",
        "breadcrumb": "IBPS Signature Resizer",
        "desc": "Resize and compress signature (140x60 px, 10KB to 20KB) and left thumb impression (240x240 px, 20KB to 50KB) for IBPS PO, Clerk, SO, and SBI recruitment forms.",
        "content": '''  <main class="container guide-wrap">
    <article style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-sm);">
      <h1 style="font-size:2rem; font-weight:800; color:var(--text-main); margin-bottom:0.75rem; letter-spacing:-0.02em;">IBPS Signature &amp; Thumb Impression Resizer Online</h1>
      <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:2rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem;">
        Official dimensional requirements and browser-based resize tools for Institute of Banking Personnel Selection (IBPS PO, Clerk, SO, RRB) and SBI recruitment portals.
      </p>

      <div class="action-cta-card">
        <h3>Direct Tool Shortcuts</h3>
        <p style="margin:0; font-size:0.95rem; color:#cbd5e1;">Open our tools configured for banking application specifications:</p>
        <div class="cta-btn-group">
          <a href="signature.html" class="btn btn-primary" style="background:#2563eb; color:#ffffff; padding:10px 20px;">Signature Resizer (140x60 px)</a>
          <a href="resize.html" class="btn btn-primary" style="background:#059669; color:#ffffff; padding:10px 20px;">Thumb Impression Resizer (240x240 px)</a>
          <a href="compress.html" class="btn btn-outline" style="background:#ffffff; color:#0f172a; padding:10px 20px;">Compress Under 20KB</a>
        </div>
      </div>

      <h2>Official IBPS Technical Specifications</h2>
      <table class="spec-table">
        <thead>
          <tr>
            <th>Document</th>
            <th>Pixel Dimensions</th>
            <th>File Size Bracket</th>
            <th>Ink / Guidelines</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Signature</strong></td>
            <td>140 x 60 pixels</td>
            <td>10 KB to 20 KB</td>
            <td>Black ink on white paper (NO capital letters only)</td>
          </tr>
          <tr>
            <td><strong>Left Thumb Impression</strong></td>
            <td>240 x 240 pixels (3x3 cm)</td>
            <td>20 KB to 50 KB</td>
            <td>Blue or black ink stamp on white paper</td>
          </tr>
          <tr>
            <td><strong>Handwritten Declaration</strong></td>
            <td>800 x 400 pixels (10x5 cm)</td>
            <td>50 KB to 100 KB</td>
            <td>English only, black ink on white paper</td>
          </tr>
        </tbody>
      </table>

      <h2>Tips to Prevent IBPS Application Rejection</h2>
      <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1.5rem;">
        <li>Do NOT sign in capital letters; IBPS rejects signatures written solely in block letters.</li>
        <li>Ensure the left thumb impression is clean without smudge lines.</li>
        <li>Use <a href="photo-enhancer.html" style="color:#2563eb; font-weight:600;">Photo Enhancer</a> to sharpen ink contrast if photographed under dim room lighting.</li>
      </ul>
    </article>
  </main>'''
    },
    {
        "slug": "passport-photo-size-india",
        "title": "Passport Photo Size in India – Dimensions in CM, MM, Pixels & Print Guidelines | DigitalSaathi",
        "tool_name": "Indian Passport Photo Size Guide & Tool",
        "breadcrumb": "Passport Photo Size India",
        "desc": "Official Indian passport photo size in centimeters (3.5x4.5 cm), millimeters (35x45 mm), pixels (413x531 px at 300 DPI), and inches. Make printable A4 sheets online.",
        "content": '''  <main class="container guide-wrap">
    <article style="background:#ffffff; border:1px solid var(--border-default); border-radius:var(--radius-lg); padding:2.5rem; box-shadow:var(--shadow-sm);">
      <h1 style="font-size:2rem; font-weight:800; color:var(--text-main); margin-bottom:0.75rem; letter-spacing:-0.02em;">Indian Passport Photo Size &amp; Dimensions Guide</h1>
      <p style="font-size:1rem; color:var(--text-muted); line-height:1.6; margin-bottom:2rem; border-bottom:1px solid var(--border-subtle); padding-bottom:1rem;">
        Standard official measurements in centimeters, millimeters, inches, and pixel counts for Indian Passport, Seva Kendra, PAN Card, OCI, and Driving License.
      </p>

      <div class="action-cta-card">
        <h3>Create Your Passport Photo Online</h3>
        <p style="margin:0; font-size:0.95rem; color:#cbd5e1;">Crop and generate passport photos with white background and printable A4 grid layout:</p>
        <div class="cta-btn-group">
          <a href="passport-photo.html" class="btn btn-primary" style="background:#2563eb; color:#ffffff; padding:10px 20px;">Open Passport Photo Maker</a>
          <a href="crop.html" class="btn btn-outline" style="background:#ffffff; color:#0f172a; padding:10px 20px;">Crop to 3.5x4.5 cm</a>
        </div>
      </div>

      <h2>Official Dimensions Table</h2>
      <table class="spec-table">
        <thead>
          <tr>
            <th>Unit</th>
            <th>Width</th>
            <th>Height</th>
            <th>Aspect Ratio / DPI</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Centimeters (cm)</strong></td>
            <td>3.5 cm</td>
            <td>4.5 cm</td>
            <td>7:9 Ratio</td>
          </tr>
          <tr>
            <td><strong>Millimeters (mm)</strong></td>
            <td>35 mm</td>
            <td>45 mm</td>
            <td>7:9 Ratio</td>
          </tr>
          <tr>
            <td><strong>Inches (in)</strong></td>
            <td>1.38 inches</td>
            <td>1.77 inches</td>
            <td>Standard Indian Spec</td>
          </tr>
          <tr>
            <td><strong>Pixels at 300 DPI</strong></td>
            <td>413 pixels</td>
            <td>531 pixels</td>
            <td>High Resolution Print</td>
          </tr>
          <tr>
            <td><strong>Pixels at 600 DPI</strong></td>
            <td>826 pixels</td>
            <td>1062 pixels</td>
            <td>Ultra HD Print</td>
          </tr>
        </tbody>
      </table>

      <h2>Official Passport Seva Kendra Photo Rules</h2>
      <ul style="padding-left:1.5rem; line-height:1.8; color:var(--text-body); font-size:0.95rem; margin-bottom:1.5rem;">
        <li><strong>Background:</strong> Plain white or light off-white background. No colored patterns or wall textures.</li>
        <li><strong>Facial Coverage:</strong> The face must cover 70% to 80% of the entire photo area.</li>
        <li><strong>Expression:</strong> Neutral expression with mouth closed and eyes open, looking straight at the camera.</li>
        <li><strong>Attire:</strong> Dark colored clothing is recommended to contrast clearly against the white background. Avoid white shirts.</li>
      </ul>
    </article>
  </main>'''
    }
]

def generate_pages():
    for p in PAGES:
        html = HEADER_HTML.replace('{TITLE}', p['title'])
        html = html.replace('{DESC}', p['desc'])
        html = html.replace('{SLUG}', p['slug'])
        html = html.replace('{TOOL_NAME}', p['tool_name'])
        html = html.replace('{BREADCRUMB}', p['breadcrumb'])
        html += p['content'] + '\n' + FOOTER_HTML
        
        file_path = f"image/{p['slug']}.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[PASS] Created {file_path}")

if __name__ == '__main__':
    generate_pages()
