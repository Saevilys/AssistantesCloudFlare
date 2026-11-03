#!/usr/bin/env python3
"""List all assistant names from both JSON files."""
import json

for fname, label in [("data.json", "Roster principal"), ("data-roomservice.json", "Room service")]:
    with open(fname, "r") as f:
        data = json.load(f)
    names = [a["name"] for a in data]
    print(f"\n{label} ({len(data)} entries):")
    print(", ".join(sorted(names)))
