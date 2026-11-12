#!/usr/bin/env python3
import json
candidates = ["Nyssa", "Cosima", "Livia", "Thalia", "Mireille", "Rune", "Senna"]
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
existing = {(a.get("name") or "").strip().lower() for a in data}
for c in candidates:
    print(c, "->", "TAKEN" if c.lower() in existing else "available")
