import json
d = json.load(open("data.json", encoding="utf-8"))
names = sorted(set(e["name"].lower() for e in d))
print(len(d), "assistantes")
for n in names:
    print(n)
