# 1. Write a program that checks whether a string is a palindrome
country_list_1 = ['Canada', 'USA', 'Canada']  # Inputed list
country_list_2 = country_list_1.copy()  # copy of Inputed list
country_list_2.reverse()
if country_list_2 == country_list_1:
    print('It`s a palindrome')
else:
    print('It`s not a palindrome')
