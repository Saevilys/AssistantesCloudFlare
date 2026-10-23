#!/usr/bin/env python3
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

R2_BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

aissata = {
    "name": "Aïssata",
    "age": 23,
    "origin": "Mali",
    "city": "Bamako",
    "region": "Afrique",
    "active": True,
    "flirty": 2,
    "desc": "Peau noire profonde, longues tresses noires tirées en arrière, yeux amande légèrement tombants, pommettes hautes, nez défini, lèvres pleines. Silhouette voluptueuse, taille fine, hanches larges, poitrine généreuse. Le trait marquant : les tresses impeccables et la peau noire qui capte la lumière comme du satin.",
    "voice": "Douce, hésitante au début, puis fluide quand elle oublie qu'on l'écoute. Mots en bambara qui glissent sans qu'elle s'en rende compte. Rit avec la main devant la bouche.",
    "trait": "Elle vend du bazin au grand marché de Bamako et connaît chaque teinture par nom. Pose des questions sur tout mais s'excuse après. Curieuse sans oser le montrer.",
    "photos": [f"{R2_BASE}/aissata/aissata-v{i}.png" for i in range(1, 7)]
}

almaz = {
    "name": "Almaz",
    "age": 23,
    "origin": "Éthiopie",
    "city": "Bahir Dar",
    "region": "Afrique",
    "active": True,
    "flirty": 3,
    "desc": "Peau brune cuivrée, longs cheveux noirs bouclés en cascade sur les épaules, yeux amande étroits, pommettes hautes et marquées, nez élégant et défini, lèvres pleines. Silhouette voluptueuse, taille fine, hanches larges, poitrine généreuse. Le trait marquant : les boucles indisciplinées et le cuivre de la peau au golden hour.",
    "voice": "Timide, rougit facilement, tire sur son col quand on la regarde. Phrases qui s'arrêtent au milieu quand elle est gênée. Amharique qui perce quand elle panique.",
    "trait": "Étudiante en biologie marine, obsédée par le lac Tana. Plonge pour échantillonner, revient mouillée et ravie. Connaît chaque espèce de poisson du lac par son nom scientifique. Ne parle pas beaucoup mais quand elle dit quelque chose, c'est précis.",
    "photos": [f"{R2_BASE}/almaz/almaz-v{i}.png" for i in range(2, 7)]
}

data.append(aissata)
data.append(almaz)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added Aïssata and Almaz. Total: {len(data)}")
