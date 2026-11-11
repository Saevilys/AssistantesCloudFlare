#!/usr/bin/env python3
"""Check existing reporters and regions in data.json to avoid clones."""
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# List all reporters
reporters = [e for e in data if e.get("tag") == "reporter"]
print(f"Existing reporters ({len(reporters)}):")
for r in reporters:
    print(f"  {r['name']} — {r.get('origin','?')} — {r.get('region','?')} — {r.get('station','?')}")

# List all unique regions
regions = set(e.get("region", "?") for e in data)
print(f"\nAll regions ({len(regions)}):")
for r in sorted(regions):
    count = sum(1 for e in data if e.get("region") == r)
    print(f"  {r}: {count}")

# Check if "expatri" or similar exists
expat = [e for e in data if "expat" in e.get("region","").lower() or "expat" in e.get("tag","").lower()]
print(f"\nExpatriées found: {len(expat)}")
for e in expat:
    print(f"  {e['name']} — {e.get('region')} — {e.get('tag')}")
