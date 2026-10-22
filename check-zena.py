import json
data = json.load(open("data.json"))
for a in data:
    if a["name"].lower() == "zena":
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break
else:
    print("Zena non trouvée dans data.json")
