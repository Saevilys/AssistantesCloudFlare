#!/usr/bin/env python3
"""Check vault files for Yasmine, Yara, and find missing vault profiles for data.json entries."""
import json, os

# Get all vault names
vault_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'vault', 'assistantes')
# On the desk, vault is at /vault/assistantes — but code runs on computer
# We'll check a different way
# Actually let's just list what we can

with open('data.json') as f:
    data = json.load(f)
data_names = sorted(e['name'] for e in data)

# Check for yasmine and yara vault files
for name in ['yasmine', 'yara']:
    found = False
    for root, dirs, files in os.walk('.'):
        if name + '.md' in files:
            found = True
            print(f"Found {name}.md in {root}")

# Just print the names count
print(f"\ndata.json names: {len(data_names)}")
print(f"Looking for duplicates:")
from collections import Counter
c = Counter(e['name'] for e in data)
dups = {k: v for k, v in c.items() if v > 1}
print(f"  Duplicates: {dups}")
