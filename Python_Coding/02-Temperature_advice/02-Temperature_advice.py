#-----------------------------------------------------------------------------
# Name:        Temperature Advice (Temperature_advice.py)
# Purpose:     To provide whether they should wear a jacket, short-sleeves, or stay indoors.
#			   work in Github and Pycharm
#
# Author:      Amy Egwumba
# Created:     20-Feb-2025
# Updated:     03-Mar-2025
#-----------------------------------------------------------------------------

temperature = float(input("Enter the temperature in Celsius: "))

#Conditional statements to provide advice
if temperature < 10:
    print("It's cold outside. Wear a jacket!")
elif 10 <= temperature <= 25:
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool!")

