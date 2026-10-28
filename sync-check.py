import json, os, re

# 1. data.json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
data_names = [a["name"] for a in data]
tagged = [a["name"] for a in data if a.get("tag")]
flirty_leftover = [(a["name"], a.get("flirty")) for a in data if a.get("flirty") and a.get("tag")]
special_no_tag = [a["name"] for a in data if a.get("special") and not a.get("tag")]
tag_no_special = [a["name"] for a in data if a.get("tag") and not a.get("special")]

print(f"=== data.json : {len(data)} entrées ===")
print(f"Avec tag: {len(tagged)} → {', '.join(tagged)}")
print(f"Flirty + tag (résidu): {flirty_leftover if flirty_leftover else 'clean'}")
print(f"special=true sans tag: {special_no_tag if special_no_tag else 'clean'}")
print(f"tag sans special=true: {tag_no_special if tag_no_special else 'clean'}")

# Tag distribution
from collections import Counter
tags = Counter(a.get("tag") for a in data if a.get("tag"))
print(f"Tag distribution: {dict(tags)}")

# Flirty distribution (for non-tagged)
flirty = Counter(a.get("flirty",0) for a in data if not a.get("tag"))
print(f"Flirty (non-tagged): {dict(sorted(flirty.items()))}")

# 2. data-roomservice.json
rs_path = "data-roomservice.json"
if os.path.exists(rs_path):
    with open(rs_path, encoding="utf-8") as f:
        rs = json.load(f)
    rs_names = [a["name"] for a in rs]
    print(f"\n=== data-roomservice.json : {len(rs)} entrées ===")
    print(", ".join(rs_names))
    # Check overlap with main
    overlap = set(rs_names) & set(data_names)
    if overlap:
        print(f"⚠️ Dans les deux: {overlap}")
else:
    print(f"\n=== data-roomservice.json : NOT FOUND ===")

# 3. pick.py
pick_path = "/code/rotation/pick.py"
if os.path.exists(pick_path):
    with open(pick_path, encoding="utf-8") as f:
        pick_raw = f.read()
    # Extract pool names - look for the assistantes dict/list
    pick_names = re.findall(r'"([A-Z][a-z]+)"', pick_raw)
    # Filter to likely assistant names (cap first letter)
    pick_set = set()
    for m in re.finditer(r'["\']([A-Z][a-z]+)["\']', pick_raw):
        name = m.group(1)
        if name in data_names or name in (rs_names if 'rs_names' in dir() else []):
            pick_set.add(name)
    print(f"\n=== pick.py ===")
    print(f"Noms trouvés dans pick.py: {sorted(pick_set)}")
    in_pick_not_data = pick_set - set(data_names)
    in_data_not_pick = set(data_names) - pick_set
    print(f"Dans pick.py mais pas data.json: {in_pick_not_data if in_pick_not_data else 'clean'}")
    print(f"Dans data.json mais pas pick.py: {sorted(in_data_not_pick)}")
else:
    print(f"\n=== pick.py : NOT FOUND at {pick_path} ===")

# 4. Vault profiles
vault_path = "/vault/assistantes/"
if os.path.exists(vault_path):
    vault_files = [f for f in os.listdir(vault_path) if f.endswith(".md")]
    vault_names = set(f.replace(".md","") for f in vault_files)
    print(f"\n=== Vault : {len(vault_files)} profils ===")
    all_names = set(data_names) | (set(rs_names) if 'rs_names' in dir() else set())
    missing_vault = all_names - vault_names
    orphan_vault = vault_names - all_names
    print(f"Manquants dans vault: {sorted(missing_vault) if missing_vault else 'clean'}")
    print(f"Orphelins vault: {sorted(orphan_vault) if orphan_vault else 'clean'}")
else:
    print(f"\n=== Vault : NOT FOUND ===")

# 5. Check index.html filter
idx_path = "index.html"
if os.path.exists(idx_path):
    with open(idx_path, encoding="utf-8") as f:
        idx = f.read()
    # Find the filter line
    m = re.search(r'all\.filter\([^)]+\)', idx)
    if m:
        print(f"\n=== index.html filter ===")
        print(f"Filter: {m.group(0)}")
    else:
        print(f"\n=== index.html filter : NOT FOUND ===")
    # Check for leftover flirty references
    flirty_refs = [m.start() for m in re.finditer(r'flirty', idx)]
    print(f"Flirty references in index.html: {len(flirty_refs)}")
else:
    print(f"\n=== index.html : NOT FOUND ===")

# 6. Check specials.html
sp_path = "specials.html"
if os.path.exists(sp_path):
    with open(sp_path, encoding="utf-8") as f:
        sp = f.read()
    flirty_refs_sp = [m.start() for m in re.finditer(r'flirty', sp)]
    print(f"\n=== specials.html ===")
    print(f"Flirty references: {len(flirty_refs_sp)}")
    if flirty_refs_sp:
        for pos in flirty_refs_sp:
            print(f"  @{pos}: ...{sp[max(0,pos-40):pos+40]}...")
