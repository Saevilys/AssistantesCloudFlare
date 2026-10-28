import json
d = json.load(open("data.json"))
for a in d:
    if a["name"].lower() == "dahye":
        print(json.dumps(a, indent=2, ensure_ascii=False))
