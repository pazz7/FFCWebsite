#!/usr/bin/env python3
"""
Fix all double/triple-encoded characters in HTML files.
Fixes: Â® â€" â€™ Â© and other mojibake characters.
Place this file in your FFCWebsite folder and run it.
"""

import os
import glob

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Working in: {script_dir}")

    if not os.path.isfile('index.html'):
        print("ERROR: index.html not found!")
        input("Press Enter to close...")
        return

    # All known mojibake patterns -> correct HTML entities or characters
    replacements = [
        # Double-encoded (Â + character)
        ('\u00c2\u00ae', '&reg;'),       # Â® -> ®
        ('\u00c2\u00a9', '&copy;'),      # Â© -> ©

        # Triple-encoded (â€ + character)
        ('\u00e2\u20ac\u201d', '&ndash;'),   # â€" (em-dash) -> –
        ('\u00e2\u20ac\u201c', '&ndash;'),   # â€" (en-dash) -> –
        ('\u00e2\u20ac\u2122', "'"),          # â€™ (right single quote) -> '
        ('\u00e2\u20ac\u2019', "'"),          # â€™ (right single quote variant) -> '
        ('\u00e2\u20ac\u0153', '&ldquo;'),   # â€œ (left double quote) -> "
        ('\u00e2\u20ac\u009d', '&rdquo;'),   # â€ (right double quote) -> "
        ('\u00e2\u20ac\u00a2', '&bull;'),    # â€¢ (bullet) -> •
    ]

    total = 0
    for filepath in sorted(glob.glob('*.html')):
        with open(filepath, 'rb') as f:
            content = f.read().decode('utf-8', errors='ignore')

        changed = False
        fixes = []
        for old, new in replacements:
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                fixes.append(f"{new} x{count}")
                changed = True

        if changed:
            with open(filepath, 'wb') as f:
                f.write(content.encode('utf-8'))
            print(f"  \u2713 {filepath}: {', '.join(fixes)}")
            total += 1

    if total == 0:
        print("  No encoding issues found!")
    else:
        print(f"\nDone! Fixed {total} file(s).")

    input("Press Enter to close...")

if __name__ == '__main__':
    main()
