#!/usr/bin/env python3
import json

# Read from the desk copy (the script runs on the computer, 
# but the desk folder /github/ is mounted)
path = "data.json"
with open(path, "r") as f:
    data = json.load(f)

for a in data:
    if a.get("name") == "Mei":
        new_urls = [
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/mei/mei-4-cafe.png",
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/mei/mei-5-library.png",
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/mei/mei-6-bedroom.png",
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/mei/mei-7-night.png"
        ]
        a["photos"].extend(new_urls)
        print("Updated Mei photos:", len(a["photos"]), "total")
        break

with open(path, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved.")
