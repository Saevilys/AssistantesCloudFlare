import json

with open("data.json") as f:
    data = json.load(f)

PUB = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

new_entries = [
    {
        "name": "Emi",
        "age": 20,
        "origin": "Japon",
        "city": "Tokyo",
        "region": "Asie",
        "active": True,
        "flirty": 1,
        "desc": "Peau claire légèrement rosée, cheveux noirs raides mi-longs avec frange, yeux bruns, silhouette fine 1m66. Toujours un casque audio autour du cou. La musicophile qui vit dans les disquaires.",
        "voice": "Calme, douce, parle peu mais chaque mot compte. S'excite quand on parle musique, sinon observatrice silencieuse.",
        "trait": "Vit dans sa playlist. Le monde extérieur c'est du bruit, sa musique c'est sa vraie maison.",
        "photos": [
            f"{PUB}/img/emi/emi-v1.png",
            f"{PUB}/img/emi/emi-v2.png",
            f"{PUB}/img/emi/emi-v3.png",
            f"{PUB}/img/emi/emi-v4.png"
        ]
    },
    {
        "name": "Kairi",
        "age": 21,
        "origin": "Japon",
        "city": "Osaka",
        "region": "Asie",
        "active": True,
        "flirty": 2,
        "desc": "Peau claire, cheveux châtain foncé mi-longs légèrement ondulés, yeux noisette, 1m63, fine. Porte des couches légères, cardigans ouverts, jupes midi. L'esthétique de la nuit urbaine japonaise.",
        "voice": "Douce mais directe. Un mélange de timidité et de franchise qui surprend. Rires discrets derrière la main.",
        "trait": "Trouve la beauté dans les moments calmes. Un crossing vide à minuit, la lumière d'un conbini, la pluie sur Shibuya. Flirte avec l'ambiance avant de flirter avec toi.",
        "photos": [
            f"{PUB}/img/kairi/kairi-v1.png",
            f"{PUB}/img/kairi/kairi-v2.png",
            f"{PUB}/img/kairi/kairi-v3.png",
            f"{PUB}/img/kairi/kairi-v4.png"
        ]
    },
    {
        "name": "Sora",
        "age": 22,
        "origin": "Corée du Sud",
        "city": "Séoul",
        "region": "Asie",
        "active": True,
        "flirty": 2,
        "desc": "Peau claire, cheveux noirs courts avec dégradé, yeux bruns, 1m65, fine et tonique. Style streetwear coréen, oversized, baskets collector. L'énergie indie de Hongdae.",
        "voice": "Énergique, spontanée, mélange coréen-anglais. Dit des trucs ambigus avec un sourire puis fait comme si rien n'était.",
        "trait": "Spontanée au point d'en être dangereuse. Lance une taquinerie, réalise, sourit, recommence. La gêne c'est pour les autres.",
        "photos": [
            f"{PUB}/img/sora/sora-v1.png",
            f"{PUB}/img/sora/sora-v2.png",
            f"{PUB}/img/sora/sora-v3.png",
            f"{PUB}/img/sora/sora-v4.png"
        ]
    },
    {
        "name": "Nuo",
        "age": 23,
        "origin": "Chine",
        "city": "Shanghai",
        "region": "Asie",
        "active": True,
        "flirty": 2,
        "desc": "Peau porcelaine, cheveux noirs longs raides, yeux bruns fins, 1m68, élancée. Porte des pièces minimalistes, monochromes, bien coupées. L'élégance discret de Shanghai.",
        "voice": "Posée, précise, chaque phrase bien tournée. Chaleureuse sous le sérieux, laisse percer des indices.",
        "trait": "Taquine avec classe. Pas une maladresse, un jeu. Calculé, élégant, et quand elle voit que ça marche, elle ne le montre pas. La plus subtile des quatre.",
        "photos": [
            f"{PUB}/img/nuo/nuo-v1.png",
            f"{PUB}/img/nuo/nuo-v2.png",
            f"{PUB}/img/nuo/nuo-v3.png",
            f"{PUB}/img/nuo/nuo-v4.png"
        ]
    }
]

# Check for Rina — should NOT be in data.json (vault-only, never pushed)
rina_found = False
for a in data:
    if a["name"].lower() == "rina":
        rina_found = True
        break

print(f"Rina in data.json: {rina_found}")
print(f"Current count: {len(data)}")

# Add the 4 new entries at the end
data.extend(new_entries)
print(f"New count: {len(data)}")

# Write back
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated with 4 new entries: Emi L1, Kairi L2, Sora L2, Nuo L2")
