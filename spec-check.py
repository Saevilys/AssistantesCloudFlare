h=open("specials.html").read()
# Trouver le mapping avec les couleurs
i=h.find("ange:[")
if i==-1:
    i=h.find("'ange'")
print("ange mapping:", repr(h[i-20:i+80]))
# Lister tout le bloc de mapping
i=h.find("const tags={")
if i==-1:
    i=h.find("tags={")
print("tags block:", repr(h[i:i+500]))
