import json, os

base = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base, "data.json"), encoding="utf-8") as f:
    data = json.load(f)

new_urls = [
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yaritza/yaritza-soir-1.png",
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yaritza/yaritza-soir-2.png",
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yaritza/yaritza-soir-3.png",
    "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/yaritza/yaritza-fin-journee.png",
]

for a in data:
    if a["name"] == "Yaritza":
        existing = set(a.get("photos", []))
        for url in new_urls:
            if url not in existing:
                a.setdefault("photos", []).append(url)
        print(f"Yaritza now has {len(a['photos'])} photos")
        for p in a["photos"]:
            print(f"  {p}")
        break

with open(os.path.join(base, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("\nDone — data.json updated")
