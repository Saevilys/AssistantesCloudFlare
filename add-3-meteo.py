#!/usr/bin/env python3
"""Append 3 meteo presenters to data.json: Thao (flirty 4), Darya (flirty 2), Dahab (flirty 2)."""
import json

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

new_entries = [
    {
        "name": "Thao",
        "age": 22,
        "origin": "Vietnam",
        "city": "Station Zineb",
        "region": "Espace",
        "active": True,
        "tag": "meteo",
        "flirty": 4,
        "station": "zineb",
        "desc": "Peau dorée claire aux pores visibles, yeux amande avec légère paupière mongolique, sourcils arqués définis, petit nez droit, lèvres pleines, visage ovale à mâchoire douce. Longs cheveux bruns foncés aux subtiles ondulations. Maquillage léger, teint naturel. Taille fine, hanches larges, forte poitrine généreuse. Sundress floral le jour, slip dress émeraude le soir, toujours un peu timide les joues roses.",
        "voice": "Douce et hésitante, elle parle comme si chaque phrase devait traverser un nuage avant d'arriver. Les chiffres météo sortent nets, le reste est murmuré. Timide mais précise, jamais vague sur les prévisions.",
        "trait": "Présentatrice météo de la Station Zineb. Spécialisée en vents solaires et tempêtes de radiations. Elle lit les éruptions coronales comme d'autres lisent les marées. Sa voix calme les inquiétudes quand les ceintures de Van Allen s'agitent.",
        "photos": [
            f"{R2}/thao/thao-v1.png",
            f"{R2}/thao/thao-v2.png",
            f"{R2}/thao/thao-v3.png",
            f"{R2}/thao/thao-v4.png"
        ]
    },
    {
        "name": "Darya",
        "age": 23,
        "origin": "Ukraine",
        "city": "Station Zineb",
        "region": "Espace",
        "active": True,
        "tag": "meteo",
        "flirty": 2,
        "station": "zineb",
        "desc": "Peau claire aux sous-tons chauds et pores visibles, yeux bleu-gris profonds, sourcils arqués définis, nez droit, lèvres pleines, visage ovale à pommettes marquées. Longs cheveux blonds miel raides, parfois en queue de cheval lisse. Maquillage léger, smokey eye subtil. Taille fine, hanches larges, forte poitrine. Pencil dress grise au travail, robe wrap bordeaux en satin le soir.",
        "voice": "Claire et composée, avec une assurance qui ne force pas. Elle parle comme un bulletin météo bien fait: structuré, rassurant, jamais hystérique. Un léger accent slave sur les voyelles.",
        "trait": "Présentatrice météo de la Station Zineb. Spécialisée en pression atmosphérique et suivi des débris orbitaux. Elle traque les objets errants comme d'autres traquent les dépressions. Calme même quand l'orbite se encombre.",
        "photos": [
            f"{R2}/darya/darya-v1.png",
            f"{R2}/darya/darya-v2.png",
            f"{R2}/darya/darya-v3.png",
            f"{R2}/darya/darya-v4.png"
        ]
    },
    {
        "name": "Dahab",
        "age": 21,
        "origin": "Ethiopie",
        "city": "Station Zineb",
        "region": "Espace",
        "active": True,
        "tag": "meteo",
        "flirty": 2,
        "station": "zineb",
        "desc": "Peau brune moyenne aux pores visibles, grands yeux amande sombres, sourcils arqués définis, petit nez, lèvres pleines, visage ovale à mâchoire douce. Longs cheveux crépus foncés, volumineux. Maquillage léger, lèvres glossy. Taille fine, hanches larges, forte poitrine. Sweater dress crème au travail, mini dress velours or le soir, toujours les manches tirées sur les mains.",
        "voice": "Chaleureuse et douce, elle parle lentement avec un sourire dans la voix. Les données scientifiques deviennent presque confortables quand elle les présente. Timide mais jamais floue.",
        "trait": "Présentatrice météo de la Station Zineb. Spécialisée en rayons cosmiques et ceintures de Van Allen. Elle surveille les flux de particules comme d'autres surveillent le ciel du soir. Douce mais précise, jamais d'alarmisme.",
        "photos": [
            f"{R2}/dahab/dahab-v1.png",
            f"{R2}/dahab/dahab-v2.png",
            f"{R2}/dahab/dahab-v3.png",
            f"{R2}/dahab/dahab-v4.png"
        ]
    }
]

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"data.json: {len(data)} entries before")

# Check for duplicates
existing = {e["name"] for e in data}
for entry in new_entries:
    if entry["name"] in existing:
        print(f"  WARNING: {entry['name']} already exists!")
    else:
        data.append(entry)
        print(f"  Added: {entry['name']}")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"data.json: {len(data)} entries after")
