import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for a in data:
    if a.get("name") == "Calypso":
        if "idle" in a:
            del a["idle"]
            print("idle removed")
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved.")
