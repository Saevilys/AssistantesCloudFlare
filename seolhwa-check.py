import json
with open("data.json") as f:
    data = json.load(f)
for a in data:
    n = a.get("name","").lower()
    if "seolhwa" in n:
        print(json.dumps(a["photos"], indent=2, ensure_ascii=False))
        break
