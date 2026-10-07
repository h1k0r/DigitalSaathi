import glob
import re

html_files = sorted(glob.glob('**/*.html', recursive=True))

blocking_lines = []

for f in html_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines):
        if '<script' in line and 'src=' in line:
            line_lower = line.lower()
            if 'async' not in line_lower and 'defer' not in line_lower:
                m = re.search(r'src=["\']([^"\']+)["\']', line)
                if m:
                    blocking_lines.append((f, idx + 1, m.group(1), line.strip()))

print(f"Total blocking script tags: {len(blocking_lines)}")
for f, lineno, src, full in blocking_lines:
    print(f"{f}:{lineno} -> {src}")
