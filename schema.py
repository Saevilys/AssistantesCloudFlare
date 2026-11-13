#!/usr/bin/env python3
"""Show one example entry and check for bodycon/chaebol entries."""
import json

data = json.load(open("data.json"))
# Show first entry as schema example
print("=== SCHEMA EXAMPLE ===")
print(json.dumps(data[0], ensure_ascii=False, indent=2))
print("\n=== LAST 5 ENTRIES ===")
for e in data[-5:]:
    print(f"  - {e.get('name','?')}: photos={len(e.get('photos',[]))}")
