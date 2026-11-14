#!/usr/bin/env python3
"""Rename reporter Yasmine → Rima in data.json, fix photos paths, and fix Rin tag."""
import json, os

with open('data.json') as f:
    data = json.load(f)

fixed = 0
for e in data:
    # Rename reporter Yasmine → Rima
    if e['name'] == 'Yasmine' and e.get('tag') == 'reporter':
        e['name'] = 'Rima'
        e['photos'] = [p.replace('img/yasmine/yasmine-', 'img/rima/rima-') for p in e.get('photos', [])]
        print(f"Renamed: Yasmine (reporter, Beirut) → Rima")
        print(f"  Photos: {e['photos']}")
        fixed += 1
    
    # Fix Rin tag
    if e['name'] == 'Rin' and e.get('tag') == 'garde du corps':
        e['tag'] = 'garde-du-corps'
        print(f"Fixed Rin tag: 'garde du corps' → 'garde-du-corps'")
        fixed += 1

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify no more dups
from collections import Counter
c = Counter(e['name'] for e in data)
dups = {k: v for k, v in c.items() if v > 1}
print(f"\nTotal: {len(data)} entries, duplicates: {dups}")
print(f"Fixed: {fixed} issues")
