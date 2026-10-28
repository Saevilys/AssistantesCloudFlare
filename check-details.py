import json, os, re

# Check the 20 flirty references in index.html
with open("index.html", encoding="utf-8") as f:
    idx = f.read()
for m in re.finditer(r'flirty', idx):
    start = max(0, m.start()-30)
    end = min(len(idx), m.end()+30)
    print(f"@{m.start()}: ...{idx[start:end]}...")
    print()

# Check special:true on tagged entries
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
print("=== special:true status ===")
for a in data:
    if a.get("tag"):
        print(f"  {a['name']}: tag={a['tag']} special={a.get('special', 'MISSING')}")

# Check pick.py is_speciale
print("\n=== pick.py is_speciale issue ===")
print("is_speciale checks: flirty >= 5 OR region == 'Androides'")
print("Succubes (tag=succube, no flirty): NOT caught → go to CLASSIQUE pool ❌")
print("Surnaturel (tag=surnaturel, no flirty): NOT caught → go to CLASSIQUE pool ❌")
print("Androides (tag=androide, region=Androides): caught by region check ✅")
print("\n→ pick.py needs update to use tag instead of flirty")
