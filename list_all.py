import json

with open("data.json", encoding="utf-8") as f:
    roster = json.load(f)
with open("data-roomservice.json", encoding="utf-8") as f:
    rs = json.load(f)

roster_names = [d["name"] for d in roster]
rs_names = [d["name"] for d in rs]

print(f"Roster principal: {len(roster_names)} entrees")
print(f"Room service: {len(rs_names)} entrees")
print("\nRoom service noms existants:")
for n in rs_names:
    print(f"  {n}")

all_names = set(n.lower() for n in roster_names + rs_names)
print(f"\nTotal noms uniques: {len(all_names)}")
