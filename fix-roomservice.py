import json

with open("data-roomservice.json", encoding="utf-8") as f:
    rs = json.load(f)

to_remove = {"Ligeia", "Angele", "Thandi", "Iara", "Chaerin", "Senna", "Esra", "Zoraida"}
before = len(rs)
rs = [a for a in rs if a["name"] not in to_remove]
after = len(rs)

with open("data-roomservice.json", "w", encoding="utf-8") as f:
    json.dump(rs, f, ensure_ascii=False, indent=2)

print(f"Room service: {before} → {after} (removed {before-after})")
print(f"Removed: {to_remove}")
print(f"Remaining: {[a['name'] for a in rs]}")
