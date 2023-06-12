import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_QUESTION = 4

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    # 0 = + and 1 = *
    operator_str = "+"
    if o == 1:
        operator_str = "*"

    reponse_str = input(f"Faire le calcule suivant: {a} {operator_str} {b} = ")

    try:
        reponse_int = int(reponse_str)
    except:
        print("ERREUR - Veuillez entrer un nombre")

    calcul = a + b
    if o == 1:
        calcul = a * b

    if reponse_int == calcul:
        return True

    return False

nbr_point=0
for i in range (0, NOMBRE_QUESTION):
    print(f"Question n°{i+1} sur {NOMBRE_QUESTION}")

    if poser_question():
        print("Réponse correcte :-)")
        nbr_point += 1
    else:
        print("Réponse incorrecte :-(")

    print()



print(f"Votre note est : {nbr_point} / {NOMBRE_QUESTION}")

moyenne = int(NOMBRE_QUESTION/2)
if nbr_point == NOMBRE_QUESTION:
    print("Excellent!!!")
elif nbr_point == 0:
    print("Révisez vos math.")
elif nbr_point > moyenne:
    print("Pas mal")
elif nbr_point < moyenne:
    print("Peut mieux faire")
else:
    print("Vous avez la moyenne")