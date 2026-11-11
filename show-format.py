import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Print last 2 entries to see the format
for entry in data[-2:]:
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    print("---")

print(f"\nTotal entries: {len(data)}")
