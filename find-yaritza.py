import json, os
base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base, "data.json"), encoding="utf-8"))
for a in data:
    if a["name"] == "Yaritza":
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break
