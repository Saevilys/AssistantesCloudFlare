#!/usr/bin/env python3
"""Check main branch data.json for the 3 secretaries"""
import json

# This is the main branch version (pulled first as main)
# Actually we pulled nemini over it... let me check what we have
# The nemini pull replaced the files. Let me check the git log
import subprocess
result = subprocess.run(["git", "log", "--oneline", "-5"], capture_output=True, text=True)
print("Git log:", result.stdout)

# Check current branch
result = subprocess.run(["git", "branch"], capture_output=True, text=True)
print("Branches:", result.stdout)

# Let's just search the data.json we have
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

print(f"\nTotal entries in current data.json: {len(data)}")
for name in ["Mayumi", "Thinzar", "Pema"]:
    found = [e for e in data if e.get("name","").lower() == name.lower()]
    print(f"  {name}: {'FOUND' if found else 'MISSING'} ({len(found)} entries)")
