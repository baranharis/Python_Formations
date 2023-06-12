import turtle


# fonction escalier(taille, nb)
def escalier(taille, nbr):
    for i in range(0, nbr):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        # taille = taille - 10
    t.forward(taille)

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

def carres(taille_depart, nbr):
    for i in range(1, nbr):
        taille = i * taille_depart
        carre(taille)

t = turtle.Turtle()

TAILLE = 60
NBR = 5
# escalier(TAILLE, NBR)
# carre(TAILLE)
carres(TAILLE,NBR)


turtle.done()