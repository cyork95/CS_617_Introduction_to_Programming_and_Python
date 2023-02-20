"""
Treadmill Calorie Burn Calculator

Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the
number of calories burned after 10, 15, 20, 25, and 30 minutes.
"""

calories_per_minute = 4.2

starting_minute = 10
end_minute = 30

while starting_minute <= end_minute:
    burnt_calories = starting_minute * calories_per_minute
    print("You will burn ", burnt_calories, " calories in ", starting_minute, " minutes.")
    starting_minute += 5
