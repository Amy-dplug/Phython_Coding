#Ask the user to enter the current temperature
temperature = float(input("Enter the temperature in Celsius: "))

#Conditional statements to provide advice
if temperature < 10:
    print("It's cold outside. Wear a jacket!")
elif 10 <= temperature <= 25:
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool!")

