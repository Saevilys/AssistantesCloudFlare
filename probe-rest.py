import json

raw = open("data.json", encoding="utf-8").read()
data = json.loads(raw)

remaining = ["Zari","Eisheth","Alukah","Nyx","Nova","Echo","Ember","Sayaka","Soyun","Qiao"]
for name in remaining:
    i = raw.find(f'"name": "{name}"')
    j = raw.find('"flirty"', i)
    k = raw.find("\n", j)
    print(f"=== {name} ===")
    print(raw[i:k])
    print()
