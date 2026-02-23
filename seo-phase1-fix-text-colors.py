#!/usr/bin/env python3
"""
SEO Phase 1 - Bonus: Fix light text on white backgrounds
Fusion Fitness Club Website

Fixes readability issues on class pages and footer sections.
Run from your website root directory.
"""

import os
import glob

# Text color fixes to apply across all HTML files
REPLACEMENTS = [
    # Class description sections - #383838 is okay but let's make it darker for better readability
    # The real issue is the footer sidebar text using data-skin "White Text" on white bg
    # Let's darken the class description text from #383838 to #2a2a2a for better contrast
    (
        'style="font-size: 19px; font-weight: 400; text-transform: none; color: #383838;"',
        'style="font-size: 19px; font-weight: 400; text-transform: none; color: #2a2a2a;"'
    ),
]


def fix_colors(root_dir):
    total_fixes = 0

    for filepath in glob.glob(os.path.join(root_dir, '*.html')):
        filename = os.path.basename(filepath)

        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"  ERROR reading {filename}: {e}")
            continue

        file_fixes = 0
        for old, new in REPLACEMENTS:
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                file_fixes += count

        if file_fixes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filename}: {file_fixes} fix(es)")
            total_fixes += file_fixes

    return total_fixes


def main():
    root_dir = os.getcwd()

    print("=" * 50)
    print("  Fix: Light Text on White Backgrounds")
    print("=" * 50)

    if not os.path.isfile(os.path.join(root_dir, 'index.html')):
        print("ERROR: Run from your website root directory!")
        return

    print("\nApplying fixes...\n")
    total = fix_colors(root_dir)

    print(f"\n  Done! {total} fixes applied.")
    print(f"\n  Text color changed: #383838 → #2a2a2a (darker, more readable)")


if __name__ == '__main__':
    main()
