import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

base = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/ruoxi/"
e = data[527]
e["photos"] = [
    base + "ruoxi-v1.png",
    base + "ruoxi-v2.png",
    base + "ruoxi-v3.png",
]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('done,', len(e["photos"]), 'photos')
