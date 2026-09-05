# Number Guessing Game - Version 1
# Goal: Build the basic working game before adding additional features.

# IMPORTS
import random

# SETUP
random_number = random.randint(1, 100)

player_guesses_made = 0
player_guesses_remaining = 10
guessed_correctly = False

# MAIN GAME LOOP
while player_guesses_remaining > 0 and not guessed_correctly:

    player_guess = input('Guess the number between 1 and 100: ')
    player_guess = int(player_guess)
    player_guesses_remaining -= 1
    player_guesses_made += 1

    # CHECK THE GUESS
    if random_number == player_guess:
        print(f'You guessed the number {random_number} in {player_guesses_made} guesses!')
        guessed_correctly = True

    elif random_number < player_guess:
        print(f'{player_guess} is too high!')
        print(f'You have made {player_guesses_made} and have {player_guesses_remaining} guesses left.')
    else:
        print(f'{player_guess} is too low!')
        print(f'You have made {player_guesses_made} and have {player_guesses_remaining} guesses left.')

if not guessed_correctly:
    print(f'Game over! The number was {random_number}.')
    print(f'You used all {player_guesses_made} guesses.')
