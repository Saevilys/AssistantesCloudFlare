#!/usr/bin/env python3
"""Check if proposed chaebol names already exist in data.json or data-roomservice.json."""
import json
from pathlib import Path

proposed = ["Reika", "Baihe", "Jisoo", "Tsukasa", "Meifeng", "Eunbi",
            "Yumeko", "Qian", "Hyuna", "Ruriko", "Weili", "Nabi"]

for fname in ["data.json", "data-roomservice.json"]:
    data = json.loads(Path(fname).read_text(encoding="utf-8"))
    existing = {e["name"] for e in data}
    for name in proposed:
        if name in existing:
            print(f"  ⚠️  {name} ALREADY EXISTS in {fname}")
    print(f"{fname}: {len(data)} entries checked")

print("\nDone. No output above = all clear.")
