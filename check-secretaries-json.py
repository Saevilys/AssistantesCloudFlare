#!/usr/bin/env python3
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
names = {"fariya","saanvi","ondina","mayu","ga-eun","morana","sena","mio","dilara","sora","eira","calliope"}
for a in data:
    n = (a.get("name","") or "").lower()
    if n in names:
        print(n, "| station:", a.get("station"), "| tag:", a.get("tag"), "| photos:", len(a.get("photos",[])))
