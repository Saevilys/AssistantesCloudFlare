#!/usr/bin/env python3
"""Fix station field for Mayumi, Thinzar, Pema — set to 'minorea' to match the filter"""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

fixed = 0
for e in data:
    if e.get("name") in ("Mayumi", "Thinzar", "Pema"):
        old = e.get("station")
        e["station"] = "minorea"
        print(f"  {e['name']}: '{old[:50]}...' -> 'minorea'")
        fixed += 1

print(f"\nFixed {fixed} entries")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json written")
