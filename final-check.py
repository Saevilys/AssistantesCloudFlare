#!/usr/bin/env python3
"""Check vault fiches vs data.json — find mismatches, missing vault, missing data."""
import json, os, glob

# Load data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data_names = {e['name'].lower() for e in data}
data_by_name = {e['name'].lower(): e for e in data}

# Collect vault names
vault_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'vault', 'assistantes')
vault_files = glob.glob(os.path.join(vault_dir, '**', '*.md'), recursive=True)
vault_names = set()
for f in vault_files:
    name = os.path.splitext(os.path.basename(f))[0].lower()
    vault_names.add(name)

# Also check reporters
reporters_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'vault', 'reporters')
reporter_files = glob.glob(os.path.join(reporters_dir, '**', '*.md'), recursive=True)
reporter_names = set()
for f in reporter_files:
    name = os.path.splitext(os.path.basename(f))[0].lower()
    reporter_names.add(name)

print(f"data.json: {len(data)} entries, {len(data_names)} unique names")
print(f"vault assistantes: {len(vault_names)} fiches")
print(f"vault reporters: {len(reporter_names)} fiches")

# Check duplicates in data.json
from collections import Counter
name_counts = Counter(e['name'].lower() for e in data)
dups = {n: c for n, c in name_counts.items() if c > 1}
if dups:
    print(f"\nDUPLICATES in data.json: {dups}")
else:
    print("\nNo duplicates in data.json.")

# In data.json but not in vault
missing_vault = data_names - vault_names - reporter_names
# Filter out tags that don't need vault (like reporters already in reporters/)
missing_vault_real = set()
for name in missing_vault:
    entry = data_by_name.get(name)
    if entry and entry.get('tag') == 'reporter':
        if name not in reporter_names:
            missing_vault_real.add(name + " (reporter)")
    elif entry and entry.get('tag') in ('anchor',):
        if name not in vault_names:
            missing_vault_real.add(name + " (anchor)")
    # skip other tags — not all need vault

if missing_vault_real:
    print(f"In data.json but missing vault: {missing_vault_real}")
else:
    print("All anchors and reporters have vault fiches.")

# Check Rima specifically
if 'rima' in data_names:
    print(f"\nRima found in data.json: {data_by_name['rima']['origin']} — {data_by_name['rima']['city']}")
if 'rima' in reporter_names:
    print("Rima found in vault reporters.")
if 'yasmine' in data_names:
    print("WARNING: Yasmine still in data.json!")
else:
    print("Yasmine removed from data.json: OK")

# Check Ruoxi
if 'ruoxi' in data_names:
    print(f"\nRuoxi found in data.json: {data_by_name['ruoxi']['origin']} — {data_by_name['ruoxi']['city']} — tag={data_by_name['ruoxi']['tag']}")
    print(f"  photos: {data_by_name['ruoxi']['photos']}")
if 'ruoxi' in vault_names:
    print("Ruoxi found in vault assistantes.")

# Anchors summary
anchors = [e for e in data if e.get('tag') == 'anchor']
print(f"\nAnchors ({len(anchors)}):")
for a in anchors:
    print(f"  {a['name']} — {a['origin']} — {a['city']} — photos={len(a.get('photos',[]))}")
