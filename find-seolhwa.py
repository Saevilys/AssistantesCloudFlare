import json
with open("data.json") as f:
    data = json.load(f)
for a in data:
    if a.get("name","").lower() == "seolhwa":
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break
