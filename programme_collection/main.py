# Collections : (Tableau : Array), Listes, Tuples...
# Tuples (): immuable -> Non modifiable
# Listes []: muable -> modifiable : rajouter/supprimer des éléments ou les modifier
# Plusieur élémentss


# TUPLES --------------------------------------------
'''
personnes = ("Haris", "Ayse", "Yigit", "Elif")
print(len(personnes))
print(personnes[0]) # -1 pour le dernier élément du Tuples

print()
for i in range (0, len(personnes)):
    print(personnes[i])

print()
for i in personnes:
    print(i)
'''

# LISTES --------------------------------------------
'''
personnes = ["Haris", "Ayse", "Yigit", "Elif"]
nouvelle_personne = "Baran"

# print(personnes)
personnes.append(nouvelle_personne)
# print(personnes)

def afficher_valeur(c):
    for i in c:
        print(i)

afficher_valeur(personnes)
'''

# FONCTIONS --------------------------------------------
'''
personnes = ["Haris", "Ayse", "Yigit", "Elif"]
def obtenir_informations():
    return "Haris", 40, 1.79

def afficher_informations(nom, age, taille):
    print(f"Informations: Nom: {nom}, age: {age}, taille: {taille}")

infos = obtenir_informations()

# print("Nom: "+ infos[0])
# print("Age: "+ str(infos[1]))
# print("Taille: "+ str(infos[2]))

afficher_informations(*infos) # = unpack le Tuples
nom, age, taille = obtenir_informations()
afficher_informations(nom, age, taille)
'''

# SLICES --------------------------------------------
personnes = ["Haris", "Ayse", "Yigit", "Elif"]

# [start:stop:step]

for i in personnes[::-2]:
    print(i)

print()
nom = "Muhammed"
print(nom[0:3:])
print(nom[::-1])