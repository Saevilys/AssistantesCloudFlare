import json
from pathlib import Path

p = Path("data.json")
data = json.loads(p.read_text(encoding="utf-8"))

changed = []
for a in data:
    if a["name"] == "Kali":
        a["flirty"] = 4
        changed.append("Kali")
    elif a["name"] == "Defne":
        a["flirty"] = 4
        changed.append("Defne")

p.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Updated: {changed}")

# verify
data2 = json.loads(p.read_text(encoding="utf-8"))
for a in data2:
    if a["name"] in ("Kali", "Defne"):
        print(f"{a['name']}: flirty = {a['flirty']}")
