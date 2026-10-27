#!/usr/bin/env python3
"""Build Vytra Form-Ready Kit pages: image tools + form tools.

Positioning: "Vytra = Form-Ready Kit for Indian applicants". All specs come
from data/exam-specs.json (single source — edit there, re-run this builder).
Nav/footer/mega are extracted from pdf/compress.html, so every nav change
there propagates here on the next run.

Pages generated:
  image/index.html, image/resize.html, image/signature.html, image/compress.html
  forms/index.html, forms/preflight.html, forms/specs.html
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
SNIPPET_SRC = os.path.join(ROOT, "pdf", "compress.html")
SPECS_PATH = os.path.join(ROOT, "data", "exam-specs.json")
SITE = "https://vytra.in"
TODAY = "2026-10-27"

ADSENSE = ('  <script async defer src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
           '?client=ca-pub-7919122689237518" crossorigin="anonymous"></script>')

TOOL_STYLE = """
  <style>
    .breadcrumb-nav { display:flex; align-items:center; gap:8px; font-size:.8125rem;
      color:var(--text-muted); margin-bottom:var(--space-4); }
    .breadcrumb-nav a { color:var(--text-muted); text-decoration:none; }
    .breadcrumb-nav a:hover { color:var(--primary); }
    .ik-card { background:#fff; border:1px solid var(--border-subtle,#e2e8f0); border-radius:16px;
      padding:1.25rem; margin:1.25rem 0; box-shadow:0 4px 6px -1px rgba(0,0,0,.05); }
    .ik-row { display:flex; flex-wrap:wrap; gap:.6rem; align-items:center; margin:.8rem 0; }
    .ik-label { font-weight:700; font-size:.92rem; color:var(--text-main,#0f172a); margin:.9rem 0 .35rem; }
    .ik-help { font-size:.8rem; color:var(--text-muted,#64748b); line-height:1.55; }
    .ik-fileline { display:flex; gap:12px; align-items:center; }
    .ik-fileline img { width:74px; height:74px; object-fit:cover; border-radius:10px;
      border:1px solid #e5e7eb; background:#f8fafc; }
    .ik-compare { display:grid; grid-template-columns:1fr auto 1fr; gap:10px; align-items:center;
      text-align:center; font-weight:800; color:var(--text-main,#0f172a); font-size:1rem; }
    .ik-compare span { display:block; font-weight:600; color:var(--text-muted,#64748b);
      font-size:.85rem; margin-top:4px; }
    .ik-select, .ik-input { padding:9px 12px; border:1px solid #d1d5db; border-radius:8px;
      font-size:.9rem; background:#fff; font-family:inherit; }
    .ik-input { width:110px; }
    .ik-check { display:flex; gap:.5rem; align-items:flex-start; font-size:.88rem;
      color:#374151; line-height:1.5; }
    .ik-verdict { display:flex; gap:.55rem; align-items:flex-start; padding:.55rem .2rem;
      border-bottom:1px dashed #e5e7eb; font-size:.88rem; line-height:1.55; color:#374151; }
    .ik-verdict b.ok { color:#16a34a; }
    .ik-verdict b.no { color:#dc2626; }
    .ilp-outline { background:#fff; border:1.5px solid #d1d5db; padding:11px 18px;
      border-radius:8px; font-weight:700; cursor:pointer; font-family:inherit; font-size:.95rem; }
    .vp-chip { font-size:.75rem; color:#16a34a; font-weight:700; }
    .ik-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:14px; margin:1.2rem 0; }
    .ik-toolcard { border:1px solid #e5e7eb; border-radius:12px; padding:16px; background:#fff; }
    .ik-toolcard:hover { border-color:#fca5a5; box-shadow:0 4px 14px rgba(0,0,0,.05); }
    .ik-toolcard h2 { font-size:1.02rem; margin:0 0 6px; }
    .ik-toolcard h2 a { color:#111827; text-decoration:none; }
    .ik-toolcard h2 a:hover { color:#E5322D; }
    .ik-toolcard p { font-size:.86rem; color:#4b5563; line-height:1.55; margin:0 0 8px; }
    .ik-cta a { display:inline-block; background:#E5322D; color:#fff; padding:10px 18px;
      border-radius:8px; font-weight:700; text-decoration:none; margin:4px 6px 4px 0; font-size:.9rem; }
    .ik-cta a:hover { background:#c8291f; }
    .editorial h2 { font-size:1.15rem; margin-top:1.7rem; color:#111827; }
    .editorial p, .editorial li { font-size:.93rem; line-height:1.7; color:#374151; }
    .editorial table { width:100%; border-collapse:collapse; font-size:.86rem; margin:1rem 0; }
    .editorial th, .editorial td { border:1px solid #e5e7eb; padding:7px 9px; text-align:left; }
    .editorial th { background:#f9fafb; }
    .editorial a { color:#E5322D; }
    .ik-author { display:flex; gap:14px; align-items:flex-start; background:#f9fafb;
      border:1px solid #e5e7eb; border-radius:12px; padding:16px; margin-top:2rem; }
    .ik-faq dt { font-weight:700; margin-top:14px; color:#111827; }
    .ik-faq dd { margin:5px 0 0; color:#374151; line-height:1.65; font-size:.93rem; }
    .ik-warn { background:#fffbeb; border:1px solid #fde68a; color:#92400e; border-radius:10px;
      padding:10px 14px; font-size:.85rem; line-height:1.6; margin:1rem 0; }
  </style>
"""


def extract_block(src, start_marker, end_marker):
    i = src.index(start_marker)
    j = src.index(end_marker, i) + len(end_marker)
    return src[i:j]


def load_shell():
    with open(SNIPPET_SRC, encoding="utf-8") as f:
        src = f.read()
    nav = extract_block(src, '<nav class="ilp-topnav"', "</nav>")
    footer = extract_block(src, '<footer class="footer">', "</footer>")
    k = src.index("(function ilpMegaInit()")
    s0 = src.rindex("<script>", 0, k)
    s1 = src.index("</script>", k) + len("</script>")
    return nav, footer, src[s0:s1]


def load_specs():
    with open(SPECS_PATH, encoding="utf-8") as f:
        return json.load(f)


def head(title, desc, canonical, ld):
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
  <meta http-equiv="X-DNS-Prefetch-Control" content="on">
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
  <meta property="og:type" content="website">
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
{TOOL_STYLE}
  <script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
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
            out.append('      <span>/</span>')
        out.append(f'      <a href="{href}">{label}</a>' if href
                   else f'      <span style="color:var(--text-main);font-weight:600;">{label}</span>')
    out += ['    </nav>', '  </div>']
    return "\n".join(out) + "\n"


def hero(title, subtitle, steps):
    step_html = "".join(
        f'<span class="ilp-step{" active" if i == 0 else ""}"><b>{i+1}</b> {html.escape(s)}</span>'
        for i, s in enumerate(steps))
    return f"""    <div class="vytra-tool-hero" style="text-align:center;">
      <h1 class="vytra-tool-title">{html.escape(title)}</h1>
      <p class="vytra-tool-subtitle">{subtitle}</p>
      <div class="ilp-steps" aria-label="Workflow steps">{step_html}</div>
      <div class="vytra-trust-chips">
        <span class="vytra-trust-chip">&#10003; Free</span>
        <span class="vytra-trust-chip">&#10003; 100% in-browser</span>
        <span class="vytra-trust-chip">&#10003; No signup</span>
        <span class="vytra-trust-chip">&#10003; No upload</span>
      </div>
      <div class="vp-chip" data-vp style="margin-top:10px;">&#128274; Checking network activity&hellip;</div>
    </div>
"""


def dropzone(pick_label, accept, hint):
    return f"""    <div class="ilp-dropzone-large">
      <input type="file" id="fileInput" accept="{accept}" style="display:none;" aria-label="Upload file">
      <div class="vytra-dz-topbar">
        <div class="vytra-dz-secure-badge">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
          <span>File never leaves this device</span>
        </div>
        <div class="vytra-dz-desktop-link"><span>100% In-Browser Privacy</span></div>
      </div>
      <div>
        <button type="button" class="ilp-select-btn" id="btnChoose">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="12" y1="18" x2="12" y2="12"/><polyline points="9 15 12 12 15 15"/></svg>
          <span>{html.escape(pick_label)}</span>
        </button>
      </div>
      <div class="ilp-drop-hint">{hint}</div>
      <div class="ilp-secure"><span>&#128274; Files stay on device</span><span>&#9889; Instant</span><span>&#128241; Mobile ready</span></div>
    </div>
"""


def editorial_block(html_body, word_min=500):
    words = len(re.sub(r"<[^>]+>", " ", html_body).split())
    return f'    <div class="editorial ik-card">\n{html_body}\n    </div>\n', words


def faq_block(faqs, title="Common questions"):
    dl = "\n".join(
        f'      <dt>{html.escape(f[0])}</dt>\n      <dd>{f[1]}</dd>' for f in faqs)
    return f"""    <div class="ik-card">
      <h2 style="font-size:1.15rem;margin-top:0;">{html.escape(title)}</h2>
      <dl class="ik-faq">
{dl}
      </dl>
    </div>
"""


def author_related(related_tools, related_articles):
    tool_links = " ".join(
        f'<a href="../{h}">{html.escape(n)}</a>' for h, n in related_tools)
    art_links = "\n".join(
        f'        <li><a href="../blog/{s}.html">{html.escape(t)}</a></li>' for s, t in related_articles)
    return f"""    <div class="ik-author">
      <div class="vytra-author-avatar" style="flex:0 0 auto;">H</div>
      <div>
        <div style="font-weight:800;">h1k0r</div>
        <div style="font-size:.87rem;color:#64748b;line-height:1.65;margin-top:2px;">
          Independent developer who designs and builds Vytra's tools. Every spec shown here is
          compiled from official notifications &mdash; always verify against the notification you
          are applying under. <a href="../about.html" style="color:#E5322D;">About Vytra</a>
        </div>
      </div>
    </div>
    <div class="ik-card" style="margin-top:1.2rem;">
      <h2 style="font-size:1.1rem;margin-top:0;">Related tools &amp; guides</h2>
      <div class="ik-cta">{tool_links}</div>
      <ul style="margin:.6rem 0 0;padding-left:1.2rem;font-size:.9rem;color:#374151;line-height:1.8;">
{art_links}
      </ul>
    </div>
"""


def specs_js(specs):
    slim = []
    for e in specs["exams"]:
        slim.append({
            "id": e["id"], "name": e["name"],
            "photo": {k: e["photo"][k] for k in e["photo"]},
            "signature": {k: e["signature"][k] for k in e["signature"]},
        })
    return "window.EXAM_SPECS = " + json.dumps(slim, ensure_ascii=False) + ";"


# ----------------------------------------------------------------------------
# Tool page definitions
# ----------------------------------------------------------------------------

RESIZE_SCRIPT = """
  <script src="../assets/js/form-kit.js"></script>
  <script>
  (function(){
    var V = window.VytraImage, img = null, file = null;
    var dz = document.querySelector('.ilp-dropzone-large');
    var ws = document.getElementById('workspace');
    var res = document.getElementById('result');
    var $ = function(id){ return document.getElementById(id); };
    $('btnChoose').addEventListener('click', function(){ $('fileInput').click(); });
    $('fileInput').addEventListener('change', function(e){ if (e.target.files[0]) open(e.target.files[0]); });
    ['dragover','dragenter'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor='#E5322D'; }); });
    ['dragleave','drop'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor=''; }); });
    dz.addEventListener('drop', function(e){ if (e.dataTransfer.files[0]) open(e.dataTransfer.files[0]); });
    $('preset').addEventListener('change', function(){
      var p = this.value;
      if (!p) { $('w').value=''; $('h').value=''; $('kb').value='100'; return; }
      var parts = p.split('|');
      $('kb').value = parts[1];
      var px = (parts[2]||'').split('x');
      $('w').value = px[0]||''; $('h').value = px[1]||'';
      var note = document.getElementById('presetNote');
      note.textContent = parts[3] || '';
    });
    function open(f){
      file = f;
      V.loadFile(f).then(function(im){
        img = im;
        $('preview').src = im.src || URL.createObjectURL(f);
        $('fileName').textContent = f.name;
        $('fileMeta').textContent = im.naturalWidth + ' \u00d7 ' + im.naturalHeight + ' px \u00b7 ' + V.fmtSize(f.size);
        dz.style.display = 'none'; ws.style.display = ''; res.style.display = 'none';
      }).catch(function(){ alert('Could not read that image. Try a JPG or PNG.'); });
    }
    $('btnRun').addEventListener('click', async function(){
      if (!img) return;
      var kb = Math.max(1, parseInt($('kb').value || '100', 10));
      var w = parseInt($('w').value || '0', 10), h = parseInt($('h').value || '0', 10);
      var c;
      if (w && h) { c = V.drawScaled(img, w, h); }
      else { var d = V.fitInto(img.naturalWidth, img.naturalHeight, 2000, 2000); c = V.drawScaled(img, d[0], d[1]); }
      var out = await V.encodeToTarget(c, { targetKB: kb, type: 'image/jpeg' });
      $('beforeSize').textContent = V.fmtSize(file.size);
      $('afterSize').textContent = V.fmtSize(out.blob.size) + (out.ok ? '' : ' (closest possible)');
      $('saved').textContent = out.width + ' \u00d7 ' + out.height + ' px';
      var name = 'Photo_' + Math.round(out.blob.size/1024) + 'KB.jpg';
      var a = $('btnDownload');
      a.href = URL.createObjectURL(out.blob); a.download = name;
      res.style.display = '';
      res.scrollIntoView({behavior:'smooth', block:'center'});
    });
    $('btnAgain').addEventListener('click', function(){ location.reload(); });
  })();
  </script>
"""

SIGNATURE_SCRIPT = """
  <script src="../assets/js/form-kit.js"></script>
  <script>
  (function(){
    var V = window.VytraImage, img = null, file = null;
    var dz = document.querySelector('.ilp-dropzone-large');
    var ws = document.getElementById('workspace');
    var res = document.getElementById('result');
    var $ = function(id){ return document.getElementById(id); };
    $('btnChoose').addEventListener('click', function(){ $('fileInput').click(); });
    $('fileInput').addEventListener('change', function(e){ if (e.target.files[0]) open(e.target.files[0]); });
    ['dragover','dragenter'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor='#E5322D'; }); });
    ['dragleave','drop'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor=''; }); });
    dz.addEventListener('drop', function(e){ if (e.dataTransfer.files[0]) open(e.dataTransfer.files[0]); });
    $('preset').addEventListener('change', function(){
      var p = this.value;
      var note = document.getElementById('presetNote');
      if (!p) { $('kb').value = '15'; note.textContent = ''; return; }
      var parts = p.split('|');
      $('kb').value = parts[1];
      note.textContent = parts[2] || '';
    });
    function open(f){
      file = f;
      V.loadFile(f).then(function(im){
        img = im;
        $('preview').src = URL.createObjectURL(f);
        $('fileName').textContent = f.name;
        $('fileMeta').textContent = im.naturalWidth + ' \u00d7 ' + im.naturalHeight + ' px \u00b7 ' + V.fmtSize(f.size);
        dz.style.display = 'none'; ws.style.display = ''; res.style.display = 'none';
      }).catch(function(){ alert('Could not read that image. Try a JPG or PNG.'); });
    }
    $('btnRun').addEventListener('click', async function(){
      if (!img) return;
      var kb = Math.max(1, parseInt($('kb').value || '15', 10));
      var d = V.fitInto(img.naturalWidth, img.naturalHeight, 1200, 600);
      var c = V.drawScaled(img, d[0], d[1]);
      if ($('whiten').checked) V.whiten(c, 185);
      var out = await V.encodeToTarget(c, { targetKB: kb, type: 'image/jpeg', minQ: 0.4 });
      $('beforeSize').textContent = V.fmtSize(file.size);
      $('afterSize').textContent = V.fmtSize(out.blob.size) + (out.ok ? '' : ' (closest possible)');
      $('saved').textContent = out.width + ' \u00d7 ' + out.height + ' px';
      var name = 'Signature_' + Math.round(out.blob.size/1024) + 'KB.jpg';
      var a = $('btnDownload');
      a.href = URL.createObjectURL(out.blob); a.download = name;
      res.style.display = '';
      res.scrollIntoView({behavior:'smooth', block:'center'});
    });
    $('btnAgain').addEventListener('click', function(){ location.reload(); });
  })();
  </script>
"""

COMPRESS_SCRIPT = """
  <script src="../assets/js/form-kit.js"></script>
  <script>
  (function(){
    var V = window.VytraImage, img = null, file = null;
    var dz = document.querySelector('.ilp-dropzone-large');
    var ws = document.getElementById('workspace');
    var res = document.getElementById('result');
    var $ = function(id){ return document.getElementById(id); };
    $('btnChoose').addEventListener('click', function(){ $('fileInput').click(); });
    $('fileInput').addEventListener('change', function(e){ if (e.target.files[0]) open(e.target.files[0]); });
    ['dragover','dragenter'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor='#E5322D'; }); });
    ['dragleave','drop'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor=''; }); });
    dz.addEventListener('drop', function(e){ if (e.dataTransfer.files[0]) open(e.dataTransfer.files[0]); });
    function open(f){
      file = f;
      V.loadFile(f).then(function(im){
        img = im;
        $('preview').src = URL.createObjectURL(f);
        $('fileName').textContent = f.name;
        $('fileMeta').textContent = im.naturalWidth + ' \u00d7 ' + im.naturalHeight + ' px \u00b7 ' + V.fmtSize(f.size);
        dz.style.display = 'none'; ws.style.display = ''; res.style.display = 'none';
      }).catch(function(){ alert('Could not read that image. Try a JPG or PNG.'); });
    }
    $('btnRun').addEventListener('click', async function(){
      if (!img) return;
      var kb = Math.max(1, parseInt($('kb').value || '100', 10));
      var type = $('fmt').value;
      var c = V.drawScaled(img, img.naturalWidth, img.naturalHeight);
      var out = await V.encodeToTarget(c, { targetKB: kb, type: type, minQ: 0.3 });
      $('beforeSize').textContent = V.fmtSize(file.size);
      $('afterSize').textContent = V.fmtSize(out.blob.size) + (out.ok ? '' : ' (closest possible)');
      $('saved').textContent = out.width + ' \u00d7 ' + out.height + ' px \u00b7 quality ' + Math.round(out.quality*100) + '%';
      var ext = type === 'image/png' ? 'png' : (type === 'image/webp' ? 'webp' : 'jpg');
      var a = $('btnDownload');
      a.href = URL.createObjectURL(out.blob);
      a.download = file.name.replace(/\\.[^.]+$/, '') + '_' + Math.round(out.blob.size/1024) + 'KB.' + ext;
      res.style.display = '';
      res.scrollIntoView({behavior:'smooth', block:'center'});
    });
    $('btnAgain').addEventListener('click', function(){ location.reload(); });
  })();
  </script>
"""

PREFLIGHT_SCRIPT = """
  <script src="../assets/js/form-kit.js"></script>
  <script src="https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js" defer></script>
  <script>
  (function(){
    var V = window.VytraImage, img = null, file = null, fixedBlob = null;
    var dz = document.querySelector('.ilp-dropzone-large');
    var ws = document.getElementById('workspace');
    var $ = function(id){ return document.getElementById(id); };
    $('btnChoose').addEventListener('click', function(){ $('fileInput').click(); });
    $('fileInput').addEventListener('change', function(e){ if (e.target.files[0]) open(e.target.files[0]); });
    ['dragover','dragenter'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor='#E5322D'; }); });
    ['dragleave','drop'].forEach(function(ev){ dz.addEventListener(ev, function(e){ e.preventDefault(); dz.style.borderColor=''; }); });
    dz.addEventListener('drop', function(e){ if (e.dataTransfer.files[0]) open(e.dataTransfer.files[0]); });

    function specFor(){
      var ex = window.EXAM_SPECS.filter(function(e){ return e.id === $('exam').value; })[0];
      return ex ? ex[$('kind').value] : null;
    }
    function open(f){
      file = f; img = null; fixedBlob = null;
      $('verdicts').innerHTML = ''; $('fixbox').style.display = 'none';
      $('fileName').textContent = f.name;
      if (f.type.indexOf('image/') === 0) {
        V.loadFile(f).then(function(im){
          img = im;
          $('preview').src = URL.createObjectURL(f);
          $('preview').style.display = '';
          $('fileMeta').textContent = 'Image \u00b7 ' + im.naturalWidth + ' \u00d7 ' + im.naturalHeight + ' px \u00b7 ' + V.fmtSize(f.size);
          dz.style.display = 'none'; ws.style.display = '';
        });
      } else if (f.type === 'application/pdf') {
        $('preview').style.display = 'none';
        $('fileMeta').textContent = 'PDF \u00b7 ' + V.fmtSize(f.size);
        dz.style.display = 'none'; ws.style.display = '';
      } else {
        alert('This checker handles images (JPG/PNG) and PDFs.');
      }
    }
    function row(ok, label, detail){
      var d = document.createElement('div');
      d.className = 'ik-verdict';
      d.innerHTML = '<b class="' + (ok ? 'ok' : 'no') + '">' + (ok ? '\u2705' : '\u274c') + '</b> ' +
        '<div><strong>' + label + '</strong> \u2014 ' + detail + '</div>';
      $('verdicts').appendChild(d);
    }
    $('btnRun').addEventListener('click', async function(){
      if (!file) return;
      $('verdicts').innerHTML = ''; $('fixbox').style.display = 'none'; fixedBlob = null;
      if (img) {
        var sp = specFor();
        if (!sp) { row(false, 'Exam spec', 'Select an exam first.'); return; }
        var kb = file.size / 1024;
        row(kb >= sp.minKB - 0.5 && kb <= sp.maxKB + 0.5, 'File size',
            kb.toFixed(1) + ' KB \u2014 allowed band ' + sp.minKB + '\u2013' + sp.maxKB + ' KB' +
            (kb < sp.minKB ? ' (below minimum \u2014 portals reject this)' : (kb > sp.maxKB ? ' (over the limit)' : '')));
        var fmtOk = (sp.format === 'JPG') ? /jpe?g/.test(file.type) : true;
        row(fmtOk, 'Format', file.type || 'unknown' + (fmtOk ? '' : ' \u2014 convert to ' + sp.format));
        var ar = img.naturalWidth / img.naturalHeight;
        var sr = sp.ratioNum[0] / sp.ratioNum[1];
        row(Math.abs(ar - sr) / sr <= 0.1, 'Aspect ratio',
            ar.toFixed(2) + ':1 \u2014 expected about ' + sr.toFixed(2) + ':1');
        var tp = (sp.typicalPx || '').split('x');
        var tw = parseInt(tp[0]||'0',10), th = parseInt(tp[1]||'0',10);
        var dimOk = tw ? (Math.abs(img.naturalWidth-tw)/tw <= 0.3 && Math.abs(img.naturalHeight-th)/th <= 0.3) : true;
        row(dimOk, 'Pixel dimensions',
            img.naturalWidth + '\u00d7' + img.naturalHeight + ' px' + (tw ? ' \u2014 portals usually expect about ' + sp.typicalPx + ' px' : ''));
        var white = V.edgeWhiteness(img.__canvas || (img.__canvas = V.drawScaled(img, Math.min(img.naturalWidth,400), Math.min(img.naturalHeight,400))));
        row(white >= 0.55, 'Background',
            Math.round(white*100) + '% of the frame edge looks plain white' +
            (white >= 0.55 ? '' : ' \u2014 use a plain light background'));
        if (sp.note) {
          var n = document.createElement('div');
          n.className = 'ik-warn';
          n.textContent = sp.note + ' Always verify with the official notification.';
          $('verdicts').appendChild(n);
        }
        $('fixbox').style.display = '';
      } else if (file.type === 'application/pdf') {
        row(file.size <= parseInt($('docKb').value||'200',10)*1024, 'File size',
            V.fmtSize(file.size) + ' \u2014 your portal cap input: ' + $('docKb').value + ' KB');
        try {
          var buf = await file.arrayBuffer();
          var enc = false, pages = 0;
          try { var doc = await window.pdfLib.PDFDocument.load(buf); pages = doc.getPageCount(); }
          catch (e) {
            if (String(e).indexOf('Encrypt') > -1) { enc = true; }
            else { var doc2 = await window.pdfLib.PDFDocument.load(buf, {ignoreEncryption:true}); pages = doc2.getPageCount(); }
          }
          row(!enc, 'Encryption', enc ? 'PDF is password-protected \u2014 most portals reject encrypted files' : 'Not password-protected');
          row(pages > 0 && pages <= 10, 'Page count', pages + ' page(s) \u2014 most attachment slots ask for 1\u20133 pages');
        } catch (e) {
          row(false, 'PDF structure', 'Could not parse this PDF \u2014 try repairing it first');
        }
        var tip = document.createElement('div');
        tip.className = 'ik-warn';
        tip.innerHTML = 'To bring this PDF under a size cap, use the <a href="../pdf/compress.html" style="color:#b45309;">Compress PDF tool</a> (Extreme preset for scanned documents).';
        $('verdicts').appendChild(tip);
      }
    });
    $('btnFix').addEventListener('click', async function(){
      if (!img) return;
      var sp = specFor(); if (!sp) return;
      var tp = (sp.typicalPx || '').split('x');
      var tw = parseInt(tp[0]||'0',10) || 400, th = parseInt(tp[1]||'0',10) || 500;
      var sr = sp.ratioNum[0] / sp.ratioNum[1];
      var iw = img.naturalWidth, ih = img.naturalHeight;
      var cw = iw, ch = Math.round(iw / sr);
      if (ch > ih) { ch = ih; cw = Math.round(ih * sr); }
      var c = V.drawScaled(img, cw, ch);
      c = (function(src, w, h){
        var out = document.createElement('canvas');
        out.width = w; out.height = h;
        var x = out.getContext('2d');
        x.imageSmoothingQuality = 'high';
        x.drawImage(src, (w - Math.min(w, Math.round(h * (src.width/src.height)))) / 2, 0, Math.min(w, Math.round(h * (src.width/src.height))), Math.min(h, Math.round(w * (src.height/src.width))));
        return out;
      })(c, tw, th);
      if ($('kind').value === 'signature') V.whiten(c, 185);
      var midKB = Math.round((sp.minKB + sp.maxKB) / 2);
      var out = await V.encodeToTarget(c, { targetKB: midKB, type: 'image/jpeg', minQ: 0.4 });
      fixedBlob = out.blob;
      $('fixResult').innerHTML = 'Fixed: <strong>' + V.fmtSize(out.blob.size) + '</strong> \u00b7 ' +
        out.width + ' \u00d7 ' + out.height + ' px \u00b7 JPG';
      $('btnDlFix').style.display = '';
      $('btnDlFix').href = URL.createObjectURL(out.blob);
      $('btnDlFix').download = ($('kind').value === 'signature' ? 'Signature_' : 'Photo_') + Math.round(out.blob.size/1024) + 'KB.jpg';
    });
    $('btnAgain').addEventListener('click', function(){ location.reload(); });
  })();
  </script>
"""


def tool_pages(specs):
    presets_photo = "|".join(
        f'{e["id"]}|{round((e["photo"]["minKB"]+e["photo"]["maxKB"])/2)}|{e["photo"]["typicalPx"]}|{e["name"]}'
        for e in specs["exams"])
    photo_opts = "".join(
        f'<option value="{e["id"]}|{round((e["photo"]["minKB"]+e["photo"]["maxKB"])/2)}|{e["photo"]["typicalPx"]}|{e["name"]} photo \u2014 {e["photo"]["minKB"]}\u2013{e["photo"]["maxKB"]} KB">{html.escape(e["name"])} photo ({e["photo"]["minKB"]}\u2013{e["photo"]["maxKB"]} KB, ~{e["photo"]["typicalPx"]} px)</option>'
        for e in specs["exams"])
    sig_opts = "".join(
        f'<option value="{e["id"]}|{round((e["signature"]["minKB"]+e["signature"]["maxKB"])/2)}|{e["name"]} signature \u2014 {e["signature"]["minKB"]}\u2013{e["signature"]["maxKB"]} KB">{html.escape(e["name"])} signature ({e["signature"]["minKB"]}\u2013{e["signature"]["maxKB"]} KB)</option>'
        for e in specs["exams"])
    exam_opts = "".join(
        f'<option value="{e["id"]}">{html.escape(e["name"])}</option>' for e in specs["exams"])

    return [
    # ---------------- image/resize.html ----------------
    {
        "dir": "image", "slug": "resize",
        "title": "Photo Resizer \u2014 Set Exact KB &amp; Pixels | Vytra",
        "desc": "Resize form photos to the exact KB and pixel size your exam portal asks for. SSC, IBPS, RRB, UPSC presets. Free, private, in-browser.",
        "h1": "Photo Resizer",
        "tagline": "Set the exact KB <em>and</em> pixels your form asks for \u2014 no signup, nothing uploaded.",
        "steps": ["Select photo", "Exam preset or custom", "Download"],
        "body": f"""    <div class="ik-card" id="workspace" style="display:none;">
      <div class="ik-fileline">
        <img id="preview" alt="Selected photo preview">
        <div><div id="fileName" style="font-weight:700;"></div><div class="ik-help" id="fileMeta"></div></div>
      </div>
      <div class="ik-label">Exam preset (sets KB + pixels automatically)</div>
      <select class="ik-select" id="preset" style="width:100%;max-width:480px;">
        <option value="">Custom \u2014 set KB and pixels yourself</option>
        {photo_opts}
      </select>
      <div class="ik-help" id="presetNote"></div>
      <div class="ik-row">
        <label>Target size <input class="ik-input" id="kb" type="number" min="1" value="100"> KB</label>
        <label>Width <input class="ik-input" id="w" type="number" min="1" placeholder="auto"> px</label>
        <label>Height <input class="ik-input" id="h" type="number" min="1" placeholder="auto"> px</label>
      </div>
      <div class="ik-help">Leave width/height empty to keep your photo's original shape. Set both to force exact portal pixels.</div>
      <div class="ik-row">
        <button class="ilp-select-btn" id="btnRun">Resize &amp; compress to target</button>
        <button class="ilp-outline" id="btnAgain">Start over</button>
      </div>
    </div>
    <div class="ik-card" id="result" style="display:none;">
      <div class="ik-compare">
        <div>Original<span id="beforeSize"></span></div><div>\u2192</div>
        <div>Resized<span id="afterSize"></span></div>
      </div>
      <div class="ik-help" id="saved" style="text-align:center;"></div>
      <div class="ik-row" style="justify-content:center;">
        <a class="ilp-select-btn" id="btnDownload">Download photo</a>
      </div>
    </div>
{dropzone("Choose your photo", "image/jpeg,image/png,image/webp", "... or drag &amp; drop a JPG / PNG here")}
""",
        "script": RESIZE_SCRIPT,
        "editorial": """
      <h2>Why portals reject photos \u2014 and why "it looks fine" is not a spec</h2>
      <p>Indian exam and recruitment portals validate three numbers before a human ever sees your
      photo: the <strong>byte count</strong> (KB band), the <strong>pixel dimensions</strong>, and the
      <strong>aspect ratio</strong>. A photo that "looks perfect" in your gallery fails instantly if it
      is 2.4 MB, or if it is 18 KB when the minimum is 20 KB, or if it is 400&times;400 px when the form
      wants roughly 200&times;230. The gallery app never shows you these three numbers \u2014 which is
      exactly why this tool does.</p>
      <h2>How this resizer works</h2>
      <p>Pick your exam from the preset list: the tool fills in the middle of that exam's usual KB band
      and the typical pixel size, both compiled from recent official notifications (see the
      <a href="../forms/specs.html">Exam Specs Database</a> for sources). Or ignore presets and type your
      own target KB and exact pixels \u2014 portals that ask for "4 cm &times; 2 cm at 96 DPI" are really
      asking for a pixel count, and you can type that directly.</p>
      <p>Behind the scenes the engine draws your photo at the requested size and then
      <strong>binary-searches the JPEG quality</strong> until the output lands at or under your target KB.
      If the smallest acceptable quality still overshoots (rare for photos), it quietly scales the pixels
      down a notch and searches again. You always see the real before/after numbers \u2014 the same
      numbers the portal will count.</p>
      <h2>Pixels, centimetres, DPI \u2014 reading the portal's language</h2>
      <p>Instructions speak three dialects. Some ask in <strong>pixels</strong> ("200&times;230 px") \u2014
      type that straight into the width and height boxes. Some ask in <strong>centimetres</strong>
      ("4 cm &times; 2 cm"), which is a print measurement; screens and portals ultimately store pixels,
      and the typical pixel values in each preset are what those forms actually accept. Some mention
      <strong>DPI</strong>, which only matters for printing, not for upload. If your instruction page
      states an exact pixel size, that number overrides everything else \u2014 including our presets.</p>
      <h2>Presets are guidance; the notification is the law</h2>
      <div class="ik-warn">Limits change between notifications \u2014 SSC has even moved many posts to
      <strong>live webcam photo capture</strong> instead of file uploads. Use the preset as your starting
      point, then verify the exact band in the notification you are applying under.</div>
      <h2>Habits that save an application</h2>
      <ul>
      <li>Land in the <strong>middle</strong> of the KB band, not at its edge \u2014 byte-rounding alone can push a "49.9 KB" file over a 50,000-byte cap.</li>
      <li>Check the final file in your file manager after download; the size written there is what the portal sees.</li>
      <li>Name the download with its size (the tool does this: <em>Photo_31KB.jpg</em>) so deadline-hour uploads are unambiguous.</li>
      <li>Keep your original photo untouched; always work on a copy like this one.</li>
      </ul>
      <p>Everything happens inside this browser tab. No account, no queue, no server storing your
      face \u2014 the privacy badge above counts file-upload requests in real time, and it stays at zero.
      The same flow works identically on a phone browser and a desktop, because resizing a photo for a
      form should never depend on installing software, on a slow café connection, or on creating an
      account you will forget you ever made.</p>
""",
        "faqs": [
            ("Will resizing make my photo look blurry?", "At the pixel sizes portals ask for (around 200\u00d7230), a decent phone photo stays sharp. Blur comes from an out-of-focus original, not from correct resizing."),
            ("My photo is 5 MB. Can this really make it 40 KB?", "Yes \u2014 the combination of correct pixel size and quality search removes the enormous camera-resolution weight. The tool shows you the exact result before you download."),
            ("What if I go under the minimum KB?", "Portals can reject files below the stated minimum too. Aim for the band's middle \u2014 the presets do this automatically."),
            ("Do I need to install anything?", "No. The resizing runs in your browser on phones and computers alike, and your photo never leaves the device."),
        ],
        "related_tools": [("image/signature.html", "Signature Resizer"), ("image/compress.html", "Exact-KB Compressor"), ("forms/preflight.html", "Pre-flight Checker"), ("pdf/compress.html", "Compress PDF")],
        "related_articles": [("ssc-photo-signature-size", "SSC photo & signature size guide"), ("file-size-too-large-error", "File size too large error fix"), ("upsc-document-upload-limits", "UPSC document upload limits")],
    },
    # ---------------- image/signature.html ----------------
    {
        "dir": "image", "slug": "signature",
        "title": "Signature Resizer \u2014 10\u201320KB, White Background | Vytra",
        "desc": "Resize exam signatures to the exact KB band with optional white-background cleanup and ink darkening. SSC, IBPS, RRB, UPSC presets. In-browser.",
        "h1": "Signature Resizer",
        "tagline": "White paper, tight crop, exact KB \u2014 the signature upload forms actually accept.",
        "steps": ["Upload signature", "KB + cleanup", "Download"],
        "body": f"""    <div class="ik-card" id="workspace" style="display:none;">
      <div class="ik-fileline">
        <img id="preview" alt="Selected signature preview">
        <div><div id="fileName" style="font-weight:700;"></div><div class="ik-help" id="fileMeta"></div></div>
      </div>
      <div class="ik-label">Exam preset</div>
      <select class="ik-select" id="preset" style="width:100%;max-width:480px;">
        <option value="">Custom \u2014 set KB yourself</option>
        {sig_opts}
      </select>
      <div class="ik-help" id="presetNote"></div>
      <div class="ik-row">
        <label>Target size <input class="ik-input" id="kb" type="number" min="1" value="15"> KB</label>
      </div>
      <label class="ik-check"><input type="checkbox" id="whiten" checked>
        White-background cleanup \u2014 pushes paper grey to pure white and deepens the ink</label>
      <div class="ik-row">
        <button class="ilp-select-btn" id="btnRun">Resize signature to target</button>
        <button class="ilp-outline" id="btnAgain">Start over</button>
      </div>
    </div>
    <div class="ik-card" id="result" style="display:none;">
      <div class="ik-compare">
        <div>Original<span id="beforeSize"></span></div><div>\u2192</div>
        <div>Signature<span id="afterSize"></span></div>
      </div>
      <div class="ik-help" id="saved" style="text-align:center;"></div>
      <div class="ik-row" style="justify-content:center;">
        <a class="ilp-select-btn" id="btnDownload">Download signature</a>
      </div>
    </div>
{dropzone("Choose your signature photo", "image/jpeg,image/png,image/webp", "... or drag &amp; drop the scanned signature here")}
""",
        "script": SIGNATURE_SCRIPT,
        "editorial": """
      <h2>The signature is the most-rejected upload in Indian forms</h2>
      <p>Photos get attention, signatures get rejected. The typical ask is tiny \u2014 a
      <strong>10\u201320 KB JPG</strong> around 4 cm &times; 2 cm \u2014 and the usual failure is a phone
      photo of a signature on lined paper, taken at an angle, with the paper's shadow visible. The
      portal sees megabytes; the officer sees a grey rectangle. Both problems are fixable here.</p>
      <h2>Shoot it right once, reuse it for years</h2>
      <p>Sign in dark ink on a plain white sheet. Photograph it straight-on in even light \u2014 window
      light beats flash. Crop tight around the signature (no surrounding paper, no fingers). That one
      photo, resized properly, serves SSC, IBPS, RRB and UPSC forms for years.</p>
      <h2>What the white-background cleanup does</h2>
      <p>Real paper under real light photographs as <em>grey</em>, often with a gradient. The cleanup
      pass classifies every pixel: near-white paper is pushed to pure white, deep ink is deepened
      towards black, and everything in between stays untouched. The result reads like a flatbed scan
      of the signature instead of a phone photo of it \u2014 which is what form reviewers expect.</p>
      <h2>Getting the KB band right</h2>
      <p>Signature files are small, so the band is narrow: below the minimum and above the maximum both
      fail. The preset sets the target to the middle of your exam's band (typically 15 KB for the common
      10\u201320 KB window) and the encoder fine-tunes quality to land there. Download, check the size in
      your file manager, upload with confidence. As always: verify the exact band in your notification,
      and check the <a href="../forms/specs.html">Exam Specs Database</a> for sources.</p>
      <h2>Framing: what should surround the signature</h2>
      <p>Crop so the signature fills most of the frame with a small, even white margin \u2014 no other
      text, no date, no page border, no finger. Reviewers compare the scanned signature against the one
      on your application record, so stray context around it only adds noise. Landscape (wide and short)
      is the natural shape for signatures, and every preset here keeps that proportion. If your photo
      contains two signatures or an accidental second stroke, re-shoot rather than crop cleverly: tidy
      source in, tidy output out.</p>
      <h2>Common signature rejections and their real cause</h2>
      <ul>
      <li><strong>"File size outside limits"</strong> \u2014 not cropped tight, or shot at camera-max resolution. Resize here fixes both.</li>
      <li><strong>"Image is blurred / not visible"</strong> \u2014 out-of-focus original or heavy compression applied twice. Start from a sharp photo; this tool compresses once, carefully.</li>
      <li><strong>"Signature does not match"</strong> \u2014 an old signature from a different document. Sign fresh on paper and scan that; never trace or edit a signature's shape.</li>
      </ul>
      <p>One rule above all: never alter what a signature <em>says</em>. Cleaning the paper and setting
      the size is honest preparation; changing the signature itself is fraud, and verification checks
      originals. Re-sign on paper if your style has drifted over the years \u2014 consistency between
      your form signature, your application record and the one you carry to verification is the
      acceptance criterion that actually matters, far beyond any kilobyte band.</p>
""",
        "faqs": [
            ("What KB should my signature be?", "Most notifications ask for 10\u201320 KB JPG. The presets target the middle of that band; always confirm against your notification."),
            ("Will the white-background cleanup remove my signature strokes?", "No \u2014 it only affects near-white paper tones and deep ink tones. Intermediate strokes (the pen's lighter edges) are preserved."),
            ("Should I sign on lined paper?", "No. Plain white paper, dark pen, straight-on photo. Lined paper adds background noise the cleanup cannot fully hide."),
            ("Is my signature stored anywhere?", "No. Everything runs in this browser tab; the file is never uploaded. Close the tab and nothing remains."),
        ],
        "related_tools": [("image/resize.html", "Photo Resizer"), ("image/compress.html", "Exact-KB Compressor"), ("forms/preflight.html", "Pre-flight Checker"), ("pdf/jpg-to-pdf.html", "JPG to PDF")],
        "related_articles": [("ssc-photo-signature-size", "SSC photo & signature size guide"), ("upsc-document-upload-limits", "UPSC document upload limits"), ("file-size-too-large-error", "File size too large error fix")],
    },
    # ---------------- image/compress.html ----------------
    {
        "dir": "image", "slug": "compress",
        "title": "Exact-KB Image Compressor \u2014 Hit Any Target Size | Vytra",
        "desc": "Compress a JPG, PNG or WebP to a target KB you choose \u2014 'under 50KB' or 'between 20 and 50KB' \u2014 via quality binary search. Private, in-browser.",
        "h1": "Exact-KB Image Compressor",
        "tagline": "Tell it the KB number. It finds the quality that hits it.",
        "steps": ["Select image", "Type target KB", "Download"],
        "body": """    <div class="ik-card" id="workspace" style="display:none;">
      <div class="ik-fileline">
        <img id="preview" alt="Selected image preview">
        <div><div id="fileName" style="font-weight:700;"></div><div class="ik-help" id="fileMeta"></div></div>
      </div>
      <div class="ik-row">
        <label>Target size <input class="ik-input" id="kb" type="number" min="1" value="100"> KB</label>
        <label>Output format
          <select class="ik-select" id="fmt">
            <option value="image/jpeg">JPG</option>
            <option value="image/png">PNG</option>
            <option value="image/webp">WebP</option>
          </select>
        </label>
      </div>
      <div class="ik-help">Type the exact number your portal demands \u2014 "under 200 KB" becomes 180, "20\u201350 KB" becomes 35. Dimensions stay unchanged; only encoding adapts.</div>
      <div class="ik-row">
        <button class="ilp-select-btn" id="btnRun">Compress to target</button>
        <button class="ilp-outline" id="btnAgain">Start over</button>
      </div>
    </div>
    <div class="ik-card" id="result" style="display:none;">
      <div class="ik-compare">
        <div>Original<span id="beforeSize"></span></div><div>\u2192</div>
        <div>Compressed<span id="afterSize"></span></div>
      </div>
      <div class="ik-help" id="saved" style="text-align:center;"></div>
      <div class="ik-row" style="justify-content:center;">
        <a class="ilp-select-btn" id="btnDownload">Download image</a>
      </div>
    </div>
""",
        "script": COMPRESS_SCRIPT,
        "editorial": """
      <h2>Presets guess. This tool listens.</h2>
      <p>"Compress to High quality" is a guess about a file it has never seen. But forms don't speak
      in High/Medium/Low \u2014 they speak in <strong>numbers</strong>: photo between 20 and 50 KB,
      signature under 20 KB, attachment under 200 KB. This compressor takes the number as its input.
      Type "50", and it will find the encoding that lands at or under 50 KB \u2014 as close to the line
      as quality allows, without going over.</p>
      <h2>How the binary search works (in plain words)</h2>
      <p>Imagine quality settings from 35% to 95%. The tool encodes at 65%, sees the size, then
      checks 80% or 50% depending on whether it was too small or too big \u2014 halving the search
      range each time. Within a handful of passes it has found the highest quality that still fits
      your target. If even 35% quality overshoots (very heavy images), it scales the pixels down
      slightly and searches again. The result: the best possible quality <em>inside</em> your band.</p>
      <h2>Which format should you pick?</h2>
      <ul>
      <li><strong>JPG</strong> \u2014 the default for photos and nearly every Indian portal's accepted format.</li>
      <li><strong>PNG</strong> \u2014 lossless; useful for screenshots with sharp text. Size control comes only from scaling, so hitting small targets may reduce dimensions.</li>
      <li><strong>WebP</strong> \u2014 modern and efficient, but check your portal accepts it before choosing; many still want JPG only.</li>
      </ul>
      <p>One file at a time is deliberate: form uploads are single files, and seeing each before/after
      pair individually is how you confirm the exact number you will be judged on. Photos taken outdoors
      compress far better than screenshots full of sharp text \u2014 that's why the same target KB looks
      perfect on one file and forces a small downscale on another. Both results are shown honestly,
      including when the tool had to settle for "closest possible" instead of an exact hit.</p>
      <h2>Target the middle of the band</h2>
      <p>If a portal says "20\u201350 KB", type 35, not 49.9. File managers round KB differently than
      portals count bytes, and a file sitting exactly on the ceiling can fail a stricter check. The
      middle of the band is safe from both sides \u2014 this one habit removes an entire category of
      upload errors.</p>
      <h2>What number should I actually type?</h2>
      <ul>
      <li><strong>Photo bands</strong> \u2014 "20\u201350 KB": type 35. "Under 50 KB": type 45.</li>
      <li><strong>Signature bands</strong> \u2014 "10\u201320 KB": type 15.</li>
      <li><strong>Document attachments</strong> \u2014 "max 200 KB": type 180 for margin (documents go through <a href="../pdf/compress.html">Compress PDF</a> instead).</li>
      <li><strong>WhatsApp or email sharing</strong> \u2014 type 100\u2013300 depending on the platform's practical limits.</li>
      </ul>
      <p>Two byte-level details worth knowing: metadata (camera model, date, GPS) is stripped during
      re-encoding \u2014 which both protects your privacy and saves a few KB \u2014 and JPEG dimensions
      never change silently: if the tool had to scale pixels to reach an extreme target, the result line
      says so in plain numbers.</p>
      <h2>Where this fits in the form workflow</h2>
      <p>This tool handles <strong>images</strong>: photos, signatures, scans of certificates saved as
      JPG/PNG. For whole documents, use <a href="../pdf/compress.html">Compress PDF</a>. And before you
      upload anything, run it through the <a href="../forms/preflight.html">Pre-flight Checker</a>, which
      verifies size, pixels, format and background against your exam's compiled rules.</p>
""",
        "faqs": [
            ("Can it compress below a minimum too?", "Yes \u2014 type the band's middle value (for 20\u201350 KB, type 35). The tool targets exactly the number you give it."),
            ("Why did my PNG not get small?", "PNG is lossless \u2014 quality is not adjustable. The tool can only reduce dimensions to hit small targets; convert to JPG for photos."),
            ("Does it work on scanned certificates?", "Yes, for image scans (JPG/PNG). For certificate PDFs use Compress PDF with the Extreme preset."),
            ("Is the image uploaded to a server?", "No. Encoding happens in this tab using the browser's canvas; the privacy badge above counts upload requests and stays at zero."),
        ],
        "related_tools": [("image/resize.html", "Photo Resizer"), ("image/signature.html", "Signature Resizer"), ("pdf/compress.html", "Compress PDF"), ("forms/preflight.html", "Pre-flight Checker")],
        "related_articles": [("file-size-too-large-error", "File size too large error fix"), ("why-pdf-is-so-large", "Why your files are so large"), ("compress-marksheet-under-200kb", "Marksheet under 200KB guide")],
    },
    # ---------------- forms/preflight.html ----------------
    {
        "dir": "forms", "slug": "preflight",
        "title": "Pre-flight Checker \u2014 Verify Files Before Upload | Vytra",
        "desc": "Check your form photo, signature or PDF against your exam's rules before uploading: KB band, pixels, format, background, encryption and page count \u2014 with auto-fix.",
        "h1": "Pre-flight Checker",
        "tagline": "Upload se pehle check karo \u2014 reject hone se pehle fix karo.",
        "steps": ["Pick exam &amp; file", "See \u2705 / \u274c reasons", "Auto-fix or download"],
        "body": f"""    <div class="ik-card" id="workspace" style="display:none;">
      <div class="ik-fileline">
        <img id="preview" alt="File preview" style="display:none;">
        <div><div id="fileName" style="font-weight:700;"></div><div class="ik-help" id="fileMeta"></div></div>
      </div>
      <div class="ik-row">
        <label>Exam
          <select class="ik-select" id="exam">{exam_opts}</select>
        </label>
        <label>File is a
          <select class="ik-select" id="kind">
            <option value="photo">Photo</option>
            <option value="signature">Signature</option>
          </select>
        </label>
        <label id="docKbWrap" style="display:none;">Portal cap <input class="ik-input" id="docKb" type="number" value="200"> KB</label>
      </div>
      <div class="ik-row">
        <button class="ilp-select-btn" id="btnRun">Run pre-flight check</button>
        <button class="ilp-outline" id="btnAgain">Start over</button>
      </div>
      <div id="verdicts" style="margin-top:.6rem;"></div>
      <div id="fixbox" style="display:none;">
        <div class="ik-row">
          <button class="ilp-select-btn" id="btnFix">Auto-fix this file</button>
          <a class="ilp-outline" id="btnDlFix" style="display:none;text-decoration:none;">Download fixed file</a>
        </div>
        <div class="ik-help" id="fixResult"></div>
      </div>
    </div>
{dropzone("Choose the file to verify", "image/jpeg,image/png,image/webp,application/pdf", "... or drag &amp; drop a photo, signature or PDF here")}
""",
        "script": PREFLIGHT_SCRIPT,
        "editorial": """
      <h2>What the portal's error message never tells you</h2>
      <p>"Invalid file" is not a reason \u2014 it's a shrug. By the time a portal rejects your file, you
      may be minutes from a deadline, with no way to know which of six possible rules you broke. This
      checker replaces the shrug with a list: every rule the portal would apply, checked in your
      browser, with a plain reason next to each result.</p>
      <h2>What it checks</h2>
      <ul>
      <li><strong>KB band</strong> \u2014 is the file inside your exam's minimum\u2013maximum window? Files below the minimum fail just as hard as files above the maximum.</li>
      <li><strong>Format</strong> \u2014 JPG where the form demands JPG, not PNG in disguise.</li>
      <li><strong>Aspect ratio</strong> \u2014 photo 4:5-ish, signature wide-and-short. Wrong ratio is a common silent reject.</li>
      <li><strong>Pixel dimensions</strong> \u2014 compared against the typical values for your exam.</li>
      <li><strong>Background</strong> \u2014 the frame edges are sampled to estimate whether your background is actually plain and light, the way most notifications require.</li>
      <li><strong>PDFs</strong> \u2014 file size against your portal's cap, password encryption (most portals refuse encrypted files), and page count.</li>
      </ul>
      <h2>Auto-fix: what it will and won't touch</h2>
      <p>For images, Auto-fix recentres and crops to your exam's aspect ratio, resizes to the typical
      pixel size, applies white-background cleanup for signatures, and encodes to the middle of the KB
      band. It does <strong>not</strong> invent pixels that aren't there: a hopelessly blurry original
      stays blurry \u2014 the checker will tell you that honestly rather than pretending otherwise. For
      PDFs, size fixes route you to <a href="../pdf/compress.html">Compress PDF</a>, which handles the
      document pipeline properly.</p>
      <h2>What a clean run looks like</h2>
      <p>For a photo that's ready, the verdict list reads like a checklist of green ticks: size inside
      the band with the exact number shown, format accepted, ratio within tolerance, dimensions near
      the typical values, background edges measured as plain white. When something fails, the \u274c row
      says what the portal would say <em>and</em> what it means \u2014 "14.8 KB \u2014 allowed band
      20\u201350 KB (below minimum)" instead of a bare rejection. The difference matters: you cannot fix
      a number you were never shown.</p>
      <h2>Honesty: checks are not guarantees</h2>
      <p>This checker applies the compiled rules it can measure locally \u2014 bytes, pixels, ratio,
      format, edge whiteness, encryption, page count. It cannot see everything a portal sees: OCR that
      compares your photo to a past application, validity dates on a certificate, or a rule unique to
      one recruitment's instruction page. Treat a green list as "these mechanical checks pass", and keep
      the live form's instruction page open as the final word. Where they disagree, the form wins \u2014
      always.</p>
      <h2>Specs are compiled, not invented</h2>
      <div class="ik-warn">The rules behind each verdict come from recent official notifications and are
      listed with sources in the <a href="../forms/specs.html" style="color:#92400e;">Exam Specs
      Database</a>. Limits change between notifications \u2014 when your form's instruction page
      disagrees with this tool, <strong>the form wins</strong>. Always verify there.</div>
      <h2>Run it the night before, not the minute before</h2>
      <p>The real value of a pre-flight check is time. Run it the evening before the deadline: if a
      fix is needed, you still have a sharp re-shoot, a scanner, or a fresh signature on clean paper
      available. A check done one minute before submission can only tell you bad news.</p>
""",
        "faqs": [
            ("Which files can it check?", "Photos and signatures as JPG/PNG/WebP, and PDF attachments (size, encryption, page count)."),
            ("What does Auto-fix actually change?", "For images: centre-crop to the exam ratio, resize to typical pixels, whiten the background for signatures, encode to the band's middle. Original file untouched \u2014 you download a copy."),
            ("The tool says \u2705 but the portal still rejects. Why?", "When the portal's own instruction line disagrees with compiled specs, the portal is right \u2014 limits change per notification. Adjust to what the form's page states."),
            ("Is anything uploaded?", "No. All checks run in this tab; the privacy badge counts file-upload requests and stays at zero."),
        ],
        "related_tools": [("image/resize.html", "Photo Resizer"), ("image/signature.html", "Signature Resizer"), ("forms/specs.html", "Exam Specs Database"), ("pdf/compress.html", "Compress PDF")],
        "related_articles": [("file-size-too-large-error", "File size too large error fix"), ("ssc-photo-signature-size", "SSC photo & signature size guide"), ("upsc-document-upload-limits", "UPSC document upload limits")],
    },
    ]


def build_specs_page(specs):
    rows = []
    for e in specs["exams"]:
        p, s = e["photo"], e["signature"]
        rows.append(
            f"""        <tr>
          <td><strong>{html.escape(e['name'])}</strong></td>
          <td>{p['minKB']}\u2013{p['maxKB']} KB, JPG<br><span class="ik-help">~{p['typicalPx']} px, ratio {p['ratioNum'][0]}:{p['ratioNum'][1]}</span></td>
          <td>{s['minKB']}\u2013{s['maxKB']} KB, JPG<br><span class="ik-help">~{s['typicalPx']} px</span></td>
          <td><a href="{e['source']}" target="_blank" rel="noopener">{e['sourceLabel']}</a></td>
        </tr>""")
        if p.get("note") or s.get("note"):
            rows.append(
                f"""        <tr><td colspan="4" class="ik-help" style="background:#f9fafb;"><strong>{html.escape(e['name'])}:</strong> {html.escape(p.get('note',''))} {html.escape(s.get('note',''))}</td></tr>""")
    return f"""    <div class="editorial ik-card">
      <h2 style="margin-top:0;">Exam photo &amp; signature limits \u2014 with sources</h2>
      <p>Every number below is compiled from recent official notifications. <strong>Limits change
      between notifications</strong> \u2014 the instruction page of the exact form you are filling is
      always the final authority. Last compiled: <strong>{specs['updated']}</strong>. Source link in
      every row.</p>
      <table>
        <tr><th>Exam</th><th>Photo</th><th>Signature</th><th>Official source</th></tr>
{chr(10).join(rows)}
      </table>
      <div class="ik-warn">{html.escape(specs['disclaimer'])}</div>
      <h2>How to use this database</h2>
      <p>Find your exam's row, note the KB band and pixel values, then go straight to the
      <a href="../image/resize.html">Photo Resizer</a> / <a href="../image/signature.html">Signature
      Resizer</a> and type those numbers in \u2014 or pick the matching preset, which reads the same
      data. Before uploading, run the <a href="../forms/preflight.html">Pre-flight Checker</a>, which
      applies these very rules and explains each verdict in plain words.</p>
      <h2>Why the numbers are ranges, not single values</h2>
      <p>Because portals really do express limits as bands ("20 KB to 50 KB"), and because byte
      rounding differs between systems \u2014 a file manager's "50KB" may exceed a portal's 50,000-byte
      cap. Ranges with a safe middle are more honest (and more useful) than a single "magic number"
      copied across the internet.</p>
      <h2>Keeping this page honest</h2>
      <p>When a notification changes a limit, this table is updated and the date above moves. If you
      spot a mismatch between a live form and this table, the live form is right \u2014 tell us on the
      <a href="../contact.html">contact page</a> and we will re-verify against the source.</p>
    </div>
"""


def specs_faq():
    return """
    <div class="ik-card">
      <h2 style="font-size:1.15rem;margin-top:0;">Common questions</h2>
      <dl class="ik-faq">
        <dt>Are these limits official?</dt>
        <dd>They are compiled from recent official notifications, with the official source linked per exam. Always verify against the exact notification you are applying under \u2014 limits can change per recruitment.</dd>
        <dt>SSC photo section says "live capture". What does that mean?</dt>
        <dd>Many recent SSC notifications capture your photo live via webcam or phone during the form, instead of accepting an uploaded file. If yours does, follow the form's flow; the 20\u201350 KB band applies when a file upload is asked.</dd>
        <dt>My exam is not listed.</dt>
        <dd>The band structure is usually similar (20\u201350 KB photos, 10\u201320 KB signatures) \u2014 but read your notification's instruction page and type the numbers manually into the resizers.</dd>
        <dt>Do the tools read these numbers automatically?</dt>
        <dd>Yes \u2014 the resizer presets and the Pre-flight Checker read this same data file, so one update refreshes every tool at once.</dd>
      </dl>
    </div>
"""


def hub_image_page():
    return """    <div class="editorial ik-card">
      <h2 style="margin-top:0;">Image tools built for forms, not for Instagram</h2>
      <p>Every Indian application form eventually asks the same three things about your images: a
      <strong>KB band</strong>, a <strong>pixel size</strong>, and a <strong>background</strong>. This
      section exists for exactly those questions \u2014 not for filters or effects.</p>
      <div class="ik-grid">
        <div class="ik-toolcard">
          <h2><a href="resize.html">Photo Resizer</a></h2>
          <p>Set the exact KB and pixels your portal asks for. Exam presets for SSC, IBPS, RRB and UPSC fill both automatically.</p>
          <a href="resize.html" style="color:#E5322D;font-weight:700;">Open \u2192</a>
        </div>
        <div class="ik-toolcard">
          <h2><a href="signature.html">Signature Resizer</a></h2>
          <p>Tight-crop your signature into the 10\u201320 KB band, with white-background cleanup and ink deepening.</p>
          <a href="signature.html" style="color:#E5322D;font-weight:700;">Open \u2192</a>
        </div>
        <div class="ik-toolcard">
          <h2><a href="compress.html">Exact-KB Compressor</a></h2>
          <p>Type any target \u2014 "under 50 KB" \u2014 and the encoder binary-searches quality until it lands there.</p>
          <a href="compress.html" style="color:#E5322D;font-weight:700;">Open \u2192</a>
        </div>
      </div>
      <p>Not sure which one you need? The <a href="../forms/preflight.html">Pre-flight Checker</a>
      inspects your file against your exam's rules and tells you exactly what to fix \u2014 then points
      you to the right tool. Limits and their sources live in the
      <a href="../forms/specs.html">Exam Specs Database</a>.</p>
      <div class="ik-warn">All tools on this site process files inside your browser. Nothing is uploaded
      \u2014 the privacy badge on every tool page counts upload requests in real time.</div>
    </div>
"""


def hub_forms_page():
    return """    <div class="editorial ik-card">
      <h2 style="margin-top:0;">Form-Ready Kit for Indian applicants</h2>
      <p>Generic file tools stop at "we edited your file". Form portals ask a follow-up question:
      <em>does this file follow the rules?</em> The Form-Ready Kit answers it \u2014 every tool here
      knows the KB bands, pixel sizes and formats that SSC, IBPS, RRB and UPSC portals actually
      validate, compiled from official notifications with sources.</p>
      <div class="ik-grid">
        <div class="ik-toolcard">
          <h2><a href="preflight.html">Pre-flight Checker</a></h2>
          <p>Verify photo, signature or PDF against your exam's rules: KB band, pixels, format, background, encryption, page count \u2014 with plain-language reasons and one-click auto-fix.</p>
          <a href="preflight.html" style="color:#E5322D;font-weight:700;">Open \u2192</a>
        </div>
        <div class="ik-toolcard">
          <h2><a href="specs.html">Exam Specs Database</a></h2>
          <p>Every exam's photo and signature limits in one table, each row linked to its official source, with a visible last-compiled date.</p>
          <a href="specs.html" style="color:#E5322D;font-weight:700;">Open \u2192</a>
        </div>
        <div class="ik-toolcard">
          <h2><a href="../image/resize.html">Photo Resizer</a></h2>
          <p>The companion image tool: exact KB + exact pixels, with exam presets that read the same specs database.</p>
          <a href="../image/resize.html" style="color:#E5322D;font-weight:700;">Open \u2192</a>
        </div>
      </div>
      <h2>Exam-specific guides (with the tool pre-set)</h2>
      <p>Each guide below opens the right tool with that exam's preset already active, shows the
      official spec table with sources, and fixes the rejections its candidates actually see:</p>
      <ul style="line-height:2;font-size:.95rem;">
        <li><a href="../ssc-photo-resize-20kb-50kb/">SSC photo resize (20\u201350 KB, exact pixels)</a></li>
        <li><a href="../ibps-signature-resize-20kb/">IBPS signature resize (10\u201320 KB)</a></li>
        <li><a href="../rrb-photo-signature-size/">RRB photo &amp; signature size guide</a></li>
        <li><a href="../compress-pdf-to-100kb/">Compress PDF to under 100 KB</a></li>
        <li><a href="../compress-pdf-to-200kb/">Compress PDF to under 200 KB</a></li>
      </ul>
      <h2>The workflow this kit assumes</h2>
      <ol>
      <li>Read the notification's instruction page once \u2014 note KB bands and pixel asks.</li>
      <li>Resize photo and signature with the matching presets (or manual numbers).</li>
      <li>Run the Pre-flight Checker on every file the night before the deadline.</li>
      <li>Upload the \u2705 files with confidence \u2014 and keep originals untouched for the next form.</li>
      </ol>
      <div class="ik-warn">Exam limits change between notifications. This kit's numbers are compiled
      with sources and dates \u2014 but the instruction page of the live form is always the final
      authority. When they disagree, the form wins.</div>
      <p>Everything runs in your browser: no accounts, no queues, no files on a server. The privacy
      badge on each tool counts file-upload requests since page load \u2014 it stays at zero because
      nothing here has anywhere to upload to.</p>
    </div>
"""


def build_page(p, nav, footer, mega, specs_json_slim):
    crumb_root = "../"
    parts = [(crumb_root, "Home"),
             ("../image/" if p["dir"] == "image" else "../forms/",
              "Image Tools" if p["dir"] == "image" else "Form-Kit"),
             (None, re.sub(r"&amp;", "&", re.sub(r"<[^>]+>", "", p["h1"])))]
    webapp_ld = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": re.sub(r"&amp;", "&", re.sub(r"<[^>]+>", "", p["h1"])),
        "url": f"{SITE}/{p['dir']}/{p['slug']}.html",
        "description": p["desc"],
        "applicationCategory": "MultimediaApplication",
        "operatingSystem": "Any",
        "browserRequirements": "Requires JavaScript",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "author": {"@type": "Person", "name": "h1k0r"},
        "publisher": {"@type": "Organization", "name": "Vytra"},
    }
    bc_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": parts[1][1],
             "item": f"{SITE}/{p['dir']}/"},
            {"@type": "ListItem", "position": 3, "name": parts[2][1],
             "item": f"{SITE}/{p['dir']}/{p['slug']}.html"},
        ],
    }
    page = head(p["title"], p["desc"], f"{SITE}/{p['dir']}/{p['slug']}.html",
                {"@context": "https://schema.org", "@graph": [webapp_ld, bc_ld]})
    page += nav + "\n"
    page += breadcrumb(parts)
    page += hero(p["h1"], p["tagline"], p["steps"])
    page += p["body"]
    ed_html, ed_words = editorial_block(p["editorial"])
    page += ed_html
    page += faq_block(p["faqs"])
    page += author_related(p["related_tools"], p["related_articles"])
    page += f"""  <script>window.EXAM_SPECS = {specs_json_slim};</script>
  {p['script']}
  {footer}
  {mega}
  <script defer src="../data/tools.js"></script>
  <script defer src="../assets/js/common.js"></script>
</body>
</html>
"""
    path = os.path.join(ROOT, p["dir"], p["slug"] + ".html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return path, ed_words


def build_hubs(nav, footer, mega):
    out = []
    # image hub
    p = head("Free Image Tools for Indian Exam Forms | Vytra",
             "Photo Resizer, Signature Resizer and Exact-KB Image Compressor \u2014 client-side image tools built around exam form limits.",
             f"{SITE}/image/",
             {"@context": "https://schema.org", "@type": "WebSite", "name": "Vytra Image Tools",
              "url": f"{SITE}/image/", "author": {"@type": "Person", "name": "h1k0r"}})
    p += nav + "\n"
    p += breadcrumb([("../", "Home"), (None, "Image Tools")])
    p += hero("Image Tools", "Form-ready images: exact KB, exact pixels, clean backgrounds.", ["Pick a tool", "Drop your image", "Download"])
    p += hub_image_page()
    p += f"  {footer}\n  {mega}\n  <script defer src=\"../data/tools.js\"></script>\n  <script defer src=\"../assets/js/common.js\"></script>\n</body>\n</html>\n"
    ipath = os.path.join(ROOT, "image", "index.html")
    with open(ipath, "w", encoding="utf-8", newline="\n") as f:
        f.write(p)
    out.append(ipath)
    # forms hub
    p = head("Form-Ready Kit for Indian Exam Applications | Vytra",
             "Pre-flight Checker and Exam Specs Database \u2014 verify photos, signatures and PDFs against exam rules before uploading.",
             f"{SITE}/forms/",
             {"@context": "https://schema.org", "@type": "WebSite", "name": "Vytra Form-Ready Kit",
              "url": f"{SITE}/forms/", "author": {"@type": "Person", "name": "h1k0r"}})
    p += nav + "\n"
    p += breadcrumb([("../", "Home"), (None, "Form-Kit")])
    p += hero("Form-Ready Kit", "Upload se pehle check karo \u2014 reject hone se pehle fix karo.", ["Check file", "See reasons", "Fix &amp; upload"])
    p += hub_forms_page()
    p += f"  {footer}\n  {mega}\n  <script defer src=\"../data/tools.js\"></script>\n  <script defer src=\"../assets/js/common.js\"></script>\n</body>\n</html>\n"
    fpath = os.path.join(ROOT, "forms", "index.html")
    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(p)
    out.append(fpath)
    return out


def build_specs_html(nav, footer, mega, specs):
    rows = []
    for e in specs["exams"]:
        pn, sn = e["photo"].get("note", ""), e["signature"].get("note", "")
        rows.append(f"""        <tr>
          <td><strong>{html.escape(e['name'])}</strong></td>
          <td>{e['photo']['minKB']}\u2013{e['photo']['maxKB']} KB, {e['photo']['format']}<br><span class="ik-help">~{e['photo']['typicalPx']} px</span></td>
          <td>{e['signature']['minKB']}\u2013{e['signature']['maxKB']} KB, {e['signature']['format']}<br><span class="ik-help">~{e['signature']['typicalPx']} px</span></td>
          <td><a href="{e['source']}" target="_blank" rel="noopener">{e['sourceLabel']}</a></td>
        </tr>""")
        rows.append(f"""        <tr><td colspan="4" class="ik-help" style="background:#f9fafb;">{html.escape((pn + ' ' + sn).strip())}</td></tr>""")
    ed = f"""    <div class="editorial ik-card">
      <h2 style="margin-top:0;">Exam photo &amp; signature limits \u2014 every row with its source</h2>
      <p>These bands are compiled from recent official notifications. <strong>Limits change between
      notifications</strong> \u2014 the instruction page of the exact form you are filling is always the
      final authority. Compiled: <strong>{specs['updated']}</strong>.</p>
      <table>
        <tr><th>Exam</th><th>Photo</th><th>Signature</th><th>Official source</th></tr>
{chr(10).join(rows)}
      </table>
      <div class="ik-warn">{html.escape(specs['disclaimer'])}</div>
      <h2>How to use this database</h2>
      <p>Find your exam's row, note the KB band and pixel values, then open the
      <a href="../image/resize.html">Photo Resizer</a> or <a href="../image/signature.html">Signature
      Resizer</a> \u2014 their presets read this same data file, so one update refreshes every tool at
      once. Before uploading, run the <a href="../forms/preflight.html">Pre-flight Checker</a>, which
      applies these very rules and explains each verdict in plain words with an auto-fix.</p>
      <h2>Why the numbers are ranges, not magic digits</h2>
      <p>Portals express limits as bands ("20 KB to 50 KB"), and byte rounding differs between
      systems \u2014 a file manager's "50KB" can exceed a portal's 50,000-byte cap. A safe middle inside
      the band works on both sides of the check; a single copied "magic number" often sits exactly on
      the edge where rounding bites.</p>
      <h2>Keeping this page honest</h2>
      <p>When a notification changes a limit, this table and the date above are updated together. If a
      live form disagrees with this table, the live form is right \u2014 tell us on the
      <a href="../contact.html">contact page</a> and we will re-verify against the linked source.</p>
    </div>
"""
    page = head("Exam Specs Database \u2014 Photo &amp; Signature Limits | Vytra",
                "Photo and signature KB/pixel limits for SSC, IBPS, RRB and UPSC forms, each row linked to its official source, with last-compiled date.",
                f"{SITE}/forms/specs.html",
                {"@context": "https://schema.org", "@type": "WebPage", "name": "Exam Specs Database",
                 "url": f"{SITE}/forms/specs.html", "author": {"@type": "Person", "name": "h1k0r"}})
    page += nav + "\n"
    page += breadcrumb([("../", "Home"), ("./", "Form-Kit"), (None, "Exam Specs")])
    page += hero("Exam Specs Database",
                 "Har exam ke photo/signature limits \u2014 source link ke saath.", ["Find exam", "Copy limits", "Resize &amp; verify"])
    page += ed
    page += specs_faq()
    page += author_related([("forms/preflight.html", "Pre-flight Checker"), ("image/resize.html", "Photo Resizer"), ("image/signature.html", "Signature Resizer")],
                           [("ssc-photo-signature-size", "SSC photo & signature size guide"), ("upsc-document-upload-limits", "UPSC document upload limits")])
    page += f"  {footer}\n  {mega}\n  <script defer src=\"../data/tools.js\"></script>\n  <script defer src=\"../assets/js/common.js\"></script>\n</body>\n</html>\n"
    path = os.path.join(ROOT, "forms", "specs.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return path


def update_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        s = f.read()
    urls = ["/image/", "/image/resize.html", "/image/signature.html", "/image/compress.html",
            "/forms/", "/forms/preflight.html", "/forms/specs.html"]
    add = []
    for loc in urls:
        full = SITE + loc
        if f"<loc>{full}</loc>" not in s:
            add.append("  <url>\n"
                       f"    <loc>{full}</loc>\n"
                       f"    <lastmod>{TODAY}</lastmod>\n"
                       "    <changefreq>monthly</changefreq>\n"
                       "    <priority>0.8</priority>\n"
                       "  </url>\n")
    if add:
        s = s.replace("</urlset>", "".join(add) + "</urlset>")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
    return len(add)


def main():
    nav, footer, mega = load_shell()
    specs = load_specs()
    specs_json_slim = json.dumps(
        [{"id": e["id"], "name": e["name"],
          "photo": {k: e["photo"][k] for k in ("minKB", "maxKB", "format", "ratioNum", "typicalPx", "note")},
          "signature": {k: e["signature"][k] for k in ("minKB", "maxKB", "format", "ratioNum", "typicalPx", "note")}}
         for e in specs["exams"]], ensure_ascii=False)
    print(f"shell: nav={len(nav)}B footer={len(footer)}B mega={len(mega)}B")
    ok = True
    for p in tool_pages(specs):
        path, words = build_page(p, nav, footer, mega, specs_json_slim)
        flag = "OK " if words >= 500 else "LOW"
        if words < 500:
            ok = False
        print(f"  [{flag}] {os.path.relpath(path, ROOT):<28} editorial {words} words")
    for path in build_hubs(nav, footer, mega):
        print(f"  [OK ] {os.path.relpath(path, ROOT)}")
    spath = build_specs_html(nav, footer, mega, specs)
    print(f"  [OK ] {os.path.relpath(spath, ROOT)}")
    n = update_sitemap()
    print(f"sitemap entries added: {n}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
