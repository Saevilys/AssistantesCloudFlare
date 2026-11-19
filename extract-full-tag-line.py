#!/usr/bin/env python3
"""Extract the full tag badge line (L546) from index.html"""
with open("index.html", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[545]  # L546
print(f"Full line ({len(line)} chars):")
print(line.rstrip())
