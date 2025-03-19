#-----------------------------------------------------------------------------
#Name:        Chappy (ChatGPT) loops lesson (Chappy_ChatGPT_Loop_Lesson.py)
#Purpose:     learning Loops from ChatGPT (Chappy)
#			  Work in GitHub and Pycharm
#
#Author:      Amy Egwumba
#Created:     18-Mar-2025
#Updated:     19-Mar-2025
#-----------------------------------------------------------------------------

# Simple counter loop from 1 to 10
counter = 1  # Start at 1

while counter < 11:  # Keep going until counter hits 10
    print(counter)  # Print current counter
    print("You're doing great")  # Motivational message each time
    counter += 1  # Add 1 to counter each loop

print()  # Blank line for spacing
print()  # Another blank line for spacing

# ----- Number Guessing Game -----

import random  # Import random module for generating a random number

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

guess = None  # We haven't guessed anything yet
tries = 0  # Start try counter at 0

# Game intro
print("Alright, genius. I'm thinking of a number between 1 and 20.")
print("Bet you can't guess it!")

# Loop until the player guesses the secret number
while guess != secret_number:
    try:
        # Get user's guess and convert it to an integer
        guess = int(input("Your guess: "))
        tries += 1  # Increase try counter by 1

        # Check if guess is too low
        if guess < secret_number:
            print("Pfft. Too low. Are you even trying?")

        # Check if guess is too high
        elif guess > secret_number:
            print("Whoa there, too high! Overshooting much?")

        # If guess is correct
        else:
            print(f"Well, well, well... You got it! Took you {tries} tries though. U suck still nevertheless.")

    # Handle bad input (non-numbers)
    except ValueError:
        print("Bruh, that's not even a number. Focus!")
