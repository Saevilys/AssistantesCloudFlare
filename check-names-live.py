#!/usr/bin/env python3
"""Check names against the CURRENT github data.json + vault files."""
import json, os, glob

# Load current github data.json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

existing_names = {a.get("name","").lower() for a in data}
print(f"data.json: {len(existing_names)} entries")

# Also check vault files
vault_names = set()
for f in glob.glob("/vault/assistantes/*.md"):
    base = os.path.basename(f).replace(".md","").lower()
    vault_names.add(base)
print(f"vault: {len(vault_names)} fiches")

# Names to check
to_check = ["Fariya", "Saanvi", "Ondina", "Mayu", "Eira", "Calliope",
            "Nari", "Soyeon", "Jiyeon", "Seoyeon", "Yewon", "Sooyun", 
            "Jieun", "Haeri", "Nayeon"]

print("\n=== Results ===")
for name in to_check:
    in_data = name.lower() in existing_names
    in_vault = name.lower() in vault_names
    status = []
    if in_data: status.append("IN data.json")
    if in_vault: status.append("IN vault")
    if not status: status.append("FREE")
    print(f"  {name}: {' + '.join(status)}")
