import json

with open("data.json") as f:
    data = json.load(f)

names = [a["name"].lower() for a in data]
print(f"Total: {len(data)} assistantes")
for n in ["miral","kiana","rana"]:
    if n in names:
        print(f"  {n}: DÉJÀ PRÉSENT")
    else:
        print(f"  {n}: absent, OK")

# Afficher le dernier entry pour voir la structure exacte
print("\nDernier entry:")
print(json.dumps(data[-1], indent=1, ensure_ascii=False))
