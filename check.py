#!/usr/bin/env python3
import json
with open("data.json") as f:
    data = json.load(f)
for item in data:
    if item.get("name") == "bomsori":
        print(json.dumps(item, indent=2, ensure_ascii=False))
        break
print("=== HINA ===")
for item in data:
    if item.get("name") == "hina":
        print(json.dumps(item, indent=2, ensure_ascii=False))
        break
