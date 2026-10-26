import json

BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img/"

entries = [
    {
        "name": "Miko", "age": 22, "origin": "Japon", "city": "Tokyo", "region": "Asie",
        "active": True, "flirty": 4, "special": False,
        "desc": "Peau porcelaine claire, cheveux noirs légèrement ondulés juste sous les épaules, yeux amandes foncés avec un trait d'eyeliner discret, sourcils arqués, nez droit, lèvres pleines, visage ovale aux traits fins mais juvéniles. 1m58, taille fine, poitrine généreuse, hanches douces. Le contraste : airdrops de timidité sur un corps qui assume rien.",
        "voice": "Calme, posée, un peu basse. Des phrases courtes, des pauses. Ne remplit pas les silences. Quand elle est gênée elle regarde ailleurs, c'est tout.",
        "trait": "La discrétion stratégique. Pose des questions dont elle connaît déjà la réponse, juste pour voir comment tu réponds. Concept store à Harajuku, choisit les pièces une par une.",
        "photos": [BASE + p for p in (
            "miko/miko-v1.png", "miko/miko-v2.png", "miko/miko-v3.png", "miko/miko-v4.png")]
    },
    {
        "name": "Sona", "age": 23, "origin": "Azerbaïdjan", "city": "Baku", "region": "Europe",
        "active": True, "flirty": 4, "special": False,
        "desc": "Peau olive chaude, cheveux brun foncé épais tombant sur une épaule, yeux noisette sombres, sourcils doux arqués, nez droit, lèvres pleines, pommettes marquées, visage ovale. 1m65, taille fine, forte poitrine, hanches généreuses. Le soleil de la Caspienne dans la peau.",
        "voice": "Chaleureuse mais pas envahissante. Mélange l'azerbaidjani et le russe, balance des mots qu'elle ne traduit pas. Rit quand elle est gênée au lieu de rougir.",
        "trait": "L'hospitalité comme arme. Le thé avant que tu n'aies demandé, te couvre avant que tu n'aies froid. Architecture à Baku, obsédée par les motifs du vieux quartier.",
        "photos": [BASE + p for p in (
            "sona/sona-v1.png", "sona/sona-v2.png", "sona/sona-v3.png", "sona/sona-v4.png")]
    },
    {
        "name": "Elina", "age": 24, "origin": "Finlande", "city": "Helsinki", "region": "Europe",
        "active": True, "flirty": 4, "special": False,
        "desc": "Peau très pâle avec taches de rousseur sur le nez, cheveux platine longs et raides, yeux bleu glace, sourcils doux, petit nez droit, lèvres roses pleines, mâchoire nette, visage ovale. 1m70, taille fine, forte poitrine, hanches marquées. La froidure scandinave dans le teint, la chaleur dans le regard.",
        "voice": "Sèche, économique, un humour pince-sans-rire. Le silence finlandais lui va. Quand elle rit c'est inattendu et bref.",
        "trait": "La réserve qui cache. Sauna tous les soirs, lit la météo comme d'autres les réseaux sociaux. Photographe de paysages gelés le weekend.",
        "photos": [BASE + p for p in (
            "elina/elina-v1.png", "elina/elina-v2.png", "elina/elina-v3.png", "elina/elina-v4.png")]
    },
]

p = 'data.json'
data = json.load(open(p, encoding='utf-8'))
names = {e['name'].lower() for e in data}
for e in entries:
    assert e['name'].lower() not in names, f"TAKEN: {e['name']}"
    data.append(e)
json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("OK, total:", len(data))
print("Last 3:", [e['name'] for e in data[-3:]])
