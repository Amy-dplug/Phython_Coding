#-----------------------------------------------------------------------------
#Name:        Sum of numbers (Sum_of_numbers.py)
#Purpose:     Calculate the sum of all numbers from '1' to 'n' using a loop
#			  Work in GitHub and Pycharm
#
#Author:      Amy Egwumba
#Created:     20-Mar-2025
#Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

#Ask user for input
n = int(input("Enter the number: "))

# Initialize sum variable
sum = 0

# Loop from 1 to n and calculate the sum
for i in range(1, n + 1):
    sum += i

# Print the result
print("Sum =", sum)