#!/usr/bin/env python3
"""Find Yaritza in local data.json and check her photo URLs"""
import json

with open("data.json") as f:
    data = json.load(f)

for a in data:
    if a["name"] == "Yaritza":
        print(f"Yaritza — {len(a['photos'])} photos:")
        for p in a["photos"]:
            print(f"  {p}")
        break
else:
    print("Yaritza NOT found")
    print(f"Total entries: {len(data)}")
