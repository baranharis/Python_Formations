

#  PARTIE 1

# personne = {'nom': 'Haris', 'age': 25, 'taille':1.730}

# #print(personne)
# #print(personne['nom'])
# #print(personne['age'])
# #print(personne['taille'])

# personne['poste'] = "Développeur"
# achat = ("Chocolat", "Beurre", "Fromage")
# personne['achat'] = achat
# #print(personne)

# for i in personne:
#     print(f"Clé: {i} - Valeur: {personne[i]}")

#  PARTIE 2

personnes = [
    ("Melanie",25,1.6),
    ("Paul",26,1.75),
    ("Jacque",27,1.7),
    ("Toto",28,1.8)
]

def obtenir_infomations(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

# Jacque
infos = obtenir_infomations("Jacque", personnes)
print(infos)


personnes_dict = {
    "Melanie":(25,1.6),
    "Paul":(26,1.75),
    "Jacque":(27,1.7),
    "Toto":(28,1.8)
}
infos = personnes_dict["Jacque"]
print(infos)