"""
At one college, the tuition for a full-time student is $8,000 per semester.
It has been announced that the tuition will increase by 3 percent each year for the next 5 years.
Write a program with a loop that displays the projected semester tuition amount for each of the next 5 years.
"""

tuition = 8000

x = 0

while x < 5:
    tuition += tuition * 0.03
    print("The projected tuition for year", x + 1, "is $", round(tuition, 2))
    x += 1