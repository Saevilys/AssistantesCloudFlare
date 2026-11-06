#!/usr/bin/env python3
import json

with open("data.json", "r") as f:
    main = json.load(f)
names = [e.get("name") for e in main]
print(f"data.json: {len(main)} entries")
for n in ("Liezel", "Mayaris", "Mika", "Nika", "Lena"):
    print(f"  {n}: {'IN' if n in names else 'out'}")
print(f"Last 3: {names[-3:]}")

with open("data-roomservice.json", "r") as f:
    rs = json.load(f)
rs_names = [e.get("name") for e in rs]
print(f"\ndata-roomservice.json: {len(rs)} entries")
for n in ("Liezel", "Mayaris", "Mika", "Nika", "Lena"):
    print(f"  {n}: {'IN' if n in rs_names else 'out'}")
print(f"Last 3: {rs_names[-3:]}")
