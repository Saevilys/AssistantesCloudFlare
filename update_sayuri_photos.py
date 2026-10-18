import json

with open("data.json") as f:
    data = json.load(f)

PUB = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

new_photos = [
    f"{PUB}/img/sayuri/sayuri-v5.png",
    f"{PUB}/img/sayuri/sayuri-v6.png",
    f"{PUB}/img/sayuri/sayuri-v7.png",
    f"{PUB}/img/sayuri/sayuri-v8.png",
    f"{PUB}/img/sayuri/sayuri-v9.png",
    f"{PUB}/img/sayuri/sayuri-v10.png",
]

for a in data:
    if a["name"] == "Sayuri":
        a["photos"].extend(new_photos)
        print(f"Sayuri: {len(a['photos'])} photos total")
        for p in a["photos"]:
            print(f"  {p}")
        break

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\ndata.json updated")
