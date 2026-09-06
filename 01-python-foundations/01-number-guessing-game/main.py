# Number Guessing Game - Version 2
# Goal: Add input validation and replay functionality.

import random

play_again = True

while play_again:

    random_number = random.randint(1, 100)

    player_guesses_made = 0
    player_guesses_remaining = 10
    guessed_correctly = False

    while player_guesses_remaining > 0 and not guessed_correctly:

        try:
            player_guess = int(input('Guess the number between 1 and 100: '))

            if player_guess < 1 or player_guess > 100:
                print('Please enter a number between 1 and 100.')
                continue

            player_guesses_remaining -= 1
            player_guesses_made += 1

        except ValueError:
            print('That is not a valid number. Please enter a whole number between 1 and 100.')
            continue

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

    while True:
        answer = input('Would you like to play again? ').strip().lower()

        if answer == 'yes':
            break

        elif answer == 'no':
            play_again = False
            break

        else:
            print('Please enter yes or no.')
