#!/usr/bin/env python3
import json

# data.json
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

changed = 0
for entry in data:
    s = entry.get("station", "")
    if s in ("sgr", "sgr-a", "sgr-a "):
        entry["station"] = "suyin"
        changed += 1
        print(f"  {entry['name']}: {s} -> suyin")

print(f"\ndata.json: {changed} entries renamed to suyin")

# data-roomservice.json - check too
with open("data-roomservice.json", "r", encoding="utf-8") as f:
    rs = json.load(f)

changed_rs = 0
for entry in rs:
    s = entry.get("station", "")
    if s in ("sgr", "sgr-a", "sgr-a "):
        entry["station"] = "suyin"
        changed_rs += 1
        print(f"  RS {entry['name']}: {s} -> suyin")

print(f"data-roomservice.json: {changed_rs} entries renamed to suyin")

# Write back
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data-roomservice.json", "w", encoding="utf-8") as f:
    json.dump(rs, f, ensure_ascii=False, indent=2)

print("\nDone. Both files written.")

# Verify
with open("data.json", "r", encoding="utf-8") as f:
    verify = json.load(f)
stations = {}
for e in verify:
    stations.setdefault(e.get("station", "<none>"), []).append(e["name"])
print("\nStations after rename:")
for s, names in sorted(stations.items()):
    print(f"  {s}: {len(names)}")
