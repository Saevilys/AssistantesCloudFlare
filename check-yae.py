#!/usr/bin/env python3
"""Check Yae entry in exported data.json."""
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
yae = [e for e in data if e.get("name") == "Yae"]
if yae:
    print("Yae photos in exported JSON:")
    for p in yae[0].get("photos", []):
        print(f"  {p}")
else:
    print("Yae not found!")
