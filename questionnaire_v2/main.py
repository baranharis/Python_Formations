# FONCTION : PROJET QUESTIONNAIRE


def poser_question(question):
    global score
    
    titre = question[0]
    choix = question[1]
    bonne_reponse = question[2]

    print()
    print("QUESTION :", titre)
    for i in range(len(choix)):
        print(f"    ({i+1})", choix[i])
     
    print()
    reponse_str = input(f"Votre réponse (entre 1 et {str(len(choix))}): ")
    reponse_int = int(reponse_str)
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")


score = 0
question1 = ("Quelle est la capital de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capital de la Turquie ?", ("Istanbul", "Konya", "Antalya", "Ankara"), "Ankara")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capital de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
# poser_question("Quelle est la capital de la Turquie ?", "Istanbul", "Konya", "Antalya", "Ankara", "d")

print("Le score final : ", score)