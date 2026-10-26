#!/usr/bin/env python3
"""Check Aino's photos in data.json."""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

for entry in data:
    if entry.get("name", "").lower() == "aino":
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        break
