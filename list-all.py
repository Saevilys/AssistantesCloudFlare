import json

with open("data.json") as f:
    data = json.load(f)

print(f"Total: {len(data)}")
print("\nAll names:")
for i, a in enumerate(data):
    print(f"  {i+1}. {a['name']} (L{a.get('flirty','?')})")

# Check for the missing ones
missing = ["Niko", "Yara", "Savi", "Liana", "Sumaq", "Chloé", "Amira", "Freya", "Dara", 
           "Dana", "Shamsa", "Maha", "Hala", "Chiara", "Thandi", "Zeynep",
           "Anahit", "Bopha", "Amani", "Xihe", "Suwanna", "Lulit", "Fanta",
           "Miku", "Devika", "Djamila", "Yuki", "Adaeze", "Adama", "Adèle", "Adjoua", "Aigul", "Amal"]
print("\nMissing check:")
for name in missing:
    found = any(a["name"].lower() == name.lower() for a in data)
    print(f"  {name}: {'OK' if found else 'MISSING'}")
