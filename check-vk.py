#!/usr/bin/env python3
"""Check if virgin killer assistants exist in data.json."""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

targets = ["miko", "sona", "elina", "dulce", "yejin", "fatou", "ximena"]
print(f"Total assistants: {len(data)}\n")
for entry in data:
    name = entry.get("name", "").lower()
    if any(t in name for t in targets):
        print(f"FOUND: {entry.get('name')} — {entry.get('origin')} — photos: {len(entry.get('photos', []))}")
        for p in entry.get("photos", []):
            print(f"  {p}")
        print()

# Also check for virgin killer in descriptions
print("\n--- 'virgin' in desc ---")
for entry in data:
    desc = entry.get("desc", "").lower()
    if "virgin" in desc or "killer" in desc or "sweat" in desc:
        print(f"  {entry.get('name')}: {entry.get('desc', '')[:120]}")
