#!/usr/bin/env python3
"""Read full structure of last entries in data.json."""
import json

with open('data.json') as f:
    data = json.load(f)

print(f"Total: {len(data)}")
print()
# Print last entry in full
print(json.dumps(data[-1], indent=2, ensure_ascii=False))
