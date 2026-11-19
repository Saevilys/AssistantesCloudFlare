#!/usr/bin/env python3
"""Check if Mayumi, Thinzar, Pema are in data.json"""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")
for name in ["Mayumi", "Thinzar", "Pema"]:
    found = [e for e in data if e.get("name","").lower() == name.lower()]
    if found:
        print(f"\n=== {name} FOUND ===")
        for e in found:
            print(f"  id={e.get('id')} station={e.get('station')} tag={e.get('tag')}")
            photos = e.get("photos", e.get("photo", []))
            print(f"  photos: {photos}")
    else:
        print(f"\n=== {name} MISSING ===")
