"""
Write a function def merge(a, b) that merges two lists, alternating elements from both lists.
If one list is shorter than the other, then alternate as long as you can and then append the remaining elements from
 the longer list. For example, if a is 1 4 9 16 and if b is 2 7 5 8 20 17 then merge returns a new list containing the
  values 1 2 4 7 9 5 16 8 20 17.
"""

merged_list = []


def merge(a, b):
    i = 0
    while i < len(a) and i < len(b):
        merged_list.append(a[i])
        merged_list.append(b[i])
        i += 1
    if len(a) > len(b):
        while i < len(a):
            merged_list.append(a[i])
            i += 1
    elif len(a) < len(b):
        while i < len(b):
            merged_list.append(b[i])
            i += 1
    return merged_list


merged_list = merge([1, 4, 9, 6], [2, 7, 5, 8, 20, 17])

print(merged_list)
