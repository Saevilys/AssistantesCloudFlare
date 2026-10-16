import json
with open("data.json") as f:
    data = json.load(f)
print(f"Total: {len(data)}")
print("Last 7:")
for a in data[-7:]:
    print(f"  {a['name']} (L{a['flirty']}) — {len(a['photos'])} photos — {a['photos'][0] if a['photos'] else 'NO PHOTOS'}")
# verify JSON is valid
print("\nJSON valid ✓")
# check all 5
for name in ["Niko","Yara","Savi","Liana","Sumaq"]:
    found = [a for a in data if a["name"] == name]
    if found:
        a = found[0]
        print(f"  {name}: L{a['flirty']}, {a['origin']}, {len(a['photos'])} photos, active={a.get('active','?')}")
    else:
        print(f"  {name}: MISSING!")
