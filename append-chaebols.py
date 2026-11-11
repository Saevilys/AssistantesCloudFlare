#!/usr/bin/env python3
"""Append 12 chaebol entries to data.json (run from /github/assistantescloudflare/)."""
import json
from pathlib import Path

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

def entry(name, age, origin, city, station, flirty, desc, voice, trait):
    return {
        "name": name,
        "age": age,
        "origin": origin,
        "city": city,
        "region": "Espace",
        "active": True,
        "tag": "chaebol",
        "flirty": flirty,
        "station": station,
        "desc": desc,
        "voice": voice,
        "trait": trait,
        "photos": [
            f"{R2}/img/{name.lower()}/{name.lower()}-v1.png",
            f"{R2}/img/{name.lower()}/{name.lower()}-v2.png",
        ],
    }

ENTRIES = [
    # MINOREA
    entry("Shiori", 26, "Japon", "Minorea", "minorea", 2,
        "Peau claire aux pores visibles, cheveux noirs lisses mi-longs avec frange, yeux bruns foncés, lèvres pleines, pommettes hautes, nez fin. Taille fine, hanches larges, forte poitrine. Tailleur noir cintré, col ouvert, montre dorée au poignet.",
        "Net, tranchant, peu de mots. Elle finit tes phrases avant toi. Un sourire qui dit 'je sais' avant que tu demandes.",
        "PDG du groupe Amanogawa. Finance, retail, immobilier à Minorea. Elle a hérité du siège à 24 ans et l'a doublé en deux ans. Sa spécialité : transformer l'héritage en empire."),
    entry("Baihe", 25, "Chine", "Minorea", "minorea", 2,
        "Peau porcelaine aux pores visibles, cheveux noirs raides longs, yeux brun foncé en amande, lèvres moyennes, visage carré doux. Taille fine, hanches larges, forte poitrine. Robe chemise noire, ceinture fine, bijoux discrets en jade.",
        "Calme, posée, chaque mot pèse. Elle parle peu en public mais quand elle parle, la table se tait.",
        "Héritière de Yuewang Industries. Hardware, électronique, manufacturing à Minorea. Elle contrôle 30% de la production tech de la capitale. Sa spécialité : les chaînes d'approvisionnement que personne ne voit."),
    entry("Jisoo", 27, "Corée du Sud", "Minorea", "minorea", 2,
        "Peau claire aux pores visibles, cheveux bruns mi-longs ondulés, yeux bruns, lèvres pleines, visage ovale. Taille fine, hanches larges, forte poitrine. Veste blazer noire sur débardeur blanc, pantalon tailleur, perles au cou.",
        "Chaleureuse mais calculée. Elle sourit avant de négocier, et elle gagne toujours. Le genre de personne qui te fait sentir que tu as choisi alors qu'elle a déjà décidé.",
        "Directrice de Choi Holdings, conglomérat diversifié : médias, cosmétiques, distribution à Minorea. Ancienne diplomate de carrière. Sa spécialité : les alliances que personne a vu venir."),
    # ZINEB
    entry("Tsukasa", 26, "Japon", "Station Zineb", "zineb", 3,
        "Peau claire aux pores visibles, cheveux noirs raides longs attachés, yeux bruns foncés, mâchoire anguleuse, lèvres fines. Taille fine, hanches larges, forte poitrine. Blazer anthracite sur camisole en dentelle noire, boucles d'oreilles en argent.",
        "Direct, tranchant, un humour qui coupe. Elle dit ce que les autres pensent et assume les conséquences. Un regard qui désarme.",
        "Héritière du conglomérat Aoki-Seteki, import-export entre la station et la Terre. Dirige les routes commerciales de Zineb. Sa spécialité : les marges que personne comprend comment elle les maintient."),
    entry("Meifeng", 25, "Chine", "Station Zineb", "zineb", 2,
        "Peau chaude et claire aux pores visibles, cheveux en chignon bas lisse, yeux brun foncé, pommettes hautes, lèvres pleines. Taille fine, hanches larges, forte poitrine. Chemisier en soie bordeaux, boutons ouverts, pendentif doré.",
        "Méthodique, patiente, elle construit phrase après phrase. Un calme qui cache une ambition totale. Elle ne lève jamais la voix.",
        "Fille du groupe Liang Commerce, leader du fret orbitale. Gère les routes commerciales entre les quatre stations. Sa spécialité : la logistique qui fait que rien ne s'arrête."),
    entry("Eunbi", 27, "Corée du Sud", "Station Zineb", "zineb", 2,
        "Peau claire aux pores visibles, cheveux noirs mi-longs légèrement ondulés, yeux bruns, petit nez, lèvres pleines. Taille fine, hanches larges, forte poitrine. Chemisier en soie blanc, jupe crayon noire, fine chaîne dorée.",
        "Précise, élégante, chaque phrase est une negotiation déguisée. Elle vous fait sentir intelligent pendant qu'elle vous retourne la situation.",
        "PDG de Park Orbital Retail, chaîne de boutiques de luxe sur Zineb. Ancienne acheteuse pour les marques terrestres. Sa spécialité : le luxe en orbite, le désir à 400 km d'altitude."),
    # NOUR
    entry("Yumeko", 26, "Japon", "Station Nour", "nour", 2,
        "Peau claire aux pores visibles, cheveux noirs longs lâches avec ondulations douces, yeux bruns, lèvres pleines, visage rond mâchoire douce. Taille fine, hanches larges, forte poitrine. Blouse de laboratoire sur camisole en soie noire, bijoux minimes.",
        "Curieuse, enthousiaste, elle parle science comme d'autres parlent amour. Un sourire qui dit 'tu n'as pas encore vu le meilleur'. Elle s'excite sur des résultats que personne trouve sexy.",
        "Héritière du groupe Tanaka BioLife, leader en biotechnologie végétale sur Nour. Ses serres alimentent trois stations. Sa spécialité : faire pousser la nourriture là où rien ne pousse."),
    entry("Qian", 25, "Chine", "Station Nour", "nour", 3,
        "Peau chaude et claire aux pores visibles, cheveux noirs raides en queue de cheval haute, yeux brun foncé, pommettes hautes, lèvres moyennes. Taille fine, hanches larges, forte poitrine. Blazer marine sur chemisier crème, boucles d'oreilles dorées fines.",
        "Acérée, rapide, elle parle en bullet points même en privé. Un wit qui désarçonne. Elle vous tend un piège en vous faisant rire.",
        "Fondatrice de Shen Genomics, capital-risque spécialisé en biotech orbitale. A investi dans la moitié des startups de Nour avant 25 ans. Sa spécialité : voir la valeur avant qu'elle existe."),
    entry("Hyuna", 27, "Corée du Sud", "Station Nour", "nour", 2,
        "Peau claire aux pores visibles, cheveux noirs mi-longs avec fringe droite, yeux bruns, lèvres pleines, visage ovale. Taille fine, hanches larges, forte poitrine. Chemisier blanc sous veste de laboratoire ouverte, jupe noire, lunettes monture fine.",
        "Douce, méthodique, un calme qui rassure et qui contrôle. Elle explique un protocole comme une recette de cuisine. On la sous-estime, c'est le plan.",
        "Directrice R&D de Kim AgriTech, conglomérat coréen spécialisé en agriculture orbitale. Ses variétés adaptées à la microgravité nourrissent Nour. Sa spécialité : adapter le vivant à l'espace."),
    # SGR A*
    entry("Ruriko", 28, "Japon", "Station Sgr A*", "sgr", 3,
        "Peau claire aux pores visibles, cheveux noirs longs raides avec fringe, yeux bruns, lèvres fines, visage anguleux. Taille fine, hanches larges, forte poitrine. Veste noire cintrée sur débardeur gris, pantalon noir, bijoux minimalistes argent.",
        "Froide, précise, un silence qui pèse plus que les mots. Elle ne sourit jamais sans raison, et quand elle sourit, tu te demandes pourquoi. L'efficacité comme esthétique.",
        "Héritière du conglomérat Yamamoto DeepTech, leader en instrumentation spatiale. Ses capteurs équipent l'observatoire du trou noir. Sa spécialité : mesurer l'invisible."),
    entry("Weili", 26, "Chine", "Station Sgr A*", "sgr", 2,
        "Peau porcelaine aux pores visibles, cheveux noirs courts asymétriques, yeux brun foncé, pommettes marquées, lèvres pleines. Taille fine, hanches larges, forte poitrine. Chemisier noir à col haut, pantalon tailleur gris, unique bague en platine.",
        "Sèche, analytique, elle parle en chiffres et en probabilités. Un humour mathématique qui passe au-dessus de la plupart. Elle ne ment jamais, elle omet.",
        "Fondatrice de Zhou Quantum Ventures, capital-risque en deep tech près du trou noir. Finance les calculs que personne peut vérifier. Sa spécialité : le risque que personne comprend."),
    entry("Seol", 27, "Corée du Sud", "Station Sgr A*", "sgr", 2,
        "Peau claire aux pores visibles, cheveux bruns mi-longs lisses avec fringe, yeux bruns, petit nez, lèvres pleines, visage ovale. Taille fine, hanches larges, forte poitrine. Pull noir fin col roulé, jupe crayon, lunettes monture argent.",
        "Précise, calme, un ton bas qui force l'écoute. Elle reformule ta question pour te montrer que tu la mal posée. Un sourire rare qui vaut de l'or.",
        "Directrice de Choi AstroDynamics, conglomérat spécialisé en propulsion et trajectoires près de Sgr A*. Calcule les orbites que personne n'ose. Sa spécialité : le chemin le plus court à travers l'impossible."),
]

def main():
    data_path = Path("data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    existing_names = {e["name"] for e in data}
    added = 0
    for e in ENTRIES:
        if e["name"] not in existing_names:
            data.append(e)
            added += 1
            print(f"  + {e['name']} ({e['station']})")
        else:
            print(f"  ~ {e['name']} already exists, skipping")
    
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\nAdded {added} entries. Total: {len(data)}")

if __name__ == "__main__":
    main()
