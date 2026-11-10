#!/usr/bin/env python3
"""Find soubrette entries in data.json to understand the structure."""
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find entries with category containing "soubrette" or "maid" or similar
for entry in data:
    cat = entry.get("category", "").lower()
    if "soubrette" in cat or "maid" in cat:
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        print("---")
        break

# Also show a room-service soubrette if any
with open("data-roomservice.json", "r", encoding="utf-8") as f:
    rs = json.load(f)

for entry in rs:
    cat = entry.get("category", "").lower()
    if "soubrette" in cat or "maid" in cat:
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        print("---")
        break

# Show last entry in data.json for structure
print("LAST data.json entry:")
print(json.dumps(data[-1], indent=2, ensure_ascii=False))
print("\nLAST roomservice entry:")
print(json.dumps(rs[-1], indent=2, ensure_ascii=False))
print(f"\ndata.json: {len(data)} entries")
print(f"data-roomservice.json: {len(rs)} entries")
