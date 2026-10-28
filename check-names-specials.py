import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

existing = {a["name"].lower() for a in data}

# Read room service too
with open("data-roomservice.json", encoding="utf-8") as f:
    rs = json.load(f)
existing_rs = {a["name"].lower() for a in rs}

all_existing = existing | existing_rs

candidates = {
    "Angélique": ["Seraphine", "Celestine", "Liora", "Aurelia", "Seraphina"],
    "Vampire": ["Carmilla", "Vespera", "Lenore", "Carmilla", "Mircalla"],
    "Marionnette": ["Olympia", "Marion", "Cosette", "Petrinka"],
    "Démon": ["Abyza", "Malika", "Zarena", "Ignis", "Pyra"],
    "Cyborg": ["Vex", "Nadia", "Kira", "Revy"],
    "Sirène": ["Naida", "Marina", "Coralia", "Thalassa", "Delphine"],
}

for type_name, names in candidates.items():
    print(f"\n=== {type_name} ===")
    for n in names:
        taken = n.lower() in all_existing
        print(f"  {n}: {'❌ DEJA PRIS' if taken else '✅ libre'}")
