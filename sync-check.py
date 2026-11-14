#!/usr/bin/env python3
"""Compare data.json names with pick.py pool and vault files."""
import json, os, re

# data.json
with open('data.json') as f:
    data = json.load(f)
data_names = {e['name'] for e in data}

# pick.py
with open('/code/rotation/pick.py') as f:
    pick_content = f.read()

# Extract the pool - look for assistantes list
# Find "assistantes" or similar pool definition
m = re.search(r'assistantes\s*[=:]\s*\[([^\]]+)\]', pick_content, re.DOTALL)
if not m:
    # Try alternate pattern
    m = re.search(r'pool.*?assistantes.*?\[([^\]]+)\]', pick_content, re.DOTALL)
if m:
    pool_raw = m.group(1)
    pick_names = set(re.findall(r"['\"]([^'\"]+)['\"]", pool_raw))
else:
    # Maybe it reads from data.json directly
    if 'data.json' in pick_content or 'json.load' in pick_content:
        pick_names = "READS_DATA_JSON"
    else:
        pick_names = set(re.findall(r"['\"]([A-Za-z]+)['\"]", pick_content))

print(f"data.json: {len(data_names)} names")
print(f"pick.py pool: {pick_names if pick_names == 'READS_DATA_JSON' else len(pick_names)}")

if pick_names == "READS_DATA_JSON":
    print("pick.py reads data.json directly — auto-sync")
else:
    in_pick_not_data = pick_names - data_names
    in_data_not_pick = data_names - pick_names
    if in_pick_not_data:
        print(f"In pick.py but NOT data.json ({len(in_pick_not_data)}): {sorted(in_pick_not_data)}")
    if in_data_not_pick:
        print(f"In data.json but NOT pick.py ({len(in_data_not_pick)}): {sorted(in_data_not_pick)[:20]}...")
    if not in_pick_not_data and not in_data_not_pick:
        print("PERFECT SYNC")

# Check prev_assistante
m2 = re.search(r'prev_assistante\s*=\s*["\']([^"\']+)["\']', pick_content)
if m2:
    print(f"\nprev_assistante: {m2.group(1)}")

# data-roomservice.json
with open('data-roomservice.json') as f:
    rs = json.load(f)
rs_names = {e['name'] for e in rs}
print(f"\ndata-roomservice.json: {len(rs_names)} names")

# Vault check
vault_dir = '/vault/assistantes'
if os.path.exists(vault_dir):
    vault_files = [f for f in os.listdir(vault_dir) if f.endswith('.md')]
    vault_names = {f.replace('.md','') for f in vault_files}
    print(f"Vault: {len(vault_names)} files")
    
    missing_vault = data_names - vault_names
    orphan_vault = vault_names - data_names - rs_names
    
    if missing_vault:
        print(f"Missing vault ({len(missing_vault)}): {sorted(missing_vault)[:20]}")
    else:
        print("Vault: all data.json entries have a profile")
    
    if orphan_vault:
        print(f"Orphan vault ({len(orphan_vault)}): {sorted(orphan_vault)[:20]}")
else:
    print("Vault dir not found")

# Check station pages exist
stations = ['index.html']
for s in ['station-minorea.html', 'station-zineb.html', 'station-nour.html', 'station-suyin.html']:
    if os.path.exists(s):
        stations.append(s)
    else:
        print(f"MISSING: {s}")
print(f"\nStation pages: {len(stations)} found")

# Check if SVG hearts are in place
for s in stations:
    with open(s) as f:
        c = f.read()
    has_svg = 'function heartSVG' in c or 'heartSVG(' in c
    has_emoji = '♥\\uFE0E' in c or '♥\uFE0E' in c
    print(f"  {s}: SVG={'YES' if has_svg else 'NO'}, emoji_hearts={'STILL THERE' if has_emoji else 'cleaned'}")
