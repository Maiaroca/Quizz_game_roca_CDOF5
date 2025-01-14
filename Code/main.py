questions = [
    {"question": "Quelle est la capitale de la France ?", "answer": "Paris"},
    {"question": "Combien font 2 + 2 ?", "answer": "4"},
    {"question": "Quel est le langage de programmation utilisé ici ?", "answer": "Python"},
    {"question": "En quelle année est née Maia ?", "answer": "2005"},

]

score = 0
for q in questions:
    response = input(q["question"] + " ")
    if response == q["answer"]:
        print("Correct !")
        score += 1
    else:
        print("Faux !")
print(f"Votre score : {score}/{len(questions)}")
