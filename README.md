# AssistantesCloudFlare

Site statique pour Cloudflare Pages. Les images sont servies depuis Cloudflare R2 (`pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev`), le repo ne contient que le HTML/CSS/JS et les data.json.

## Structure

- `index.html` — page principale
- `roomservice.html` — room service
- `data.json` — données assistantes (images en URLs R2) — 244 entrées
- `data-roomservice.json` — données room service (images en URLs R2) — 40 entrées
- `.nojekyll` — désactive Jekyll

## Déploiement Cloudflare Pages

- Framework preset: None
- Build command: (vide)
- Build output directory: `/`
- Production branch: `nemini`
