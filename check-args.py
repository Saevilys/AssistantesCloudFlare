#!/usr/bin/env python3
"""Check arbitrary names passed as CLI args against current data.json."""
import json, sys

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
low = {a.get("name","").lower().replace("-","").replace(" ","") for a in data}

for arg in sys.argv[1:]:
    norm = arg.lower().replace("-","").replace(" ","")
    variants = [norm, norm.replace("gaeun","ga-eun"), norm.replace("gaeun","gaeun")]
    hit = any(v in low for v in variants)
    print(f"{arg}: {'TAKEN' if hit else 'FREE'}")
