#!/usr/bin/env python3
"""Show full entries for Shinobu and Burcu (anchors) to understand structure."""
import json
with open('data.json') as f:
    data = json.load(f)

for name in ['Shinobu', 'Burcu']:
    for e in data:
        if e['name'] == name:
            print(f"\n=== {name} ===")
            print(json.dumps(e, indent=2, ensure_ascii=False))
