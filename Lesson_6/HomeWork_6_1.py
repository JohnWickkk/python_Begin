# Task 1. Write a program that outputs all numbers from the list that are divisible by a given number
# num. should be inputed from the keyboard
print('введіть числівник')
den = int(input())  # getting denominator
print('введіть кінець послідовності')
sequence = int(input())  # getting param. for sequence of numbers

for sequence_1 in range(1, sequence):  # bild a conditions and make a correct sequence from second element
    if sequence_1 % den == 0:  # conditions of verification
        print(sequence_1)
