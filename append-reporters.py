#!/usr/bin/env python3
"""Append 4 reporter entries to data.json (read from repo, write back)."""
import json
from pathlib import Path

R2_BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

NEW_ENTRIES = [
    {
        "name": "Kartika",
        "age": 24,
        "origin": "Indonésie",
        "city": "Minorea",
        "region": "Asie",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "minorea",
        "desc": "Peau brun-doré chaud aux pores visibles, longs cheveux noirs raides lâches sur les épaules, yeux amande brun foncé, lèvres pleines, pommettes hautes, petit nez. Taille fine, hanches larges, poitrine généreuse. Badge presse au lanyard.",
        "voice": "Rapide, vive, elle parle comme elle respire. Des phrases courtes qui s'enchaînent, un rire facile. Elle pose des vraies questions et attend de vraies réponses.",
        "trait": "Reporter de terrain à Minorea. Elle couvre la ville côtière et la ville haute, les canaux et les food stalls, les gens et leur quotidien. Elle est partout, elle voit tout, elle écrit vite. Sa spécialité : l'humain dans la machine géante.",
        "photos": [
            f"{R2_BASE}/img/kartika/kartika-v1.png",
            f"{R2_BASE}/img/kartika/kartika-v2.png",
            f"{R2_BASE}/img/kartika/kartika-v3.png"
        ]
    },
    {
        "name": "Mila",
        "age": 23,
        "origin": "Eurasie",
        "city": "Station Zineb",
        "region": "Espace",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "zineb",
        "desc": "Peau olive claire aux pores visibles, cheveux bruns foncés ondulés lâches sur les épaules, yeux noisette, lèvres pleines, nez droit, mâchoire douce. Taille fine, hanches larges, poitrine généreuse. Badge de station clipsé au col.",
        "voice": "Précise, posée, un ton de radio courte distance. Elle choisit ses mots avec soin et les place bien. Un humour sec qui surgit quand tu t'y attends pas.",
        "trait": "Correspondante de la Station Zineb en orbite terrestre. Elle couvre la vie à bord, les 800 âmes, le hub, les labos, la Terre vu d'en haut. Elle sait que l'espace c'est pas le vide, c'est un quartier.",
        "photos": [
            f"{R2_BASE}/img/mila/mila-v1.png",
            f"{R2_BASE}/img/mila/mila-v2.png",
            f"{R2_BASE}/img/mila/mila-v3.png"
        ]
    },
    {
        "name": "Wassila",
        "age": 25,
        "origin": "Tunisie",
        "city": "Station Nour",
        "region": "Espace",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "nour",
        "desc": "Peau olive chaude aux pores visibles, longs cheveux bruns foncés bouclés lâches, yeux brun foncé, lèvres pleines, mâchoire forte, nez droit. Taille fine, hanches larges, poitrine généreuse. Badge presse au lanyard.",
        "voice": "Engagée, curieuse, elle parle avec ses mains même au micro. Des phrases qui montent quand elle est excitée par une découverte. Elle vulgarise sans condescendre.",
        "trait": "Journaliste scientifique à la Station Nour sur TRAPPIST-1d. Elle couvre la recherche, les serres hydroponiques, l'atmosphère rouge, la vie dans une autre lumière. Sa spécialité : rendre la science vivante pour ceux qui la font.",
        "photos": [
            f"{R2_BASE}/img/wassila/wassila-v1.png",
            f"{R2_BASE}/img/wassila/wassila-v2.png",
            f"{R2_BASE}/img/wassila/wassila-v3.png"
        ]
    },
    {
        "name": "Aisulu",
        "age": 24,
        "origin": "Kazakhstan",
        "city": "Station Sgr A*",
        "region": "Espace",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "sgr-a",
        "desc": "Peau claire aux sous-tons dorés et pores visibles, longs cheveux bruns foncés raides avec quelques mèches plus claires, yeux amande foncés, pommettes hautes, lèvres pleines, nez droit. Taille fine, hanches larges, poitrine généreuse. Turtleneck noir, badge presse clipsé au col.",
        "voice": "Contemplative, lente, elle laisse le silence exister entre ses phrases. Elle écrit comme elle regarde le trou noir : en essayant de saisir quelque chose qui ne se laisse pas saisir.",
        "trait": "Journaliste contemplative à la Station Sgr A*. Elle couvre le trou noir, la distorsion, la lumière qui plie. Elle écrit sur l'indicible et le mesure quand même. Sa spécialité : le vertige devant ce qui dépasse.",
        "photos": [
            f"{R2_BASE}/img/aisulu/aisulu-v1.png",
            f"{R2_BASE}/img/aisulu/aisulu-v2.png",
            f"{R2_BASE}/img/aisulu/aisulu-v3.png"
        ]
    }
]

# Read existing data.json
data_path = Path("data.json")
data = json.loads(data_path.read_text(encoding="utf-8"))

# Check for duplicates
existing_names = {e["name"] for e in data}
for entry in NEW_ENTRIES:
    if entry["name"] in existing_names:
        print(f"WARNING: {entry['name']} already exists in data.json, skipping")
        continue
    data.append(entry)
    print(f"Added: {entry['name']}")

# Write back
data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTotal entries: {len(data)}")
