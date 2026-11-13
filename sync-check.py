#!/usr/bin/env python3
"""Sync check: data.json vs pick.py vs vault vs data-roomservice.json"""
import json, os, glob, re
from collections import Counter

here = os.path.dirname(os.path.abspath(__file__))

# 1. data.json
with open(os.path.join(here, "data.json"), encoding="utf-8") as f:
    data = json.load(f)
data_names = sorted({e["name"] for e in data})
print(f"data.json: {len(data)} entries, {len(data_names)} unique names")

# Duplicates
dupes = [n for n, c in Counter(e["name"] for e in data).items() if c > 1]
if dupes:
    print(f"  DUPLICATES: {dupes}")
    for d in dupes:
        entries = [e for e in data if e["name"] == d]
        for e in entries:
            print(f"    {d}: station={e.get('station','?')}, station_zh={e.get('station_zh','?')}, photos={e.get('photos','?')}")

# Inactive
inactive = [e["name"] for e in data if not e.get("active", True)]
if inactive:
    print(f"  INACTIVE ({len(inactive)}): {inactive}")

# 2. data-roomservice.json
rs_path = os.path.join(here, "data-roomservice.json")
with open(rs_path, encoding="utf-8") as f:
    rs = json.load(f)
rs_names = sorted({e["name"] for e in rs})
print(f"data-roomservice.json: {len(rs)} entries, {len(rs_names)} unique")

# 3. Vault fiches — path relative to desk on computer
vault_dir = os.path.join(here, "..", "..", "vault", "assistantes")
if not os.path.exists(vault_dir):
    # try absolute
    vault_dir = "/data/desk/vault/assistantes"
vault_files = glob.glob(os.path.join(vault_dir, "*.md"))
vault_names = sorted({os.path.basename(f).replace(".md","") for f in vault_files})
print(f"Vault: {len(vault_names)} fiches (from {vault_dir})")

# 4. Compare data.json vs vault (case-insensitive)
data_lower = {n.lower() for n in data_names}
vault_lower = {n.lower() for n in vault_names}
in_data_not_vault = data_lower - vault_lower
in_vault_not_data = vault_lower - data_lower
if in_data_not_vault:
    real = {n for n in in_data_not_vault if not n.startswith("etat-")}
    if real:
        print(f"  IN data.json NOT vault ({len(real)}): {sorted(real)[:30]}")
if in_vault_not_data:
    extra = {n for n in in_vault_not_data if not n.startswith("etat-")}
    if extra:
        print(f"  IN vault NOT data.json ({len(extra)}): {sorted(extra)[:20]}")

# 5. Reporters — check various field names
for field in ["reporter", "is_reporter", "type"]:
    reporters = [e["name"] for e in data if e.get(field) in (True, "reporter", "yes")]
    if reporters:
        print(f"Reporters (field={field}): {len(reporters)} — {reporters}")
        break

# 5b. Check for station field
stations = Counter(e.get("station", "?") for e in data)
print(f"Stations ({len(stations)}): {dict(stations.most_common(10))}")

# 6. New entries check
for name in ["Chihiro", "Jiaxin", "Dasom"]:
    entry = next((e for e in data if e["name"] == name), None)
    if entry:
        photos = entry.get("photos", [])
        if isinstance(photos, list) and photos:
            if isinstance(photos[0], str):
                urls = [p[-40:] for p in photos]
            else:
                urls = [p.get("url","?")[-40:] for p in photos]
            print(f"  {name}: station={entry.get('station','?')}, {len(photos)} photos — {urls}")
        else:
            print(f"  {name}: photos={photos}")
    else:
        print(f"  {name}: NOT IN data.json!")

# 7. pick.py
pick_path = os.path.join(here, "..", "..", "code", "rotation", "pick.py")
if not os.path.exists(pick_path):
    pick_path = "/data/desk/code/rotation/pick.py"
if os.path.exists(pick_path):
    with open(pick_path, encoding="utf-8") as f:
        pick_text = f.read()
    pool_match = re.search(r'"assistantes"\s*:\s*\[(.*?)\]', pick_text, re.DOTALL)
    if pool_match:
        pool_names = set(re.findall(r'"([^"]+)"', pool_match.group(1)))
        in_pick_not_data = pool_names - data_lower
        in_data_not_pick = data_lower - pool_names
        print(f"pick.py pool: {len(pool_names)} names")
        if in_pick_not_data:
            print(f"  IN pick NOT data ({len(in_pick_not_data)}): {sorted(in_pick_not_data)[:15]}")
        if in_data_not_pick:
            print(f"  IN data NOT pick ({len(in_data_not_pick)}): {sorted(in_data_not_pick)[:30]}")
    else:
        print("pick.py: pool not found, checking for data.json reference")
        if "data.json" in pick_text:
            print("  pick.py references data.json (dynamic pool)")
        else:
            print("  pick.py: no pool and no data.json ref found")
else:
    print("pick.py: NOT FOUND")

# 8. prev_assistante
prev_path = os.path.join(here, "..", "..", "code", "rotation", "prev_assistante.txt")
if not os.path.exists(prev_path):
    prev_path = "/data/desk/code/rotation/prev_assistante.txt"
if os.path.exists(prev_path):
    with open(prev_path) as f:
        prev = f.read().strip()
    print(f"prev_assistante: {prev}")
else:
    print("prev_assistante.txt: NOT FOUND")

print("\nDone.")
