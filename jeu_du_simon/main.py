"""
Pour cet exercice vous allez réaliser un jeu de mémoire (aussi connu sous le nom du "Simon").

- Le principe :
Vous allez demander à l'utilisateur de mémoriser une séquence de chiffres de plus en plus longue.
La séquence sera aléatoire, et commencera avec 4 chiffres. L'utilisateur à 3 secondes pour la mémoriser.
Si il donne la bonne réponse, on rajoute un nouveau chiffre à la suite de la séquence on la redemande à
l'utilisateur... et ainsi de suite, jusqu'à ce que l'utilisateur se trompe.

- Remarques :
La séquence sera affichée pendant 3 secondes, puis effacée de l'écran pour que l'utilisateur donne sa réponse.

-------
Pour effacer l'écran, vous allez copier dans votre code cette fonction :
    import os
    def clear_screen():
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')

-------
Pour bloquer l'execution de votre programme pendant "x" secondes, vous utiliserez la fonction :
    import time
    time.sleep(x)

Vous devez aussi gérer un score, initialement égal à 0, et qui s'incrémente de 1 à chaque bonne réponse.

Quand l'utilisateur donne une mauvaise réponse, le programme s'arrête directement et affiche (exemple) :
    Mauvaise réponse, la séquence était : 77686
    Votre score final : 1

- Voici le déroulement exact de votre programme :
V - 0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.
V 1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence
V 2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde
V 3 - Afficher la séquence à mémoriser pendant 3 secondes
4 - Nettoyer n'écran et demander la réponse à l'utilisateur
5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx",
puis reboucler à l'étape 1
5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence
était : xxxx, votre score final : xxxx"
"""

# IMPORT
import os
import random
import time


# FONCTIONS

"""
Fonction qui permet d'effacer l'écran (ou contenu du terminal
"""
def clear_screen() -> None :
    if (os.name == 'posix'): # Si Linux ou MacOs
        os.system('clear')
    else: # Windows
        os.system('cls')


def generer_sequence(boucleFor : bool, prevsequence : False):
    clear_screen()
    print("Retenez la séquence")
    time.sleep(1)

    if prevsequence == "":
        seq = ""
    else:
        seq = prevsequence
    
    for i in range(0,boucleFor):
        c = random.randint(0, 9)
        seq += str(c)
    
    print(seq)
    time.sleep(3)
    clear_screen()
    
    return seq


sequence = generer_sequence(4, "")
reponse = input("Votre réponse : ")

score = 0
while True:
    if sequence == reponse:
        score += 1
        print("Bonne réponse")
        print(f"Votre score : {score} ")
        time.sleep(3)
        sequence = generer_sequence(1, sequence)
        reponse = input("Votre réponse : ")
    else:
        break
    
    
print(f"Mauvaise réponse, la séquence était : {sequence}")
print(f"Votre score final : {score}")
