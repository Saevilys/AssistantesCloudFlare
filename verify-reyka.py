import json

# Check local repo JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total roster: {len(data)}")

# Find Reyka
reyka = [c for c in data if c.get("name") == "Reyka"]
if reyka:
    r = reyka[0]
    print(f"\nReyka found: id={r['id']}, station={r['station']}, role={r['role']}")
    print(f"  photos: {len(r.get('photos', []))}")
    for p in r.get("photos", []):
        print(f"    {p}")
else:
    print("REYKA NOT FOUND!")

# Sentinels
sentinel_names = ["Datchesi", "Joëlle", "Malya", "Kurenai", "Iseul"]
for name in sentinel_names:
    found = [c for c in data if c.get("name") == name]
    print(f"  {name}: {'OK' if found else 'MISSING'}")
