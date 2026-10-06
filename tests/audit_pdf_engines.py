import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

tools = [
    'pdf/merge.html', 'pdf/split.html', 'pdf/organize.html', 'pdf/rotate.html', 'pdf/crop.html', 'pdf/page-numbers.html',
    'pdf/pdf-to-word.html', 'pdf/pdf-to-ppt.html', 'pdf/pdf-to-excel.html', 'pdf/word-to-pdf.html', 'pdf/ppt-to-pdf.html', 'pdf/excel-to-pdf.html',
    'pdf/pdf-to-jpg.html', 'pdf/jpg-to-pdf.html', 'pdf/html-to-pdf.html', 'pdf/pdf-a.html',
    'pdf/compress.html', 'pdf/repair.html',
    'pdf/edit.html', 'pdf/sign.html', 'pdf/watermark.html', 'pdf/redact.html', 'pdf/forms.html',
    'pdf/protect.html', 'pdf/unlock.html',
    'pdf/scan-to-pdf.html', 'pdf/ocr.html',
    'pdf/compare.html', 'pdf/info.html',
    'pdf/ai-summarizer.html', 'pdf/translate.html', 'pdf/pdf-to-markdown.html',
    'pdf/workflow.html', 'pdf/extract.html', 'pdf/reorder.html', 'pdf/viewer.html', 'pdf/page-counter.html'
]

print("=" * 70)
print("AUDITING DIGITALSAATHI PDF ENGINES & SCRIPTS")
print("=" * 70)

missing = 0
issues = []

for t in tools:
    if not os.path.exists(t):
        print(f"❌ MISSING: {t}")
        missing += 1
        continue
    
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find external scripts
    src_scripts = re.findall(r'<script\b[^>]*src=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
    # Find inline scripts
    inline_scripts = re.findall(r'<script\b(?![^>]*src=)[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    
    total_inline_len = sum(len(s.strip()) for s in inline_scripts)
    
    # Check key features
    has_file_input = 'type="file"' in content or 'type=\'file\'' in content
    has_upload_zone = 'class="upload-zone"' in content or 'class=\'upload-zone\'' in content
    
    # Check for actual development markers
    has_todo = bool(re.search(r'\b(TODO|FIXME|UNDER_DEVELOPMENT|NOT_IMPLEMENTED)\b', content))
    
    status = "✅"
    notes = []
    if total_inline_len < 1000:
        status = "⚠️"
        notes.append(f"Short JS ({total_inline_len}b)")
    if has_todo:
        status = "❌"
        notes.append("Contains TODO/placeholder code")
    if not has_file_input and t not in ['pdf/scan-to-pdf.html', 'pdf/html-to-pdf.html']:
        status = "⚠️"
        notes.append("No file input")
        
    print(f"{status} {t:<28} | {len(content):>6} bytes | {len(src_scripts)} CDNs | {total_inline_len:>5}b JS | {' '.join(notes)}")

print("=" * 70)
