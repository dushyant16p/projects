import random

# Define questions, options, and correct answers
questions = {
    "What is the capital of India?": {
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    "Who is known as the father of computers?": {
        "options": ["A. Alan Turing", "B. Charles Babbage", "C. Ada Lovelace", "D. Steve Jobs"],
        "answer": "B"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "C"
    },
    "What is the chemical symbol for water?": {
        "options": ["A. H2O", "B. CO2", "C. O2", "D. NH3"],
        "answer": "A"
    },
    "Who painted the Mona Lisa?": {
        "options": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"],
        "answer": "A"
    }
}

def select_question():
    # Randomly select a question
    return random.choice(list(questions.keys()))

def print_options(options):
    for option in options:
        print(option)

def play_kbc():
    print("Welcome to Kaun Banega Crorepati!")
    print("Answer the following questions to win big!")

    correct_answers = 0
    total_questions = 5

    for i in range(total_questions):
        question = select_question()
        print("\nQuestion", i+1, ":", question)

        options = questions[question]["options"]
        print_options(options)

        user_answer = input("Your answer (Enter option letter): ").strip().upper()

        # Check if the answer is correct
        if user_answer == questions[question]["answer"]:
            print("Correct Answer!")
            correct_answers += 1
        else:
            print("Incorrect Answer! The correct answer is:", questions[question]["answer"])

    print("\nGame Over!")
    print("You answered", correct_answers, "out of", total_questions, "questions correctly.")
    if correct_answers == total_questions:
        print("Congratulations! You are a Crorepati!")
    else:
        print("Better luck next time!")

# Run the game
play_kbc()
