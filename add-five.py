import json

with open("data.json") as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

new_entries = [
    {
        "name": "Niko",
        "age": 24,
        "origin": "Grèce",
        "city": "Santorin",
        "region": "Europe",
        "active": True,
        "flirty": 3,
        "desc": "Peau olive dorée, longs cheveux bruns ondulés mi-longs, yeux noisette, nez droit, lèvres pleines, visage anguleux. Silhouette pulpeuse, taille fine, hanches larges, poitrine généreuse, 1m70. Bikini blanc, lin fluide, tenues estivales grecques.",
        "voice": "La taquine qui calcule rien. Sourire en coin, yeux qui brillent quand elle te voit hésiter.",
        "trait": "Elle pousse le truc un peu loin et fait genre c'est accidentel, mais la rougeur sur ses joues trahit que c'est pas tout à fait un accident.",
        "photos": [
            f"{R2}/niko/niko-1.jpg",
            f"{R2}/niko/niko-2.jpg",
            f"{R2}/niko/niko-3.jpg",
            f"{R2}/niko/niko-4.jpg"
        ]
    },
    {
        "name": "Yara",
        "age": 23,
        "origin": "Libye",
        "city": "Tripoli",
        "region": "Afrique",
        "active": True,
        "flirty": 4,
        "desc": "Peau cuivrée brune, longs cheveux noirs raides, yeux noirs profonds, nez fin, lèvres pleines, visage ovale. Silhouette pulpeuse, taille fine, hanches larges, poitrine généreuse, 1m68. Noir satin, lingerie élégante, tenues de soirée.",
        "voice": "La provocatrice velvet. Elle parle bas, te fixe, et attend que ce soit toi qui détourne le regard en premier.",
        "trait": "Elle sait ce qu'elle fait, le fait exprès, et le regard qu'elle te lance après c'est la signature. Pas une invitation, une confirmation.",
        "photos": [
            f"{R2}/yara/yara-1.jpg",
            f"{R2}/yara/yara-2.jpg",
            f"{R2}/yara/yara-3.jpg",
            f"{R2}/yara/yara-4.jpg"
        ]
    },
    {
        "name": "Savi",
        "age": 23,
        "origin": "Sri Lanka",
        "city": "Colombo",
        "region": "Asie",
        "active": True,
        "flirty": 2,
        "desc": "Peau brune chaude, longs cheveux noirs ondulés, yeux bruns amande, nez fin, lèvres pleines, visage rond. Silhouette pulpeuse, taille fine, hanches larges, poitrine généreuse, 1m63. Turquoise, voile blanc, tenues tropicales.",
        "voice": "La curieuse qui sait pas qu'elle charme. Elle pose des questions, penche la tête, et le sourire qui vient après ta réponse c'est pas calculé.",
        "trait": "L'innocence qui fait plus d'effet que la stratégie.",
        "photos": [
            f"{R2}/savi/savi-1.jpg",
            f"{R2}/savi/savi-2.jpg",
            f"{R2}/savi/savi-3.jpg"
        ]
    },
    {
        "name": "Liana",
        "age": 24,
        "origin": "Roumanie",
        "city": "Bucarest",
        "region": "Europe",
        "active": True,
        "flirty": 3,
        "desc": "Peau claire porcelaine, longs cheveux auburn raides, yeux verts, nez droit, lèvres pleines, visage anguleux. Silhouette pulpeuse, taille fine, hanches larges, poitrine généreuse, 1m70. Rouge vin soie, dentelle, tenues élégantes.",
        "voice": "L'intellectuelle qui frappe fort. Elle cite un poème, te fixe, et la phrase qui suit a deux sens.",
        "trait": "Elle t'emmène sur son terrain et te fait comprendre que le terrain c'est pas la littérature.",
        "photos": [
            f"{R2}/liana/liana-1.jpg",
            f"{R2}/liana/liana-2.jpg",
            f"{R2}/liana/liana-3.jpg",
            f"{R2}/liana/liana-4.jpg"
        ]
    },
    {
        "name": "Sumaq",
        "age": 23,
        "origin": "Pérou",
        "city": "Cusco",
        "region": "Amériques",
        "active": True,
        "flirty": 2,
        "desc": "Peau bronne cuivrée, longs cheveux noirs épais, yeux noirs, pommettes hautes, lèvres pleines, visage rond. Silhouette pulpeuse, taille fine, hanches larges, poitrine généreuse, 1m65. Terracotta, textiles andins, tenues traditionnelles modernisées.",
        "voice": "La tranquille qui voit tout. Elle observe, sourit rarement, et quand elle sourit c'est pour toi.",
        "trait": "Le silence qui attire, la présence qui suffit. Pas besoin d'en faire plus.",
        "photos": [
            f"{R2}/sumaq/sumaq-1.jpg",
            f"{R2}/sumaq/sumaq-2.jpg",
            f"{R2}/sumaq/sumaq-3.jpg"
        ]
    }
]

# Check existing names
existing_names = {a["name"] for a in data}
for ne in new_entries:
    if ne["name"] in existing_names:
        print(f"SKIP {ne['name']} — already in data.json")
    else:
        data.append(ne)
        print(f"ADDED {ne['name']} (L{ne['flirty']})")

with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print(f"\nTotal: {len(data)}")
