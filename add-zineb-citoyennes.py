#!/usr/bin/env python3
"""Append 4 new Station Zineb citizens to data.json."""
import json
from pathlib import Path

data_path = Path("data.json")
data = json.loads(data_path.read_text(encoding="utf-8"))

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

new_entries = [
    {
        "name": "Haneul",
        "age": 24,
        "origin": "Corée du Sud",
        "city": "Séoul",
        "region": "Asie",
        "active": True,
        "tag": "debris-specialist",
        "flirty": 2,
        "desc": "Peau pâle d'Asie de l'Est, yeux amande avec plis épicanthiques, sourcils fins arqués, petit nez droit, lèvres pleines, visage ovale. Cheveux bruns foncés en queue de cheval basse et désordonnée. Taille fine, hanches larges, forte poitrine, voluptueuse. Un regard qui passe des écrans à toi sans prévenir.",
        "voice": "Calme, précise, parle peu mais chaque mot compte. Anglais technique mâché avec coréen quand elle fatigue. Sourit rarement, mais quand ça arrive c'est vrai.",
        "trait": "Spécialiste en débris spatiaux sur Station Zineb. Surveillance des orbites, trajectoires de débris, alertes de collision. Passe ses nuits à tracker des éclats invisibles qui pourraient perforer la coque. La Terre tourne derrière elle et elle compte les menaces.",
        "photos": [
            f"{R2}/img/haneul/haneul-v1.png",
            f"{R2}/img/haneul/haneul-v2.png",
            f"{R2}/img/haneul/haneul-v3.png"
        ],
        "station": "zineb"
    },
    {
        "name": "Suda",
        "age": 23,
        "origin": "Thaïlande",
        "city": "Chiang Mai",
        "region": "Asie",
        "active": True,
        "tag": "cook",
        "flirty": 2,
        "desc": "Peau mate d'Asie du Sud-Est, yeux amande rondes, petit nez en bouton, lèvres pleines, visage rond aux traits juvéniles. Longs cheveux noirs lisses en chignon désordonné avec un bandana. Taille fine, hanches larges, forte poitrine, voluptueuse. Toujours une trace de farine quelque part.",
        "voice": "Chaleureuse, rapide, rit en plein milieu d'une phrase. Mélange thaï et français quand elle s'excite. Nourrit tout le monde, c'est pas une question.",
        "trait": "Cuisinière de la cantine partagée sur Station Zineb. Les repas du soir, le social de la station. Trois cents personnes à nourrir en orbite avec des cultures hydroponiques et des réserves rationnées. Sa cuisine sent le basilic et le curry, même en microgravité.",
        "photos": [
            f"{R2}/img/suda/suda-v1.png",
            f"{R2}/img/suda/suda-v2.png",
            f"{R2}/img/suda/suda-v3.png"
        ],
        "station": "zineb"
    },
    {
        "name": "Lika",
        "age": 25,
        "origin": "Géorgie",
        "city": "Tbilissi",
        "region": "Europe",
        "active": True,
        "tag": "recycling-tech",
        "flirty": 2,
        "desc": "Peau olivâtre claire, grands yeux noisette, sourcils définis et arqués, nez droit avec une légère bosse, lèvres pleines, visage ovale aux pommettes marquées. Cheveux bruns foncés ondulés en queue de cheval pratique. Taille fine, hanches larges, forte poitrine, voluptueuse. Des mains qui sentent le savon technique.",
        "voice": "Directe, terne, humour sec caucasien. Grommelle en géorgien quand les filtres bouchent. Pas le genre à réconforter, le genre à réparer.",
        "trait": "Technicienne de recyclage d'air et d'eau sur Station Zineb. La respiration de la station. Entretient les filtres, les pompes, les systèmes de récupération. Sans elle, 800 personnes étouffent en une semaine. Elle le sait, elle en parle pas, elle bosse.",
        "photos": [
            f"{R2}/img/lika/lika-v1.png",
            f"{R2}/img/lika/lika-v2.png",
            f"{R2}/img/lika/lika-v3.png"
        ],
        "station": "zineb"
    },
    {
        "name": "Vittoria",
        "age": 26,
        "origin": "Italie",
        "city": "Florence",
        "region": "Europe",
        "active": True,
        "tag": "artist",
        "flirty": 2,
        "desc": "Peau olivâtre méditerranéenne, grands yeux noirs, sourcils épais définis, nez droit au profil légèrement romain, lèvres pleines, visage ovale aux pommettes saillantes. Longs cheveux bruns ondulés lâchés sur une épaule. Taille fine, hanches larges, forte poitrine, voluptueuse. Toujours de la peinture sous les ongles.",
        "voice": "Passionnée, théâtrale, gesticule en parlant. Italien qui perle quand elle s'émeut. Voit la beauté partout, c'est insupportable et contagieux.",
        "trait": "Artiste en résidence sur Station Zineb. Peint la Terre depuis le dôme d'observation. La station entière est sa galerie, les murs métalliques sa toile. Elle est là pour rendre l'orbite habitable pour l'âme, pas pour le corps.",
        "photos": [
            f"{R2}/img/vittoria/vittoria-v1.png",
            f"{R2}/img/vittoria/vittoria-v2.png",
            f"{R2}/img/vittoria/vittoria-v3.png"
        ],
        "station": "zineb"
    }
]

# Check for duplicates
existing_names = {e["name"] for e in data}
for entry in new_entries:
    if entry["name"] in existing_names:
        print(f"WARNING: {entry['name']} already exists in data.json, skipping")
        continue
    data.append(entry)
    print(f"Added: {entry['name']}")

data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nTotal entries: {len(data)}")
