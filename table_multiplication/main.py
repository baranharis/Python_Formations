# EXERCICES FONCTIONS
# Table de multiplication
#



def afficher_table_multiplication(nombre, min = 1, max = 10):
    if min > max:
        print("ERREUR - Le min est supérieur au max")
        return

    for i in range(min, max+1):
        total = (i) * int(nombre)
        print(str(i),"x",nombre,"=",str(total))

afficher_table_multiplication(5,5,10)