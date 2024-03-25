# Task 5. Write a program that takes a string and repeats it a given number of times. /
# For example, we have the string 'abc' and the number 3. The result of the program should be 'abcabcabc'

print('pls input some sequence of symbols')
Your_str_4_5 = str(input())  # getting inputted sequence"
print('input  q-ty of multiple')
multiple = int(input())  # getting multiplier
if isinstance(multiple, str):
    print('Your multiple does`t looks like a number')
else:
    multiple_sequence = Your_str_4_5 * multiple
    print(multiple_sequence)