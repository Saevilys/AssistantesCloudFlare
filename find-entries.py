#!/usr/bin/env python3
"""Show the entries for the assistants being renamed."""
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
targets = {"morana","sena","mio","dilara","sora"}
for i, a in enumerate(data):
    n = (a.get("name","") or "").lower()
    if n in targets:
        print(i, json.dumps(a, ensure_ascii=False)[:600])
        print("---")
