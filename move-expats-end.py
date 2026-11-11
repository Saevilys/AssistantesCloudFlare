#!/usr/bin/env python3
"""Move Sigrid, Amara, Priya to the end of data.json so they appear as last arrivals."""
import json
from pathlib import Path

data = json.loads(Path("data.json").read_text(encoding="utf-8"))

targets = {"Sigrid", "Amara", "Priya"}
moved = []
kept = []

for entry in data:
    if entry["name"] in targets:
        moved.append(entry)
    else:
        kept.append(entry)

# Preserve order: Sigrid, Amara, Priya
order = ["Sigrid", "Amara", "Priya"]
moved.sort(key=lambda e: order.index(e["name"]))

kept.extend(moved)

Path("data.json").write_text(json.dumps(kept, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Moved {len(moved)} entries to end. Total: {len(kept)}")
for e in moved:
    print(f"  {e['name']} → position {kept.index(e)}")
