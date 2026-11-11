#!/usr/bin/env python3
"""Find and print existing Sigrid, Amara, Priya entries."""
import json
from pathlib import Path

data = json.loads(Path("data.json").read_text(encoding="utf-8"))

for name in ["Sigrid", "Amara", "Priya"]:
    for entry in data:
        if entry["name"] == name:
            print(f"=== {name} ===")
            print(json.dumps(entry, ensure_ascii=False, indent=2))
            print()
