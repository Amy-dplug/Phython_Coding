#-----------------------------------------------------------------------------
#Name:        Countdown timer (Countdown_timer.py)
#Purpose:     counts down, starting from '10' o '1'
#			  Work in GitHub and Pycharm
#
#Author:      Amy Egwumba
#Created:     20-Mar-2025
#Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

# Set the countdown starting point
countdown = 10

# Loop for countdown
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrement countdown

    # Get user input to stop countdown
    user_input = input("Enter 'stop' to cancel or press Enter: ")

    # If the user types "stop", break the loop
    if user_input.lower() == "stop":
        print("Countdown stopped!")
        break