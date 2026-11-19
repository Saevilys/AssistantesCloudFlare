#!/usr/bin/env python3
"""Extract lines around tag rendering in index.html — find the full ternary chain"""
with open("index.html", encoding="utf-8") as f:
    lines = f.readlines()

# Print lines 540-550 to see the full tag rendering chain
for i in range(538, min(552, len(lines))):
    print(f"L{i+1}: {lines[i].rstrip()[:250]}")
