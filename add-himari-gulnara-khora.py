#!/usr/bin/env python3
"""Append Himari, Gulnara, Khora to data.json."""
import json

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_entries = [
    {
        "name": "Himari",
        "age": 24,
        "origin": "Japon",
        "city": "Minorea",
        "region": "Asie",
        "active": True,
        "tag": "cloud-architect",
        "flirty": 2,
        "desc": "Peau claire, cheveux bruns foncés raides en queue de cheval défaite, yeux amande bruns, joues rondes, sourire ouvert. Slim avec courbes, poitrine généreuse. Le sourire de qui construit demain.",
        "voice": "Vive, enthousiaste, parle avec ses mains. Elle commence par le plan et finit par vous montrer le ciel. Gesticule, corrige, recommence. L'énergie de quelqu'un qui aime ce qu'il fait.",
        "trait": "Architecte de nuages à Minorea. Elle conçoit les nouveaux quartiers flottants, modules empilés, gestion de l'espace vertical. La ville pousse et c'est elle qui dessine comment.",
        "photos": [
            f"{R2}/img/himari/himari-v1-cloudbridge.png",
            f"{R2}/img/himari/himari-v2-skyline.png",
            f"{R2}/img/himari/himari-v3-rooftop.png"
        ],
        "station": "minorea"
    },
    {
        "name": "Gulnara",
        "age": 25,
        "origin": "Kazakhstan",
        "city": "Station Zineb",
        "region": "Asie centrale",
        "active": True,
        "tag": "station-meteorologist",
        "flirty": 2,
        "desc": "Peau olive clair, cheveux noirs ondulés lâches sur les épaules, yeux brun foncé, joues rondes, regard confiant. Slim avec courbes, poitrine généreuse. Le calme de qui lit les tempêtes.",
        "voice": "Posée, précise, chaque phrase mesurée. Elle parle de l'orbite comme d'une météo. Silences entre les mots, comme si elle écoutait encore les données. S'emballe rarement, mais quand ça arrive c'est sur une anomalie.",
        "trait": "Météorologue spatiale à la station Zineb. Elle suit les tempêtes solaires, les vents de plasma, les aurores orbitales. Prévoit le temps de l'espace comme d'autres prévoient la pluie.",
        "photos": [
            f"{R2}/img/gulnara/gulnara-v1-viewport.png",
            f"{R2}/img/gulnara/gulnara-v2-corridor.png",
            f"{R2}/img/gulnara/gulnara-v3-cupola.png"
        ],
        "station": "zineb"
    },
    {
        "name": "Khora",
        "age": 26,
        "origin": "Éthiopie",
        "city": "Station Sagittarius A*",
        "region": "Afrique",
        "active": True,
        "tag": "horizon-cartographer",
        "flirty": 2,
        "desc": "Peau brun foncé, cheveux bruns en boucles serrées coupées court, yeux brun profond, pommettes hautes, expression calme et intense. Slim avec courbes, poitrine généreuse. Le regard de qui cartographie l'invisible.",
        "voice": "Lente, grave, chaque mot pèse. Elle parle du trou noir comme d'un voisin. Silences longs, comme si elle laissait à la gravité le temps de répondre. Ne s'emballe jamais, sauf quand l'horizon des événements fait un truc inattendu.",
        "trait": "Cartographe de l'horizon à Sgr A*. Elle cartographie la topologie de l'espace-temps autour du trou noir supermassif. dessine les cartes de ce qui n'a pas de carte, parce que la lumière ne sort pas.",
        "photos": [
            f"{R2}/img/khora/khora-v1-horizon.png",
            f"{R2}/img/khora/khora-v2-console.png",
            f"{R2}/img/khora/khora-v3-galaxy.png"
        ],
        "station": "sgr-a"
    }
]

# Check for duplicates
existing_names = {e["name"] for e in data}
for entry in new_entries:
    if entry["name"] in existing_names:
        print(f"WARNING: {entry['name']} already exists!")
    else:
        data.append(entry)
        print(f"Added: {entry['name']}")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nTotal entries: {len(data)}")

# Validate
with open("data.json", "r", encoding="utf-8") as f:
    json.load(f)
print("JSON valid ✓")
