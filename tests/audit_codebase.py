import os
import glob
import re
import sys
from html.parser import HTMLParser

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 60)
print("DIGITALSAATHI AUTOMATED AUDIT & INSPECTION SUITE")
print("=" * 60)

html_files = sorted(glob.glob('**/*.html', recursive=True))

# Data structures for report
link_report = []
root_relative_issues = []
broken_links = []
dead_hash_links = []
seo_report = []
accessibility_issues = []
html_validation_issues = []
security_issues = []
design_system_issues = []

class CustomHTMLValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.ids = set()
        self.duplicate_ids = []
        self.tag_stack = []
        self.h1_count = 0
        self.headings = []
        self.images_without_alt = []
        self.inputs_without_labels = []
        self.buttons_without_text = []
        self.inline_styles_count = 0
        self.current_tag = None
        self.in_title = False
        self.title_text = ""
        self.meta_desc = ""
        self.canonical = ""
        self.has_viewport = False
        self.has_charset = False
        self.has_lang = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.current_tag = tag

        # Check html lang
        if tag == 'html':
            if 'lang' in attr_dict:
                self.has_lang = True

        # Check meta tags
        if tag == 'meta':
            if 'charset' in attr_dict:
                self.has_charset = True
            if attr_dict.get('name', '').lower() == 'viewport':
                self.has_viewport = True
            if attr_dict.get('name', '').lower() == 'description':
                self.meta_desc = attr_dict.get('content', '')

        if tag == 'link':
            if attr_dict.get('rel', '').lower() == 'canonical':
                self.canonical = attr_dict.get('href', '')

        if tag == 'title':
            self.in_title = True

        # Check duplicate ID
        if 'id' in attr_dict:
            elem_id = attr_dict['id']
            if elem_id in self.ids:
                self.duplicate_ids.append(elem_id)
            else:
                self.ids.add(elem_id)

        # Check Headings
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if tag == 'h1':
                self.h1_count += 1
            self.headings.append(tag)

        # Check Images
        if tag == 'img':
            if 'alt' not in attr_dict or attr_dict['alt'].strip() == '':
                self.images_without_alt.append(attr_dict.get('src', 'unknown_src'))

        # Check Inputs
        if tag in ['input', 'select', 'textarea']:
            inp_type = attr_dict.get('type', 'text')
            if inp_type not in ['hidden', 'submit', 'button', 'reset']:
                if 'id' not in attr_dict and 'aria-label' not in attr_dict and 'aria-labelledby' not in attr_dict and 'placeholder' not in attr_dict:
                    self.inputs_without_labels.append(f"<{tag} name='{attr_dict.get('name','')}' type='{inp_type}'>")

        # Check inline styles
        if 'style' in attr_dict:
            self.inline_styles_count += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data.strip()

print(f"\n1. AUDITING {len(html_files)} HTML FILES...")

for hf in html_files:
    dir_name = os.path.dirname(hf)
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Parse HTML
    parser = CustomHTMLValidator(hf)
    try:
        parser.feed(content)
    except Exception as e:
        html_validation_issues.append((hf, f"Parser error: {e}"))

    # Validate DOCTYPE & basic structure
    if not content.strip().lower().startswith('<!doctype html>'):
        html_validation_issues.append((hf, "Missing <!DOCTYPE html>"))
    if not parser.has_lang:
        html_validation_issues.append((hf, "Missing lang attribute on <html>"))
    if not parser.has_charset:
        html_validation_issues.append((hf, "Missing <meta charset='UTF-8'>"))
    if not parser.has_viewport:
        html_validation_issues.append((hf, "Missing <meta name='viewport'>"))
    if not parser.title_text:
        seo_report.append((hf, "MISSING_TITLE", "Page has empty or missing <title>"))
    else:
        seo_report.append((hf, "TITLE", parser.title_text))

    if not parser.meta_desc:
        seo_report.append((hf, "MISSING_DESC", "Page has missing meta description"))

    if parser.duplicate_ids:
        html_validation_issues.append((hf, f"Duplicate IDs found: {parser.duplicate_ids}"))

    if parser.h1_count == 0:
        accessibility_issues.append((hf, "Missing <h1> heading"))
    elif parser.h1_count > 1:
        accessibility_issues.append((hf, f"Multiple <h1> headings found ({parser.h1_count})"))

    if parser.images_without_alt:
        accessibility_issues.append((hf, f"Images missing alt text: {parser.images_without_alt}"))

    if parser.inputs_without_labels:
        accessibility_issues.append((hf, f"Inputs missing accessibility labels: {parser.inputs_without_labels}"))

    # Link extraction via regex (strip script tags first to avoid matching dynamic JS template literals)
    content_no_scripts = re.sub(r'<script\b[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content_no_scripts)
    for l in links:
        if l.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:', 'blob:', '${')):
            continue
        if l.startswith('#'):
            if l == '#' and ('class="btn' in content or '<a href="#">' in content):
                dead_hash_links.append((hf, l))
            continue

        is_root_relative = l.startswith('/')
        if is_root_relative:
            root_relative_issues.append((hf, l))
            target_clean = l.lstrip('/').split('#')[0].split('?')[0]
            disk_target = os.path.normpath(target_clean)
        else:
            clean_l = l.split('#')[0].split('?')[0]
            if not clean_l:
                continue
            disk_target = os.path.normpath(os.path.join(dir_name, clean_l))

        # Check if disk file exists
        if not os.path.exists(disk_target):
            broken_links.append((hf, l, disk_target))
        else:
            link_report.append((hf, l, "PASS"))

    # Security check: search for inline eval, API keys, unsafe innerHTML
    if 'eval(' in content:
        security_issues.append((hf, "Use of eval() detected in inline script"))
    if 'api_key' in content.lower() or 'secret_key' in content.lower():
        security_issues.append((hf, "Potential API key reference in code"))

    # CSS check: verify if assets/css/style.css is linked
    if 'style.css' not in content:
        design_system_issues.append((hf, "Does not include style.css"))

    # Check for excessive inline styles
    if parser.inline_styles_count > 15:
        design_system_issues.append((hf, f"High number of inline styles ({parser.inline_styles_count}) bypassing design system CSS"))

print(f"Total internal link occurrences checked: {len(link_report) + len(broken_links)}")
print(f"Total broken links: {len(broken_links)}")
if broken_links:
    for src_file, link, target in broken_links:
        print(f"  ❌ BROKEN in {src_file}: '{link}' (Looked for: {target})")

print(f"\nTotal Root-Relative links (Potential GitHub Pages issue): {len(root_relative_issues)}")
if root_relative_issues:
    # Print distinct list
    distinct_rr = set(root_relative_issues)
    print(f"  Found {len(distinct_rr)} unique root-relative link patterns across pages:")
    for src_file, link in sorted(list(distinct_rr))[:15]:
        print(f"  ⚠️  {src_file} -> {link}")

print(f"\nTotal Dead '#' href links: {len(dead_hash_links)}")
if dead_hash_links:
    for src_file, link in dead_hash_links[:10]:
        print(f"  ⚠️  {src_file} has placeholder href='#'")

print(f"\nHTML Validation & Accessibility Issues: {len(html_validation_issues) + len(accessibility_issues)}")
for src_file, issue in html_validation_issues:
    print(f"  ⚠️ HTML [VALIDATION] in {src_file}: {issue}")
for src_file, issue in accessibility_issues:
    print(f"  ⚠️ A11Y [ACCESSIBILITY] in {src_file}: {issue}")

print(f"\nSEO Missing Metadata Issues:")
missing_seo = [item for item in seo_report if item[1].startswith('MISSING')]
for src_file, issue_type, desc in missing_seo:
    print(f"  ⚠️ SEO in {src_file}: {desc}")

print(f"\nDesign System Inconsistencies:")
for src_file, issue in design_system_issues:
    print(f"  ⚠️ DESIGN in {src_file}: {issue}")

print(f"\nSecurity Issues: {len(security_issues)}")
for src_file, issue in security_issues:
    print(f"  ⚠️ SECURITY in {src_file}: {issue}")

print("\n" + "=" * 60)
print("AUDIT SCRIPT RUN COMPLETE")
print("=" * 60)
