import json
data = json.load(open("./data.json", encoding="utf-8"))
names = [a["name"] for a in data]
print(len(data), "entrées | Nova:", "Nova" in names, "| Echo:", "Echo" in names, "| Ember:", "Ember" in names)
