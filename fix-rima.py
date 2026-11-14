#!/usr/bin/env python3
"""Fix: rename reporter Yara (was Yasmine) → Rima, fix photo paths."""
import json

with open('data.json') as f:
    data = json.load(f)

fixed = 0
for e in data:
    # Rename reporter Yara (ex-Yasmine) → Rima
    if e['name'] == 'Yara' and e.get('tag') == 'reporter':
        e['name'] = 'Rima'
        e['photos'] = [p.replace('img/yara/yasmine-', 'img/rima/rima-') for p in e.get('photos', [])]
        print(f"Renamed: Yara (reporter, Beirut) → Rima")
        print(f"  Photos: {e['photos']}")
        fixed += 1
    
    # Fix Rin tag if still broken
    if e['name'] == 'Rin' and e.get('tag') == 'garde du corps':
        e['tag'] = 'garde-du-corps'
        print(f"Fixed Rin tag")
        fixed += 1

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

from collections import Counter
c = Counter(e['name'] for e in data)
dups = {k: v for k, v in c.items() if v > 1}
print(f"\nTotal: {len(data)} entries, duplicates: {dups}")
print(f"Fixed: {fixed} issues")
