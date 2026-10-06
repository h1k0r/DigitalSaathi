import os
import glob
import re
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base_url = "https://digitalsaathi.com"

# Scan all html files
html_files = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__', 'scripts', 'tests', 'seo']]
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

print(f"Injecting top-tier SEO across {len(html_files)} HTML pages...")

updated_count = 0

for file_path in sorted(html_files):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
        
    orig_content = content
    rel_url = file_path.lstrip('./')
    canonical_url = f"{base_url}/{rel_url}"
    
    # Extract Title
    title_m = re.search(r'<title>([^<]+)</title>', content, re.IGNORECASE)
    title = title_m.group(1).strip() if title_m else "DigitalSaathi — Free Online Tools"
    clean_title = title.replace(' | DigitalSaathi', '').replace(' — DigitalSaathi', '').replace(' - DigitalSaathi', '')
    
    # Extract Description
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if not desc_m:
        desc_m = re.search(r'<meta\s+content=["\']([^"\']+)["\']\s+name=["\']description["\']', content, re.IGNORECASE)
    desc = desc_m.group(1).strip() if desc_m else "Free, secure, and fast browser-based online tool by DigitalSaathi. Zero server uploads."
    
    # 1. Ensure Canonical
    if '<link rel="canonical"' not in content and "<link rel='canonical'" not in content:
        canonical_tag = f'  <link rel="canonical" href="{canonical_url}">\n'
        # Insert before </head> or after description
        if '</head>' in content:
            content = content.replace('</head>', f'{canonical_tag}</head>', 1)
            
    # 2. Ensure Open Graph & Twitter Cards
    if '<meta property="og:title"' not in content and "<meta property='og:title'" not in content:
        og_tags = f'''  <!-- Open Graph / Social Media Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:site_name" content="DigitalSaathi">
  
  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
'''
        if '</head>' in content:
            content = content.replace('</head>', f'{og_tags}</head>', 1)
            
    # 3. Ensure Schema.org JSON-LD Structured Data
    if '<script type="application/ld+json">' not in content:
        if rel_url == 'index.html':
            schema_json = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "WebSite",
                        "@id": f"{base_url}/#website",
                        "url": f"{base_url}/",
                        "name": "DigitalSaathi",
                        "description": "Free Online Tools for Everyday Digital Work. Convert, compress, edit, calculate, and manage files directly in your web browser.",
                        "potentialAction": {
                            "@type": "SearchAction",
                            "target": f"{base_url}/tools/index.html?q={{search_term_string}}",
                            "query-input": "required name=search_term_string"
                        }
                    },
                    {
                        "@type": "Organization",
                        "@id": f"{base_url}/#organization",
                        "name": "DigitalSaathi",
                        "url": f"{base_url}/",
                        "logo": f"{base_url}/assets/images/logo.png"
                    },
                    {
                        "@type": "FAQPage",
                        "mainEntity": [
                            {
                                "@type": "Question",
                                "name": "Are DigitalSaathi tools 100% free?",
                                "acceptedAnswer": {
                                    "@type": "Answer",
                                    "text": "Yes, all DigitalSaathi tools are completely free to use without restrictions, subscriptions, or hidden charges."
                                }
                            },
                            {
                                "@type": "Question",
                                "name": "Are my files secure and private?",
                                "acceptedAnswer": {
                                    "@type": "Answer",
                                    "text": "All processing executes locally in your browser using WebAssembly and client-side JavaScript. Your files are never uploaded to any server."
                                }
                            }
                        ]
                    }
                ]
            }
        elif rel_url.startswith(('pdf/', 'image/', 'developer/', 'calculators/', 'text/', 'utilities/')) and not rel_url.endswith('index.html'):
            # Tool page schema
            cat_name = "UtilitiesApplication"
            if rel_url.startswith('calculators/'):
                cat_name = "FinanceApplication"
            elif rel_url.startswith('developer/'):
                cat_name = "DeveloperApplication"
                
            schema_json = {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "WebApplication",
                        "name": title,
                        "url": canonical_url,
                        "description": desc,
                        "applicationCategory": cat_name,
                        "operatingSystem": "All (Web Browser)",
                        "offers": {
                            "@type": "Offer",
                            "price": "0",
                            "priceCurrency": "INR"
                        }
                    },
                    {
                        "@type": "BreadcrumbList",
                        "itemListElement": [
                            {
                                "@type": "ListItem",
                                "position": 1,
                                "name": "Home",
                                "item": f"{base_url}/"
                            },
                            {
                                "@type": "ListItem",
                                "position": 2,
                                "name": rel_url.split('/')[0].capitalize() + " Tools",
                                "item": f"{base_url}/{rel_url.split('/')[0]}/index.html" if os.path.exists(f"{rel_url.split('/')[0]}/index.html") else f"{base_url}/tools/index.html"
                            },
                            {
                                "@type": "ListItem",
                                "position": 3,
                                "name": clean_title,
                                "item": canonical_url
                            }
                        ]
                    }
                ]
            }
        else:
            # Standard page schema
            schema_json = {
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": title,
                "url": canonical_url,
                "description": desc
            }
            
        schema_tag = f'''  <!-- Top Ranking Structured Data Schema -->
  <script type="application/ld+json">
{json.dumps(schema_json, indent=2)}
  </script>
'''
        if '</head>' in content:
            content = content.replace('</head>', f'{schema_tag}</head>', 1)
            
    if content != orig_content:
        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(content)
        updated_count += 1

print(f"Universal SEO successfully injected across {updated_count} pages!")
