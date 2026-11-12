#!/usr/bin/env python3
"""Extract unique stations from data.json."""
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
stations = {}
for a in data:
    s = a.get("station","") or a.get("ville","") or ""
    if s:
        stations.setdefault(s, 0)
        stations[s] += 1
for s, c in sorted(stations.items(), key=lambda x: -x[1]):
    print(f"  {s}: {c}")
