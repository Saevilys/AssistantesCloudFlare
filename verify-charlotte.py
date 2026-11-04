#!/usr/bin/env python3
import json

with open('data.json') as f:
    data = json.load(f)

# Verify Charlotte
c = [e for e in data if e['name'] == 'Charlotte'][0]
print(f"Name: {c['name']}")
print(f"Tag: {c['tag']}")
print(f"Special: {c['special']}")
print(f"Flirty: {c['flirty']}")
print(f"City: {c['city']}")
print(f"Photos: {len(c['photos'])}")
for p in c['photos']:
    print(f"  {p}")
print(f"\nTotal entries: {len(data)}")
print("JSON valid ✓")
