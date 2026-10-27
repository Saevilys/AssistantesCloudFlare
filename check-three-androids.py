import json
data = json.load(open("data.json"))
names = {e["name"].lower() for e in data}
for n in ["sayaka", "reika", "kiriko", "kanna", "miyu"]:
    print(n, "TAKEN" if n in names else "FREE")
print("total", len(data))
