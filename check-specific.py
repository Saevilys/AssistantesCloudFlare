#!/usr/bin/env python3
"""Check specific names against vault and data.json."""
import json, os

# Load data.json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
data_names = {a.get("name","").lower() for a in data}

# Names to check
names = ["Saanvi", "Ondina", "Mayu", "Nayeon", "Soyeon", "Seoyeon", 
         "Yewon", "Sooyun", "Haeri", "Nari"]

print("=== data.json check (502 entries) ===")
for n in names:
    print(f"  {n}: {'TAKEN' if n.lower() in data_names else 'free'}")

# Also check if vault files exist by trying to read them
print("\n=== Checking vault (via data.json names only) ===")
# We can't list vault from here, but we already know:
# fariya, eira, calliope exist in vault
# jieun, jiyeon exist in vault
# Let's just report what we know
print("Already confirmed in vault: fariya, eira, calliope, jieun, jiyeon")
print("Need desktop_list for: saanvi, ondina, mayu, nayeon, soyeon, seoyeon, yewon, sooyun, haeri, nari")
