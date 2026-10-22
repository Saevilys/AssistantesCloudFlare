import json
data = json.load(open("data.json"))
for a in data:
    if a["name"].lower() in ("kenza", "diya"):
        print(json.dumps(a, indent=2, ensure_ascii=False))
