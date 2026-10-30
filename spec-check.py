h=open("specials.html").read()
# Vérifier que le badge est bien dans le template
i=h.find("card-tag-badge")
print("CSS:", "card-tag-badge" in h)
# Vérifier le template
i=h.find("card-trait")
print("template has card-trait:", "card-trait" in h)
# Vérifier le mapping
print("mapping surnaturel:", "Surnaturel" in h)
print("mapping succube:", "Succube" in h)
print("mapping anomalie:", "Anomalie" in h)
print("mapping kungfupunk:", "Kung Fu Punk" in h)
print("flirt-anomalie retiré:", "flirt-anomalie" not in h)
