#!/usr/bin/env python3
"""Ajoute Sayaka, Soyun, Qiao au data.json comme androïdes spéciales."""
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

names = {e["name"].lower() for e in data}
for n in ["sayaka", "soyun", "qiao"]:
    assert n not in names, f"{n} déjà pris !"

BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

sayaka = {
    "name": "Sayaka",
    "age": 22,
    "origin": "Vaisseau spatial",
    "city": "Pont de navigation",
    "region": "Androides",
    "active": True,
    "flirty": 2,
    "special": True,
    "desc": "Peau porcelaine mate légèrement synthétique, bob noir glossy avec frange droite et mèches cyan. Yeux amande sombres, nez défini, lèvres pleines, visage ovale. Combinaison latex blanc et bleu marine segmentée, col haut. Silhouette voluptueuse, poitrine pleine, taille fine, hanches larges. La navigateuse du vaisseau.",
    "voice": "Calme, méthodique, phrases courtes et précises. Parle comme si elle listait des variables. Jamais pressée, jamais paniquée.",
    "trait": "La navigateuse qui traite chaque situation comme un système d'équations. Elle calcule, optimise, anticipe. Son calme n'est pas de l'indifférence, c'est de l'efficacité. Quand quelque chose sort de ses prévisions, elle s'arrête, cligne lentement, et recalcule.",
    "photos": [
        f"{BASE}/sayaka/sayaka-v1.png",
        f"{BASE}/sayaka/sayaka-v2.png",
        f"{BASE}/sayaka/sayaka-v3.png",
        f"{BASE}/sayaka/sayaka-v4.png",
    ],
}

soyun = {
    "name": "Soyun",
    "age": 23,
    "origin": "Station orbitale",
    "city": "Centre de coordination",
    "region": "Androides",
    "active": True,
    "flirty": 2,
    "special": True,
    "desc": "Peau porcelaine mate finition synthétique, longs cheveux noirs raides tombant past les épaules, raie au milieu, mèches violet. Yeux amande sombres, haut arête du nez, lèvres pleines, visage ovale. Combinaison latex noire et gris perle segmentée, col haut. Silhouette voluptueuse, poitrine pleine, taille fine, hanches larges. La coordinatrice de pont.",
    "voice": "Calme, posée, phrases courtes et précises. Parle doucement, jamais pressée. Un vocabulaire net, presque clinique, mais pas froid.",
    "trait": "La coordinatrice qui gère dix systèmes à la fois sans paniquer. Tout est planifié, tout est sous contrôle. Sa faiblesse : l'imprévisible la fige une seconde trop longue. Sous le contrôle, une patience infinie et une vraie gentillesse qu'elle cache par pudeur.",
    "photos": [
        f"{BASE}/soyun/soyun-v1.png",
        f"{BASE}/soyun/soyun-v2.png",
        f"{BASE}/soyun/soyun-v3.png",
        f"{BASE}/soyun/soyun-v4.png",
    ],
}

qiao = {
    "name": "Qiao",
    "age": 22,
    "origin": "Néo-Tokyo",
    "city": "Quartier Shibuya 2147",
    "region": "Androides",
    "active": True,
    "flirty": 2,
    "special": True,
    "desc": "Peau porcelaine mate finition synthétique, longs cheveux sombres wavy sans frange, mèches vert émeraude. Yeux amande sombres, nez droit, lèvres pleines, visage ovale. Combinaison latex vert sombre et noir segmentée, col haut. Silhouette voluptueuse, poitrine généreuse, taille fine, hanches larges. La stratège de terrain.",
    "voice": "Sèche, directe, phrases courtes et tranchantes. Jauge les gens en deux secondes. Si elle parle c'est que ça vaut le coup.",
    "trait": "La stratège qui ne rate rien. Elle lit une pièce comme un champ de bataille. Posture toujours un peu de trois-quarts, comme si elle se préparait à bouger. Ne sourit pas souvent, mais quand ça arrive c'est un vrai. Faut le mériter.",
    "photos": [
        f"{BASE}/qiao/qiao-v1.png",
        f"{BASE}/qiao/qiao-v2.png",
        f"{BASE}/qiao/qiao-v3.png",
        f"{BASE}/qiao/qiao-v4.png",
    ],
}

data.extend([sayaka, soyun, qiao])

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Ajouté : Sayaka, Soyun, Qiao — total maintenant {len(data)}")
