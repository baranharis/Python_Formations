"""
nom = "haris baran"
print(nom)
print("je m'appelle " + nom + ".")
print("mon nom est " + nom + ".")
"""


def demander_age(nom):
    age_int = 0
    while age_int == 0:
        age_str = input(nom + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR - Vous devez entrer un nombre ;-)")
    return age_int


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ? ")
    return reponse_nom


def afficher_infos(nom, age):
    print()
    print("**********************************************************")
    print("Votre nom est " + nom + ", vous avez " + str(age) + " ans.")
    print(f"Votre nom est {nom} vous avez {age} ans.")
    print("Votre nom est %s vous avez %s ans." % (nom, age))
    print(nom + " l'an prochain vous aurez " + str(age + 1) + " ans.")

    if age < 10:
        print(nom + " vous êtes enfant.")
    elif age == 17:
        print(nom + " vous êtes presque majeur.")
    elif age > 60:
        print(nom + " vous êtes presque sénior.")
    elif age >= 18:
        print(nom + " vous êtes majeur.")
    else:
        print(nom + " vous êtes mineur.")
    print("**********************************************************")


NB_PERS = 2
for i in (0, NB_PERS):
    nom = demander_nom()
    age = demander_age(nom)
    afficher_infos(nom, age)
