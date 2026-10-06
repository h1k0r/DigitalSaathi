import glob
import re
from collections import defaultdict

with open('missing_classes.txt', 'r', encoding='utf-8') as f:
    missing_classes = [line.strip() for line in f if line.strip()]

usage = defaultdict(list)
for html_file in glob.glob('**/*.html', recursive=True):
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            for cls in missing_classes:
                if f'class="{cls}"' in line or f'class=\'{cls}\'' in line or f' {cls} ' in line or f'"{cls} ' in line or f' {cls}"' in line or f"'{cls} " in line or f" {cls}'" in line:
                    if len(usage[cls]) < 3:
                        usage[cls].append((html_file, idx + 1, line.strip()[:100]))

with open('missing_classes_context.txt', 'w', encoding='utf-8') as out:
    for cls in sorted(missing_classes):
        out.write(f'=== Class: {cls} (found in {len(usage[cls])} locations) ===\n')
        for loc in usage[cls]:
            out.write(f'  {loc[0]}:{loc[1]} -> {loc[2]}\n')
        out.write('\n')

print('Wrote missing_classes_context.txt')
