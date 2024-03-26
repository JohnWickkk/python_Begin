# Task 2. Write a program that will find the first non-consecutive number in the list
# Specify the list in the program itself in the form: list = [1, 5, 68, 0]
# It can contain any number of elements
# For example, given a list [1,2,3,4,6,7,8]
# The answer will be the number 6. If the list is consecutive, display the corresponding message

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 24]
for i in range(len(numbers) - 1):  # calculate the condition: difference between 2 near numbers as len
    if numbers[i + 1] - numbers[i] > 1:  # comparing a two range items
        print("Непослідовне значення в списку:", numbers[i + 1])
