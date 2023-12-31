# PREMIER PAS EN Programmation orienté objet (POO)

# Personne
#   Données : Nom, age, ...
#   Actions :
#       - SePresenter
#       - DemanderNom (input)


# --------- DEFINITION ---------
class Personne:
    espece_etre_vivant = "Humain (mammifère homo sapiens)" # Variable de classe

    def __init__(self, nom: str = "", age: int = 0) -> None: # CONSTRUCTEUR
        self.nom = nom # Création d'une instance : nom
        if nom  == "":
            self.nom  = self.DemanderNom()

        self.age = age # Création d'une instance : age
        print("Constructeur personne: "+ self.nom)

    def SePresenter(self): # METHODE
        info_personne = "Bonjour je m'appelle "+ self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"

        
        print(info_personne)
        if self.age != 0:    
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
        
    def EstMajeur(self):
        # if self.age >= 18:
        #     return True
        # return False
        return self.age >= 18

    def DemanderNom(self):
        nomDemander = input("Veuillez entrer votre nom: ")
        return nomDemander
    
    def AfficherInfosEtreVivant():
        print("Info être vivant :" + Personne.espece_etre_vivant)

# --------- UTILISATION - V1 ---------
# personne1 = Personne("Haris", 30) # Creation de personne
# personne2 = Personne("Ayse", 15) # Creation de personne
# personne3 = Personne() # Creation de personne
# personne4 = Personne(age = 29) # Creation de personne

# personne1.SePresenter() # Methode d'instance
# personne2.SePresenter() # Methode d'instance
# personne3.SePresenter() # Methode d'instance
# personne4.SePresenter() # Methode d'instance

# print("Est Majeur 1 :", personne1.EstMajeur())
# print("Est Majeur 2 :", personne2.EstMajeur())

# --------- UTILISATION - V2---------

liste_personnes = [(Personne("Haris", 39))
                    , (Personne("Ayse", 30))
                    , (Personne("Yigit", 14))]
print()
print("-----------------")
print("Affichage liste 1")
print("-----------------")
for perso in liste_personnes:
    perso.SePresenter()
    Personne.AfficherInfosEtreVivant()


print()
print("-----------------")
print("Affichage liste 2")
print("-----------------")
liste_personnes.append(Personne(age = 29))
for perso in liste_personnes:
    perso.SePresenter()
    Personne.AfficherInfosEtreVivant()
    print()