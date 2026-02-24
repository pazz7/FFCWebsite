#!/usr/bin/env python3
"""
Fix copyright text across all HTML files.
Place this file in your FFCWebsite folder and run it.
"""

import os
import glob

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Working in: {script_dir}")

    if not os.path.isfile('index.html'):
        print("ERROR: index.html not found! Place this script in your FFCWebsite folder.")
        input("Press Enter to close...")
        return

    old_texts = [
        # Double-encoded by PowerShell (Â©)
        'Copyright \u00c2\u00a92022',
        'Copyright \u00c2\u00a92023',
        'Copyright \u00c2\u00a92025',
        'Copyright \u00c2\u00a92026',
        # Normal UTF-8 ©
        'Copyright \u00a92022',
        'Copyright \u00a92023',
        'Copyright \u00a92025',
        'Copyright \u00a92026',
        # Already HTML entity
        'Copyright &copy;2022',
        'Copyright &copy;2023',
        'Copyright &copy;2025',
        # Plain text without symbol
        'Copyright 2022,',
        'Copyright 2023,',
    ]
    new_text = 'Copyright &copy;2026'

    total = 0
    for filepath in glob.glob('*.html'):
        with open(filepath, 'rb') as f:
            content = f.read().decode('utf-8', errors='ignore')

        changed = False
        for old in old_texts:
            if old in content:
                if old.endswith(','):
                    content = content.replace(old, new_text + ',')
                else:
                    content = content.replace(old, new_text)
                changed = True

        if changed:
            with open(filepath, 'wb') as f:
                f.write(content.encode('utf-8'))
            print(f"  \u2713 {filepath}")
            total += 1

    print(f"\nDone! Fixed {total} files.")
    input("Press Enter to close...")

if __name__ == '__main__':
    main()
