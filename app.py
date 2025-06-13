def ask_question(question, options, answer):
    print(question)
    for opt in options:
        print(opt)
    user = input("Your answer (A/B/C/D): ")
    
    if user == answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was {answer}.\n")
        return 0

def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C"
        }
    ]
    print("Welcome to the Quiz Game!\n")
    score = 0
    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])
    print(f"Quiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()