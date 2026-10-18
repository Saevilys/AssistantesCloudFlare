import json

with open("data.json") as f:
    data = json.load(f)

PUB = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"
IDLE_URL = f"{PUB}/img/sayuri/sayuri-hover-v8.mp4"

for a in data:
    if a["name"] == "Sayuri":
        a["idle"] = IDLE_URL
        print(f"Sayuri idle set to: {IDLE_URL}")
        break

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("data.json updated")
