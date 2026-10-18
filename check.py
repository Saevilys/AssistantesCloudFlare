import json
d = json.load(open("data.json", encoding="utf-8"))
k = [e for e in d if e["name"] == "Keilani"][0]
print(json.dumps(k, ensure_ascii=False, indent=2))
print(f"\nTotal: {len(d)} assistantes")
