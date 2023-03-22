"""
Write a program that reads numbers and adds them to a list if they aren’t already contained in the list.
When the list contains ten numbers, the program displays the contents and quits.
"""

i = 0
number_list = []

while i < 10:
    number = float(input("Enter a number to add to the list in spot {}: ".format(i + 1)))
    if number not in number_list:
        number_list.append(number)
    else:
        continue
    i += 1

print("Your number list is: ", number_list)