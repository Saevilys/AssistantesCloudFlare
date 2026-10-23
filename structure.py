#!/usr/bin/env python3
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Show structure of last entry
last = data[-1] if isinstance(data, list) else data[list(data.keys())[-1]]
print(json.dumps(last, indent=2, ensure_ascii=False)[:2000])

# Check if aissata or almaz exist
names = [e.get("name","") for e in data] if isinstance(data, list) else list(data.keys())
print("\n---")
print(f"Total: {len(names)}")
print(f"Aïssata in list: {'Aïssata' in names or 'aissata' in [n.lower() for n in names]}")
print(f"Almaz in list: {'Almaz' in names or 'almaz' in [n.lower() for n in names]}")
