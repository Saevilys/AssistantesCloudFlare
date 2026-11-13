#!/usr/bin/env python3
"""Check names against data.json only."""
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

candidates = ["Sela", "Pacha", "Tuuli", "Mele", "Lose", "Mayu", "Killa", "Halla", "Kuura"]
for cand in candidates:
    cl = cand.lower()
    if cl in existing:
        print(f"  {cand} -> TAKEN")
    else:
        near = [(n, s) for n, s in existing.items() if levenshtein(cl, n) <= 2 and n != cl]
        if near:
            near.sort(key=lambda x: levenshtein(cl, x[0]))
            print(f"  {cand} -> WARNING: near {', '.join(n for n, s in near[:5])}")
        else:
            print(f"  {cand} -> FREE")
