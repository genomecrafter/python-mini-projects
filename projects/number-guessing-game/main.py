# Number Guessing Game

import random
import time

MIN_LIMIT = -9999
MAX_LIMIT = 9999

print(
    f"Enter the range of numbers to choose the target number.\n"
    f"The range should be between {MIN_LIMIT} and {MAX_LIMIT}."
)

lb = int(input("Enter the lower bound: "))
ub = int(input("Enter the upper bound: "))

while lb < MIN_LIMIT:
    print(f"Please ensure the lower bound is greater than or equal to {MIN_LIMIT}.")
    lb = int(input("Enter the lower bound: "))

while ub > MAX_LIMIT:
    print(f"Please ensure the upper bound is less than or equal to {MAX_LIMIT}.")
    ub = int(input("Enter the upper bound: "))

while lb >= ub:
    print("The lower bound must be less than the upper bound.")
    lb = int(input("Enter the lower bound: "))
    ub = int(input("Enter the upper bound: "))

print("Thank you for providing the range.")
print("The system will choose the target number...")

target = random.randint(lb, ub)

time.sleep(1)

print("The system has chosen the number!")
print("You have a maximum of 10 guesses. Start guessing!")

guess = None
attempt = 0

while guess != target and attempt < 10:
    guess = int(input("Your guess: "))
    attempt += 1

    if guess == target:
        print(f"\nCongratulations! You guessed the number {target} in {attempt} attempt(s).")
        break
    elif guess < target:
        print(f"Guess {attempt}: {guess} -> Too low. {10 - attempt} guesses left.")
    else:
        print(f"Guess {attempt}: {guess} -> Too high. {10 - attempt} guesses left.")

if guess != target:
    print(f"\nGame Over! The correct number was {target}.")
else:
    print("\nThanks for playing!")