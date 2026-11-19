#!/usr/bin/env python3
"""Find how tags (reporter, anchor, secretaire) are rendered in HTML pages"""
import re

for fname in ["index.html", "station-minorea.html", "specials.html"]:
    with open(fname, encoding="utf-8") as f:
        html = f.read()
    
    # Look for tag-related CSS classes or patterns
    # Search for "tag" in class names, "reporter", "anchor", "secrétaire", "secretaire"
    patterns = re.findall(r'(tag|reporter|anchor|secretaire|secrétaire|badge|role)[^"]*', html, re.IGNORECASE)
    print(f"\n=== {fname} — tag-related patterns ===")
    for p in set(patterns):
        print(f"  {p}")
    
    # Find lines containing 'tag' as a class
    tag_lines = [l for l in html.split('\n') if 'tag' in l.lower() and ('class' in l.lower() or 'css' in l.lower())]
    print(f"  Lines with 'tag' + 'class': {len(tag_lines)}")
    for l in tag_lines[:5]:
        print(f"    {l.strip()[:120]}")
