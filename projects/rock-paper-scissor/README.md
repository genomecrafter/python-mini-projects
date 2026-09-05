# Rock Paper Scissor

## About the project
In this game, the player has 3 options - rock/paper/scissor. The time player chooses an option, the system also simultaneously chooses an option. The program compares both choices and declares the points. The player who gets 3 points will win the game.


## Concepts Involved
- Input and Output
- Loops and Conditional Statements
- Lists
- Game Logic Implementation
- Algorithm Design

## Algorithm
1. Display the rules of the game.
2. Accept the user's choice.
3. Validate the input and ensure it is within the allowed options.
4. Generate the computer's choice randomly.
5. Compare both choices and determine who gets the point.
6. Display the current score.
7. Continue until any player gets 3 points wins the round, show the msg accordingly and exit.

### Winning Rules
- Rock defeats Scissors.
- Scissors defeats Paper.
- Paper defeats Rock.
If both players choose the same option, the round ends in a draw, no one gets a point.

## Run
`cd python-mini-projects/projects/rock-paper-scissor`

`python main.py`