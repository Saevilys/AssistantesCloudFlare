import json
with open("data.json", "r") as f:
    data = json.load(f)
print(f"Total: {len(data)}")
print(f"Last 3: {[a['name'] for a in data[-3:]]}")
