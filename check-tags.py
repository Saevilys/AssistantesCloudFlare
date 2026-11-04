#!/usr/bin/env python3
import json

with open('data.json') as f:
    data = json.load(f)

# Show a djinn entry in detail
for e in data:
    if e.get('tag') == 'djinn' and e.get('name') == 'Zafira':
        print(json.dumps(e, indent=2, ensure_ascii=False))
        break

print("\n---\n")

# Show last entry's photos format
for e in data:
    if e.get('tag') == 'djinn' and e.get('photos'):
        print(f"Name: {e['name']}")
        print(f"Photos: {json.dumps(e['photos'], indent=2, ensure_ascii=False)}")
        break
