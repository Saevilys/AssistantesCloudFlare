#!/usr/bin/env python3
"""Check Yara duplicates."""
import json
with open('data.json') as f:
    data = json.load(f)
for i, e in enumerate(data):
    if e['name'] == 'Yara':
        print(f"[{i}] Yara — tag={e.get('tag','none')} — origin={e.get('origin','?')} — city={e.get('city','?')} — photos={len(e.get('photos',[]))}")
        for p in e.get('photos',[]):
            print(f"  {p}")
