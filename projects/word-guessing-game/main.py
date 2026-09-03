# Word guessing game

import random
import time

# List of words to choose from
words = ["Nadal", "Federer", "Djokovic", "Murray", "Thiem",
         "Zverev", "Medvedev", "Tsitsipas", "Alcaraz"]

print("Welcome to the word guessing game!")
print("You have to guess the name of a famous male tennis player, which the system has chosen.")
time.sleep(1)

word = random.choice(words).lower()

print("\nThe system has chosen a player.")
print("You have 10 attempts.")
print("Guess one character at a time.")
print("Type 'hint' for a hint (costs 2 attempts).")
print("You have 3 hints.\n")

attempts = 10
hints = 3
guessed = ""

while attempts > 0:

    # Display the word
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if won
    if "_" not in display:
        print("\nCongratulations! You guessed the player:", word.title())
        break

    ch = input("Guess a character or type 'hint': ").lower()

    if ch == "hint":

        if hints == 0:
            print("No hints left!")
            continue

        # Find unrevealed positions
        hidden_positions = []
        for i in range(len(word)):
            if word[i] not in guessed:
                hidden_positions.append(i)

        # Reveal one random hidden letter
        if hidden_positions:
            pos = random.choice(hidden_positions)
            guessed += word[pos]
            print("Hint: Letter at position", pos + 1, "is", word[pos].upper())

        hints -= 1
        attempts -= 2

    elif len(ch) != 1 or not ch.isalpha():
        print("Please enter only one alphabet.")

    else:
        if ch in guessed:
            print("You already guessed that letter.")

        elif ch in word:
            guessed += ch
            print("Correct!")

        else:
            attempts -= 1
            print("Wrong!")

    print("Attempts left:", attempts)
    print("Hints left:", hints)

if attempts <= 0:
    print("\nGame Over!")
    print("The player was:", word.title())