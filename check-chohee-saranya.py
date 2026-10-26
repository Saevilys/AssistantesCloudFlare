#!/usr/bin/env python3
"""Check Cho-hee and Saranya entries in data.json."""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

for entry in data:
    name = entry.get("name", "")
    if name.lower() in ("cho-hee", "saranya"):
        print(f"=== {name} ===")
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        print()
