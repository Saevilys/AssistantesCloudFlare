import json, os
base = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(base, "data.json")))
lst = data if isinstance(data, list) else data.get("assistants", [])
names = {a["name"] for a in lst}
for n in ["Emi", "Kanna", "Hina"]:
    print(n, "LIBRE" if n not in names else "DEJA PRIS")
