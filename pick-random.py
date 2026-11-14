#!/usr/bin/env python3
"""Pick a random assistant for Discord ping — not Iliana (today's)."""
import json, random

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

exclude = {"Iliana"}
pool = [e for e in data if e["name"] not in exclude and e.get("active", True)]
pick = random.choice(pool)
print(f"{pick['name']} — {pick.get('origin', '?')} — {pick.get('city', '?')} — tag={pick.get('tag', 'none')} — flirty={pick.get('flirty', '?')}")
print(f"photos: {len(pick.get('photos', []))}")
for p in pick.get("photos", []):
    print(f"  {p}")
print(f"desc: {pick.get('desc', '')[:200]}")
