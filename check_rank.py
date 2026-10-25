import json
d = json.load(open("data.json"))
for x in d:
    if x["name"] in ("Chaerin","Seojin","Dahye"):
        print(x["name"], "flirty:", x.get("flirty"), "special:", x.get("special"))
