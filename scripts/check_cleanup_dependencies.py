import os
import glob
import re
import sys
from collections import defaultdict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# List of all files in project
all_files = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__']]
    for f in files:
        if not f.endswith('.pyc'):
            all_files.append(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

print(f"Scanning references across {len(all_files)} files...")

# Map of target file -> list of (source file, match context)
references = defaultdict(list)

# Regex patterns for links and imports
link_patterns = [
    r'href=["\']([^"\']+)["\']',
    r'src=["\']([^"\']+)["\']',
    r'url\(["\']?([^"\'\)]+)["\']?\)',
    r'import\s+.*?from\s+["\']([^"\']+)["\']',
    r'require\(["\']([^"\']+)["\']\)',
    r'url:\s*["\']([^"\']+)["\']',
    r'fetch\(["\']([^"\']+)["\']\)'
]

for src in all_files:
    if not (src.endswith('.html') or src.endswith('.js') or src.endswith('.css') or src.endswith('.xml')):
        continue
    with open(src, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Check all target files
    for target in all_files:
        if target == src:
            continue
        target_basename = os.path.basename(target)
        
        # Check direct path, relative path, or basename reference
        # Avoid short ambiguous names like 'index.html' matching everything unless specific
        if target in content:
            references[target].append((src, 'direct_path'))
        elif f'/{target}' in content or f'"{target}"' in content or f"'{target}'" in content:
            references[target].append((src, 'quoted_path'))

print("\n--- REFERENCE AUDIT RESULTS ---")
candidates = [
    'jobs/government.html',
    'student/resume.html',
    'student/resume-templates.html',
    'cybercafe/passport-photo.html',
    'cybercafe/signature.html',
    'assets/css/resume-templates.css',
    'assets/js/resume-data.js',
    'assets/js/resume-engine.js',
    'assets/js/resume-templates.js',
    'design-system.html'
]

for cand in candidates:
    refs = references.get(cand, [])
    print(f"\nCandidate: {cand}")
    print(f"  Referenced by {len(refs)} files:")
    for r in refs[:10]:
        print(f"    <- {r[0]} ({r[1]})")

