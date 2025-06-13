print("Welcome to the Quiz Game!\n")

score = 0

print("Q1: What is the capital of France?")
print("A) Paris")
print("B) London")
print("C) Rome")
print("D) Berlin")
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "A":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer was A.\n")

print("Q2: Which planet is known as the Red Planet?")
print("A) Earth")
print("B) Mars")
print("C) Jupiter")
print("D) Venus")
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer was B.\n")

print("Q3: Who wrote 'Hamlet'?")
print("A) Charles Dickens")
print("B) Mark Twain")
print("C) William Shakespeare")
print("D) Jane Austen")
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "C":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer was C.\n")

print(f"Quiz finished! Your score: {score}/3")