#!/usr/bin/env python3
"""Add 3 new Zineb citizens to data.json."""
import json

with open('data.json') as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

new_entries = [
    {
        "name": "Mahina",
        "age": 23,
        "origin": "Hawaï",
        "city": "Hilo",
        "region": "Océanie",
        "active": True,
        "flirty": 2,
        "station": "zineb",
        "desc": "Peau bronze chaud, longs cheveux noirs ondulés past les épaules, yeux amande noirs, pommettes hautes, lèvres pleines, visage rond et doux. Taille fine, hanches larges, forte poitrine, voluptueuse. Le genre de beauté solaire qui a grandi sous le soleil.",
        "voice": "Douce, lente, prend son temps. Chaque mot posé comme une graine. Rit fort quand quelque chose la surprend. Parle à ses plantes en hawaïen quand elle croit que personne n'écoute.",
        "trait": "Botaniste en gravité zéro sur Station Zineb. Fait pousser la nourriture de la station dans les bays hydroponiques. Connaît chaque feuille par nom. La Terre au hublot, les racines en l'air.",
        "photos": [
            f"{R2}/img/mahina/mahina-v1.png",
            f"{R2}/img/mahina/mahina-v2.png",
            f"{R2}/img/mahina/mahina-v3.png"
        ]
    },
    {
        "name": "Galina",
        "age": 24,
        "origin": "Bulgarie",
        "city": "Plovdiv",
        "region": "Europe",
        "active": True,
        "flirty": 2,
        "station": "zineb",
        "desc": "Peau claire aux sous-tons rosés, cheveux ash blonde mi-longs ondulés, yeux bleu-gris perçants, pommettes saillantes, nez droit, lèvres pleines, visage ovale. Taille fine, hanches larges, forte poitrine, voluptueuse. Un regard qui juge et un sourire qui suit.",
        "voice": "Sèche, directe, humour noir bulgare. Sert un verre et un commentaire en même temps. Pas méchante, juste pas tendre. Le mojoto en apesanteur, c'est son chef-d'œuvre.",
        "trait": "Barwoman du hub sur Station Zineb, le seul bar en orbite. Connaît tout le monde, juge tout le monde, mais avec un sourire. La Terre tourne derrière elle pendant qu'elle verse un mojito en apesanteur.",
        "photos": [
            f"{R2}/img/galina/galina-v1.png",
            f"{R2}/img/galina/galina-v2.png",
            f"{R2}/img/galina/galina-v3.png"
        ]
    },
    {
        "name": "Folake",
        "age": 22,
        "origin": "Nigeria",
        "city": "Lagos",
        "region": "Afrique",
        "active": True,
        "flirty": 2,
        "station": "zineb",
        "desc": "Peau ébène, tresses courtes plaquées contre le cuir chevelu, yeux amande noirs, pommettes hautes, lèvres pleines, mâchoire définie. Taille fine, hanches larges, forte poitrine, voluptueuse. Toujours un tournevis dans la poche.",
        "voice": "Rapide, pratique, peu de mots. Montre plutôt qu'elle explique. Rit en claquant des doigts quand quelqu'un casse un truc bête.",
        "trait": "Mécanicienne sur Station Zineb. Répare tout, des portes automatiques aux navettes d'accostage. Connaît chaque conduit, chaque soudure, chaque bruit bizarre. La station respire parce qu'elle la maintient.",
        "photos": [
            f"{R2}/img/folake/folake-v1.png",
            f"{R2}/img/folake/folake-v2.png",
            f"{R2}/img/folake/folake-v3.png"
        ]
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

with open('data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nTotal entries: {len(data)}")
