# my_list_1 = [1,2,3]
# my_list_2 = []

# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)


# t = [[3-i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     print(t[i][i])
#     s += t[i][i]
# print(s)
# print(t)

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     # print(my_list[v])
#     my_list.insert(1, my_list[v])
# print(my_list)

# for i in range(1):
#     print("#")
# else:
#     print("#")

# my_list = [3,1,-2]
# print(my_list[my_list[-1]])

# my_list = [1,2,3,4]
# print(my_list[-3:-2])

# my_list = [i for i in range(-1,2)]
# print(my_list)

# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# a = 1 
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c)
# print(d)
# print(e)
# print(c+d+e)

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

# my_list = [[0,1,2,3] for i in range(2)]
# print(my_list)

# nums = [1,2,3]
# vals = nums
# del vals[1:2]
# print(nums)
# print(vals)

# We can write two simple functions to convert imperial units to metric ones. Let's start with pounds.
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def lb_to_kg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))




# def est_majeur(age: int):
#     if age <= 0:
#         return False

#     if age >= 18:
#         return True
#     else:
#         return False

# def recuperer_infos_personne(numero_personne):
#     nom_personne = input("Nom de la personne " + str(numero_personne) + ":")
#     age_personne = input("Age de la personne " + str(numero_personne) + ":")
#     return nom_personne, int(age_personne)

# def afficher_infos_personne(numero_personne, nom, age):
#     print("La personne", str(numero_personne), "est", nom, "son age est", age, "ans")
#     print("Le nom comporte", len(nom), "lettres")
#     if est_majeur(age):
#         print("Il est majeur")
#     else:
#         print("Il est mineur")

# def recuperer_et_afficher_infos_personne(numero_personne):
#     nom, age = recuperer_infos_personne(numero_personne)
#     afficher_infos_personne(numero_personne, nom, age)


# nb_personne = 2

# #for i in range(nb_personne):
#  #   recuperer_et_afficher_infos_personne(i+1)


# def demander_choix_utilisateur(min, max):
#     reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + ": ")

#     try:
#         reponse_int = int(reponse_str)
#         if not min <= reponse_int <= max:
#             print("ERREUR - Vous devez entrer un chiffre entre", min,"et", max)
#             return demander_choix_utilisateur(min, max)
#         return reponse_int
#     except:
#         print("ERREUR - Vous devez entrer un nombre")
#         return demander_choix_utilisateur(min, max)

# choix = demander_choix_utilisateur(1,5)
# print("Votre choix est", choix)