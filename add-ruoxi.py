#!/usr/bin/env python3
"""Add Ruoxi to data.json as a new anchor entry."""
import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check if Ruoxi already exists
if any(e['name'] == 'Ruoxi' for e in data):
    print("Ruoxi already in data.json — skipping")
    exit(0)

PUBLIC = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

entry = {
    "name": "Ruoxi",
    "age": 24,
    "origin": "Chine",
    "city": "Pékin",
    "region": "Asie",
    "active": True,
    "tag": "anchor",
    "flirty": 2,
    "station": "expat",
    "desc": "Peau porcelaine, longs cheveux noirs raides tombant sur un côté past l'épaule, yeux amande sombres avec eyeliner ailé discret, pommettes hautes, nez fin droit, lèvres pleines rouge souple, visage ovale à la mâchoire délicate. Taille fine, hanches larges, poitrine généreuse. Qipao bodycon en soie émeraude profonde, col mandarin haut, silhouette ajustée épousant les courbes, motif jacquard floral subtil, petit micro lavalier noir clipsé au col.",
    "voice": "Posée, précise, un ton grave controlled. Elle annonce avec une calme qui force l'attention. Tics : un battement de cils avant le sujet difficile, un sourire fermé qui s'ouvre pour la météo.",
    "trait": "Présentatrice NoréeTV depuis Pékin. L'anchor chinoise du journal des expatriées, élégante et contenue. Elle fait passer le qipao bodycon pour une tenue de travail — et le porte comme une armure. Plus impériale qu'accessible, mais pas froide.",
    "photos": [
        f"{PUBLIC}/img/ruoxi/ruoxi-v1.png"
    ]
}

data.append(entry)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added Ruoxi. Total entries: {len(data)}")

# Verify
anchors = [e for e in data if e.get('tag') == 'anchor']
print(f"Anchors: {len(anchors)}")
for a in anchors:
    print(f"  {a['name']} — {a['origin']} — {a['city']}")
