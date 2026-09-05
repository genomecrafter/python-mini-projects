# Rock Paper Scissor

import random

print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")
print("First to score 3 points wins the game!\n")

choices = ["Rock", "Paper", "Scissors"]

player , system = 0,0

while True:
    if player == 3:
        print("User wins the game!")
        break
    if system == 3:
        print("Computer wins the game!")
        break

    print("Choose an option:")
    print("1 - Rock\n2 - Paper\n3 - Scissors")

    choice = int(input("Enter your choice (1-3):"))
    while choice < 1 or choice > 3:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice (1-3):"))

    user_choice = choices[choice - 1]
    print("\nUser choice is:", user_choice)

    print("Now it's Computer's Turn...")
    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]

    print("Computer choice is:", computer_choice)
    print(user_choice, "vs", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!No points awarded.\n")

    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print("<== User gets a point! ==>")
        player += 1
    else:
        print("<== Computer gets a point! ==>")
        system += 1

    print("\nScore:")
    print("User:", player)
    print("Computer:", system)

print("\nThanks for playing!")