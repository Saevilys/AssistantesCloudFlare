#!/usr/bin/env python3
import json, sys

with open(sys.argv[1] if len(sys.argv) > 1 else "data.json") as f:
    raw = f.read()

data = json.loads(raw)
if isinstance(data, dict):
    for k in list(data.keys())[:10]:
        print(f"key: {k}")
    # Check if assistants is a key
    if "assistants" in data:
        al = data["assistants"]
        print(f"assistants: {len(al)} items")
        if al:
            print(json.dumps(al[0], indent=2, ensure_ascii=False)[:2000])
elif isinstance(data, list):
    print(f"list of {len(data)}")
    if data:
        print(json.dumps(data[0], indent=2, ensure_ascii=False)[:2000])
