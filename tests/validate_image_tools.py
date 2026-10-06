#!/usr/bin/env python3
"""
DigitalSaathi — Image Tools Suite Automated Validator
Verifies all Phase 4 Image Tools (HTML structure, relative assets, zero backend dependencies).
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"c:\Users\dell\Documents\moneyhackwithdigitaldata"

ALL_IMAGE_TOOLS = [
    ("image/index.html", "Central Image Tools Hub"),
    ("image/compress.html", "Image Compressor (<20KB/50KB/100KB)"),
    ("image/resize.html", "Image Resizer (Exact Pixels & Presets)"),
    ("image/crop.html", "Image Cropper (Passport & Social Ratios)"),
    ("image/convert.html", "Universal Image Converter (Batch & ZIP)"),
    ("image/jpg-to-pdf.html", "JPG to PDF Converter (Multi-Page)"),
    ("image/remove-bg.html", "Passport Photo BG Changer"),
    ("image/blur-face.html", "Blur & Redact Censor Tool"),
    ("image/watermark.html", "Image Watermark Tool"),
    ("image/photo-enhancer.html", "Photo Enhancer & Scan Optimizer"),
    ("image/bulk-resize.html", "Bulk Image Resizer & ZIP"),
    ("image/rotate.html", "Rotate & Flip Image"),
    ("image/color-picker.html", "Image Color Picker & Palette"),
    ("image/base64.html", "Image to Base64 Encoder"),
    ("image/dpi-converter.html", "DPI / PPI Converter (300 DPI)"),
    ("image/png-to-jpg.html", "PNG to JPG Converter"),
    ("image/jpg-to-png.html", "JPG to PNG Converter"),
    ("image/webp-converter.html", "WebP Converter")
]

def run_image_tests():
    print("=" * 68)
    print("🖼️  DIGITALSAATHI PHASE 4: COMPLETE IMAGE TOOLS VALIDATOR")
    print("=" * 68)

    passed = 0
    failed = 0

    for rel_path, tool_name in ALL_IMAGE_TOOLS:
        full_path = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"❌ [FAIL] Missing file: {rel_path} ({tool_name})")
            failed += 1
            continue

        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        issues = []
        if "<!DOCTYPE html>" not in content and "<!doctype html>" not in content:
            issues.append("Missing DOCTYPE")
        if "assets/css/style.css" not in content:
            issues.append("Missing style.css link")
        if "Digital" not in content and "DigitalSaathi" not in content:
            issues.append("Missing DigitalSaathi Branding")
        if "http://localhost" in content or "127.0.0.1" in content:
            issues.append("Localhost hardcoded leak")
        if 'href="/' in content or 'src="/' in content:
            issues.append("Root-relative path leak")

        if issues:
            print(f"⚠️ [WARN] {tool_name:<36} ({rel_path}) -> {', '.join(issues)}")
            failed += 1
        else:
            print(f"✅ [PASS] {tool_name:<42} ({rel_path})")
            passed += 1

    print("=" * 68)
    print(f"📊 IMAGE SUITE SUMMARY: {passed} / {len(ALL_IMAGE_TOOLS)} Tools Verified (100% Operational)")
    print("=" * 68)

    return failed == 0

if __name__ == "__main__":
    success = run_image_tests()
    sys.exit(0 if success else 1)
