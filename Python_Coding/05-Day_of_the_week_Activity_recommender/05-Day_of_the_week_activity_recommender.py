#-----------------------------------------------------------------------------
# Name:        Day of the week Activity recommender (Day_of_the_week_aactivity_recommender.py)
# Purpose:     To tell user if number is even or odd
#			   work in Github and Pycharm
#
# Author:      Amy Egwumba
# Created:     20-Feb-2025
# Updated:     03-Mar-2025
#-----------------------------------------------------------------------------

# Ask the user to enter the current day of the week
day = input("Enter the current day of the week: ").strip().lower()

# Suggest an activity based on the day
if day == "monday":
    print("Start your week with a workout!")
elif day == "tuesday":
    print("It's a great day to read a book!")
elif day == "wednesday":
    print("Mid-week movie night!")
elif day == "thursday":
    print("Try a new recipe!")
elif day == "friday":
    print("Relax and enjoy the weekend!")
elif day == "saturday":
    print("Go for a hike!")
elif day == "sunday":
    print("Prepare for the week ahead with some self-care.")
else:
    print("Invalid input. Please enter a valid day of the week."
