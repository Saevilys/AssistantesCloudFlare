import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for a in data:
    if a.get("name") == "Calypso":
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break
