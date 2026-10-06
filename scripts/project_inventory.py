import os
import glob
import sys
from collections import defaultdict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def scan_project():
    all_files = []
    all_dirs = set()
    
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ['.git', '.gemini', '__pycache__']]
        for d in dirs:
            all_dirs.add(os.path.normpath(os.path.join(root, d)))
        for f in files:
            if not f.endswith('.pyc'):
                all_files.append(os.path.normpath(os.path.join(root, f)))
    
    # Categorize files
    file_tree = defaultdict(list)
    for f in sorted(all_files):
        parts = f.split(os.sep)
        top_level = parts[0] if len(parts) == 1 else parts[0]
        file_tree[top_level].append(f)
        
    print("==================================================")
    print("DIGITALSAATHI COMPLETE PROJECT INVENTORY")
    print("==================================================")
    print(f"Total Folders: {len(all_dirs)}")
    print(f"Total Files (excluding pyc): {len(all_files)}")
    print("--------------------------------------------------")
    
    for folder, files in sorted(file_tree.items()):
        print(f"\n📂 [{folder}] ({len(files)} files):")
        for f in sorted(files):
            size_kb = os.path.getsize(f) / 1024.0
            print(f"   • {f} ({size_kb:.1f} KB)")

if __name__ == '__main__':
    scan_project()
