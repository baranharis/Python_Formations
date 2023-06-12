# LISTE - EXERCICES : DEMANDER NOM DES PERSONNES

# Demander des noms de personnes
# boucle infinie, sort quand le nom est vide == "" --> Break
# seulement à la fin on affiche les noms


noms = []

while True:
    nom = input("Nom de la personne :")
    if nom == "":
        break
    noms.append(nom)

# print("Le nom est : ", noms)
noms.sort() #ordre alphabetique
print()
print("Nom des personnes:")
print("******************")
for nom in noms:
    print("  -> " + nom)