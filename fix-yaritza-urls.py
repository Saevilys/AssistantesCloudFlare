#!/usr/bin/env python3
"""Fix Yaritza photo URLs in data.json"""
import json

with open("data.json") as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

for a in data:
    if a["name"] == "Yaritza":
        # Replace the old broken URLs with clean ones
        new_photos = [
            f"{R2}/yaritza/yaritza-1.png",
            f"{R2}/yaritza/yaritza-2.png",
            f"{R2}/yaritza/yaritza-3.png",
            f"{R2}/yaritza/yaritza-4.png",
            f"{R2}/yaritza/yaritza-5.png",
            f"{R2}/yaritza/yaritza-6.png",
        ]
        a["photos"] = new_photos
        print(f"Yaritza — {len(a['photos'])} photos:")
        for p in a["photos"]:
            print(f"  {p}")
        break

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("\nDone.")
