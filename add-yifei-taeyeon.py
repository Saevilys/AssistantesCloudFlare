#!/usr/bin/env python3
"""Add Yifei and Taeyeon (meteo, Minorea) to data.json"""
import json

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Check if they already exist
existing_names = {e["name"].lower() for e in data}
if "yifei" in existing_names or "taeyeon" in existing_names:
    print("WARNING: Yifei or Taeyeon already in data.json!")
    for e in data:
        if e["name"].lower() in ("yifei", "taeyeon"):
            print(f"  Found: {e['name']}")
    print("Aborting to avoid duplicates.")
    exit(1)

new_entries = [
    {
        "name": "Yifei",
        "age": 24,
        "origin": "Chine",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 2,
        "station": "minorea",
        "tag": "meteo",
        "desc": "Peau claire chaude aux pores visibles, cheveux noirs raides en bob mi-long, yeux amande sombres, sourcils fins arqués, nez droit, lèvres pleines, visage ovale aux traits doux. Taille fine, hanches larges, forte poitrine. Crêpe dress bordeaux fluide, V-neck subtil, manches courtes.",
        "voice": "Posée, analytique. Elle lit le ciel comme un chercheur lit des données : avec précision, sans émotion inutile. Chaque phrase est une observation.",
        "trait": "Présentatrice météo des decks extérieurs de Minorea. Elle lit le ciel depuis les ponts, pas depuis un studio. Analytique, posée, elle explique les courants ascendants du Pacifique et les formations célestes avec une précision de chercheuse.",
        "photos": [
            f"{R2}/img/yifei/yifei-v1.png",
            f"{R2}/img/yifei/yifei-v2.png",
            f"{R2}/img/yifei/yifei-v3.png"
        ]
    },
    {
        "name": "Taeyeon",
        "age": 23,
        "origin": "Corée du Sud",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 3,
        "station": "minorea",
        "tag": "meteo",
        "desc": "Teint clair, longs cheveux bruns ondulés au vent, yeux monolides, sourcils droits, petit nez droit, lèvres pleines, visage rond aux traits juvéniles, sourire énergique. Taille fine, hanches larges, forte poitrine. Maille côtelée charcoal, col rond, manches longues, genoux.",
        "voice": "Vive, haute, parfois elle crie par-dessus le vent. Le bulletin météo comme un terrain, pas un studio. L'énergie d'une orageuse.",
        "trait": "Présentatrice météo matinale des decks extérieurs de Minorea. Énergie vive, sourire large, elle crie presque par-dessus le vent parfois. Le bulletin météo comme un terrain, pas un studio. Elle est dehors quand tout le monde rentre.",
        "photos": [
            f"{R2}/img/taeyeon/taeyeon-v1.png",
            f"{R2}/img/taeyeon/taeyeon-v2.png",
            f"{R2}/img/taeyeon/taeyeon-v3.png"
        ]
    }
]

data.extend(new_entries)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added Yifei and Taeyeon. Total entries: {len(data)}")
# Verify
with open("data.json", "r", encoding="utf-8") as f:
    verify = json.load(f)
print(f"JSON valid. {len(verify)} entries.")
for e in verify:
    if e["name"] in ("Yifei", "Taeyeon"):
        print(f"  {e['name']}: {len(e['photos'])} photos, tag={e.get('tag','?')}, station={e.get('station','?')}")
