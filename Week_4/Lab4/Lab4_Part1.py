"""
Write a program that uses a loop to compute and print the sum of all even numbers between 2 and 100 (inclusive).
"""

x = 0
sum_of_even = 0

while x <= 98:
    x += 2
    sum_of_even += x
    print("The current sum of evens is: ", sum_of_even)

print("The final sum of evens is: ", sum_of_even)
