"""
Write a function FirstDigit(n) that returns the first digit of n. For example, FirstDigit(51280) returns 5.
"""


def FirstDigit(number):
    while number >= 10:
        number = number // 10
    return number


number = int(input("Enter the number you wish to ge the first digit of: "))

first_digit = FirstDigit(number)

print("The first digit of {} is {}!".format(number, first_digit))
