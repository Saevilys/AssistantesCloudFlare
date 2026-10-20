#!/usr/bin/env python3
"""Fetch old data.json from commit 8f88de2, extract name order, reorder current data.json."""
import json, urllib.request

# Fetch old version
old_url = "https://raw.githubusercontent.com/Saevilys/AssistantesCloudFlare/8f88de2/data.json"
req = urllib.request.Request(old_url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as r:
    old_data = json.loads(r.read())

old_names = [item["name"] for item in old_data]
print(f"Old data.json: {len(old_names)} entries")
print(f"First 10: {old_names[:10]}")
print(f"Last 10: {old_names[-10:]}")

# Read current data.json
with open("data.json") as f:
    current = json.load(f)

current_names = {item["name"] for item in current}
old_names_set = set(old_names)

# Entries in old order
ordered = []
used = set()
for name in old_names:
    item = next((x for x in current if x["name"] == name), None)
    if item:
        ordered.append(item)
        used.add(name)

# New entries not in old version — added after commit 8f88de2
# Order based on commit history:
# 26fb8f7: Hodan, Danait
# 3b4b3ad: Moana, Maeva, Tahia, Maya
# 0bc344d: Yomi, Kyra, Kalya, Sira
# 1214e9d: Yuka
# 7398d5a: Thandi, Makena, Akua, Zuri
# 73d91da: Bomsori, Danbi
# 7acd62b: Kam
# fd75619: Chaewon, Ami

new_order = [
    "Hodan", "Danait",
    "Moana", "Maeva", "Tahia", "Maya",
    "Yomi", "Kyra", "Kalya", "Sira",
    "Yuka",
    "Thandi", "Makena", "Akua", "Zuri",
    "Bomsori", "Danbi",
    "Kam",
    "Chaewon", "Ami",
]

for name in new_order:
    item = next((x for x in current if x["name"] == name), None)
    if item:
        ordered.append(item)
        used.add(name)

# Any remaining entries not accounted for
remaining = [item for item in current if item["name"] not in used]
if remaining:
    print(f"WARNING: {len(remaining)} entries not in old order or commit history:")
    for item in remaining:
        print(f"  {item['name']}")
    ordered.extend(remaining)

# Verify
print(f"\nCurrent: {len(current)} entries")
print(f"Ordered: {len(ordered)} entries")

# Check for missing
ordered_names = set(item["name"] for item in ordered)
missing = current_names - ordered_names
if missing:
    print(f"MISSING from ordered: {missing}")
else:
    print("All entries accounted for ✓")

# Check for duplicates
seen = set()
dups = []
for item in ordered:
    if item["name"] in seen:
        dups.append(item["name"])
    seen.add(item["name"])
if dups:
    print(f"DUPLICATES: {dups}")
else:
    print("No duplicates ✓")

# Write reordered data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ordered, f, ensure_ascii=False, indent=2)
print("\ndata.json rewritten in arrival order ✓")
print(f"First 5: {[item['name'] for item in ordered[:5]]}")
print(f"Last 5: {[item['name'] for item in ordered[-5:]]}")
