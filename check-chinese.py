#!/usr/bin/env python3
"""Find Chinese entries in data.json and check available Chinese names."""
import json
with open('data.json') as f:
    data = json.load(f)

chinese = [e for e in data if e.get('origin') == 'Chine' or e.get('region') == 'Asie' and e.get('origin') in ['Chine', 'China']]
print(f"Chinese entries: {len(chinese)}")
for e in chinese:
    print(f"  {e['name']} — {e.get('origin','?')} — {e.get('city','?')} — tag={e.get('tag','none')}")

# Also check all names to find Chinese-sounding ones
all_names = {e['name'].lower() for e in data}
candidates = ['Meifeng', 'Qian', 'Weili', 'Anqi', 'Baihe', 'Jiaxin']
print("\nChinese name candidates already in data:")
for c in candidates:
    print(f"  {c} — {'EXISTS' if c.lower() in all_names else 'available'}")

# Available Chinese anchor names
print("\nAvailable Chinese names for anchor:")
new_candidates = ['Liling', 'Xinya', 'Suyin', 'Jing', 'Mei', 'Yanlin', 'Fang', 'Ruoxi', 'Xiaolan', 'Hong', 'Lan', 'Yun', 'Shu', 'Hua', 'Xiaomei', 'Xiu', 'Zhen', 'Min', 'Ying']
for c in new_candidates:
    if c.lower() in all_names:
        print(f"  {c} — EXISTS")
    else:
        print(f"  {c} — available")
