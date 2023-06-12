# JEU DU SUDOKU

"""
Si l == 0 et c == 0 (quand on écrit verifier()), alors la fonction vérifie toutes les cases de la grille.
Pour tout vérifier, on suit la logique suivante pour chaque cases :
    La case contient une liste --> Si la liste contient 1 élément différent de 0 : Vrai
    La case contient un entier --> Si entier différent de 0 : Vrai
Si on donne des valeurs différentes à l et c, on vérifie juste la case en appliquant la logique précédente en voulant
que la case contienne une liste.
"""
def verifier(l=0,c=0):
    global grille,grilleFinie
    if not l and not c:
        for i in range(9):
            for j in range(9):
                if type(grille[i][j]) is list:
                    if len(grille[i][j]) == 1 and grille[i][j][0]:
                        grilleFinie[i][j] = True
                        grille[i][j] = grille[i][j][0]
                else:
                    if grille[i][j] != 0:
                        grilleFinie[i][j] = True
    else:
        if type(grille[l][c]) is list:
            if len(grille[l][c]) == 1 and grille[l][c][0]:
                grilleFinie[l][c] = True
                grille[l][c] = grille[l][c][0]

def solutions(l,c,ites):
    lc = l in [0, 1, 2] and [0, 1, 2] or l in [3, 4, 5] and [3, 4, 5] or l in [6, 7, 8] and [6, 7, 8]
    cc = c in [0, 1, 2] and [0, 1, 2] or c in [3, 4, 5] and [3, 4, 5] or c in [6, 7, 8] and [6, 7, 8]

    lc = l in [0, 1, 2] and [0, 1, 2] or l in [3, 4, 5] and [3, 4, 5] or l in [6, 7, 8] and [6, 7, 8]
    # Est strictement equivalent Ã  :
    if l in [0, 1, 2]:
        lc = [0, 1, 2]
    elif l in [3, 4, 5]:
        lc = [3, 4, 5]
    elif l in [6, 7, 8]:
        lc = [6, 7, 8]
    # Avec : l in [0,1,2] ssi 0 <= l <= 2