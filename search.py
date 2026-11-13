#!/usr/bin/env python3
"""Search for Mentari/Suchada across all JSON files."""
import json, os

for fname in os.listdir("."):
    if fname.endswith(".json"):
        try:
            data = json.load(open(fname))
            if isinstance(data, list):
                for e in data:
                    n = str(e.get("name","") + e.get("nom","")).lower()
                    if "mentari" in n or "suchada" in n:
                        print(f"[{fname}] {json.dumps(e, ensure_ascii=False, indent=2)}")
                        print("---")
        except:
            pass
