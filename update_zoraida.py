#!/usr/bin/env python3
import json

with open("data.json") as f:
    data = json.load(f)

for a in data:
    if a["name"] == "Zoraida":
        a["photos"].extend([
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/zoraida/zoraida-zoraida-night-visit.png",
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/zoraida/zoraida-zoraida-dodo.png",
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/zoraida/zoraida-zoraida-dessin-du-jour.png"
        ])
        print("Photos Zoraida:", len(a["photos"]))
        break

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
