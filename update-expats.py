#!/usr/bin/env python3
"""Update existing Sigrid, Amara, Priya entries: transform into expat reporters."""
import json
from pathlib import Path

R2_BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

UPDATES = {
    "Sigrid": {
        "age": 27,
        "origin": "Islande",
        "city": "Reykjavik",
        "region": "Europe du Nord",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "expat",
        "desc": "Peau porcelaine aux pores visibles, longs cheveux cendré-blond ondulés lâches sur les épaules, yeux bleu glacier, lèvres moyennes, pommettes hautes, nez droit. Taille fine, hanches larges, forte poitrine. Badge presse au lanyard, turtleneck noir sous un manteau de laine.",
        "voice": "Claire, précise, un ton grave pour son âge. Elle laisse le vent parler entre ses phrases. Un humour sec qui gèle pas.",
        "trait": "Correspondante arctique depuis Reykjavik. Elle couvre les aurores boréales, la géothermie, le climat, l'Islande qui vit entre feu et glace. Sa spécialité : le monde qui change sous la glace.",
        "photos": [
            f"{R2_BASE}/img/sigrid/sigrid-v1.png",
            f"{R2_BASE}/img/sigrid/sigrid-v2.png",
            f"{R2_BASE}/img/sigrid/sigrid-v3.png"
        ]
    },
    "Amara": {
        "age": 24,
        "origin": "Nigeria",
        "city": "Lagos",
        "region": "Afrique de l'Ouest",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "expat",
        "desc": "Peau brun foncé aux pores visibles, cheveux courts crépus naturels, yeux brun foncé, lèvres pleines, pommettes définies, nez large. Taille fine, hanches larges, forte poitrine. Top ankara imprimé, badge presse au lanyard.",
        "voice": "Vive, chaude, elle rit entre les phrases. Elle parle vite et fort, comme la rue qui l'entoure. Elle pose des questions pointues avec un sourire.",
        "trait": "Correspondante Afrique de l'Ouest depuis Lagos. Elle couvre les Afrobeats, la tech qui explose, la rue qui vibre, vingt millions d'âmes en mouvement. Sa spécialité : l'énergie qui n'attend pas la permission.",
        "photos": [
            f"{R2_BASE}/img/amara/amara-v1b.png",
            f"{R2_BASE}/img/amara/amara-v2.png",
            f"{R2_BASE}/img/amara/amara-v3.png"
        ]
    },
    "Priya": {
        "age": 25,
        "origin": "Inde",
        "city": "Mumbai",
        "region": "Asie du Sud",
        "active": True,
        "tag": "reporter",
        "flirty": 1,
        "station": "expat",
        "desc": "Peau brune aux pores visibles, longs cheveux noirs raides lâches sur les épaules, yeux brun foncé, lèvres pleines, pommettes définies, nez droit. Taille fine, hanches larges, forte poitrine. Kurta bordeaux, dupatta crème, badge presse au lanyard.",
        "voice": "Mélodieuse, posée, elle raconte comme elle respire. Des phrases qui s'enchaînent naturellement, un sourire dans la voix. Elle vulgarise sans simplifier.",
        "trait": "Correspondante Asie du Sud depuis Mumbai. Elle couvre la mousson, Bollywood, les foules, la tech, l'Inde qui court en mille directions. Sa spécialité : un milliard et demi d'histoires qui se croisent.",
        "photos": [
            f"{R2_BASE}/img/priya/priya-v1.png",
            f"{R2_BASE}/img/priya/priya-v2.png",
            f"{R2_BASE}/img/priya/priya-v3.png"
        ]
    }
}

data_path = Path("data.json")
data = json.loads(data_path.read_text(encoding="utf-8"))

for entry in data:
    if entry["name"] in UPDATES:
        name = entry["name"]
        old_origin = entry.get("origin", "?")
        old_tag = entry.get("tag", "citoyenne")
        entry.update(UPDATES[name])
        print(f"Updated {name}: {old_origin} → {entry['origin']}, {old_tag} → reporter, {len(entry['photos'])} photos")

data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTotal entries: {len(data)}")
