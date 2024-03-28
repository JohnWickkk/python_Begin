"""Задача 3: Написати програму, яка на вхід приймає список чисел і перевіряє,
#чи всі числа в цій послідовності є унікальними"""

incoming_list = (1, 2, 3, 5, 55, 8, 13, 21, 34, 89)  # list 1
uniq_incoming_list_1 = set(incoming_list)  # set 1
uniq_incoming_list_2 = list(uniq_incoming_list_1)
if len(uniq_incoming_list_2) < len(incoming_list):
    print('looks like your:', incoming_list, 'isn`t unique')
else:
    print('your incoming list:', incoming_list, 'is unique')

