import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for a in data:
    if a.get("name") == "Calypso":
        a["photos"] = [
            "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/calypso/calypso-1.jpg"
        ]
        break

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done. Calypso photos reduced to 1.")
