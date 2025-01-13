#ths is a python quiz exercise for tuple

questions = ("how many elements are there in the periodic table?: ",
             "who does thien love the most?: ",
             "what is thiens birthday?: ",
             "what is 5 + 5?: ",
             "what is 10 + 10?:")

options = (("A. 116","B 117","C. 118","D. 119"),
           ("A mom","B dad","C krista","D layla"),
           ("A. 11/10","B. 11/11","C. 11/12","D. 11/13"),
           ("A. 11","B. 10","C. 13","D. 14"),
           ("A. 16","B. 17","C. 18","D. 20"))

answers = ("C","A","B","B","D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

guess = input("Enter (A, B, C, D): ").upper()
guesses.append(guess)
if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
    print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")