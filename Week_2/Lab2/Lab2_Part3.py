"""
Write a program that reads an integer and prints whether it is negative, zero, or positive.
"""

chosen_number = int(input("Please enter a number to check: "))

if chosen_number < 0:
    print("Your chosen number was: ", chosen_number)
    print("This number is negative.")
elif chosen_number == 0:
    print("Your chosen number is zero.")
else:
    print("Your chosen number was: ", chosen_number)
    print("This number is positive.")
