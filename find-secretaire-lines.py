#!/usr/bin/env python3
"""Extract the tag rendering lines from index.html and station-minorea.html"""
import re

for fname in ["index.html", "station-minorea.html"]:
    with open(fname, encoding="utf-8") as f:
        html = f.read()
    
    # Find all lines containing 'secretaire' or 'Secrétaire'
    lines = html.split('\n')
    print(f"\n=== {fname} — lines with 'secretaire'/'Secrétaire' ===")
    for i, l in enumerate(lines):
        if 'secretaire' in l.lower() or 'secrétaire' in l.lower():
            print(f"  L{i}: {l.strip()[:200]}")
