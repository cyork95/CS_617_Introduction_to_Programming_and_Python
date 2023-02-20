"""
Hot Dog Calculator

Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates
the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum
 amount of leftovers. The program should ask the user for the number of people attending the cookout and the
 number of hot dogs each person will be given. The program should display the following details:

The minimum number of packages of hot dogs required
The minimum number of packages of hot dog buns required
The number of hot dogs that will be left over
The number of hot dog buns that will be left over

"""
import math

number_of_people = int(input("Enter the number of people attending: "))
number_of_hotdogs = int(input("Enter the number of hot dogs each person will be given: "))

number_of_hotdogs_needed = number_of_people * number_of_hotdogs
number_of_buns_needed = number_of_hotdogs_needed
number_of_hotdog_packages = math.ceil(number_of_hotdogs_needed / 10)
number_of_bun_packages = math.ceil(number_of_people * number_of_hotdogs / 8)
leftover_hotdogs = (number_of_hotdog_packages * 10) - number_of_hotdogs_needed
leftover_buns =  (number_of_bun_packages * 8) - number_of_buns_needed

print("The minimum number of hotdog packages needed is: ", number_of_hotdog_packages)
print("The minimum number of hotdog bun packages needed is: ", number_of_bun_packages)
print("The number of leftover hotdogs will be: ", leftover_hotdogs)
print("The number of leftover buns will be: ", leftover_buns)

