import json

with open("data.json") as f:
    data = json.load(f)

for a in data:
    if a["name"].lower() == "mio":
        print(json.dumps(a, indent=2, ensure_ascii=False))
