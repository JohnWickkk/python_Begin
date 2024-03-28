"""
Task 1: There are 2 lists: # needed to turn a list,\
# which consists of unique elements, general for these two lists.
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""

first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tr = first_list + second_list
f_s_set = set(first_list + second_list)
print(sorted(f_s_set))