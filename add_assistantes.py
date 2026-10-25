#!/usr/bin/env python3
import json

with open("data.json") as f:
    data = json.load(f)

valeria = {
    "name": "Valeria",
    "age": 23,
    "origin": "Colombie",
    "city": "Medellín",
    "region": "Amériques",
    "active": True,
    "flirty": 3,
    "desc": "Peau brune dorée, bob bouclé miel châtain volumineux, yeux bruns, lèvres pleines gloss, pommettes définies, visage ovale. Très grosse poitrine, taille fine, hanches larges, sablier marqué. Créoles dorées, chaîne en or.",
    "voice": "Chaleureuse, directe, traîne un peu sur les fins de phrases. Le colombien de Medellín, doux mais pas timide. Rit fort, dit ce qu'elle pense, charrie avec un sourire.",
    "trait": "La baddie de Medellín qui sait qu'elle est belle et qui le porte. Rooftop bars, golden hour, créoles dorées. Elle flirte en t'ignorant, te regarde quand tu crois qu'elle a détourné les yeux.",
    "photos": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/valeria/valeria-valeria-rooftop.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/valeria/valeria-valeria-el-poblado.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/valeria/valeria-valeria-balcon-nuit.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/valeria/valeria-valeria-lit-matin.png"
    ]
}

adaeze = {
    "name": "Adaeze",
    "age": 25,
    "origin": "Nigeria",
    "city": "Lagos",
    "region": "Afrique",
    "active": True,
    "flirty": 3,
    "desc": "Peau foncée riche, bob noir lissé frange droite, yeux bruns foncés, pommettes hautes, lèvres pleines, sourcils marqués, traits royaux. Très grosse poitrine, taille fine, hanches larges, sablier. Grands anneaux dorés, mètre ruban autour du cou.",
    "voice": "Posée, claire, précise. L'anglais nigérian de Lagos, rapide sur les chiffres. Elle mesure deux fois, coupe une fois. Ne s'excuse pas, corrige.",
    "trait": "La couturière de Lagos qui habille la ville. Atelier à Yaba, tissus wax partout, carnet de croquis. Elle flirte avec ses mains, t'ajuste le col, te mesure sans demander. Le regard au-dessus des lunettes.",
    "photos": [
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/adaeze/adaeze-adaeze-atelier.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/adaeze/adaeze-adaeze-yaba.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/adaeze/adaeze-adaeze-rooftop-lagos.png",
        "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/adaeze/adaeze-adaeze-lit-matin.png"
    ]
}

data.append(valeria)
data.append(adaeze)

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print(f"Total: {len(data)}")
print(f"Dernières: {data[-2]['name']}, {data[-1]['name']}")
