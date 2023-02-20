"""
A year with 366 days is called a leap year. Usually years that are divisible by 4 are leap years (2024).
However, years that are divisible by 100 (1800) are not leap years, but years that are divisible by 400 are
leap years (2000). Write a function IsLeapYear(year) to determine if year is a leap year. Use if statements,
boolean operators, and the return statement.
"""


def IsLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year to check if leap year: "))

is_leap_year = IsLeapYear(year)

if is_leap_year:
    print("Yes it is a lead year!")
else:
    print("No it is not a leap year!")
