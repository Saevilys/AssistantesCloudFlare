import json

data = json.load(open('data.json', encoding='utf-8'))
BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

for a in data:
    if a["name"] == "Eisheth":
        new = [
            f"{BASE}/img/eisheth/eisheth-v1.png",
            f"{BASE}/img/eisheth/eisheth-v2.png",
            f"{BASE}/img/eisheth/eisheth-v3.png",
            f"{BASE}/img/eisheth/eisheth-v4.png",
            f"{BASE}/img/eisheth/eisheth-v5.png",
            f"{BASE}/img/eisheth/eisheth-v6.png",
            f"{BASE}/img/eisheth/eisheth-v7.png",
        ]
        a["photos"] = new
        print(f"Eisheth: {len(a['photos'])} photos")
        for p in a["photos"]:
            print(f"  {p}")
        break

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"\nTotal: {len(data)} assistantes")
