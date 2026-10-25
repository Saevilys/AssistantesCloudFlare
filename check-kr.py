import json
d = json.load(open("data.json"))
names = [a["name"].lower() for a in d]
for n in ("soomin","ryunhee"):
    print(n, n in names)
for a in d:
    orig = a.get("origin","").lower()
    if "cor" in orig or "korea" in orig:
        print(a["name"], a.get("origin"), a.get("city"), "flirty="+str(a.get("flirty","?")))
