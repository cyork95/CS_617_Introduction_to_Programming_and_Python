"""
Write a program that generates a sequence of 20 random values between 0 and 99, stores them in a list,
prints the sequence, sorts it, and prints the sorted sequence.
"""

import random

random_list = [random.randrange(0, 100) for i in range(20)]

print('Here is the random list: ', random_list)

random_list.sort()

print('Here is the sorted list: ', random_list)
