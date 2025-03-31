#-----------------------------------------------------------------------------
#Name:        Skipping even numbers (Skipping_even_numbers.py)
#Purpose:     skips even numbers from '1' to '10'
#			  Work in GitHub and Pycharm
#
#Author:      Amy Egwumba
#Created:     20-Mar-2025
#Updated:     20-Mar-2025
#-----------------------------------------------------------------------------

# Loop from 1 to 10
for num in range(1, 11):
    # Check if the number is even
    if num % 2 == 0:
        continue  # Skip even numbers

    # Print odd numbers
    print(num)