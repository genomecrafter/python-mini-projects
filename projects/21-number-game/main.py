# 21 Number Game

# Computer to calculate its optimal move
def nearestmultiple(num):
    if num>=4:
        return num + (4 - num%4)
    else:
        return 4

# Check if the entered numbers are consecutive
def check(x):
    i = 1
    while i<len(x):
        if x[i]-x[i-1] != 1:
            return False
        i+=1
    return True

# Losing msg
def lose():
    print("You lost! The computer has won the game.\n Better luck next time!")
    exit(0)

# To decide who will start the game
def start():
    x = []
    last = 0

    while True:
        chance = input("Enter 'F' to start first or 'S' to start second: \n")

        # Game logic if chance == 'F' 
        if chance.upper() == 'F':
            while True:
                if last ==20:
                    lose()

                print("Your turn.")
                inp = int(input("How many numbers do you want to enter? (1-3): "))
                if 1<= inp <=3:
                    comp = 4 - inp
                else:
                    print("Wrong input. You are disqualified from the game.")
                    lose()

                print("Enter the numbers:")
                for i in range(inp):
                    x.append(int(input('Enter number: ')))

                last = x[-1]
                if not check(x):
                    print("You entered non-consecutive numbers. You are disqualified from the game.")
                    lose()
                if last == 21:
                    lose()

                print("Computer's turn:")
                for j in range(1,comp+1):
                    x.append(last+j)

                print("Numbers after computer's turn:", x)
                last = x[-1]

        elif chance.upper() == 'S':
            comp = 1
            last = 0

            while last <20:
                print("Computer's turn:")
                for j in range(1,comp+1):
                    x.append(last+j)

                print("Numbers after computer's turn:", x)
                last = x[-1]

                if x[-1] == 20:
                    lose()

                print("Your turn.")
                inp = int(input("How many numbers do you want to enter? (1-3): "))
                if 1<= inp <=3:
                    pass
                else:
                    print("Wrong input. You are disqualified from the game.")
                    lose()

                print("Enter the numbers:")
                for i in range(inp):
                    x.append(int(input('Enter number: ')))  

                last = x[-1]

                if not check(x):
                    print("You entered non-consecutive numbers. You are disqualified from the game.")
                    lose()

                near = nearestmultiple(last)
                comp = near - last
                if comp == 4:
                    comp = 3
                
            print("\n\nCONGRATULATIONS!!!")
            print("YOU WON!")
            exit(0)

        else:
            print("Wrong choice. Please enter F or S.")


game = True

while game:
    print("Welcome to the 21 number game!")
    ans = input("Do you want to play the 21 number game? (Yes / No)\n> ")
    print("The rules of the game are as follows:")
    print("1. You can enter 1, 2, or 3 numbers in each turn.")
    print("2. The numbers must be consecutive, game starts from 1.")
    print("3. The player who reaches 21 loses.")
    print("You are Player 1. \nPlayer 2 is Computer.")
    

    if ans.lower() == 'yes':
        start()
    else:
        nex = input("Do you want to quit the game? (Yes / No)\n> ")

        if nex.lower() == "yes":
            print("You are quitting the game...")
            exit(0)
        elif nex.lower() == "no":
            print("Continuing...")
        else:
            print("Wrong choice")