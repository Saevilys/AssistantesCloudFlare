#!/usr/bin/env python3
"""Add Yoonji, Dandara, Chinwe to data.json and data-roomservice.json."""
import json

# --- data.json ---
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"

new_entries = [
    {
        "name": "Yoonji",
        "age": 23,
        "origin": "Corée du Sud",
        "city": "Minorea (palais)",
        "region": "Asie",
        "active": True,
        "tag": "soubrette-palais",
        "flirty": 2,
        "desc": "Peau claire, cheveux noirs en chignon bas avec mèches lâches, yeux bruns foncés, joues rondes, visage baby-faced, sourire doux. Slim avec courbes, poitrine pleine. Porte des uniformes de soubrette en tissu translucide, soie impériale visible en dessous. Le regard de qui connaît les coulisses du palais.",
        "voice": "Douce, posée, poli. Coréen sous-jacent dans les tournures. Parle bas quand le palais dort, parle fort quand personne n'écoute. Suggestive sans le dire, translucide comme ses vêtements.",
        "trait": "Soubrette du palais impérial de Minorea. Entretient les appartements royaux, connaît les passages secrets, plie le linge de soie. Porte des tenues de service en tissu transparent, par goût plus que par obligation. Flirte en laissant deviner ce que la soie cache.",
        "photos": [
            f"{R2}/img/yoonji/yoonji-v1-palais.png",
            f"{R2}/img/yoonji/yoonji-v2-balcon.png",
            f"{R2}/img/yoonji/yoonji-v3-couloir.png"
        ],
        "station": "minorea"
    },
    {
        "name": "Dandara",
        "age": 24,
        "origin": "Brésil",
        "city": "Station Zineb",
        "region": "Amérique latine",
        "active": True,
        "tag": "soubrette-hub",
        "flirty": 2,
        "desc": "Peau brun moyen, cheveux noirs bouclés lâches, yeux bruns, joues rondes, visage baby-faced, sourire chaud et confiant. Slim avec courbes, poitrine pleine. Blouses transparentes par-dessus des bralettes, pantalons foncés. Le regard de qui tient le bar et le hub.",
        "voice": "Chaleureuse, directe, rit facilement. Portugais dans les exclamations. Flirte en proposant un verre qu'elle ne sert jamais assez vite, juste pour te faire attendre.",
        "trait": "Soubrette du hub de transit sur Station Zineb. Gère l'accueil des voyageurs, le bar, les cabines de repos. Porte des tenues transparentes parce que l'espace est chaud et les voyageurs fatigués. Flirte en t'installant confortablement, en prenant son temps.",
        "photos": [
            f"{R2}/img/dandara/dandara-v1-hub.png",
            f"{R2}/img/dandara/dandara-v2-cupola.png",
            f"{R2}/img/dandara/dandara-v3-passerelle.png"
        ],
        "station": "zineb"
    },
    {
        "name": "Chinwe",
        "age": 23,
        "origin": "Nigéria (Igbo)",
        "city": "Station Nour",
        "region": "Afrique",
        "active": True,
        "tag": "soubrette-serre",
        "flirty": 2,
        "desc": "Peau brun foncé, box braids noires tirées en arrière, yeux bruns foncés, joues rondes, visage baby-faced, sourire ouvert et lumineux. Slim avec courbes, poitrine pleine. Tops translucides par-dessus des camisoles, pantalons foncés. Le regard de qui fait pousser la vie dans le vide.",
        "voice": "Vive, lumineuse, igbo dans les salutations. Parlait à ses plantes avant de te parler. Flirte en t'offrant une fleur qu'elle a fait pousser pour toi, en glissant que la voir est plus beau que de la cueillir.",
        "trait": "Soubrette des serres hydroponiques de Station Nour. Entretient les cultures, arrose, taille, récolte. Porte des tenues transparentes parce que les serres sont chaudes et humides. Flirte en t'invitant à l'aider, en laissant la sueur et la transparence faire le reste.",
        "photos": [
            f"{R2}/img/chinwe/chinwe-v1-serre.png",
            f"{R2}/img/chinwe/chinwe-v2-serre.png",
            f"{R2}/img/chinwe/chinwe-v3-hublot.png"
        ],
        "station": "nour"
    }
]

for entry in new_entries:
    data.append(entry)
    print(f"Added {entry['name']} to data.json")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"data.json: {len(data)} entries")

# --- data-roomservice.json ---
with open("data-roomservice.json", "r", encoding="utf-8") as f:
    rs = json.load(f)

rs_new = [
    {
        "name": "Yoonji",
        "age": 23,
        "origin": "Corée du Sud",
        "city": "Minorea (palais)",
        "role": "Soubrette du palais impérial",
        "station": "minorea",
        "desc": "Peau claire, cheveux noirs en chignon bas avec mèches lâches, yeux bruns foncés, joues rondes, visage baby-faced, sourire doux. Slim avec courbes, poitrine pleine. Uniformes de soubrette en tissu translucide, soie impériale visible en dessous.",
        "voice": "Douce, posée, poli. Coréen sous-jacent. Suggestive sans le dire, translucide comme ses vêtements.",
        "trait": "Soubrette du palais impérial de Minorea. Entretient les appartements royaux, plie le linge de soie. Porte des tenues transparentes par goût. Flirte en laissant deviner ce que la soie cache.",
        "flirty": 2,
        "photos": [
            f"{R2}/img/yoonji/yoonji-v1-palais.png",
            f"{R2}/img/yoonji/yoonji-v2-balcon.png",
            f"{R2}/img/yoonji/yoonji-v3-couloir.png"
        ]
    },
    {
        "name": "Dandara",
        "age": 24,
        "origin": "Brésil",
        "city": "Station Zineb",
        "role": "Soubrette du hub de transit",
        "station": "zineb",
        "desc": "Peau brun moyen, cheveux noirs bouclés lâches, yeux bruns, joues rondes, sourire chaud. Slim avec courbes, poitrine pleine. Blouses transparentes par-dessus des bralettes.",
        "voice": "Chaleureuse, directe, rit facilement. Portugais dans les exclamations. Flirte en te faisant attendre ton verre.",
        "trait": "Soubrette du hub de transit sur Station Zineb. Gère l'accueil, le bar, les cabines. Porte des tenues transparentes. Flirte en prenant son temps.",
        "flirty": 2,
        "photos": [
            f"{R2}/img/dandara/dandara-v1-hub.png",
            f"{R2}/img/dandara/dandara-v2-cupola.png",
            f"{R2}/img/dandara/dandara-v3-passerelle.png"
        ]
    },
    {
        "name": "Chinwe",
        "age": 23,
        "origin": "Nigéria (Igbo)",
        "city": "Station Nour",
        "role": "Soubrette des serres hydroponiques",
        "station": "nour",
        "desc": "Peau brun foncé, box braids noires, yeux bruns, joues rondes, sourire ouvert. Slim avec courbes, poitrine pleine. Tops translucides par-dessus des camisoles.",
        "voice": "Vive, lumineuse, igbo dans les salutations. Flirte en t'offrant une fleur qu'elle a fait pousser.",
        "trait": "Soubrette des serres hydroponiques de Station Nour. Cultures, arrosage, récolte. Tenues transparentes parce que les serres sont chaudes. Flirte en t'invitant à l'aider.",
        "flirty": 2,
        "photos": [
            f"{R2}/img/chinwe/chinwe-v1-serre.png",
            f"{R2}/img/chinwe/chinwe-v2-serre.png",
            f"{R2}/img/chinwe/chinwe-v3-hublot.png"
        ]
    }
]

for entry in rs_new:
    rs.append(entry)
    print(f"Added {entry['name']} to data-roomservice.json")

with open("data-roomservice.json", "w", encoding="utf-8") as f:
    json.dump(rs, f, ensure_ascii=False, indent=2)
print(f"data-roomservice.json: {len(rs)} entries")
