#!/usr/bin/env python3
import json
data = json.load(open('data.json', encoding='utf-8'))
for i, e in enumerate(data):
    if 'seolhwa' in e['name'].lower():
        print(f"FOUND at index {i}")
        print(json.dumps(e, ensure_ascii=False, indent=2))
if not any('seolhwa' in e['name'].lower() for e in data):
    print(f"NOT FOUND — total entries: {len(data)}")
