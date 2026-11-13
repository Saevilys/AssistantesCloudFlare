#!/usr/bin/env python3
"""Check Mentari and Suchada in data.json."""
import json

data = json.load(open("data.json"))
for e in data:
    n = e.get("name","").strip().lower()
    if n in ("mentari","suchada"):
        print(json.dumps(e, ensure_ascii=False, indent=2))
        print("---")
print(f"Total entries: {len(data)}")
