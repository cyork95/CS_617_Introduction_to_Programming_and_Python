"""
Write a program that uses a loop to compute and print the sum of all odd numbers between a and b (inclusive),
where a and b are entered by the user.
"""

a = int(input("Enter a number for the start the loop: "))
b = int(input("Enter a number for the end of the loop: "))

start = a
sum_of_odd = 0

if a % 2 != 0:
    while a <= b:
        sum_of_odd += a
        print("The current sum of odds is: ", sum_of_odd)
        a += 2
else:
    a += 1
    while a <= b:
        sum_of_odd += a
        print("The current sum of odds is: ", sum_of_odd)
        a += 2
print("The final sum of odds between ", start, " and", b, " is: ", sum_of_odd)
