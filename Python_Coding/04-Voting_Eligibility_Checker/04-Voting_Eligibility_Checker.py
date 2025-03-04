#-----------------------------------------------------------------------------
# Name:        Voting Eligibility Checker (Voting_Eligibility_dChecker.py)
# Purpose:     To check if a person is eligible to vote based on their age
#			   work in Github and Pycharm
#
# Author:      Amy Egwumba
# Created:     20-Feb-2025
# Updated:     03-Mar-2025
#-----------------------------------------------------------------------------

#Voting eligibility check

age = int(input("Enter your age: "))  # Read user input and convert it to an integer

if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")
