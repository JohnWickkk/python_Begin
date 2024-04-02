"""task 2: You have 2 lists, write a program that outputs all elements of the/
 first that are not in the second.
outputs all elements of the first that are not in the second."""

first_list = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
second_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
first_set = set(first_list)
second_set = set(second_list)
tr = first_set.difference(second_set)
print(sorted(tr))
