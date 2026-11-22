import json

with open("data.json") as f:
    data = json.load(f)

for c in data:
    if c.get("name") == "Nadya":
        photos = c.get("photos", [])
        print(f"Nadya: {len(photos)} photos")
        for i, p in enumerate(photos):
            print(f"  [{i}] {p}")
        has_dessin = any("dessin" in p for p in photos)
        has_dodo = any("dodo" in p for p in photos)
        has_night = any("night-avatar" in p for p in photos)
        print(f"\nDessin: {has_dessin}")
        print(f"Dodo: {has_dodo}")
        print(f"Night avatar: {has_night}")
        break
else:
    print("Nadya NOT FOUND in JSON!")
