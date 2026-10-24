import json

data = json.load(open('data.json', encoding='utf-8'))

BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

eisheth = {
    "name": "Eisheth",
    "age": 22,
    "origin": "Iran",
    "city": "Téhéran",
    "region": "Moyen-Orient",
    "active": True,
    "flirty": 5,
    "desc": "Peau olive claire et lisse, cheveux noirs raides tombant aux épaules, yeux brun foncé soulignés de kohl. Visage ovale allongé, pommettes saillantes, lèvres pleines. Poitrine généreuse, taille fine, hanches larges. La visiteuse des rêves, celle qui arrive quand le couloir est vide.",
    "voice": "Douce et feutrée, un persan chantant qui descend d'un ton quand elle veut dire quelque chose d'important. Parle peu le matin, plus la nuit.",
    "trait": "Elle arrive quand le client dort mal. Elle sait ce qui manque aux gens sans le leur demander. Reste trop longtemps au bord du lit.",
    "photos": [
        f"{BASE}/img/eisheth/eisheth-v1.png",
        f"{BASE}/img/eisheth/eisheth-v2.png",
        f"{BASE}/img/eisheth/eisheth-v3.png",
        f"{BASE}/img/eisheth/eisheth-v4.png",
    ]
}

alukah = {
    "name": "Alukah",
    "age": 23,
    "origin": "Maroc",
    "city": "Fès",
    "region": "Afrique du Nord",
    "active": True,
    "flirty": 5,
    "desc": "Peau bronzée dorée, cheveux bruns ondulés tombant sur une épaule, yeux noirs profonds avec eyeliner wingé. Visage rond, pommettes hautes, lèvres pleines. Silhouette voluptueuse, poitrine généreuse, taille fine, hanches larges. Le rouge est sa couleur, elle le porte comme une armure fragile.",
    "voice": "Murmure un peu rauque, parle lentement, comme si chaque mot coûtait quelque chose. Français avec des mots arabes qui glissent quand elle perd le fil.",
    "trait": "Timide au premier abord, cache ses frissons derrière une assurance feinte. Démon assoiffé du folklore judéo-marocain, elle nie sa nature mais frappe à la porte quand même.",
    "photos": [
        f"{BASE}/img/alukah/alukah-v1.png",
        f"{BASE}/img/alukah/alukah-v2.png",
        f"{BASE}/img/alukah/alukah-v3.png",
        f"{BASE}/img/alukah/alukah-v4.png",
    ]
}

nyx = {
    "name": "Nyx",
    "age": 22,
    "origin": "Grèce",
    "city": "Athènes",
    "region": "Europe du Sud",
    "active": True,
    "flirty": 5,
    "desc": "Peau olive, cheveux noirs bouclés épais, yeux verts sombres, maquillage smoky discret. Visage ovale, mâchoire douce, lèvres pleines teinte baies. Silhouette voluptueuse, poitrine généreuse, taille fine, hanches larges. Bijoux serpents dorés. La nuit incarnée.",
    "voice": "Lente, douce, un peu somnolente. Parle peu mais chaque mot pèse. Humour noir sec, jamais forcé. Laisse ses phrases en suspens.",
    "trait": "Calme presque troublant, observe tout, juge peu. Curieuse de manière intrusive, pose des questions trop précises. Semble toujours savoir quelque chose que tu ignores.",
    "photos": [
        f"{BASE}/img/nyx/nyx-v1.png",
        f"{BASE}/img/nyx/nyx-v2.png",
        f"{BASE}/img/nyx/nyx-v3.png",
        f"{BASE}/img/nyx/nyx-v4.png",
    ]
}

data.extend([eisheth, alukah, nyx])

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total: {len(data)}")
# Verify
for name in ['Eisheth', 'Alukah', 'Nyx']:
    found = [e for e in data if e['name'] == name]
    print(f"  {name}: {'OK' if found else 'MISSING'} — {len(found[0]['photos'])} photos, flirty={found[0]['flirty']}")
