#!/usr/bin/env python3
"""
SEO Phase 1 - Task 3: Image Sitemap Extension
Fusion Fitness Club Website

This script scans all HTML pages in your sitemap and generates an image sitemap
that adds <image:image> entries for every image on each page.

Run AFTER the image rename script so filenames are already SEO-friendly.

IMPORTANT: Run this from your website root directory (where index.html is)
Usage: python3 seo-phase1-image-sitemap.py
"""

import os
import re
from datetime import datetime
from urllib.parse import urljoin

# ============================================================
# CONFIGURATION - Update these for your site
# ============================================================

SITE_URL = "https://www.fusionfitnessclubph.com"

# Pages in your sitemap (same as your existing sitemap.xml)
SITEMAP_PAGES = [
    "index.html",
    "about.html",
    "classes.html",
    "contact.html",
    "fit.html",
    "sweat.html",
    "strike.html",
    "mma.html",
    "our-team.html",
    "join-us.html",
    "gallery.html",
    "faq.html",
    "timetable.html",
    "more-reviewsX.html",
    "singleblog.html",
]

# Image alt text mapping (SEO-optimized descriptions)
# These should match your UPDATED filenames after running the rename script
# Key: partial filename match → Value: descriptive caption for sitemap
IMAGE_CAPTIONS = {
    # Team
    "jesse-general-manager": "Jesse, General Manager at Fusion Fitness Club Makati",
    "jm-head-coach": "JM, Head Coach at Fusion Fitness Club Makati",
    "bonie-membership-advisor": "Bonie, Membership Advisor at Fusion Fitness Club Makati",
    "flory-coach": "Flory, Coach at Fusion Fitness Club Makati",
    "powell-coach": "Powell, Coach at Fusion Fitness Club Makati",
    "van-staff": "Van, Staff at Fusion Fitness Club Makati",
    "art-coach": "Art, Coach at Fusion Fitness Club Makati",
    "coach-portrait": "Coach portrait at Fusion Fitness Club Makati",

    # Training photos
    "boxing-training": "Boxing training at Fusion Fitness Club Makati gym",
    "muay-thai-training": "Muay Thai training at Fusion Fitness Club Makati gym",
    "boxing-workout-training": "Boxing workout and heavy bag training",
    "fitness-strength-training": "Strength and fitness training at the gym",
    "martial-arts-combat": "Martial arts combat training session",
    "kickboxing-heavy-bag": "Kickboxing heavy bag workout session",
    "yoga-flexibility-training": "Yoga and flexibility training class",
    "group-fitness-class": "Group fitness class at Fusion Fitness Club",
    "mma-mixed-martial-arts": "MMA mixed martial arts training at Fusion Fitness Club",
    "boxing-gloves-punching": "Boxing gloves and punching bag workout",
    "gym-functional-training": "Functional training equipment at the gym",
    "personal-training-session": "Personal training session at Fusion Fitness Club",
    "group-fitness-hiit": "Group HIIT fitness class at Fusion Fitness Club",

    # Branding
    "fusion-fitness-club-logo": "Fusion Fitness Club official logo",
    "fusion-fitness-club-makati-martial-arts-gym-hero": "Fusion Fitness Club Makati - Martial Arts Infused Gym",
    "fusion-fitness-club-makati-martial-arts-gym-overlay": "Fusion Fitness Club training action shot",

    # Backgrounds
    "fusion-fitness-club-section-divider": "Fusion Fitness Club decorative section divider",
    "fusion-fitness-club-testimonials": "Fusion Fitness Club member testimonials section",
    "fusion-fitness-club-about-page": "Fusion Fitness Club about page background",
}


def extract_images_from_html(filepath):
    """Extract all image src/data-lazyload URLs from an HTML file."""
    images = set()

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        return images

    # Match img src attributes
    for match in re.finditer(r'(?:src|data-lazyload)\s*=\s*["\']([^"\']*?(?:upload|images)/[^"\']+)["\']', content):
        img_path = match.group(1)
        # Skip dummy/placeholder images
        if 'dummy.png' in img_path or 'gravatar' in img_path:
            continue
        images.add(img_path)

    # Match CSS background-image URLs pointing to upload/
    for match in re.finditer(r'background-image:\s*url\(([^)]*?(?:upload|images)/[^)]+)\)', content):
        img_path = match.group(1).strip('"\'')
        images.add(img_path)

    return images


def extract_videos_from_html(filepath):
    """Extract all video source URLs from an HTML file."""
    videos = set()

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except FileNotFoundError:
        return videos

    # Match <source src="videos/..."> tags
    for match in re.finditer(r'<source\s+src=["\']([^"\']*?videos/[^"\']+)["\']', content):
        videos.add(match.group(1))

    # Match direct video src attributes
    for match in re.finditer(r'<video[^>]*src=["\']([^"\']*?videos/[^"\']+)["\']', content):
        videos.add(match.group(1))

    return videos


def get_image_caption(img_path):
    """Get an SEO-friendly caption for an image based on filename."""
    filename = os.path.basename(img_path)
    name = os.path.splitext(filename)[0]

    # Remove size suffixes like -600x800
    name_clean = re.sub(r'-\d+x\d+$', '', name)

    # Try to match against our caption map
    for key, caption in IMAGE_CAPTIONS.items():
        if key in name_clean:
            return caption

    # Fallback: generate caption from filename
    caption = name_clean.replace('-', ' ').replace('_', ' ').title()
    return f"{caption} - Fusion Fitness Club Makati"


def generate_image_sitemap(root_dir):
    """Generate a sitemap with image extensions."""

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"',
        '        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">',
        '',
    ]

    total_images = 0
    total_videos = 0

    # Video metadata mapping (filename partial match → metadata)
    video_metadata = {
        "fusion-fitness-club-makati-gym-tour": {
            "title": "Fusion Fitness Club Makati - Martial Arts Infused Gym Tour",
            "description": "Take a tour of Fusion Fitness Club in Makati City. Experience our martial arts infused fitness classes including Boxing, Muay Thai, MMA, and Yoga at Assembly Grounds, The Rise.",
        },
        "FUSION GYM 1 MINUTER": {
            "title": "Fusion Fitness Club Makati - Martial Arts Infused Gym Tour",
            "description": "Take a tour of Fusion Fitness Club in Makati City. Experience our martial arts infused fitness classes including Boxing, Muay Thai, MMA, and Yoga at Assembly Grounds, The Rise.",
        },
    }

    for page in SITEMAP_PAGES:
        filepath = os.path.join(root_dir, page)

        if not os.path.isfile(filepath):
            print(f"  WARNING: {page} not found, skipping...")
            continue

        # Get page URL
        if page == 'index.html':
            page_url = SITE_URL + '/'
        else:
            page_url = f"{SITE_URL}/{page}"

        # Extract images and videos from this page
        images = extract_images_from_html(filepath)
        videos = extract_videos_from_html(filepath)

        # Filter to unique base images (remove sized duplicates)
        unique_images = {}
        for img in images:
            base = re.sub(r'-\d+x\d+(?=\.\w+$)', '', img)
            if base not in unique_images:
                unique_images[base] = img

        xml_lines.append(f'  <url>')
        xml_lines.append(f'    <loc>{page_url}</loc>')

        # Add image entries
        page_img_count = 0
        for base_img, img_path in sorted(unique_images.items()):
            img_url = f"{SITE_URL}/{img_path}"
            caption = get_image_caption(img_path)

            xml_lines.append(f'    <image:image>')
            xml_lines.append(f'      <image:loc>{img_url}</image:loc>')
            xml_lines.append(f'      <image:caption>{escape_xml(caption)}</image:caption>')
            xml_lines.append(f'    </image:image>')
            page_img_count += 1

        # Add video entries
        page_vid_count = 0
        for vid_path in sorted(videos):
            vid_url = f"{SITE_URL}/{vid_path}"
            vid_filename = os.path.splitext(os.path.basename(vid_path))[0]

            # Look up metadata
            vid_meta = None
            for key, meta in video_metadata.items():
                if key in vid_filename:
                    vid_meta = meta
                    break

            if not vid_meta:
                vid_meta = {
                    "title": f"{vid_filename.replace('-', ' ').title()} - Fusion Fitness Club Makati",
                    "description": f"Video from Fusion Fitness Club Makati - Martial arts infused fitness gym",
                }

            xml_lines.append(f'    <video:video>')
            xml_lines.append(f'      <video:content_loc>{escape_xml(vid_url)}</video:content_loc>')
            xml_lines.append(f'      <video:title>{escape_xml(vid_meta["title"])}</video:title>')
            xml_lines.append(f'      <video:description>{escape_xml(vid_meta["description"])}</video:description>')
            xml_lines.append(f'    </video:video>')
            page_vid_count += 1

        xml_lines.append(f'  </url>')
        xml_lines.append('')

        total_images += page_img_count
        total_videos += page_vid_count
        vid_label = f" + {page_vid_count} video(s)" if page_vid_count > 0 else ""
        print(f"  {page}: {page_img_count} images{vid_label}")

    xml_lines.append('</urlset>')

    return '\n'.join(xml_lines), total_images, total_videos


def escape_xml(text):
    """Escape special XML characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&apos;'))


def main():
    root_dir = os.getcwd()

    print("=" * 65)
    print("  SEO Phase 1 - Image Sitemap Extension")
    print("  Fusion Fitness Club Website")
    print("=" * 65)
    print(f"\nWorking directory: {root_dir}")
    print(f"Site URL: {SITE_URL}\n")

    # Verify we're in the right place
    if not os.path.isfile(os.path.join(root_dir, 'index.html')):
        print("ERROR: index.html not found in current directory!")
        print("Please run this script from your website root directory.")
        return

    print("Scanning pages for images...\n")

    # Generate the image sitemap
    sitemap_xml, total_images, total_videos = generate_image_sitemap(root_dir)

    # Write the image sitemap
    sitemap_path = os.path.join(root_dir, 'sitemap-images.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

    print(f"\n{'=' * 65}")
    print(f"  DONE!")
    print(f"  Total images indexed: {total_images}")
    print(f"  Total videos indexed: {total_videos}")
    print(f"  Sitemap saved to: sitemap-images.xml")
    print(f"{'=' * 65}")

    # Also update robots.txt to reference the image sitemap
    robots_path = os.path.join(root_dir, 'robots.txt')
    image_sitemap_line = f"Sitemap: {SITE_URL}/sitemap-images.xml"

    if os.path.isfile(robots_path):
        with open(robots_path, 'r', encoding='utf-8') as f:
            robots_content = f.read()

        if 'sitemap-images.xml' not in robots_content:
            with open(robots_path, 'a', encoding='utf-8') as f:
                f.write(f"\n{image_sitemap_line}\n")
            print(f"\n  ✓ Added image sitemap reference to robots.txt")
        else:
            print(f"\n  Image sitemap already referenced in robots.txt")
    else:
        print(f"\n  WARNING: robots.txt not found. Add this line manually:")
        print(f"  {image_sitemap_line}")

    print(f"\nNext steps:")
    print(f"  1. git add sitemap-images.xml robots.txt")
    print(f"  2. git commit -m 'SEO: Add image sitemap extension'")
    print(f"  3. git push origin master")
    print(f"  4. In Google Search Console → Sitemaps → Submit: {SITE_URL}/sitemap-images.xml")


if __name__ == '__main__':
    main()
