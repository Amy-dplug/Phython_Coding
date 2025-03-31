#-----------------------------------------------------------------------------
#Name:        Guess the number (Guess_the_number.py)
#Purpose:     Asks the user to keep guessing the correct number between '1' and '10'
#			  Work in GitHub and Pycharm
#
#Author:      Amy Egwumba
#Created:     20-Mar-2025
#Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

import random

#Generte  a random number between 1 and 10
secret_number = random.randint(1, 10)

#Loop until the user guesses correctly
while True:
    guess = int(input("Guess the Number: "))

    if guess == secret_number:
        print("Correct! 🎉")
        break #Exit the loop
    else:
        print("Wrong, try again!")