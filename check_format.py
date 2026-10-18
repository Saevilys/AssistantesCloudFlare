import json

with open("data.json") as f:
    data = json.load(f)

# Print full entry for a simple L1 and L2 assistant
for a in data:
    if a["name"] == "Devika":  # L1
        print("=== L1 example: Devika ===")
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break

for a in data:
    if a["name"] == "Yuki":  # L2
        print("\n=== L2 example: Yuki ===")
        print(json.dumps(a, indent=2, ensure_ascii=False))
        break
