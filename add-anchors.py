#!/usr/bin/env python3
"""Add Tsumugi and Iseul to data.json — new anchor entries for Minorea."""
import json

with open('data.json') as f:
    data = json.load(f)

# Check they don't already exist
existing = {e['name'].lower() for e in data}
if 'tsumugi' in existing or 'iseul' in existing:
    print("ERROR: Tsumugi or Iseul already in data.json")
    for e in data:
        if e['name'].lower() in ('tsumugi', 'iseul'):
            print(f"  found: {e['name']}")
    exit(1)

BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

tsumugi = {
    "name": "Tsumugi",
    "age": 23,
    "origin": "Japon",
    "city": "Minorea",
    "region": "Minorea",
    "station": "minorea",
    "active": True,
    "tag": "anchor",
    "flirty": 2,
    "desc": "Peau claire aux pores visibles, longs cheveux noirs raides parted in the middle past shoulders, yeux bruns en amande légèrement tombants, sourcils arqués fins, nez droit petit, lèvres pleines gloss rose sheer, visage ovale defined jawline. Taille fine, hanches larges, forte poitrine. Robe bodycon virgin killer noire.",
    "voice": "Calme, précise, posée. Chaque syllabe nette. Un ton bas et régulier qui ne s'emballe jamais. Rarement expressive, mais quand elle l'est, c'est dans les yeux.",
    "trait": "Anchor du journal de nuit de Minorea. Elle lit les dépêches de la capitale et des stations avec la même voix égale. Sa spécialité : faire simple sans simplifier.",
    "photos": [
        f"{BASE}/img/tsumugi/tsumugi-v1.png",
        f"{BASE}/img/tsumugi/tsumugi-v2.png",
        f"{BASE}/img/tsumugi/tsumugi-v3.png",
    ]
}

iseul = {
    "name": "Iseul",
    "age": 24,
    "origin": "Corée",
    "city": "Minorea",
    "region": "Minorea",
    "station": "minorea",
    "active": True,
    "tag": "anchor",
    "flirty": 2,
    "desc": "Peau légèrement bronzée aux pores visibles, longs cheveux bruns foncé ondulés avec subtils highlights, frange side-swept. Yeux bruns avec winged eyeliner fin, sourcils arqués définis, nez petit, lèvres pleines gloss nude, visage ovale soft jawline. Taille fine, hanches larges, forte poitrine. Robe bodycon virgin killer bordeaux.",
    "voice": "Claire, modulée, avec une légère chaleur qu'elle contrôle. Rapide sur les titres, ralentit sur les noms. Glisse des sourires quand la météo est belle.",
    "trait": "Anchor du matin de Minorea. Elle ouvre le journal à 6h, la première voix que la capitale entend. Ex-radiophonique coastale.",
    "photos": [
        f"{BASE}/img/iseul/iseul-v1.png",
        f"{BASE}/img/iseul/iseul-v2.png",
        f"{BASE}/img/iseul/iseul-v3.png",
    ]
}

data.append(tsumugi)
data.append(iseul)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done. {len(data)} entries now. Tsumugi=525, Iseul=526")
