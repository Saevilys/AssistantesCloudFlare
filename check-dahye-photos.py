import json
data = json.load(open("data.json"))
for a in data:
    if a["name"] == "Dahye":
        print(repr(json.dumps(a["photos"], ensure_ascii=False)))
