#!/usr/bin/env python3
"""Validate data-roomservice.json."""
import json

with open("data-roomservice.json", "r") as f:
    data = json.load(f)

print(f"OK — {len(data)} entries")
for a in data[-3:]:
    print(f"  {a['name']} — {a['origin']} — {a['role']} — {len(a['photos'])} photos")
