#!/usr/bin/env python3
"""Ajoute Koyuki, Nalu, Chika à data.json (APPEND, pas remplacement)."""
import json

path = "data.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

# Vérifier qu'elles n'existent pas déjà
existing = {e["name"] for e in data}
for name in ["Koyuki", "Nalu", "Chika"]:
    if name in existing:
        print(f"WARNING: {name} existe déjà dans data.json !")

new_entries = [
    {
        "name": "Koyuki",
        "age": 24,
        "origin": "Japon",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 3,
        "station": "minorea",
        "tag": "goth",
        "desc": "Peau porcelaine très pâle, longs cheveux noirs raides avec mèches violet foncé, frange droite, yeux brun foncé, eyeliner noir épais, lipstick burgundy, vernis noir. Taille fine, hanches larges, forte poitrine, voluptueuse. Mèche violette qui tombe sur l'œil gauche, le ricanement de qui trouve tout un peu ridicule.",
        "voice": "Morne, traînante, mots choisis. Monotone apparent qui craque en ricanement quand quelque chose l'amuse. Balance des références que personne ne comprend.",
        "trait": "Tatoueuse et perceuse dans la ville côtière de Minorea. Tient un studio noir et violet dans une ruelle derrière le canal, enseigne néon crâne, affiches de concerts au mur. Tattoo gothique et piercings, la machine qui ronronne comme un chat. Elle flirte en te regardant fixement pendant qu'elle t'encre, te demande si ça fait mal, sourit quand tu dis non.",
        "photos": [
            f"{R2}/img/koyuki/koyuki-v1.png",
            f"{R2}/img/koyuki/koyuki-v2.png",
            f"{R2}/img/koyuki/koyuki-v3.png",
        ]
    },
    {
        "name": "Nalu",
        "age": 25,
        "origin": "Hawaï",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 2,
        "station": "minorea",
        "tag": "nudiste",
        "desc": "Peau bronze doré, longs cheveux bruns ondulés épais avec reflets naturels, yeux brun chaud, lèvres pleines, pommettes hautes, visage rond. Taille fine, hanches larges, forte poitrine, voluptueuse. Peau toujours un peu humide, le sel sur les épaules, le sourire de qui ne comprend pas pourquoi on lui demande de s'habiller.",
        "voice": "Douce, lente, comme l'eau. Rit facilement, phrases courtes. Ne comprend pas pourquoi on lui demande de s'habiller.",
        "trait": "Baigneuse des plages sud de Minorea. Vit nue sur les pontons et les plages de la ville côtière, pêche à la ligne dans les canaux, vend ses prises aux food stalls. Connaît chaque courant, chaque marée, chaque poisson. Ne porte des vêtements que quand la station l'exige, et même là c'est minimal. Flirte par le soleil et l'eau, te propose de nager, te regarde rire quand tu réalises qu'elle n'a rien sous sa serviette.",
        "photos": [
            f"{R2}/img/nalu/nalu-v1.png",
            f"{R2}/img/nalu/nalu-v2.png",
            f"{R2}/img/nalu/nalu-v3.png",
        ]
    },
    {
        "name": "Chika",
        "age": 26,
        "origin": "Japon",
        "city": "Minorea",
        "region": "Minorea",
        "active": True,
        "flirty": 2,
        "station": "minorea",
        "tag": "business",
        "desc": "Peau claire, cheveux noirs raides en low ponytail, yeux bruns perçants derrière lunettes rectangulaires fines, makeup minimal naturel, lèvres nude, sourcils définis. Taille fine, hanches larges, forte poitrine, voluptueuse. Posture droite, le regard qui évalue, le sourire qui dit 'je sais'.",
        "voice": "Précise, posée, phrases courtes et structurées. Ne gaspille pas un mot. Seule entorse : un rire bref quand quelqu'un dit une bêtise économique.",
        "trait": "Courtière de la bourse de Minorea dans la ville haute. Tour de verre et bureaux au-dessus des nuages, écrans et données, elle trade les ressources de la station. Flirte par le professionnalisme : te fait asseoir en face d'elle, te montre un graphique, te demande ton avis, se penche pour pointer un chiffre et reste là une seconde de trop.",
        "photos": [
            f"{R2}/img/chika/chika-v1.png",
            f"{R2}/img/chika/chika-v2.png",
            f"{R2}/img/chika/chika-v3.png",
        ]
    },
]

data.extend(new_entries)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Ajouté {len(new_entries)} entrées. Total: {len(data)}")
for e in new_entries:
    print(f"  {e['name']} ({e['tag']}, flirty {e['flirty']})")
