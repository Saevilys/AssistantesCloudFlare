#!/usr/bin/env python3
"""Check vault files for name collisions."""
import os

names_to_check = ["Fariya", "Saanvi", "Ondina", "Mayu", "Eira", "Calliope",
                  "Nayeon", "Soyeon", "Jiyeon", "Seoyeon", "Yewon", "Sooyun",
                  "Jieun", "Haeri", "Nari"]

vault_dir = "/vault/assistantes"
found = os.listdir(vault_dir)

print("=== Vault check ===")
for name in names_to_check:
    fname = f"{name.lower()}.md"
    if fname in found:
        print(f"  {name}: ALREADY IN VAULT ({fname})")
    else:
        print(f"  {name}: not in vault")
