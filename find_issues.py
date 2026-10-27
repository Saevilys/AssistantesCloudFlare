import json
from pathlib import Path

data = json.loads(Path("data.json").read_text(encoding="utf-8"))

for a in data:
    if a["name"] in ("Nandita", "Meifen", "Kali", "Defne"):
        print(f"--- {a['name']} ---")
        print(f"  flirty: {a.get('flirty')}")
        for p in a.get("photos", []):
            print(f"  photo: {p}")
        print()
