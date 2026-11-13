#!/usr/bin/env python3
"""Find ALL mentari and suchada images on desk."""
import os

targets = []
for root, dirs, files in os.walk("."):
    for f in files:
        lower = f.lower()
        if ("mentari" in lower or "suchada" in lower) and f.endswith((".png", ".jpg", ".webp")):
            targets.append(os.path.join(root, f))

for t in sorted(targets):
    print(t)
