import random
import os
import json
from datetime import datetime

questions = [
    {"question": "What was the first Pokémon ever created?",
     "options": ["Pikachu", "Bulbasaur", "Rhydon", "Mew"],
     "answer": "Rhydon"},
    
    {"question": "Which Pokémon is known as the 'Eon Pokémon'?",
     "options": ["Lugia", "Mewtwo", "Latios and Latias", "Rayquaza"],
     "answer": "Latios and Latias"},
    
    {"question": "What type is the Pokémon 'Garchomp'?",
     "options": ["Dragon/Ground", "Dragon/Flying", "Ground/Rock", "Dragon/Steel"],
     "answer": "Dragon/Ground"},
    
    {"question": "In which generation was the Fairy-type introduced?",
     "options": ["Generation IV", "Generation V", "Generation VI", "Generation VII"],
     "answer": "Generation VI"},
    
    {"question": "Which of the following Pokémon is not a Legendary Pokémon?",
     "options": ["Entei", "Garchomp", "Regirock", "Cresselia"],
     "answer": "Garchomp"},
    
    {"question": "Who is the Electric-type Pokémon known for evolving from Pikachu?",
     "options": ["Raichu", "Electrode", "Zapdos", "Magnemite"],
     "answer": "Raichu"},
    
    {"question": "What is the name of the legendary Pokémon that represents time in the Pokémon universe?",
     "options": ["Dialga", "Palkia", "Giratina", "Lugia"],
     "answer": "Dialga"},
    
    {"question": "Which Pokémon is known as the 'Flame Pokémon' and evolves from Charmander?",
     "options": ["Charizard", "Flareon", "Infernape", "Ember"],
     "answer": "Charizard"},
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
        options = flashcard["options"]
        correct_answer = flashcard["answer"]

        if flashcard["question"] in user_data:
            attempts = user_data[flashcard["question"]]["attempts"]
        else:
            attempts = 1  

        print(f"Question {index + 1}: {question}")
        random.shuffle(options) 

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            user_answer_index = int(input("Your answer (1-4): ").strip()) - 1
            user_answer = options[user_answer_index]
        except (ValueError, IndexError):
            print("Invalid choice! Please select a number between 1 and 4.")
            continue

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
