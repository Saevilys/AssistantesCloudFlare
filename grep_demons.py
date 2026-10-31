import json

data = json.load(open("data.json"))
for name in ["Ruan", "Yeonsu", "Prosperine"]:
    hits = [e for e in data if e["name"].lower() == name.lower()]
    for e in hits:
        print(e["name"], "|", e.get("tag"), "|", len(e.get("photos", [])), "photos")
        for p in e.get("photos", []):
            print("   ", p)
    if not hits:
        print(name, "ABSENT")
print("total:", len(data))