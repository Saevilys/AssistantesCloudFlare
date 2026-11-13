#!/usr/bin/env python3
"""Find ALL mentari and suchada images on desk from root."""
import os

targets = []
for root, dirs, files in os.walk("/"):
    # skip github and code and other non-image dirs
    for f in files:
        lower = f.lower()
        if ("mentari" in lower or "suchada" in lower) and f.endswith((".png", ".jpg", ".webp")):
            targets.append(os.path.join(root, f))
    # don't recurse into huge dirs
    if root == "/" or root.count("/") < 3:
        continue

for t in sorted(targets):
    print(t)
print(f"\nTotal: {len(targets)}")
