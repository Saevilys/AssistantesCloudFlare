#!/usr/bin/env python3
"""Check station values for Mayumi, Thinzar, Pema vs other Minorea citizens"""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

# Get all unique station values that start with "minorea" (case insensitive)
minorea_stations = set()
for e in data:
    s = e.get("station", "")
    if s and "minorea" in s.lower():
        minorea_stations.add(s)

print("=== All station values containing 'minorea' ===")
for s in sorted(minorea_stations):
    count = sum(1 for e in data if e.get("station") == s)
    print(f"  [{count}x] {s[:80]}")

print("\n=== Filter test: station === 'minorea' ===")
exact = [e for e in data if e.get("station") == "minorea"]
print(f"  Count: {len(exact)}")

print("\n=== Filter test: station starts with 'Minorea' ===")
starts = [e for e in data if e.get("station","").startswith("Minorea")]
print(f"  Count: {len(starts)}")

print("\n=== 3 secretaries station values ===")
for name in ["Mayumi", "Thinzar", "Pema"]:
    e = next((x for x in data if x.get("name") == name), None)
    if e:
        print(f"  {name}: station = '{e.get('station')}'")
