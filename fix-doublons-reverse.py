import json

# 1. Remettre les 7 dans data-roomservice.json (je viens de les retirer par erreur)
# Zoraida ne retourne PAS dans le room service (elle reste en succube dans data.json)
with open("data-roomservice.json", encoding="utf-8") as f:
    rs = json.load(f)

rs_names = {a["name"] for a in rs}
to_restore = ["Ligeia", "Angele", "Thandi", "Iara", "Chaerin", "Senna", "Esra"]

# Re-add from the backup (we need to re-read the old version — reconstruct from data.json)
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

for name in to_restore:
    if name not in rs_names:
        entry = next((a for a in data if a["name"] == name), None)
        if entry:
            rs.append(entry)
            print(f"Restored {name} to room service")

with open("data-roomservice.json", "w", encoding="utf-8") as f:
    json.dump(rs, f, ensure_ascii=False, indent=2)
print(f"Room service: {len(rs)} entries")

# 2. Retirer les 7 de data.json (pas Zoraida)
to_remove_from_data = {"Ligeia", "Angele", "Thandi", "Iara", "Chaerin", "Senna", "Esra"}
before = len(data)
data = [a for a in data if a["name"] not in to_remove_from_data]
after = len(data)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"data.json: {before} → {after} (removed {before-after})")
