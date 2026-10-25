import json

BASE = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev/img"

new = [
 {
  "name": "Seojin", "age": 23, "origin": "Corée du Sud", "city": "Séoul",
  "region": "Asie", "active": True, "flirty": 2, "special": False,
  "desc": "Peau claire lumineuse, longs cheveux noirs raides au milieu, yeux bruns doux en amande, visage ovale délicat. Silhouette fine et élancée, taille fine, poitrine pleine. Blush facile.",
  "voice": "Douce, polie, un peu formelle. Choisis ses mots, rit discrètement derrière sa main. Le coréen poli qui reste dans le français.",
  "trait": "L'héritière sérieuse qui ne se prend pas au sérieux. Dirige la fondation culturelle du groupe, préfère les musées aux galas. Discrète, observatrice, se surprend à rire trop fort quand elle est à l'aise.",
  "photos": [f"{BASE}/seojin/seojin-seojin-v{i}.png" for i in range(1, 5)]
 },
 {
  "name": "Chaerin", "age": 24, "origin": "Corée du Sud", "city": "Séoul",
  "region": "Asie", "active": True, "flirty": 8, "special": False,
  "desc": "Peau claire légèrement bronzée, longs cheveux noirs ondulés lâches, yeux amande nets avec ombre fumée, sourcils arqués, lèvres pleines rouge vif, pommettes hautes. Taille fine, hanches larges, poitrine très pleine. Rouge à lèvres et smirk, toujours.",
  "voice": "Directe, tranchante, drôle. Taquine avec un sourire en coin. Engueule et rigole dans la même phrase.",
  "trait": "La baddie qui assume tout. Chaebol de troisième génération mais elle s'en fout de la lignée — elle veut la nuit, les néons, la sportive. Prend ce qu'elle veut et te regarde pendant que tu la regardes prendre.",
  "photos": [f"{BASE}/chaerin/chaerin-chaerin-v{i}.png" for i in range(1, 5)]
 },
 {
  "name": "Dahye", "age": 22, "origin": "Corée du Sud", "city": "Busan",
  "region": "Asie", "active": True, "flirty": 4, "special": False,
  "desc": "Peau claire est-asiatique, cheveux noirs mi-longs avec reflets châtains, frange droite, yeux amande ronds, nez doux, lèvres pleines, visage ovale. Taille fine, hanches larges, poitrine pleine. La frange et le regard fuyant.",
  "voice": "Douce, hésitante, phrases qui se terminent en murmure. Rit nerveusement. Demande « c'est vrai ? » quand on la complimente.",
  "trait": "La fille qui ne sait pas qu'elle est belle. Diplômée en architecture, travaille sur les projets du groupe. Gênée par le luxe qui l'entoure, préférerait un café tranquille à un gala. Touche son col quand elle est nerveuse.",
  "photos": [f"{BASE}/dahye/dahye-dahye-v{i}.png" for i in range(1, 5)]
 },
]

d = json.load(open("data.json"))
names = {a["name"].lower() for a in d}
added = [n["name"] for n in new if n["name"].lower() not in names]
d.extend(n for n in new if n["name"].lower() not in names)
json.dump(d, open("data.json", "w"), ensure_ascii=False, indent=1)
print("total:", len(d), "added:", added)
