# Number Guessing Game

## Project Goal

Build a command-line number guessing game using Python fundamentals.

The program should allow the player to select a difficulty level, guess a randomly generated number, receive feedback, and continue playing until they win or run out of attempts.

## Core Requirements

- Generate a random number between 1 and 100.
- Ask the player for their name.
- Personalise messages using the player's name.
- Allow the player to select a difficulty level:
  - Easy: 10 attempts
  - Medium: 7 attempts
  - Hard: 5 attempts
- Ask the player to enter a guess.
- Tell the player whether their guess is too high or too low.
- Tell the player how many attempts remain.
- Continue until:
  - The correct number is guessed, or
  - The player runs out of attempts.
- Display the number of attempts used when the player wins.
- Ask whether the player wants to play again.
- Track the best score during the current session.

## Input Validation

The program should:

- Reject guesses below 1 or above 100.
- Handle non-numeric input without crashing.
- Handle invalid difficulty selections.
- Handle invalid responses when asking whether to play again.

## Skills Demonstrated

- Variables
- Strings and f-strings
- User input
- Type conversion
- Conditional statements
- Loops
- Functions
- Exception handling
- Python's `random` module
- Program state
- Basic input validation

## Stretch Goals

Once the core program is working:

- Add proximity hints such as:
  - Very close
  - Close
  - Far away
- Save the best score to a file so it persists after the program closes.
- Organise the program into clear reusable functions.
- Add different number ranges for each difficulty level.

## Rules

This project should be built independently from a blank Python file.

Documentation, course notes, and help with individual problems may be used, but the complete solution should not be copied from a tutorial.