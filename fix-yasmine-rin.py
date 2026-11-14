#!/usr/bin/env python3
"""Fix Yasmine duplicate (reporter→Yara) and Rin tag."""
import json

with open('data.json') as f:
    data = json.load(f)

fixed = 0
for e in data:
    # Fix reporter Yasmine → Yara
    if e['name'] == 'Yasmine' and e.get('tag') == 'reporter':
        e['name'] = 'Yara'
        e['photos'] = [p.replace('img/yasmine/', 'img/yara/') for p in e.get('photos', [])]
        print(f"Renamed: Yasmine (reporter) → Yara")
        print(f"  Photos: {e['photos']}")
        fixed += 1
    
    # Fix Rin tag
    if e['name'] == 'Rin' and e.get('tag') == 'garde du corps':
        e['tag'] = 'garde-du-corps'
        print(f"Fixed Rin tag: 'garde du corps' → 'garde-du-corps'")
        fixed += 1

with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify
from collections import Counter
names = Counter(e['name'] for e in data)
dupes = {n:c for n,c in names.items() if c > 1}
print(f"\n{len(data)} entries, {len(names)} unique")
print(f"Duplicates: {dupes if dupes else 'none ✓'}")
print(f"Fixed: {fixed} issues")
