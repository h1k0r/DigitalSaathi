import glob, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

nav_patterns = {}
no_nav = []

for f in glob.glob('**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    nav_match = re.search(r'<nav[^>]*>([\s\S]*?)</nav>', content)
    if nav_match:
        nav_text = nav_match.group(1)
        links = re.findall(r'<a[^>]*class=["\']nav-link[^"\']*["\'][^>]*>(.*?)</a>', nav_text)
        clean_links = [re.sub(r'<[^>]+>', '', l).strip() for l in links]
        key = ' | '.join(clean_links)
        if key not in nav_patterns:
            nav_patterns[key] = []
        nav_patterns[key].append(f)
    else:
        no_nav.append(f)

print(f"Total files checked: {len(glob.glob('**/*.html', recursive=True))}")
print(f"Files without nav: {no_nav}")
print("\nUnique Navbar Structures Found:")
for i, (p, files) in enumerate(nav_patterns.items(), 1):
    print(f"\n--- Pattern {i} ({len(files)} files) ---")
    print(f"Links: {p}")
    print(f"Files: {files[:3]} ...")
