# Word Guessing Game

## About the project
Word guessing game is about guessing a word which the system has chosen from a set of words related to a domain for eg., Lawn Tennis Players. The user will be given only certain number of attempts to guess all the chars, they additionally are provided with 3 hints and if they take 1 hint, they lose 2 attempts out of what is left. If within the given attempts, they guess the word right, they win else they lose.

## Concepts Involved
- Input and Output char, string processing
- Random choice
- Loops
- Conditional Statements
- String Manipulation

## Algorithm
1. A list of words is initialised in the program. User enters the game, the system chooses one word in the list in random.
2. User has 3 hints and 10 attempts. Every hint reveals one char in random and reduces the remaining attempts by 2.
3. Repeatedly accept guesses from the user until the maximum number of attempts is reached.
4. Indicate whether each guess is represents a char in the word or not.
5. Stop the game when the correct number is guessed and display the result.
6. If the user fails to guess the number, display the correct answer and a game-over message.

## Example
Target word chosen: Nadal
- Guess 1: a -> Correct guess, word structure : _a_a_
- Guess 2: b -> Wrong guess, word structure : _a_a_
- Guess 3: Hint -> Attempts left = 6, word structure : _a_al
- Guess 4: n -> Correct guess, word structure : na_al
- Guess 5: l -> Congrats, you got it right!! It is Nadal aka Rafa.
Program exits.

## Run
`cd python-mini-projects/projects/word-guessing-game`

`python main.py`