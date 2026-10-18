import json

with open("data.json") as f:
    data = json.load(f)

print(f"Total: {len(data)} assistants")
print()

# Check for Rina, Emi, Kairi, Sora, Nuo
targets = ["rina", "emi", "kairi", "sora", "nuo"]
for a in data:
    n = a["name"].lower()
    if n in targets:
        print(f"FOUND: {a['name']} (flirty={a.get('flirty')}, photos={len(a.get('photos',[]))})")

print()
# List all names
print("All names:")
for a in data:
    print(f"  {a['name']}")
