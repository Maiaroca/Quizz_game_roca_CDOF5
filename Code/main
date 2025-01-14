questions = [
    {"question": "Quelle est la capitale de la France ?", "answer": "Paris"},
    {"question": "Combien font 2 + 2 ?", "answer": "4"},
    {"question": "Quel est le langage de programmation utilisé ici ?", "answer": "Python"},
]

score = 0
for q in questions:
    response = input(q["question"] + " ")
    if response.lower() == q["answer"].lower():
        print("Correct !")
        score += 1
    else:
        print("Faux !")
print(f"Votre score : {score}/{len(questions)}")
