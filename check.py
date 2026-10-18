import json
d = json.load(open("data.json", encoding="utf-8"))
# Check all unique flirty values and find S-rank ones
vals = set(e.get("flirty", "none") for e in d)
print("Valeurs flirty:", sorted(vals, key=str))
print()
for e in d:
    f = e.get("flirty", "")
    if f == "S" or f == "s" or f == 6 or f == "S-rank":
        print(f"  {e['name']}: flirty={f}")
