#!/usr/bin/env python3
import json

with open("data.json", "r") as f:
    main = json.load(f)

names = [e.get("name") for e in main]
print(f"data.json: {len(main)} entries")
print("Liezel" in names, "Mayaris" in names)

# Find their indices
for i, e in enumerate(main):
    if e.get("name") in ("Liezel", "Mayaris"):
        print(f"  [{i}] {e['name']} — role: {e.get('role','?')}")
