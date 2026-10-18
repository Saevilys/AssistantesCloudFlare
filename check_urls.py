import json

with open("data.json") as f:
    data = json.load(f)

# Check photo URL patterns for recent assistants
for name in ["yuzuki", "keilani", "elektra", "carmilla", "myunghee", "senna"]:
    for a in data:
        if a["name"].lower() == name:
            photos = a.get("photos", [])
            if photos:
                print(f"{a['name']}: {photos[0]}")
            break
