import os
import glob
from xml.dom import minidom

base_url = "https://vytra.in"

# Discover all html files
html_files = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__', 'scripts', 'tests', 'seo']]
    for f in files:
        if f.endswith('.html'):
            rel_path = os.path.normpath(os.path.join(root, f)).replace('\\', '/')
            if rel_path.startswith('./'):
                rel_path = rel_path[2:]
            html_files.append(rel_path)

html_files = sorted(list(set(html_files)))

xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

# Priority rules
for f in html_files:
    if f == 'index.html':
        priority = '1.0'
        freq = 'daily'
    elif f in ['pdf/index.html', 'image/index.html', 'tools/index.html']:
        priority = '0.95'
        freq = 'weekly'
    elif f.startswith('pdf/'):
        priority = '0.90'
        freq = 'weekly'
    elif f.startswith(('image/', 'developer/', 'calculators/', 'text/', 'utilities/')):
        priority = '0.85'
        freq = 'weekly'
    elif f in ['about.html', 'contact.html']:
        priority = '0.80'
        freq = 'monthly'
    else:
        priority = '0.50'
        freq = 'monthly'
        
    xml_lines.append(f'   <url>')
    xml_lines.append(f'      <loc>{base_url}/{f}</loc>')
    xml_lines.append(f'      <changefreq>{freq}</changefreq>')
    xml_lines.append(f'      <priority>{priority}</priority>')
    xml_lines.append(f'   </url>')

xml_lines.append('</urlset>\n')

with open('sitemap.xml', 'w', encoding='utf-8') as out:
    out.write('\n'.join(xml_lines))

print(f"Generated clean sitemap.xml with {len(html_files)} verified URLs.")
