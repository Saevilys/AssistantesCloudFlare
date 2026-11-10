#!/usr/bin/env python3
"""Check if names already exist in data.json or data-roomservice.json."""
import json

for fname in ["data.json", "data-roomservice.json"]:
    with open(fname, "r", encoding="utf-8") as f:
        data = json.load(f)
    names = [e.get("name","").lower() for e in data] if isinstance(data, list) else []
    print(f"{fname}: {len(names)} entries")
    for n in ["yoonji", "dandara", "folake", "iara", "rafaella", "chinwe"]:
        if n in names:
            print(f"  ⚠️ {n} ALREADY EXISTS")
        else:
            print(f"  ✓ {n} free")
