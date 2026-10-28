import json
d = json.load(open("data.json"))
a = [x for x in d if x["name"] == "Dahye"][0]
print(len(a["photos"]))
for p in a["photos"]: print(p.split("/img/")[-1])
