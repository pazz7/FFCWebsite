#!/usr/bin/env python3
"""
Fix: Light text on white backgrounds across all pages
Fusion Fitness Club Website

Creates a CSS override file and links it in all HTML files.
Run from your website root directory (where index.html is).
"""

import os
import glob

# CSS overrides for text readability
CSS_CONTENT = """/* ===========================================
   Text Readability Fix - Fusion Fitness Club
   Fixes light/invisible text on white backgrounds
   =========================================== */

/* Class description paragraphs on white sections */
#gdlr-core-wrapper-2 .gdlr-core-text-box-item-content {
    color: #2a2a2a !important;
}

/* Column service content (Martial Arts Infused, Result Oriented, Fun sections) */
#gdlr-core-wrapper-2 .gdlr-core-column-service-content {
    color: #3a3a3a !important;
}

/* Column service titles on white sections */
#gdlr-core-wrapper-2 .gdlr-core-column-service-title {
    color: #1a1a1a !important;
}

/* Index.html - Martial Arts PRO, All Fitness Levels, Community section */
.gdlr-core-pbf-wrapper[style*="background-color: #ffffff"] .gdlr-core-text-box-item-content {
    color: #2a2a2a !important;
}

.gdlr-core-pbf-wrapper[style*="background-color: #ffffff"] .gdlr-core-title-item-title {
    color: #060606 !important;
}

/* MMA page Greg Jackson description */
.gdlr-core-pbf-wrapper[style*="background-color: #ffffff"] .gdlr-core-text-box-item-content[style*="color: #606060"] {
    color: #3a3a3a !important;
}
"""

def main():
    root_dir = os.getcwd()

    if not os.path.isfile(os.path.join(root_dir, 'index.html')):
        print("ERROR: Run from your website root directory!")
        return

    # Step 1: Create the CSS file
    css_dir = os.path.join(root_dir, 'css')
    css_path = os.path.join(css_dir, 'text-readability-fix.css')

    if not os.path.isdir(css_dir):
        os.makedirs(css_dir)

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(CSS_CONTENT)
    print(f"  ✓ Created css/text-readability-fix.css")

    # Step 2: Add <link> to all HTML files (before </head>)
    link_tag = '    <link rel="stylesheet" href="css/text-readability-fix.css" />\n'
    total = 0

    for filepath in glob.glob(os.path.join(root_dir, '*.html')):
        filename = os.path.basename(filepath)

        try:
            with open(filepath, 'r', encoding='utf-8-sig', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"  ERROR reading {filename}: {e}")
            continue

        # Skip if already added
        if 'text-readability-fix.css' in content:
            print(f"  - {filename}: already has the fix, skipping")
            continue

        # Insert before </head>
        if '</head>' in content:
            content = content.replace('</head>', link_tag + '</head>')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ {filename}: linked CSS fix")
            total += 1
        else:
            print(f"  ! {filename}: no </head> tag found, skipping")

    print(f"\n  Done! CSS fix linked in {total} HTML files.")
    print(f"\n  Preview locally, then:")
    print(f"  git add -A; git commit -m \"Fix: darken text on white backgrounds\"; git push origin master")


if __name__ == '__main__':
    main()
