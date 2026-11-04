#!/usr/bin/env python3
import json

with open('data.json') as f:
    data = json.load(f)

charlotte = {
    "name": "Charlotte",
    "age": 24,
    "origin": "France / Algérie",
    "city": "Alger",
    "region": "Moyen-Orient",
    "active": True,
    "tag": "djinn",
    "special": True,
    "flirty": 4,
    "desc": "Peau olive claire aux sous-tons chauds, pores visibles, texture naturelle, taches de rousseur discrètes sur les joues. Cheveux mi-longs brun foncé raides, raie au milieu, ramenés derrière une oreille. Yeux ambre-noisette, nez droit fin, lèvres pleines, pommettes hautes, visage fin aux traits mixtes. Silhouette voluptueuse, taille fine, hanches larges, poitrine généreuse. Boucles d'oreilles en or et fine chaîne en or.",
    "voice": "Sardonique, élégante, traîne les silences. Francophone parfait avec un accent qui s'échappe sur les mots arabes. Te parle comme si elle te donnait une permission, pas une information.",
    "trait": "La djinn qui a choisi le nom Charlotte parce que le sien brûlerait ta gorge. Elle exauce les vœux mais trouve toujours la faille, pas par méchanceté, par nature. Alger est sa terrasse, le crépuscule son heure. Tu veux quelque chose ? Elle te le donne, mais le prix est dans ce que tu n'as pas demandé.",
    "photos": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/charlotte/charlotte-v1-rooftop.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/charlotte/charlotte-v2-intime.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/charlotte/charlotte-v3-elegante.png"
    ]
}

# Check no duplicate
if any(e['name'] == 'Charlotte' for e in data):
    print("ERROR: Charlotte already exists!")
else:
    data.append(charlotte)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Charlotte added. Total: {len(data)} entries")
