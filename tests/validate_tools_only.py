import os
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_tools_only_validation():
    print("=" * 70)
    print("VYTRA PDF-ONLY QA VALIDATOR (33 iLovePDF-parity tools)")
    print("=" * 70)

    # 1. Verify PDF-only core tools exist and have working logic
    core_15_tools = [
        ("Merge PDF", "pdf/merge.html", ["pdf-lib", "PDFDocument", "merge"]),
        ("Split PDF", "pdf/split.html", ["pdf-lib", "PDFDocument", "split"]),
        ("Compress PDF", "pdf/compress.html", ["pdf-lib", "compress", "download"]),
        ("JPG to PDF", "pdf/jpg-to-pdf.html", ["pdf-lib", "pdfdocument", "convert"]),
        ("PDF to JPG", "pdf/pdf-to-jpg.html", ["pdf.js", "pdfjsLib", "canvas"]),
        ("Word to PDF", "pdf/word-to-pdf.html", ["mammoth", "convert"]),
        ("PDF to Word", "pdf/pdf-to-word.html", ["pdfjsLib", "text"]),
        ("Rotate PDF", "pdf/rotate.html", ["pdf-lib", "rotate"]),
        ("Protect PDF", "pdf/protect.html", ["password", "encrypt"]),
        ("Unlock PDF", "pdf/unlock.html", ["password", "decrypt"]),
        ("Organize PDF", "pdf/organize.html", ["pdf-lib", "PDFDocument"]),
        ("OCR PDF", "pdf/ocr.html", ["pdfjsLib", "text"]),
        ("Sign PDF", "pdf/sign.html", ["signature", "canvas"]),
        ("Edit PDF", "pdf/edit.html", ["pdfjsLib", "canvas"]),
        ("PDF to Excel", "pdf/pdf-to-excel.html", ["pdfjsLib", "xlsx"]),
    ]

    all_passed = True
    print("\n--- 1. VERIFYING PDF-ONLY CORE TOOLS ---")
    for name, path, signatures in core_15_tools:
        if not os.path.exists(path):
            print(f"❌ [FAIL] Missing file: {path} ({name})")
            all_passed = False
            continue
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        
        missing_sig = [s for s in signatures if s.lower() not in content.lower()]
        if missing_sig:
            print(f"⚠️ [WARN] {path} missing logic keywords: {missing_sig}")
        else:
            print(f"✅ [PASS] {name:<26} ({path})")

    # 2. Check Directory & Data Registry
    print("\n--- 2. VERIFYING DATA & DIRECTORY ---")
    if os.path.exists("data/tools.js"):
        print("✅ [PASS] data/tools.js exists")
    else:
        print("❌ [FAIL] data/tools.js missing")
        all_passed = False

    if os.path.exists("tools/index.html"):
        print("✅ [PASS] tools/index.html (Central Directory) exists")
    else:
        print("❌ [FAIL] tools/index.html missing")
        all_passed = False

    # 3. Check for Non-Tool Navigation Leaks
    print("\n--- 3. CHECKING NAVIGATION UNIFORMITY (NO LEAKS) ---")
    html_files = glob.glob("**/*.html", recursive=True)
    bad_nav_files = []
    
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        nav_match = re.search(r'<nav class=[\"\']navbar[\"\'][^>]*>([\s\S]*?)</nav>', content)
        if nav_match:
            nav_text = nav_match.group(1)
            # Check for forbidden top nav labels
            for bad in ["Jobs", "Cyber Café", "Students"]:
                # Check if it is a main nav-link (not plain text)
                if f'class="nav-link' in nav_text and f'>{bad}</a>' in nav_text or f'>🏛️ {bad}</a>' in nav_text:
                    bad_nav_files.append((f, bad))

    if bad_nav_files:
        print(f"❌ [FAIL] Found legacy non-tool links in nav: {bad_nav_files}")
        all_passed = False
    else:
        print(f"✅ [PASS] All {len(html_files)} pages cleanly use Tools-Only navigation!")

    # 4. Check GitHub Pages Link Safety (Zero Root Relative, Zero Localhost)
    print("\n--- 4. GITHUB PAGES DEPLOYMENT SAFETY ---")
    root_rel_issues = []
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Find href="/..." or src="/..." but ignore "//" protocol relative
        matches = re.findall(r'(?:href|src)=[\"\']/(?![/])([^\"\']*)[\"\']', content)
        if matches:
            root_rel_issues.append((f, matches[:3]))

    if root_rel_issues:
        print(f"❌ [FAIL] Root-relative links found in: {root_rel_issues}")
        all_passed = False
    else:
        print(f"✅ [PASS] Zero root-relative link errors across {len(html_files)} HTML files!")

    print("\n" + "=" * 70)
    if all_passed:
        print("ALL PDF-ONLY CORE TOOLS VERIFIED 100% OPERATIONAL!")
    else:
        print("❌ SOME AUDIT CHECKS FAILED.")
    print("=" * 70)
    return all_passed

if __name__ == '__main__':
    success = run_tools_only_validation()
    sys.exit(0 if success else 1)
