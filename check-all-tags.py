#!/usr/bin/env python3
"""Check all unique tag values in data.json and see which match 'secretary'"""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

tags = {}
for e in data:
    t = e.get("tag", "")
    if t and t != "None" and t != "0":
        tags[t] = tags.get(t, 0) + 1

print("=== All tag values in data.json ===")
for t, c in sorted(tags.items()):
    print(f"  [{c}x] {t}")

# Also check: does any entry have tag='secretary'?
secretary_entries = [e for e in data if e.get("tag") == "secretary"]
print(f"\nEntries with tag='secretary': {len(secretary_entries)}")
for e in secretary_entries:
    print(f"  {e['name']}")

# Check secretaire-minorea-haute entries
sec_mh = [e for e in data if e.get("tag") == "secretaire-minorea-haute"]
print(f"\nEntries with tag='secretaire-minorea-haute': {len(sec_mh)}")
for e in sec_mh:
    print(f"  {e['name']}")
