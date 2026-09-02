# Number Guessing Game

## About the project
Number guessing game, user gives a range, from that range given the system chooses a number randomly. The user is given chances where the user tries to guess the number chosen by the system. The program guides the user whether the number guessed by the user is low or high compared to the target. When the user guesses it correctly, the win message is printed and program exits, or if the user reaches the maximum tries and couldnt get the number right, then try again message is printed and the program exits.

## Concepts Involved
- Input and Output processing
- Random number generation
- Loops
- Conditional Statements

## Algorithm
1. Read the lower and upper bounds from the user.
2. Generate a random number between the specified bounds.
3. Repeatedly accept guesses from the user until the maximum number of attempts is reached.
4. Indicate whether each guess is too high or too low.
5. Stop the game when the correct number is guessed and display the result.
6. If the user fails to guess the number, display the correct answer and a game-over message.

## Example
User-defined range: 1 to 20
Target number chosen: 13
- Guess 1: 5 -> Too low
- Guess 2: 10 -> Too low
- Guess 3: 15 -> Too high
- Guess 4: 13 -> Congrats, you got it right!!
Program exits.

## Run
`cd python-mini-projects/projects/number-guessing-game`
`python main.py`