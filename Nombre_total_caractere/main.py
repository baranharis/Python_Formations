# LES COLLECTIONS : LISTES / TUPLES
# Exercices : Nombre total de caractère

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# 1 - for / Len
cpt = 0
for i in noms:
    cpt += len(i)
    # print(i)
print("Nombre total de caractère (version 1):",cpt)

# 2 - Completion de liste + Sum
longueur_noms = [len(nom) for nom in noms]
print("Nombre total de caractère (version 2):", sum(longueur_noms))

# 3 - Join / len
tous_les_noms = "".join(noms)
print("Nombre total de caractère (version 3):", len(tous_les_noms))