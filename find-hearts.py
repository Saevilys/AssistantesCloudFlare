#!/usr/bin/env python3
"""Find exact flirt-related JS blocks in nour and suyin."""
import re

for fname in ['station-nour.html', 'station-suyin.html']:
    with open(fname) as f:
        content = f.read()
    
    print(f"\n=== {fname} ===")
    
    # Find flirtBannerLabel
    m = re.search(r'function flirtBannerLabel\(.*?\}', content, re.DOTALL)
    if m:
        print(f"\n--- flirtBannerLabel ({m.start()}) ---")
        print(repr(content[m.start():m.end()+1]))
    
    # Find flirtDots
    m = re.search(r'const flirtDots=.*?;', content, re.DOTALL)
    if m:
        print(f"\n--- flirtDots ({m.start()}) ---")
        print(repr(content[m.start():m.end()]))
    
    # Find profile badge
    idx = content.find('badge-flirt')
    if idx >= 0:
        # Get surrounding context
        start = max(0, idx - 50)
        end = min(len(content), idx + 600)
        print(f"\n--- badge-flirt context ({idx}) ---")
        print(repr(content[start:end]))
