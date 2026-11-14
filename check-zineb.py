#!/usr/bin/env python3
import re
with open('station-zineb.html') as f:
    content = f.read()
m = re.search(r'function flirtBannerLabel\(.*?\}', content, re.DOTALL)
if m:
    print(repr(content[m.start():m.end()+1]))
else:
    print("NOT FOUND")
# Also check if heartSVG already exists
if 'function heartSVG' in content:
    print("\nheartSVG already exists!")
if 'function flirtBannerLabel' in content:
    print("flirtBannerLabel exists")
