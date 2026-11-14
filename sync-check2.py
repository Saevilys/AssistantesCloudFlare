#!/usr/bin/env python3
"""Full sync check: data.json (Cloudflare) vs pick.py pool vs vault vs data-roomservice.json."""
import json, os, re

# 1. data.json Cloudflare (local copy on desk)
with open('data.json') as f:
    data = json.load(f)
data_names = {e['name'] for e in data}
print(f"data.json (Cloudflare): {len(data)} entries, {len(data_names)} unique names")

# 2. pick.py — reads data.json dynamically
with open('rot-data.json') as f:
    rot_data = json.load(f)
rot_names = {e['name'] for e in rot_data}
print(f"pick.py data.json (rotation): {len(rot_names)} entries")

# Compare
if data_names == rot_names:
    print("  → pick.py data.json: PERFECT SYNC with Cloudflare")
else:
    only_cloud = data_names - rot_names
    only_rot = rot_names - data_names
    if only_cloud:
        print(f"  → In Cloudflare but NOT rotation ({len(only_cloud)}): {sorted(only_cloud)}")
    if only_rot:
        print(f"  → In rotation but NOT Cloudflare ({len(only_rot)}): {sorted(only_rot)}")

# 3. prev_assistante
print("\nprev_assistante: Diya (read from desk earlier)")

# 4. data-roomservice.json
with open('data-roomservice.json') as f:
    rs = json.load(f)
rs_names = {e['name'] for e in rs}
print(f"data-roomservice.json: {len(rs)} entries")

with open('rot-rs.json') as f:
    rot_rs = json.load(f)
rot_rs_names = {e['name'] for e in rot_rs}
if rs_names == rot_rs_names:
    print("  → rotation RS: PERFECT SYNC")
else:
    only_cf = rs_names - rot_rs_names
    only_rt = rot_rs_names - rs_names
    if only_cf:
        print(f"  → In Cloudflare RS but NOT rotation RS ({len(only_cf)}): {sorted(only_cf)}")
    if only_rt:
        print(f"  → In rotation RS but NOT Cloudflare RS ({len(only_rt)}): {sorted(only_rt)}")

# 5. Vault check
print("\nVault: check via desktop tools (separate)")

# 6. Check for any duplicate names in data.json
from collections import Counter
name_counts = Counter(e['name'] for e in data)
dupes = {n:c for n,c in name_counts.items() if c > 1}
if dupes:
    print(f"\n  → DUPLICATES in data.json: {dupes}")
else:
    print(f"\n  → No duplicates ✓")

# 7. SVG hearts check
print("\n--- SVG Hearts Check ---")
for fname in ['index.html', 'station-minorea.html', 'station-zineb.html', 'station-nour.html', 'station-suyin.html']:
    if os.path.exists(fname):
        with open(fname) as f:
            c = f.read()
        has_svg = 'heartSVG(' in c
        has_emoji = '♥\\uFE0E' in c
        print(f"  {fname}: SVG={'✓' if has_svg else '✗'}, emoji_remaining={'YES' if has_emoji else 'no'}")
    else:
        print(f"  {fname}: MISSING")

# 8. Tag for 'garde du corps' (space vs hyphen)
gdc_space = [e['name'] for e in data if e.get('tag') == 'garde du corps']
gdc_hyphen = [e['name'] for e in data if e.get('tag') == 'garde-du-corps']
if gdc_space:
    print(f"\n  ⚠ 'garde du corps' (space) tag: {gdc_space} — should be 'garde-du-corps'")
