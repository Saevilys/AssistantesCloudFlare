h=open("specials.html").read()
# Voir le template de carte complet
i=h.find("card-info")
# Trouver celui dans le JS template (pas CSS)
import re
for m in re.finditer(r"card-info", h):
    j=m.start()
    ctx=h[j-50:j+300]
    if '${' in ctx:
        print(repr(ctx))
        print("===")
