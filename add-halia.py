import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Check if Halia already exists
existing = [e for e in data if e["name"] == "Halia"]
if existing:
    print("Halia déjà présente, suppression...")
    data = [e for e in data if e["name"] != "Halia"]

halia = {
    "name": "Halia",
    "age": 24,
    "origin": "Hawaï",
    "city": "Basse Minorea",
    "station": "minorea",
    "region": "Océanie",
    "active": True,
    "tag": "meteo",
    "flirty": 2,
    "desc": "Peau bronzée chaude aux pores visibles, longs cheveux bruns foncé ondulés libres et balayés par le vent past les épaules, quelques mèches sur le visage, yeux brun foncé amande, sourcils définis naturels, nez droit, lèvres pleines gloss transparent, visage ovale doux, traits jeunes, quelques taches de rousseur légères sur le nez. Taille fine, hanches larges, poitrine généreuse.",
    "voice": "Chaleureuse, naturelle, le souffle du vent dans chaque phrase. Elle te donne la météo comme elle te donnerait la marée, simplement, avec le sourire. L'hawaïen qui fuse quand elle s'excite sur un front de nuages.",
    "trait": "Présentatrice météo de Basse Minorea. Elle annonce les marées, les vents du Pacifique, la température de l'eau et les formations nuageuses au-dessus de la ville haute. Pas de studio : elle fait ses bulletins en extérieur, sur les canaux, le long des ponts de pierre, le micro dans le vent.",
    "photos": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/halia/halia-v1.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/halia/halia-v2.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/halia/halia-v3.png"
    ]
}

data.append(halia)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"OK — Halia ajoutée. Total: {len(data)}")
