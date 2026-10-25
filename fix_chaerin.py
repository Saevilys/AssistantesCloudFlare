import json
d = json.load(open("data.json"))
for x in d:
    if x["name"] == "Chaerin":
        x["flirty"] = 3
        print("corrigé:", x["name"], "flirty:", x["flirty"])
json.dump(d, open("data.json","w"), ensure_ascii=False, indent=1)
