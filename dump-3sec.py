#!/usr/bin/env python3
"""Get full details for Mayumi, Thinzar, Pema from data.json"""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

for name in ["Mayumi", "Thinzar", "Pema"]:
    for e in data:
        if e.get("name","") == name:
            print(f"\n=== {name} ===")
            for k, v in e.items():
                if k != "photos":
                    print(f"  {k}: {v}")
            print(f"  photos:")
            for p in e.get("photos", []):
                print(f"    {p}")
