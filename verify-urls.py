#!/usr/bin/env python3
"""Verify R2 URLs for the 9 new images."""
import urllib.request

R2 = "https://pub-a88b6eff97bc4ebb9c2158d3a1f98b4b.r2.dev"
urls = [
    f"{R2}/img/koyuki/koyuki-v1.png",
    f"{R2}/img/koyuki/koyuki-v2.png",
    f"{R2}/img/koyuki/koyuki-v3.png",
    f"{R2}/img/nalu/nalu-v1.png",
    f"{R2}/img/nalu/nalu-v2.png",
    f"{R2}/img/nalu/nalu-v3.png",
    f"{R2}/img/chika/chika-v1.png",
    f"{R2}/img/chika/chika-v2.png",
    f"{R2}/img/chika/chika-v3.png",
]

for url in urls:
    try:
        req = urllib.request.Request(url, method="HEAD")
        r = urllib.request.urlopen(req, timeout=10)
        print(f"OK {r.status} — {url.split('/img/')[-1]}")
    except Exception as e:
        print(f"FAIL — {url.split('/img/')[-1]} — {e}")
