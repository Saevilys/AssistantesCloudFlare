#!/usr/bin/env python3
"""Search for Elara, Carina, Nasreen in data.json."""
import json

with open("data.json") as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")

for name in ["Elara", "Carina", "Nasreen", "Elora", "Karina", "Nasrin"]:
    found = [c for c in data if name.lower() in c.get("name", "").lower()]
    if found:
        for c in found:
            print(f"  FOUND: {c['name']} | tag={c.get('tag')} | station={c.get('station')} | category={c.get('category')}")
    else:
        print(f"  {name} — not in data.json")

# Also list all anchors
print("\n=== ALL ANCHORS in data.json ===")
for c in data:
    if c.get("tag") == "anchor" or c.get("role") == "anchor":
        print(f"  {c['name']} | tag={c.get('tag')} | role={c.get('role')} | station={c.get('station')}")

# List all entries with station=minorea to see what's there
print("\n=== ALL station=minorea in data.json ===")
for c in data:
    if c.get("station") == "minorea":
        print(f"  {c['name']} | tag={c.get('tag')} | role={c.get('role')}")
