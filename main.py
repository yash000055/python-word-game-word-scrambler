# This is a simple word puzzle game where the program picks a random word, scrambles its letters, and 
# asks the user to guess the original word. The user has three attempts to guess correctly.
import random

import random

# WORD DATASET (sab uppercase for consistency)
dataset = [
    "INNOVATION", "EXPERIMENT", "HYPOTHESIS",
    "RESEARCH", "PHYSICS", "CHEMISTRY", "BIOLOGY",
    "LABORATORY", "MICROSCOPE", "DISCOVERY",

    "ALGORITHM", "MACHINELEARNING", "DEEPLEARNING",
    "NEURALNETWORK", "AUTOMATION", "ROBOTICS",
    "DATASCIENCE", "CHATBOT", "COMPUTERVISION",
    "NATURALLANGUAGEPROCESSING",

    "CAMPUS", "PROFESSOR", "ASSIGNMENT", "EXAM",
    "LECTURE", "SEMINAR", "INTERNSHIP",
    "GRADUATION", "THESIS", "UNIVERSITY",

    "TRUST", "BOND", "FUN", "HANGOUT", "SUPPORT",
    "MEMORIES", "LAUGHTER", "BROTHERHOOD",
    "SISTERHOOD", "COMPANIONSHIP",

    "COLLABORATION", "BRAINSTORMING", "STUDYGROUP",
    "CODING", "INNOVATIONHUB", "HACKATHON",
    "AICLUB", "TEAMWORK", "RESEARCHPAPER", "KNOWLEDGE"
]

print("WELCOME TO THE WORD SCRAMBLE GAME! \n")

# Shuffle dataset and pick one word
word = random.choice(dataset)
scrambled = list(word)
random.shuffle(scrambled)
scrambled_word = "".join(scrambled)

attempts = 3

print(f"SCRAMBLED WORD: {scrambled_word}\n")

while attempts > 0:
    guess = input("Your Guess: ").upper()

    if guess == word:
        print(f"\n Correct! You guessed the word with {attempts} attempts left!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f" Wrong! Try again. Attempts left: {attempts}\n")
        else:
            print(f"\n Game Over! No attempts left.")
            print(f"The correct word was: {word}")
