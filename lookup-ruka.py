import json
d = json.load(open("data.json", encoding="utf-8"))
arr = d if isinstance(d, list) else d.get("assistantes", d.get("data", []))
for a in arr:
    if a.get("name", "").lower() == "ruka":
        print(json.dumps(a, ensure_ascii=False, indent=1)[:2000])
        break
else:
    print("pas de ruka")
print("total:", len(arr))
