import random


def demander_nombre(nbr_min, nbr_max):
    nbr_int = 0
    while nbr_int == 0:
        nbr_str = input("Quel est le nombre magique (entre " + str(nbr_min) + " et " + str(nbr_max) + ") ?")
        try:
            nbr_int = int(nbr_str)
        except:
            print("ERREUR - Vous devez entrer un nombre :-(")
        else:
            if nbr_int < nbr_min or nbr_int > nbr_max:
                print(f"ERREUR - Vous devez entrer un nombre compris entre {nbr_min} et {nbr_max}. Réessayez ;-)")
                nbr_int = 0
    return nbr_int



NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIE = 4

"""nombre = 0
vies = NOMBRE_VIE
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies.")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagné :-)")
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit")
        vies -= 1
    else:
        print("le nombre magique est plus grand")
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu :-( . Le nombre magique était {NOMBRE_MAGIQUE}")"""


i = 0
gagne = False
for i in range(0, NOMBRE_VIE):
    vies = NOMBRE_VIE-i
    print(f"Il vous reste {vies} vies.")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagné :-)")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit")
    else:
        print("le nombre magique est plus grand")

if not gagne:
    print(f"Vous avez perdu :-( . Le nombre magique était {NOMBRE_MAGIQUE}")