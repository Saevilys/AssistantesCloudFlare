#!/usr/bin/env python3
"""Find Mentari and Suchada v1 images on desk."""
import os

for root_dir in ["/images", "/images-keep", "/photos-assistante-du-jour"]:
    if not os.path.exists(root_dir):
        continue
    for f in os.listdir(root_dir):
        lower = f.lower()
        if ("mentari" in lower or "suchada" in lower) and f.endswith(".png"):
            print(f"{root_dir}/{f}")
