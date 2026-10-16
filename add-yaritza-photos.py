import json

with open("data.json") as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

new_photos = [
    f"{R2}/yaritza/yaritza-reveil-2026-10-16.png",
    f"{R2}/yaritza/yaritza-pro-2026-10-16.png",
]

for a in data:
    if a["name"] == "Yaritza":
        print(f"Before: {len(a['photos'])} photos")
        for p in a["photos"]:
            print(f"  {p}")
        # Add new photos to existing ones
        for np in new_photos:
            if np not in a["photos"]:
                a["photos"].append(np)
        print(f"\nAfter: {len(a['photos'])} photos")
        for p in a["photos"]:
            print(f"  {p}")
        break

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("\nDone.")
