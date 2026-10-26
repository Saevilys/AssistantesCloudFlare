#!/usr/bin/env python3
"""Put aino-v1b-2.png as first photo of Aino in data.json."""
import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

new_url = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/aino/aino-v1b-2.png"

for entry in data:
    if entry.get("name", "").lower() == "aino":
        photos = entry.get("photos", [])
        if new_url not in photos:
            photos.insert(0, new_url)
        entry["photos"] = photos
        print("Photos Aino:", len(photos))
        break

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Saved.")
