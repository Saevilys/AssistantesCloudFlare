#!/usr/bin/env python3
"""Check if candidate names exist in data.json."""
import json
with open('data.json') as f:
    data = json.load(f)
names = {e['name'].lower() for e in data}

candidates = ['Rima', 'Lama', 'Serene', 'Reine', 'Maya', 'Tatiana', 'Carla', 'Nadine', 'Sahar', 'Dana', 'Lena', 'Yara', 'Salma', 'Rola', 'Layla', 'Myriam', 'Nadine', 'Celine', 'Joelle']
for c in candidates:
    if c.lower() in names:
        print(f"  {c} — EXISTS")
    else:
        print(f"  {c} — available")
