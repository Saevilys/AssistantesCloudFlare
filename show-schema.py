#!/usr/bin/env python3
"""Show full entries: one with station field, one reporter, to copy schema."""
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
shown = 0
for a in data:
    if a.get("station") and shown < 2:
        print(json.dumps(a, ensure_ascii=False, indent=1))
        print("---")
        shown += 1
# also a reporter-tagged one
for a in data:
    if a.get("tag") == "reporter":
        print(json.dumps(a, ensure_ascii=False, indent=1))
        break
