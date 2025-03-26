# Write your code here
import random
import os
import json
from datetime import datetime

questions = [
    {"question": "Who is the Electric-type Pokémon known for evolving from Pikachu?", "answer": "Raichu"},
    {"question": "What is the name of the legendary Pokémon that represents time in the Pokémon universe?", "answer": "Dialga"},
    {"question": "Which Pokémon is known as the 'Flame Pokémon' and evolves from Charmander?", "answer": "Charizard"},
]

filename = 'user_performance.json'

def load_user_data():
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_user_data(data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def run_flashcards():
    user_data = load_user_data()

    random.shuffle(questions)

    correct_answers = 0
    flashcard_stats = {}

    for index, flashcard in enumerate(questions):
        question = flashcard["question"]
        correct_answer = flashcard["answer"]

        if flashcard["question"] in user_data:
            attempts = user_data[flashcard["question"]]["attempts"]
        else:
            attempts = 1  

        print(f"Question {index + 1}: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
            attempts = max(1, attempts - 1) 
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
            attempts += 1  

        flashcard_stats[question] = {"attempts": attempts}

    user_data["performance"] = correct_answers
    user_data["last_session"] = str(datetime.now())
    user_data["flashcard_stats"] = flashcard_stats
    save_user_data(user_data)

    print(f"\nYou answered {correct_answers} out of {len(questions)} questions correctly.")
    print(f"Your performance has been saved.")

    if "performance" in user_data:
        total_sessions = user_data.get("total_sessions", 0) + 1
        user_data["total_sessions"] = total_sessions
        print(f"\nSummary of past sessions:")
        print(f"Total Sessions: {total_sessions}")
        print(f"Last Session: {user_data['last_session']}")
        print(f"Total Correct Answers: {user_data['performance']}")

def main():
    run_flashcards()

if __name__ == "__main__":
    main()
