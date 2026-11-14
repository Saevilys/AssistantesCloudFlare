#!/usr/bin/env python3
"""Prepare Ruoxi data.json entry (to add after R2 upload)."""
import json

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
    "desc": "Peau porcelaine, longs cheveux noirs raides tombant sur un côté past l'épaule, yeux amande sombres avec eyeliner ailé discret, pommettes hautes, nez fin droit, lèvres pleines rouge souple, visage ovale à la mâchoire délicate. Taille fine, hanches larges, poitrine généreuse. Qipao bodycon en soie émeraude profonde, col mandarin haut, silhouette ajustée, fente latérale à mi-cuisse, micro lavalier noir au col.",
    "voice": "Calme, précise, chaque mot à sa place. Tons descendants en fin de phrase, pas de superlatifs. Elle annonce la canicule de Pékin comme la neige sur Minorea. Tics : hochement de tête pour valider, pause d'une demi-seconde avant un nom.",
    "trait": "Présentatrice NoréeTV depuis Pékin. La rigide élégante — elle porte le qipao comme une uniforme, pas comme un choix. On la regarde parce qu'elle est impeccable, pas parce qu'elle est chaleureuse. Elle ne sourit pas pour être aimée, elle sourit quand l'information est bonne. Ruoxi signifie 'comme l'aube douce' en chinois.",
    "photos": []
}

print(json.dumps(entry, indent=2, ensure_ascii=False))
print("\n--- Entry ready. Photos will be added after R2 upload. ---")
