#!/usr/bin/env python3
"""
SEO Phase 1 - Task 2: Image Descriptive Filenames
Fusion Fitness Club Website

This script:
1. Renames generic image files to SEO-friendly descriptive names
2. Updates ALL HTML file references to match new filenames
3. Updates CSS background-image references
4. Handles sized variants (e.g., filename-600x800.jpg)

IMPORTANT: Run this from your website root directory (where index.html is)
Usage: python3 seo-phase1-image-rename.py
"""

import os
import re
import glob
import shutil
from pathlib import Path

# ============================================================
# IMAGE RENAME MAPPING
# Old filename (without extension) → New SEO-friendly name
# ============================================================

RENAME_MAP = {
    # === TEAM MEMBER PHOTOS ===
    "P01": "jesse-general-manager-fusion-fitness-club-makati",
    "P02": "jm-head-coach-fusion-fitness-club-makati",
    "P04": "bonie-membership-advisor-fusion-fitness-club-makati",
    "P05": "flory-coach-fusion-fitness-club-makati",
    "P07": "powell-coach-fusion-fitness-club-makati",
    "P08": "van-staff-fusion-fitness-club-makati",
    "P09": "art-coach-fusion-fitness-club-makati",
    "P10": "coach-portrait-fusion-fitness-club-makati",
    "P13": "muay-thai-training-fusion-fitness-club-makati",
    "P15": "boxing-training-fusion-fitness-club-makati",

    # === HOMEPAGE SLIDER ===
    "slider-1": "fusion-fitness-club-makati-martial-arts-gym-hero",
    "slider-1-2": "fusion-fitness-club-makati-martial-arts-gym-overlay",

    # === LOGOS ===
    "logo-fixed": "fusion-fitness-club-logo",
    "logo-fixedx2": "fusion-fitness-club-logo-retina",
    "logox1": "fusion-fitness-club-logo-full",

    # === BACKGROUNDS ===
    "LLLine": "fusion-fitness-club-section-divider-background",
    "TestT": "fusion-fitness-club-testimonials-background",
    "about-enhance-bg": "fusion-fitness-club-about-page-background",

    # === GALLERY / TRAINING PHOTOS (Stock images) ===
    "image-from-rawpixel-id-2107457-jpeg": "boxing-workout-training-gym",
    "image-from-rawpixel-id-14235-jpeg": "fitness-strength-training-gym",
    "image-from-rawpixel-id-2109005-jpeg": "martial-arts-combat-training",
    "image-from-rawpixel-id-2107452-jpeg": "kickboxing-heavy-bag-workout",
    "image-from-rawpixel-id-2194653-jpeg": "yoga-flexibility-training-gym",
    "image-from-rawpixel-id-2107319-jpeg": "group-fitness-class-training",
    "image-from-rawpixel-id-1201598-jpeg": "mma-mixed-martial-arts-training",

    # === STOCK PHOTOS ===
    "iStock-1162341181": "boxing-gloves-punching-bag-workout",
    "iStock-1133759237": "gym-functional-training-equipment",
    "iStock-1225115517": "personal-training-session-gym",
    "shutterstock_1058059004": "group-fitness-hiit-class",

    # === BLOG/MISC ===
    "avatar": "fitness-blog-author-avatar",
}

# ============================================================
# VIDEO RENAME MAPPING
# Old filename (with extension) → New SEO-friendly name
# ============================================================

VIDEO_RENAME_MAP = {
    "FUSION GYM 1 MINUTER.mp4": "fusion-fitness-club-makati-gym-tour.mp4",
}


def find_all_files_to_rename(upload_dir):
    """Find all image files that match our rename map, including sized variants."""
    files_to_rename = []

    if not os.path.isdir(upload_dir):
        print(f"ERROR: Upload directory '{upload_dir}' not found!")
        print("Make sure you run this script from your website root directory.")
        return files_to_rename

    for filename in os.listdir(upload_dir):
        name, ext = os.path.splitext(filename)
        ext_lower = ext.lower()

        if ext_lower not in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']:
            continue

        # Check direct match
        if name in RENAME_MAP:
            new_name = RENAME_MAP[name] + ext
            files_to_rename.append((filename, new_name))
            continue

        # Check for sized variants like "filename-600x800"
        # Pattern: original_name-WIDTHxHEIGHT
        size_match = re.match(r'^(.+?)(-\d+x\d+)$', name)
        if size_match:
            base_name = size_match.group(1)
            size_suffix = size_match.group(2)
            if base_name in RENAME_MAP:
                new_name = RENAME_MAP[base_name] + size_suffix + ext
                files_to_rename.append((filename, new_name))

    return files_to_rename


def update_html_references(root_dir, old_name, new_name):
    """Update all references to an image file across HTML and CSS files."""
    count = 0
    extensions = ['*.html', '*.css']

    for ext in extensions:
        for filepath in glob.glob(os.path.join(root_dir, '**', ext), recursive=True):
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                if old_name in content:
                    updated = content.replace(old_name, new_name)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    count += content.count(old_name)
            except Exception as e:
                print(f"  WARNING: Could not process {filepath}: {e}")

    return count


def main():
    # Determine root directory
    root_dir = os.getcwd()
    upload_dir = os.path.join(root_dir, 'upload')

    print("=" * 65)
    print("  SEO Phase 1 - Image Descriptive Filenames")
    print("  Fusion Fitness Club Website")
    print("=" * 65)
    print(f"\nWorking directory: {root_dir}")
    print(f"Upload directory:  {upload_dir}\n")

    # Verify we're in the right place
    if not os.path.isfile(os.path.join(root_dir, 'index.html')):
        print("ERROR: index.html not found in current directory!")
        print("Please run this script from your website root directory.")
        return

    # Find files to rename
    files_to_rename = find_all_files_to_rename(upload_dir)

    if not files_to_rename:
        print("No files found to rename. Check that the upload/ directory exists.")
        return

    print(f"Found {len(files_to_rename)} image files to rename:\n")

    # Preview changes
    print("-" * 65)
    print(f"{'OLD FILENAME':<50} → NEW FILENAME")
    print("-" * 65)
    for old, new in sorted(files_to_rename):
        print(f"  {old}")
        print(f"    → {new}\n")

    # Confirm
    response = input("\nProceed with renaming? (yes/no): ").strip().lower()
    if response != 'yes':
        print("Cancelled.")
        return

    # Phase 1: Update HTML/CSS references FIRST (before renaming files)
    print("\n--- Updating HTML & CSS references ---\n")
    total_refs = 0
    for old_name, new_name in files_to_rename:
        refs = update_html_references(root_dir, old_name, new_name)
        if refs > 0:
            print(f"  {old_name} → {new_name} ({refs} references updated)")
            total_refs += refs

    # Phase 2: Rename physical files
    print("\n--- Renaming physical files ---\n")
    renamed_count = 0
    for old_name, new_name in files_to_rename:
        old_path = os.path.join(upload_dir, old_name)
        new_path = os.path.join(upload_dir, new_name)

        if os.path.exists(old_path):
            if os.path.exists(new_path):
                print(f"  SKIP: {new_name} already exists!")
                continue
            os.rename(old_path, new_path)
            print(f"  ✓ {old_name} → {new_name}")
            renamed_count += 1
        else:
            print(f"  SKIP: {old_name} not found in upload/")

    # Phase 3: Rename video files
    videos_dir = os.path.join(root_dir, 'videos')
    video_renamed = 0
    if os.path.isdir(videos_dir) and VIDEO_RENAME_MAP:
        print("\n--- Renaming video files ---\n")
        for old_vid, new_vid in VIDEO_RENAME_MAP.items():
            # Update HTML references first
            vid_refs = update_html_references(root_dir, old_vid, new_vid)
            if vid_refs > 0:
                print(f"  Updated {vid_refs} HTML references: {old_vid} → {new_vid}")
                total_refs += vid_refs

            old_vid_path = os.path.join(videos_dir, old_vid)
            new_vid_path = os.path.join(videos_dir, new_vid)
            if os.path.exists(old_vid_path):
                if not os.path.exists(new_vid_path):
                    os.rename(old_vid_path, new_vid_path)
                    print(f"  ✓ {old_vid} → {new_vid}")
                    video_renamed += 1
                else:
                    print(f"  SKIP: {new_vid} already exists!")
            else:
                print(f"  SKIP: {old_vid} not found in videos/")

    print("\n" + "=" * 65)
    print(f"  DONE!")
    print(f"  Images renamed:     {renamed_count}")
    print(f"  Videos renamed:     {video_renamed}")
    print(f"  References updated: {total_refs}")
    print("=" * 65)
    print("\nNext steps:")
    print("  1. Test the website locally to make sure all images load")
    print("  2. git add -A && git commit -m 'SEO: Rename images to descriptive filenames'")
    print("  3. git push origin master")


if __name__ == '__main__':
    main()
