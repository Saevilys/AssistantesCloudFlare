#!/usr/bin/env python3
"""Check replacement names."""
import json
from pathlib import Path

proposed = ["Shiori", "Dami", "Mizuki", "Seol", "Setsuka", "Yona"]

for fname in ["data.json", "data-roomservice.json"]:
    data = json.loads(Path(fname).read_text(encoding="utf-8"))
    existing = {e["name"] for e in data}
    for name in proposed:
        if name in existing:
            print(f"  ⚠️  {name} ALREADY EXISTS in {fname}")
    print(f"{fname}: {len(data)} entries checked")

print("\nDone.")
