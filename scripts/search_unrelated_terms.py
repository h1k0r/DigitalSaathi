import os
import glob
import re
import sys
from collections import defaultdict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

keywords = ['jobs', 'government', 'student', 'cyber', 'career', 'scholarship', 'exam', 'vacancy']

results = defaultdict(list)

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__', 'scripts', 'tests', 'seo']]
    for f in files:
        if f.endswith(('.html', '.js', '.css', '.xml')):
            path = os.path.normpath(os.path.join(root, f)).replace('\\', '/')
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                for line_idx, line in enumerate(fp):
                    for kw in keywords:
                        # Match word boundaries
                        if re.search(r'\b' + re.escape(kw) + r'\b', line, re.IGNORECASE):
                            results[path].append((line_idx + 1, kw, line.strip()[:120]))

print("==================================================")
print("SEARCH RESULTS FOR UNRELATED TERMS")
print("==================================================")
for path, matches in sorted(results.items()):
    print(f"\n📄 {path} ({len(matches)} matches):")
    # Show first 5 matches per file
    for m in matches[:5]:
        print(f"   L{m[0]} [{m[1]}]: {m[2]}")
    if len(matches) > 5:
        print(f"   ... and {len(matches) - 5} more matches")

