import json, os

base = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base, "data.json"), encoding="utf-8") as f:
    data = json.load(f)

new_url = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yaritza/yaritza-pixel-art.png"

for a in data:
    if a["name"] == "Yaritza":
        if new_url in a["photos"]:
            print("already there")
        else:
            a["photos"].append(new_url)
            print(f"added — {len(a['photos'])} photos total")
        break

with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1, ensure_ascii=False)
print("saved")
