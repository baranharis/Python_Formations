"""
Voici l énoncé :
1. Définir le nombre de lettre à choisir  par saisie au clavier. Attention que ce nombre doit être inférieur à 10
2. Tant que le nonmbre de lettre n'est pas attend (saisie au clavier), le programme attend.
    Une fois le nombre de lettre attend, le programme rend la main et demande si on veut trier par ordre
    alphabetique ou pas (saisie clavier)
3. Le programme affiche les lettres selon le choix. Il affiche aussi les lettres dans l'ordre de la saisie (sans tri).
4. Le programme demande si on veut a nouveau refaire un essai ou si on veut quitter. Si quitter aurevoir
    et sinon on repart étape 1
"""

# IMPORT
import os

# Global variable
NOMBRE_MIN = 1
NOMBRE_MAX = 10

# FONCTIONS

"""
Fonction qui permet d'effacer l'écran (ou contenu du terminal
"""
def clear_screen() -> None :
    if (os.name == 'posix'): # Si Linux ou MacOs
        os.system('clear')
    else: # Windows
        os.system('cls')

"""
Fonction qui demande à l'utilisateur d'entrer le nombre de lettre à saisir
Retourne un nombre en entier
"""
def request_number(nbr_min, nbr_max):
    nbr_int = 0
    while nbr_int == 0:
        nbr_str = input("(A) --> Veuillez écrire le nombre de lettre que vous voulez entrer (entre " + str(nbr_min) + " et " + str(nbr_max) + ") ? ")
        try:
            nbr_int = int(nbr_str)
        except:
            print("ERREUR - Vous devez entrer un nombre.")
        else:
            if nbr_int < nbr_min or nbr_int > nbr_max:
                print(f"ERREUR - Vous devez entrer un nombre compris entre {nbr_min} et {nbr_max}. Réessayez!!")
                nbr_int = 0
    return nbr_int


"""
Fonction qui demande à l'utilisateur les lettres à trier
Paramètre : Nombre de lettres à saisir
Retourne toutes les lettres saisies
"""
def request_letters(number):
    print()
    print(f"(B) --> Veuillez saisir vos lettres ({number} lettres):")
    all_letter = ""
    for i in range(0, number):
        while True:
            letter = input(f"{i + 1}. ")
            is_letter = letter.isalpha()
            if is_letter == True:
                break
        all_letter += letter
    return all_letter

"""
Fonction qui demande à l'utilisateur les lettres à trier
Paramètre : Nombre de lettres à saisir
Retourne toutes les lettres saisies
"""
def sort_letters(letters):
    while True:
        print("(C) --> Vous voulez trier les lettres par ordre alphabétique:")
        print("1. Croissant")
        print("2. Décroissant")
        choix = input("Votre choix : ")
        if choix == "1" or choix == "2":
            break
        print("ERREUR - Vous devez choisir 1 ou 2\n")
    if choix == "1":
        lettes_sorted = ''.join(sorted(letters, reverse=False, key=str.lower))
    elif choix == "2":
        lettes_sorted = ''.join(sorted(letters, reverse=True, key=str.lower))
    return lettes_sorted

# MAIN
while True:
    clear_screen()
    print("EXERCICE : Tri des lettres ordre alphabétique (croissant ou décroissant)")
    print("------------------------------------------------------------------------")
    print()
    number = request_number(NOMBRE_MIN, NOMBRE_MAX)
    letters = request_letters(number)
    clear_screen()
    lettes_sorted = sort_letters(letters)
    clear_screen()
    print(f"--> Les lettres triées par ordre alphabétique : {lettes_sorted}")
    print(f"--> Les lettres que vous avez saisies : {letters}")
    print()
    again_game = input("Tapez sur une touche si voulez recommencer sinon 0 pour quitter : ")
    if again_game == "0":
        break

print("Aurevoir :-)\n")

