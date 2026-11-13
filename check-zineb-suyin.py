import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

from collections import defaultdict
stations = defaultdict(list)
for e in data:
    s = e.get("station", "unknown")
    stations[s].append(e)

for station in ["zineb", "suyin"]:
    print(f"\n=== Station {station} ({len(stations[station])} entries) ===")
    for e in stations[station]:
        tag = e.get("tag") or "—"
        print(f"  {e['name']} | {e.get('origin','?')} | tag={tag}")
