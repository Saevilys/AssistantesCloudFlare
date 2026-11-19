#!/usr/bin/env python3
"""Fix tag for Mayumi, Thinzar, Pema: secretaire-minorea-haute -> secretary"""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

fixed = 0
for e in data:
    if e.get("name") in ("Mayumi", "Thinzar", "Pema"):
        old = e.get("tag")
        e["tag"] = "secretary"
        print(f"  {e['name']}: tag '{old}' -> 'secretary'")
        fixed += 1

print(f"\nFixed {fixed} entries")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json written")
