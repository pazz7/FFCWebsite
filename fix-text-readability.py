#!/usr/bin/env python3
"""
Fix: Text Readability Across All Pages
Fusion Fitness Club Website

Fixes:
1. index.html - "Martial Arts PRO" section: white bg + overlay image
2. Class pages - White-Line-BG.jpg overlay covering text
3. Body background showing through as white

Run from your website root directory (where index.html is).
"""

import os
import glob
import re

def fix_index_html():
    """Fix the white section on index.html"""
    filepath = 'index.html'
    if not os.path.isfile(filepath):
        print(f"  ! {filepath} not found")
        return

    with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()

    changes = 0

    # Fix 1: Change background-color #ffffff to #1a1a1a on the "Martial Arts PRO" section
    # This is the wrapper with fusion-fitness-club-section-divider-background.jpg
    old = 'background-color: #ffffff;'
    if old in content:
        # Only replace in the context near the section-divider background
        content = content.replace(
            'background-color: #ffffff;">\n                        <div class="gdlr-core-pbf-background gdlr-core-parallax gdlr-core-js"\n                             style="background-image: url(upload/fusion-fitness-club-section-divider-background.jpg)',
            'background-color: #1a1a1a;">\n                        <div class="gdlr-core-pbf-background gdlr-core-parallax gdlr-core-js"\n                             style="background-image: none'
        )
        changes += 1
        print(f"  ✓ Changed section background from white to dark")

    # Fix 2: Change the BG-Top-ZYTH-GYM.jpg to none (if not already done)
    if 'url(upload/BG-Top-ZYTH-GYM.jpg)' in content:
        content = content.replace('url(upload/BG-Top-ZYTH-GYM.jpg)', 'none')
        changes += 1
        print(f"  ✓ Removed BG-Top-ZYTH-GYM.jpg overlay")

    # Fix 3: Change text colors in the "Martial Arts PRO" section from dark to light
    # Title colors: #060606 -> #ffffff
    content = content.replace(
        'color: #060606;">',
        'color: #ffffff;">'
    )

    # Text colors: #3a3a3a -> #cccccc
    content = content.replace(
        'color: #3a3a3a;">',
        'color: #cccccc;">'
    )

    changes += 1
    print(f"  ✓ Changed text colors to light for dark background")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ {filepath}: {changes} fixes applied")


def fix_class_pages():
    """Fix White-Line-BG overlay on class pages by removing the background image"""
    class_pages = ['fit.html', 'sweat.html', 'strike.html', 'mma.html']

    for filepath in class_pages:
        if not os.path.isfile(filepath):
            print(f"  ! {filepath} not found")
            continue

        with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
            content = f.read()

        changed = False

        # Remove White-Line-BG.jpg background image
        if 'White-Line-BG.jpg' in content:
            content = content.replace(
                'url(upload/White-Line-BG.jpg)',
                'none'
            )
            changed = True
            print(f"  ✓ {filepath}: Removed White-Line-BG.jpg overlay")

        # Change text color #383838 to #2a2a2a for better contrast
        if 'color: #383838' in content:
            content = content.replace('color: #383838', 'color: #2a2a2a')
            changed = True
            print(f"  ✓ {filepath}: Darkened text color")

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"  - {filepath}: no changes needed")


def fix_css():
    """Update the CSS fix file with comprehensive overrides"""
    css_dir = 'css'
    css_path = os.path.join(css_dir, 'text-readability-fix.css')

    if not os.path.isdir(css_dir):
        os.makedirs(css_dir)

    css_content = """/* ===========================================
   Text Readability Fix - Fusion Fitness Club
   Fixes light/invisible text on white backgrounds
   =========================================== */

/* Body background - change from white to dark */
.zyth-body-outer-wrapper,
body.zyth-full .zyth-body-wrapper {
    background-color: #0a0a0a !important;
}

body.zyth-boxed .zyth-body-wrapper {
    background-color: #0a0a0a !important;
}
"""

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

    print(f"  ✓ Updated css/text-readability-fix.css")


def ensure_css_linked():
    """Make sure the CSS fix is linked in all HTML files"""
    link_tag = '    <link rel="stylesheet" href="css/text-readability-fix.css" />\n'
    total = 0

    for filepath in glob.glob('*.html'):
        try:
            with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"  ERROR reading {filepath}: {e}")
            continue

        if 'text-readability-fix.css' in content:
            continue

        if '</head>' in content:
            content = content.replace('</head>', link_tag + '</head>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filepath}: linked CSS fix")
            total += 1

    if total == 0:
        print(f"  - All HTML files already have CSS linked")
    else:
        print(f"  ✓ CSS fix linked in {total} HTML files")


def main():
    if not os.path.isfile('index.html'):
        print("ERROR: Run from your website root directory (where index.html is)!")
        return

    print("\n=== Fixing Text Readability ===\n")

    print("[1/4] Fixing index.html...")
    fix_index_html()

    print("\n[2/4] Fixing class pages...")
    fix_class_pages()

    print("\n[3/4] Updating CSS overrides...")
    fix_css()

    print("\n[4/4] Ensuring CSS is linked...")
    ensure_css_linked()

    print("\n=== Done! ===")
    print("\nPreview locally, then push:")
    print('  git add -A; git commit -m "Fix: text readability across all pages"; git push origin master')


if __name__ == '__main__':
    main()
