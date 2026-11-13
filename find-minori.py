import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total: {len(data)}")

# Find Minori to see the structure
for entry in data:
    if entry["name"] == "Minori":
        print("\n=== Minori entry ===")
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        break

# Also find the last few entries to see the pattern
print("\n=== Last 3 entries ===")
for entry in data[-3:]:
    print(json.dumps(entry, indent=2, ensure_ascii=False))
