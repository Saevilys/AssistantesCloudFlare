import json, sys

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

names = []
if isinstance(data, list):
    for entry in data:
        if isinstance(entry, dict):
            name = entry.get("nom") or entry.get("name") or entry.get("id", "")
            if name:
                names.append(name)
elif isinstance(data, dict):
    for key in ["assistantes", "data", "entries"]:
        if key in data:
            items = data[key]
            if isinstance(items, list):
                for entry in items:
                    if isinstance(entry, dict):
                        name = entry.get("nom") or entry.get("name") or entry.get("id", "")
                        if name:
                            names.append(name)

print(f"Total: {len(names)}")
for n in sorted(names):
    print(n)
