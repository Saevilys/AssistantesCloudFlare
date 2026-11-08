#!/usr/bin/env python3
"""Read last entries of data.json to see format + find insertion point."""
import json

with open('data.json') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")
print(f"\nLast 2 entries:")
for e in data[-2:]:
    print(json.dumps(e, indent=2, ensure_ascii=False)[:500])
    print("---")
