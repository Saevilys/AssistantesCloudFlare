import json

with open("data.json") as f:
    data = json.load(f)

for name in ["Emi", "Kairi", "Sora", "Nuo"]:
    for a in data:
        if a["name"] == name:
            print(f"✓ {name} (flirty={a['flirty']}, photos={len(a['photos'])}, origin={a['origin']})")
            for p in a["photos"]:
                print(f"  {p}")
            break

print(f"\nTotal: {len(data)} assistants")
