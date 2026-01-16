# Rock Paper Scissors (Python)

Terminal-based Rock, Paper, Scissors game where the user plays against the computer over a fixed number of rounds.

## Features
- User vs Computer gameplay
- Configurable number of rounds
- Score tracking for both players
- Input validation
- Clear win/lose/tie feedback for each round
- Final game result summary

## How It Works
The player selects between rock, paper, or scissors.
The computer randomly chooses its move.

Each round:
- The winner is determined using predefined win rules
- Scores are updated accordingly
- The number of remaining attempts is displayed

The game ends after the maximum number of rounds is reached.

## Game Logic
The game uses a dictionary to define winning rules:

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper

This approach avoids complex conditional logic and keeps the code clean and easy to extend.


## Technologies
- Python 3
- random module

## Purpose
This project was created to practice:
- Function design
- Dictionaries for game rules
- Control flow and loops
- Input validation
- Writing clean and maintainable Python code
