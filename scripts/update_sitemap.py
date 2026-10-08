import xml.etree.ElementTree as ET
import os

tree = ET.parse('sitemap.xml')
root = tree.getroot()
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

existing_locs = set()
for url in root.findall('sm:url', ns):
    existing_locs.add(url.find('sm:loc', ns).text.strip())

new_urls = [
    'https://vytra.in/image/jpg-to-pdf.html',
    'https://vytra.in/image/ssc-photo-signature-resize.html',
    'https://vytra.in/image/upsc-photo-signature-resize.html',
    'https://vytra.in/image/ibps-signature-resize.html',
    'https://vytra.in/image/passport-photo-size-india.html'
]

added = 0
for u in new_urls:
    if u not in existing_locs:
        url_elem = ET.SubElement(root, '{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        loc_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        loc_elem.text = u
        lastmod_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
        lastmod_elem.text = '2026-10-08'
        added += 1

# Pretty format
ET.indent(tree, space="  ", level=0)
tree.write('sitemap.xml', encoding='UTF-8', xml_declaration=True)
total = len(root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'))
print(f"[PASS] Added {added} URLs. Total valid URLs in sitemap.xml: {total}")
