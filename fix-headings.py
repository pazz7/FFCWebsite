#!/usr/bin/env python3
"""
FFC SEO Phase 2 - Fix Heading Structure
Promotes H3 headings to proper H1/H2 hierarchy across all pages.
Visual appearance unchanged since all headings have inline styles.

Run from the FFCWebsite root directory:
    python fix-headings.py
"""

import re
import os
import sys

def fix_heading(content, old_text, old_tag='h3', new_tag='h1', occurrence=1):
    """
    Replace a specific heading tag while keeping all attributes and inner HTML.
    old_text: unique text fragment inside the heading to identify it
    occurrence: which occurrence to replace (1-based) if text appears multiple times
    """
    count = 0
    result = []
    pos = 0
    
    # Pattern matches the full h3 opening tag, content, and closing tag
    pattern = re.compile(
        rf'(<{old_tag})(\b[^>]*>)(.*?)(</{old_tag}>)',
        re.DOTALL
    )
    
    for m in pattern.finditer(content):
        inner_clean = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        inner_clean = inner_clean.replace('&nbsp;', '').replace('&NonBreakingSpace;', '').strip()
        
        if old_text in inner_clean:
            count += 1
            if count == occurrence:
                # Append everything before this match
                result.append(content[pos:m.start()])
                # Replace opening and closing tags
                result.append(f'<{new_tag}')
                result.append(m.group(2))  # attributes
                result.append(m.group(3))  # inner content
                result.append(f'</{new_tag}>')
                pos = m.end()
                
    if count >= occurrence:
        result.append(content[pos:])
        return ''.join(result)
    else:
        print(f'  WARNING: Could not find "{old_text}" (occurrence {occurrence}) in {old_tag} tag')
        return content


def add_h1_after_slider(content, h1_text):
    """
    For index.html: Insert an H1 right after the slider section ends,
    before the first content wrapper.
    """
    # Find the first content section after the slider
    # The cards section starts with this wrapper
    marker = 'gdlr-core-pbf-wrapper-container-inner gdlr-core-item-mglr clearfix'
    idx = content.find(marker)
    if idx == -1:
        print('  WARNING: Could not find insertion point for H1 on index.html')
        return content
    
    # Go back to find the wrapper div start before this
    # Find the gdlr-core-pbf-wrapper that contains this
    wrapper_start = content.rfind('<div class="gdlr-core-pbf-wrapper"', 0, idx)
    if wrapper_start == -1:
        print('  WARNING: Could not find wrapper for H1 insertion')
        return content
    
    # Insert H1 just before this wrapper
    h1_html = f'''                <!-- SEO: Main page heading -->
                <div style="text-align:center; padding:0; margin:0; height:0; overflow:hidden;">
                    <h1 style="font-size:0; margin:0; padding:0; height:0; overflow:hidden; position:absolute;">{h1_text}</h1>
                </div>
'''
    
    content = content[:wrapper_start] + h1_html + content[wrapper_start:]
    return content


def process_file(filepath, changes):
    """Apply a list of heading changes to a file."""
    print(f'\nProcessing: {filepath}')
    
    if not os.path.exists(filepath):
        print(f'  SKIPPED: File not found')
        return False
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original = content
    
    for change in changes:
        action = change.get('action', 'promote')
        
        if action == 'promote':
            content = fix_heading(
                content,
                change['text'],
                change.get('from', 'h3'),
                change['to'],
                change.get('occurrence', 1)
            )
            print(f'  {change.get("from", "h3").upper()} -> {change["to"].upper()}: "{change["text"]}"')
        
        elif action == 'add_h1':
            content = add_h1_after_slider(content, change['text'])
            print(f'  ADDED H1: "{change["text"]}"')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  SAVED')
        return True
    else:
        print(f'  NO CHANGES')
        return False


def main():
    # Define all heading changes per file
    changes = {
        'index.html': [
            # Add hidden H1 for SEO (homepage doesn't have a visible title area)
            {'action': 'add_h1', 'text': 'Fusion Fitness Club &mdash; Martial Arts-Infused Gym in Makati City'},
            # Promote section headings to H2
            {'action': 'promote', 'text': 'OUR PHILOSOPHY', 'to': 'h2'},
            {'action': 'promote', 'text': 'Our Classes', 'to': 'h2'},
            {'action': 'promote', 'text': 'WHAT CUSTOMERS SAY', 'to': 'h2', 'occurrence': 1},
            {'action': 'promote', 'text': 'WHAT CUSTOMERS SAY', 'to': 'h2', 'occurrence': 1},  # second instance (now first remaining)
            {'action': 'promote', 'text': 'Recent Articles', 'to': 'h2'},
            {'action': 'promote', 'text': 'Join Now', 'to': 'h2'},
            {'action': 'promote', 'text': 'The Timetable', 'to': 'h2'},
            # Promote feature highlights to H2
            {'action': 'promote', 'text': 'Martial Arts PRO', 'to': 'h2'},
            {'action': 'promote', 'text': 'All Fitness Levels', 'to': 'h2'},
            {'action': 'promote', 'text': 'Community', 'to': 'h2'},
        ],
        
        'classes.html': [
            # Main page heading
            {'action': 'promote', 'text': 'FFC Branded Classes', 'to': 'h1'},
            # Section heading
            {'action': 'promote', 'text': 'WHAT CUSTOMERS SAY', 'to': 'h2'},
        ],
        
        'fit.html': [
            # Main page heading
            {'action': 'promote', 'text': 'FFC FIT', 'to': 'h1'},
            # Section headings
            {'action': 'promote', 'text': 'FFC Fit Experience', 'to': 'h2'},
            {'action': 'promote', 'text': 'Signature Classes', 'to': 'h2'},
        ],
        
        'strike.html': [
            {'action': 'promote', 'text': 'FFC STRIKE', 'to': 'h1'},
            {'action': 'promote', 'text': 'FFC STRIKE EXPERIENCE', 'to': 'h2'},
            {'action': 'promote', 'text': 'Signature Classes', 'to': 'h2'},
        ],
        
        'sweat.html': [
            {'action': 'promote', 'text': 'FFC SWEAT', 'to': 'h1'},
            {'action': 'promote', 'text': 'FFC SWEAT EXPERIENCE', 'to': 'h2'},
            {'action': 'promote', 'text': 'SIGNATURE CLASSES', 'to': 'h2'},
        ],
        
        'mma.html': [
            {'action': 'promote', 'text': 'Mixed Martial Arts', 'to': 'h1'},
            {'action': 'promote', 'text': 'FFC MMA EXPERIENCE', 'to': 'h2'},
            {'action': 'promote', 'text': 'Signature Classes', 'to': 'h2'},
        ],
        
        'contact.html': [
            {'action': 'promote', 'text': 'Free Class Trial', 'to': 'h1'},
        ],
    }
    
    total_files = 0
    total_changed = 0
    
    for filepath, file_changes in changes.items():
        total_files += 1
        if process_file(filepath, file_changes):
            total_changed += 1
    
    print(f'\n{"="*50}')
    print(f'SUMMARY: {total_changed}/{total_files} files updated')
    print(f'{"="*50}')
    
    # Verification pass
    print(f'\nVERIFICATION - H1 tags per page:')
    for filepath in changes.keys():
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            h1_count = len(re.findall(r'<h1[\s>]', content))
            h2_count = len(re.findall(r'<h2[\s>]', content))
            h3_count = len(re.findall(r'<h3[\s>]', content))
            status = '✓' if h1_count == 1 else '✗' if h1_count == 0 else f'⚠ ({h1_count})'
            print(f'  {filepath}: H1={h1_count}{status}  H2={h2_count}  H3={h3_count}')


if __name__ == '__main__':
    main()
