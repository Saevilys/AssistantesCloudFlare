#!/usr/bin/env python3
"""Sync check complet : data.json, data-roomservice.json, pick.py, vault."""
import json, os, sys

# 1. data.json (nemini local)
with open("data.json") as f:
    data = json.load(f)
names_main = {e["name"] for e in data}
names_main_lower = {e["name"].lower() for e in data}
print(f"=== data.json (nemini) ===")
print(f"Total: {len(data)}")

# Doublons (insensible à la casse)
from collections import Counter
lower_counts = Counter(names_main_lower)
dups = {n for n, c in lower_counts.items() if c > 1}
if dups:
    print(f"DOUBLONS: {dups}")
else:
    print("Zéro doublon ✓")

# Actives
actives = [e for e in data if e.get("active", False)]
print(f"Actives: {len(actives)}")

# Specials
specials = [e for e in data if e.get("special", False)]
print(f"Specials: {len(specials)} — {[e['name'] for e in specials]}")

# Flirty
flirt6 = [e["name"] for e in data if e.get("flirty", 0) == 6]
print(f"Flirty=6: {len(flirt6)} — {flirt6}")

# Régions
regions = Counter(e.get("region", "?") for e in data)
print(f"Régions: {dict(regions)}")

# 2. data-roomservice.json
rs_path = "data-roomservice.json"
if os.path.exists(rs_path):
    with open(rs_path) as f:
        rs = json.load(f)
    names_rs = {e["name"] for e in rs}
    print(f"\n=== data-roomservice.json ===")
    print(f"Total: {len(rs)}")
    # Doublons internes
    rs_lower = {e["name"].lower() for e in rs}
    rs_dups = {n for n, c in Counter(rs_lower).items() if c > 1}
    if rs_dups:
        print(f"DOUBLONS RS: {rs_dups}")
    else:
        print("Zéro doublon ✓")
    # Chevauchement avec main
    overlap = names_main & names_rs
    if overlap:
        print(f"CHEVAUCHEMENT main↔RS: {overlap}")
    else:
        print("Pas de chevauchement ✓")
else:
    print("\ndata-roomservice.json: ABSENT")
    names_rs = set()

# 3. pick.py — extraire le pool
print(f"\n=== pick.py (rotation) ===")
try:
    with open("../code/rotation/pick.py") as f:
        pick_content = f.read()
    # Le pool est dans data.json lu par pick.py
    # Chercher les noms dans le pick.py
    # pick.py lit data.json donc le pool = noms actifs de data.json
    print("pick.py lit data.json (le pool = actives de data.json)")
    # Vérifier si pick.py référence data.json
    if "data.json" in pick_content:
        print("Réfère à data.json ✓")
    else:
        print("ATTENTION: ne réfère pas à data.json ?")
    # Chercher data-roomservice
    if "data-roomservice" in pick_content or "roomservice" in pick_content:
        print("Réfère à room service ✓")
except FileNotFoundError:
    print("pick.py ABSENT")

# 4. who.py — assistante du jour
print(f"\n=== who.py ===")
try:
    with open("../code/rotation/who.py") as f:
        who_content = f.read()
    print("who.py présent ✓")
except FileNotFoundError:
    print("who.py ABSENT")

# prev_assistant.txt
try:
    with open("../code/rotation/prev_assistant.txt") as f:
        prev = f.read().strip()
    print(f"Assistante du jour (prev): {prev}")
    if prev in names_main:
        print(f"  → présent dans data.json ✓")
    else:
        print(f"  → ABSENT de data.json !")
except FileNotFoundError:
    print("prev_assistant.txt ABSENT")

# 5. Vault
print(f"\n=== Vault ===")
vault_dir = "../vault/assistantes"
if os.path.exists(vault_dir):
    vault_files = [f for f in os.listdir(vault_dir) if f.endswith(".md")]
    vault_names = {f[:-3] for f in vault_files}  # strip .md
    print(f"Fiches vault: {len(vault_files)}")
    
    # Manquantes dans vault
    all_names = names_main | names_rs
    missing_vault = sorted(all_names - vault_names)
    if missing_vault:
        print(f"Manquantes ({len(missing_vault)}): {missing_vault}")
    else:
        print("Toutes présentes ✓")
    
    # Orphelines (dans vault mais pas dans les JSON)
    orphans = sorted(vault_names - all_names)
    if orphans:
        print(f"Orphelines ({len(orphans)}): {orphans}")
    else:
        print("Zéro orpheline ✓")
else:
    print(f"Dossier {vault_dir} ABSENT")

print(f"\n=== RÉSUMÉ ===")
print(f"data.json: {len(data)} ({len(actives)} actives, {len(specials)} specials)")
print(f"data-roomservice.json: {len(rs) if 'rs' in dir() else '?'}")
print(f"Vault: {len(vault_files) if 'vault_files' in dir() else '?'}")
