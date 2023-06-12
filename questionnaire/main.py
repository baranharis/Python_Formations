# FONCTION : PROJET QUESTIONNAIRE


def poser_question(question, r1,r2, r3, r4, bonne_reponse):
    global score
    print()
    print("QUESTION :", question)
    print("(a)", r1)
    print("(b)", r2)
    print("(c)", r3)
    print("(d)", r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")


score = 0
poser_question("Quelle est la capital de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capital de la Turquie ?", "Istanbul", "Konya", "Antalya", "Ankara", "d")

print("Le score final : ", score)