#!/usr/bin/env python3
import json
with open("data.json") as f:
    data = json.load(f)
names = [item["name"] for item in data]
seen = {}
dups = []
for n in names:
    nl = n.lower()
    if nl in seen:
        dups.append(nl)
    seen[nl] = True
print(f"Total: {len(data)}")
print(f"Duplicates: {dups if dups else 'none'}")
for item in data:
    if item["name"] in ("Chaewon", "Ami"):
        print(f"  {item['name']}: flirty={item['flirty']}, photos={len(item['photos'])}")
        print(f"    first photo: {item['photos'][0]}")
