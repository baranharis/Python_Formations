# LES COLLECTIONS : LISTES / TUPLES
# ANY et ALL

print("##### ANY et ALL ")
noms = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe', 'Martin']

# a = [True, True, True, False]
# print(any(a))
# print(all(a))

# found = False
# for nom in noms:
#     if "z" in nom.lower():
#         found = True
#         break
#
# if found:
#     print("Trouvé")
# else:
#     print("Non trouvé")

nom_avec_un_z_any = any([True if "e" in nom.lower() else False for nom in noms])
nom_avec_un_z_all = all([True if "e" in nom.lower() else False for nom in noms])
if nom_avec_un_z_any:
    print("Trouvé avec any")
else:
    print("Non trouvé avec any")

if nom_avec_un_z_all:
    print("Trouvé avec all")
else:
    print("Non trouvé avec all")


# Test si une chaine contient des chiffres
# any / isdigit
print()
print("##### Test si une chaine contient des chiffres ")

def chaine_contient_chiffre(chaine):
    """for c in chaine:
        if c.isdigit():
            return True
    return False"""
    return any([c.isdigit() for c in chaine])

nom = input("Quel est ton nom ?")
if nom == "":
    print("Le nom est vide")
elif chaine_contient_chiffre(nom):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print("Bonjour " + nom)


# Exercice "in insensible à la case"
print()
print("##### Exercice : in insensible à la case")
def element_dans_la_liste(element, liste):
    return [element.lower() in nom.lower() for nom in liste]

noms_liste = ['Jean', 'Sophie', 'Martin', 'Christophe', 'Zoe', 'Martin']

element_a_chercher = "jean"
if element_dans_la_liste(element_a_chercher, noms_liste):
    print(element_a_chercher + " est là")
else:
    print(element_a_chercher + " n'est pas là")


