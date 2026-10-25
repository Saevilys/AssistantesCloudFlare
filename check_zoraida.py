#!/usr/bin/env python3
import json

with open("data.json") as f:
    data = json.load(f)

for a in data:
    if a["name"] == "Zoraida":
        print(json.dumps(a["photos"], indent=2, ensure_ascii=False))
        break
