import json

with open("data.json") as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

for name in ["Niko","Yara","Savi","Liana","Sumaq"]:
    entries = [a for a in data if a["name"] == name]
    if not entries:
        print(f"{name}: NOT FOUND")
        continue
    a = entries[0]
    print(f"\n{name}:")
    for p in a["photos"]:
        print(f"  {p}")
