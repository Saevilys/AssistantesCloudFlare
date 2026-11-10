#!/usr/bin/env python3
"""Check existing names in data.json and data-roomservice.json to avoid duplicates."""
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

names = sorted([e["name"] for e in data])
print(f"data.json ({len(names)} entries):")
for n in names:
    print(f"  {n}")

# Check Minorea residents
minorea = [e for e in data if "minorea" in e.get("city","").lower() or "minorea" in e.get("station","").lower()]
print(f"\nMinorea residents ({len(minorea)}):")
for e in minorea:
    print(f"  {e['name']} — {e.get('role', e.get('trait', ''))[:60]}")

with open("data-roomservice.json", "r", encoding="utf-8") as f:
    rs = json.load(f)
rs_names = sorted([e["name"] for e in rs])
print(f"\ndata-roomservice.json ({len(rs_names)} entries):")
for n in rs_names:
    print(f"  {n}")
