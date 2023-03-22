"""
Write list functions that carry out the following tasks for a list of integers.

Swap the first and last elements in the list.
Shift all elements by one to the right and move the last element into the first position.
For example, 1 4 9 16 25 would be transformed into 25 1 4 9 16.
Replace all even elements with 0.
Remove the middle element if the list length is odd, or the middle two elements if the length is even.
Return the second-largest element in the list.
Return true if the list contains two adjacent duplicate elements.
Return true if the list contains duplicate elements (which need not be adjacent).
"""

import math


def swap_elements(orig_list, list_copy):
    # Swap the first and last elements
    orig_list[0] = list_copy[-1]
    orig_list[-1] = list_copy[0]
    return orig_list


def shift_elements(orig_list, list_copy):
    for element in range(len(orig_list) - 1):
        orig_list[element + 1] = list_copy[element]
    orig_list[0] = list_copy[0]
    orig_list[1] = list_copy[-1]
    return orig_list


def replace_even(orig_list):
    for element in range(len(orig_list)):
        if orig_list[element] % 2 == 0:
            orig_list[element] = 0
    return orig_list


def remove_middle(orig_list):
    if len(orig_list) % 2 == 0:
        first_index = math.floor(len(orig_list) / 2)
        second_index = math.floor((len(orig_list) / 2) + 1)
        orig_list.remove(orig_list[first_index])
        orig_list.remove(orig_list[second_index])
    else:
        first_index = math.floor(len(orig_list) / 2)
        orig_list.remove(orig_list[first_index])
    return orig_list


def remove_second_largest(orig_list):
    orig_list.sort()
    return orig_list[-2]


def detect_adjacent_duplicate(orig_list):
    for i in range(len(orig_list) - 1):
        if orig_list[i] == orig_list[i + 1]:
            return True
        i += 1
    return False


def detect_duplicates(orig_list):
    for i in range(len(orig_list) - 1):
        possible_dupe = orig_list[i]
        j = i + 1
        while j < len(orig_list) - 1:
            if orig_list[j] == orig_list[i]:
                return True
            j += 1
        i += 1
    return False


print("For example list: ")
list_example = [1, 4, 9, 16, 25]
list_example_copy = list_example.copy()

# Swap the first and last elements
print('Swapped first and last places: ', swap_elements(list_example, list_example_copy))

# Shift all elements to the right by 1
print('Shifted list: ', shift_elements(list_example, list_example_copy))

# Replace all even elements with 0

print('Replaced even: ', replace_even(list_example))

# Remove middle elements
print('Removed middle number(s): ', remove_middle(list_example))

# Remove second largest element

print('Second largest number: ', remove_second_largest(list_example))

# Return True for two adjacent duplicate elements

print("Are there adjacent duplicates? ", detect_adjacent_duplicate(list_example))

# Return True for two duplicate elements (not adjacent)

print("Are there duplicates? ", detect_duplicates(list_example))
