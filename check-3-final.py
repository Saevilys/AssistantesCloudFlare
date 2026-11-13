#!/usr/bin/env python3
"""Check Wayra and Tuuli against data.json."""
import json

def levenshtein(a, b):
    if a == b: return 0
    if len(a) < len(b): a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + (ca != cb)))
        prev = cur
    return prev[-1]

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

existing = {}
for entry in data:
    n = (entry.get("name") or "").strip().lower()
    if n:
        existing[n] = "data.json"

for cand in ["Wayra", "Tuuli", "Sela"]:
    cl = cand.lower()
    if cl in existing:
        print(f"  {cand} -> TAKEN ({existing[cl]})")
    else:
        near = [n for n in existing if levenshtein(cl, n) <= 2]
        if near:
            print(f"  {cand} -> FREE (near: {', '.join(sorted(near))})")
        else:
            print(f"  {cand} -> FREE")
