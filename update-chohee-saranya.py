#!/usr/bin/env python3
"""Update Cho-hee and Saranya photos in data.json to include v1-v4."""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

updates = {
    "Saranya": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/saranya/saranya-v1.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/saranya/saranya-v2.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/saranya/saranya-v3.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/saranya/saranya-v4.png",
    ],
    "Cho-hee": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/cho-hee/cho-hee-v1.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/cho-hee/cho-hee-v2.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/cho-hee/cho-hee-v3.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/cho-hee/cho-hee-v4.png",
    ],
}

for entry in data:
    name = entry.get("name", "")
    if name in updates:
        entry["photos"] = updates[name]
        print(f"Updated {name}: {len(entry['photos'])} photos")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved.")
