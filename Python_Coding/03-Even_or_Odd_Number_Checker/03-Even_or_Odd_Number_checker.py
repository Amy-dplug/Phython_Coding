#-----------------------------------------------------------------------------
# Name:        Even or Odd Number Cheker (Even_or_Odd_Number_checker.py)
# Purpose:     To tell user if number is even or odd
#			   work in Github and Pycharm
#
# Author:      Amy Egwumba
# Created:     20-Feb-2025
# Updated:     03-Mar-2025
#-----------------------------------------------------------------------------

#Step 1: Ask the user to enter a number
number = int(input("Enter a number: "))

#Step 2: Check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")  # If divisible by 2, it's even
else:
    print("The number is odd.")   # Otherwise, it's odd
