import os
import shutil
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting DigitalSaathi Safe Cleanup Process...")

# 1. Move/Copy passport-photo and signature to image/
if os.path.exists('cybercafe/passport-photo.html'):
    shutil.copy('cybercafe/passport-photo.html', 'image/passport-photo.html')
    print("✓ Copied cybercafe/passport-photo.html -> image/passport-photo.html")

if os.path.exists('cybercafe/signature.html'):
    shutil.copy('cybercafe/signature.html', 'image/signature.html')
    print("✓ Copied cybercafe/signature.html -> image/signature.html")

# 2. Update image/index.html links
if os.path.exists('image/index.html'):
    with open('image/index.html', 'r', encoding='utf-8') as f:
        img_idx = f.read()
    img_idx = img_idx.replace('../cybercafe/passport-photo.html', 'passport-photo.html')
    img_idx = img_idx.replace('../cybercafe/signature.html', 'signature.html')
    with open('image/index.html', 'w', encoding='utf-8') as f:
        f.write(img_idx)
    print("✓ Updated image/index.html internal links")

# 3. Update sitemap.xml
if os.path.exists('sitemap.xml'):
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        sitemap_lines = f.readlines()
    
    new_sitemap = []
    skip = False
    for line in sitemap_lines:
        if '/jobs/government.html' in line or '/student/resume' in line:
            # Skip the <url> ... </url> block
            continue
        if '<!-- Jobs & Career Hub -->' in line or '<!-- Student & Resume Engine -->' in line:
            continue
        line = line.replace('/cybercafe/passport-photo.html', '/image/passport-photo.html')
        line = line.replace('/cybercafe/signature.html', '/image/signature.html')
        new_sitemap.append(line)
        
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.writelines(new_sitemap)
    print("✓ Cleaned sitemap.xml (removed jobs & student, updated image tools)")

# 4. Update assets/js/common.js SEARCH_REGISTRY
if os.path.exists('assets/js/common.js'):
    with open('assets/js/common.js', 'r', encoding='utf-8') as f:
        common_js = f.read()
        
    # Replace cybercafe category and URLs with Image Tools
    common_js = common_js.replace("url: 'cybercafe/passport-photo.html'", "url: 'image/passport-photo.html'")
    common_js = common_js.replace("category: 'Cyber Café'", "category: 'Image Tools'")
    common_js = common_js.replace("url: 'cybercafe/signature.html'", "url: 'image/signature.html'")
    
    # Remove Resume and Government Jobs from SEARCH_REGISTRY
    # Regex replace the entries
    common_js = re.sub(r'\{\s*title:\s*[\'"]Resume Builder[\s\S]*?\},?\n?', '', common_js)
    common_js = re.sub(r'\{\s*title:\s*[\'"]500\+\s*Resume Templates[\s\S]*?\},?\n?', '', common_js)
    common_js = re.sub(r'\{\s*title:\s*[\'"]Government Jobs 2026[\s\S]*?\},?\n?', '', common_js)
    
    with open('assets/js/common.js', 'w', encoding='utf-8') as f:
        f.write(common_js)
    print("✓ Cleaned assets/js/common.js SEARCH_REGISTRY")

# 5. Remove obsolete folders
folders_to_delete = ['jobs', 'student', 'cybercafe']
for folder in folders_to_delete:
    if os.path.exists(folder):
        shutil.rmtree(folder)
        print(f"✓ Removed folder: {folder}/")

# 6. Remove obsolete assets
assets_to_delete = [
    'assets/css/resume-templates.css',
    'assets/js/resume-data.js',
    'assets/js/resume-engine.js',
    'assets/js/resume-templates.js'
]
for asset in assets_to_delete:
    if os.path.exists(asset):
        os.remove(asset)
        print(f"✓ Removed asset: {asset}")

print("\nSafe Cleanup complete!")
