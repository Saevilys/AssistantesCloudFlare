#!/usr/bin/env python3
"""Check which names are already taken in data.json."""
import json, os

# Names to check
candidates = [
    "vespera", "lyra", "nyssa", "thalia", "mireille", "sable", "coco",
    "kalina", "nadia", "sable", "feralda", "ines", "margaux", "yuna",
    "livia", "drusilla", "aela", "serafina", "morgan", "velvet",
    "noctis", "lunaria", "vesper", "sable", "rune", "ember",
    "kira", "naya", "zara", "miela", "senna", "valeria",
    "cosima", "delphine", "ivy", "harper", "mika", "ren",
    "suki", "nova", "lacey", "faye", "gwen", "mira",
    "yumi", "kira", "ada", "lila", "nori", "vita",
]

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

existing = set()
for a in data:
    existing.add((a.get("name","") or "").lower().strip())

# Also check vault
vault_names = set()
vault_path = "../vault/assistantes"
if os.path.isdir(vault_path):
    for fn in os.listdir(vault_path):
        if fn.endswith(".md"):
            vault_names.add(fn[:-3].lower())

for name in candidates:
    taken_json = name.lower() in existing
    taken_vault = name.lower() in vault_names
    status = "TAKEN (json+vault)" if (taken_json and taken_vault) else "TAKEN (json)" if taken_json else "TAKEN (vault)" if taken_vault else "OK"
    if status == "OK":
        print(f"  {name}: AVAILABLE")

print("\n--- Existing names in data.json for reference ---")
for a in sorted(data, key=lambda x: x.get("name","")):
    print(f"  {a.get('name','')}")
