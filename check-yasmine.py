#!/usr/bin/env python3
"""Check Yasmine entries in data.json — which one is the mathematician, which is the reporter?"""
import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

yasmine_entries = [e for e in data if 'yasmine' in e['name'].lower()]
print(f"Yasmine entries: {len(yasmine_entries)}")
for e in yasmine_entries:
    print(f"  {e['name']} — {e.get('origin','?')} — {e.get('city','?')} — tag={e.get('tag','none')}")
    print(f"  photos: {e.get('photos',[])}")

# Also check Rima
rima_entries = [e for e in data if 'rima' in e['name'].lower()]
print(f"\nRima entries: {len(rima_entries)}")
for e in rima_entries:
    print(f"  {e['name']} — {e.get('origin','?')} — {e.get('city','?')} — tag={e.get('tag','none')}")
    print(f"  photos: {e.get('photos',[])}")

# Check for any Yara remaining (should be gone)
yara_entries = [e for e in data if 'yara' in e['name'].lower()]
print(f"\nYara entries: {len(yara_entries)}")
for e in yara_entries:
    print(f"  {e['name']} — {e.get('origin','?')} — {e.get('city','?')}")
