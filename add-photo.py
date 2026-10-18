import json
d = json.load(open("data.json", encoding="utf-8"))
k = [e for e in d if e["name"] == "Keilani"][0]
url = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/keilani/keilani-v8-beach.png"
if url not in k["photos"]:
    k["photos"].append(url)
    json.dump(d, open("data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("ajouté,", len(k["photos"]), "photos")
else:
    print("déjà là")
