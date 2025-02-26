#Voting eligibility check

age = int(input("Enter your age: "))  # Read user input and convert it to an integer

if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")
