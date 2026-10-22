import json
data = json.load(open("data.json"))
for name in ["Kenza","Diya"]:
    a = next(x for x in data if x["name"]==name)
    print(name)
    print(json.dumps(a["photos"], indent=1, ensure_ascii=False))
