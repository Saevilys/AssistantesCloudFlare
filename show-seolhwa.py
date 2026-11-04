import json
with open("data.json") as f:
    data = json.load(f)
for a in data:
    if a.get("name","").lower() == "seolhwa":
        for p in a["photos"]:
            print(p)
        break
