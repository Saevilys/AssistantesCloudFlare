#!/usr/bin/env python3
"""Undo the bad fix: restore Yasmine(expat, Liban, reporter), revert Yara changes."""
import json, os

here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, "data.json"), encoding="utf-8") as f:
    data = json.load(f)

# Revert Yara changes
for e in data:
    if e["name"] == "Yara":
        if e.get("station") == "expat":
            e["station"] = None
            print("Reverted Yara station to None")
        if e.get("tag") == "reporter":
            e.pop("tag", None)
            print("Reverted Yara tag to None")

# Restore Yasmine(expat) entry
yasmine_expat = {
    "name": "Yasmine",
    "age": 25,
    "origin": "Liban",
    "city": "Beyrouth",
    "region": "Moyen-Orient",
    "station": "expat",
    "active": True,
    "flirty": 3,
    "tag": "reporter",
    "desc": "Peau olive aux sous-tons dorés et pores visibles, longs cheveux bruns foncé raides past shoulders, yeux bruns profonds, nez droit, lèvres pleines, visage ovale. Silhouette pulpeuse, taille fine, hanches larges, poitrine généreuse. Tenues décontractées-chic, tops moulants, jupes midi.",
    "voice": "La reporter terrain. Curieuse, vive, pose des questions qui vont droit au but.",
    "trait": "Elle flaire le scoop là où les autres voient du banal.",
    "photos": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yasmine/yasmine-v1.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yasmine/yasmine-v2.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yasmine/yasmine-v3.png"
    ]
}

data.append(yasmine_expat)
print(f"Restored Yasmine(expat). Total: {len(data)}")

# Check duplicates
from collections import Counter
dupes = [n for n, c in Counter(e["name"] for e in data).items() if c > 1]
print(f"Duplicates: {dupes}")
for d in dupes:
    entries = [(e["name"], e.get("station"), e.get("origin"), e.get("tag")) for e in data if e["name"] == d]
    print(f"  {d}: {entries}")

with open(os.path.join(here, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("data.json written.")
