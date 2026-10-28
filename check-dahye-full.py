import json
data = json.load(open("data.json"))
for a in data:
    if a["name"] == "Dahye":
        print(json.dumps(a, ensure_ascii=False, indent=1))
