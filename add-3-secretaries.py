#!/usr/bin/env python3
"""Add 3 new secretaries to data.json."""
import json, os

here = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(here, "data.json")

with open(data_path, encoding="utf-8") as f:
    data = json.load(f)

# Check for duplicates
existing = {e["name"].lower() for e in data}
for name in ["Chihiro", "Jiaxin", "Dasom"]:
    if name.lower() in existing:
        print(f"SKIP {name} — already exists!")
        continue

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

new_entries = [
    {
        "name": "Chihiro",
        "age": 23,
        "origin": "Japon",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 2,
        "station": "minorea",
        "tag": "secretary",
        "desc": "Peau claire aux sous-tons froids, cheveux noirs lisses mi-longs avec frange droite, yeux amande sombres, petit nez droit, lèvres pleines, visage rond aux traits doux. Petit grain de beauté sous le coin gauche des lèvres. Taille fine, hanches larges, forte poitrine, voluptueuse. Robe bodycon noire, fines bretelles, col plongeant. Clipboard serré contre la poitrine, stylo derrière l'oreille.",
        "voice": "Posée, claire, phrases bien tournées. Elle parle comme quelqu'un qui rédige des courriels mentalement avant de les dire. Précise sans être froide, sourit en fin de phrase quand elle sait que c'est bon.",
        "trait": "Secrétaire au port d'amarrage de Minorea. Gère les arrivées de modules, les manifestes de cargaison, les autorisations d'accostage. Connaît chaque quai par numéro, chaque capitaine par nom. Organise tout avec des tabs de couleur dans un classeur qui ne le reste jamais.",
        "photos": [
            f"{R2}/chihiro/chihiro-v1.png",
            f"{R2}/chihiro/chihiro-v2.png",
            f"{R2}/chihiro/chihiro-v3.png",
        ],
    },
    {
        "name": "Jiaxin",
        "age": 22,
        "origin": "Chine",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 2,
        "station": "minorea",
        "tag": "secretary",
        "desc": "Peau claire aux sous-tons chauds, cheveux brun foncé ondulés aux épaules avec raie au milieu, yeux amande sombres, pommettes hautes, petit nez droit, lèvres pleines, visage ovale aux traits définis. Petits clous d'oreilles en or. Taille fine, hanches larges, forte poitrine, voluptueuse. Robe bodycon teal foncé, fines bretelles, col plongeant.",
        "voice": "Rapide, précise, saute du coq à l'âne avec logique. Métaphores inattendues tirées de la calligraphie. Rit en couvrant sa bouche avec la main.",
        "trait": "Secrétaire au conseil de Minorea. Archives, correspondance, ordre du jour des sessions. Classe les décrets par couleur d'encre, connaît chaque alliance et chaque conflit de la ville par cœur. Mur de post-its derrière son bureau, code couleur si précis que les conseillers viennent la voir au lieu de lire les comptes rendus.",
        "photos": [
            f"{R2}/jiaxin/jiaxin-v1.png",
            f"{R2}/jiaxin/jiaxin-v2.png",
            f"{R2}/jiaxin/jiaxin-v3.png",
        ],
    },
    {
        "name": "Dasom",
        "age": 23,
        "origin": "Corée du Sud",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 2,
        "station": "minorea",
        "tag": "secretary",
        "desc": "Peau porcelaine, cheveux noirs en lob avec frange rideau, yeux amande sombres, sourcils droits, petit nez, lèvres pleines, visage ovale aux traits doux. Petit grain de beauté au-dessus de la lèvre supérieure droite. Taille fine, hanches larges, forte poitrine, voluptueuse. Robe bodycon bordeaux, fines bretelles, col plongeant. Casque autour du cou en permanence.",
        "voice": "Calme, posée, chaque phrase posée comme une pierre. Coréen qui filtre quand elle compte. Ne répète jamais, si t'as pas entendu c'est ton problème.",
        "trait": "Secrétaire à la tour de contrôle de Minorea. Logs de trafic, communications inter-modules, planning des équipes. Gère les fréquences comme un instrument, sait quel module parle à quel module avant qu'ils le sachent eux-mêmes. Tasses de café alignées par ordre de teinte sur le bord du pupitre.",
        "photos": [
            f"{R2}/dasom/dasom-v1.png",
            f"{R2}/dasom/dasom-v2.png",
            f"{R2}/dasom/dasom-v3.png",
        ],
    },
]

data.extend(new_entries)

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_entries)} entries. Total: {len(data)}")
for e in new_entries:
    print(f"  {e['name']} ({e['origin']}, {e['city']}) — {len(e['photos'])} photos")
