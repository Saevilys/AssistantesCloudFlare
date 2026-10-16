import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total: {len(data)}")
names = [d["name"] for d in data]
for n in ["Niko", "Yara", "Savi", "Liana", "Sumaq"]:
    print(f"  {n}: {'IN' if n in names else 'MISSING'}")
