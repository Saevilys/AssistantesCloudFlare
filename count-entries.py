#!/usr/bin/env python3
"""Count entries and check status of data.json and data-roomservice.json."""
import json

with open('data.json') as f:
    data = json.load(f)
print(f"data.json: {len(data)} entries")
print(f"First: {data[0]['name']}, Last: {data[-1]['name']}")

# Count by tag
from collections import Counter
tags = Counter(e.get('tag','none') for e in data)
print(f"Tags: {dict(tags)}")

# Count by active
active = sum(1 for e in data if e.get('active', True))
inactive = len(data) - active
print(f"Active: {active}, Inactive: {inactive}")

# Check photos
no_photos = [e['name'] for e in data if not e.get('photos') or len(e.get('photos',[])) == 0]
print(f"No photos: {len(no_photos)} — {no_photos[:10]}")

# Check for non-R2 URLs
non_r2 = []
for e in data:
    for p in e.get('photos', []):
        if 'r2.dev' not in p and 'pub-a88b6' not in p:
            non_r2.append(f"{e['name']}: {p}")
print(f"Non-R2 URLs: {len(non_r2)}")
if non_r2:
    for x in non_r2[:5]:
        print(f"  {x}")

# Last 10 entries
print("\nLast 10 entries:")
for e in data[-10:]:
    print(f"  {e['name']} — tag={e.get('tag','none')} — photos={len(e.get('photos',[]))}")

# Room service
with open('data-roomservice.json') as f:
    rs = json.load(f)
print(f"\ndata-roomservice.json: {len(rs)} entries")
print(f"Last: {rs[-1]['name']}")
