#!/usr/bin/env python3
"""Extract exact tag rendering line from index.html line 545"""
with open("index.html", encoding="utf-8") as f:
    lines = f.readlines()

# Line 545 (0-indexed 544)
line = lines[544]
print(f"Line 545 ({len(line)} chars):")
print(line.rstrip())
