import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
print(f"Total: {len(data)}")
print(f"Last 5: {[c['name'] for c in data[-5:]]}")
for name in ["Aimi","Ploi","Lan"]:
    found = [c for c in data if c.get("name") == name]
    print(f"  {name}: {'FOUND' if found else 'MISSING'}")
