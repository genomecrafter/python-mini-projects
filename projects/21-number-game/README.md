# 21 Number Game

## About the project
It is number guessing game, a counting game where the players(player and system) alternatively, upto 3 numbers, whoever gets 21 first will lose the game. 


## Concepts Involved
- Input and Output
- Loops and Conditional Statements
- Functions
- Lists
- Game Logic Implementation
- Algorithm Design
- Strategy-Based AI

## Algorithm
1. The game is played by two players, one after the other, in this case right here, the sytem vs you.
2. One player can call 1 to 3 numbers in one turn.
3. The numbers called should be consecutive, else will lead to disqualification.
4. The counting starts from 1 and whoever calls 21 will lose the game.

### A winning strategy is to make the total count a multiple of 4 (4, 8, 12, 16, 20) before the opponent’s turn.

## Example
Player says: 1 2
Computer says: 3 4 5
Player says: 6 7
Computer says: 8 9
...
Player says: 21

Computer wins!!

## Run
`cd python-mini-projects/projects/21-number-game`

`python main.py`