# Задача 4. Напишіть програму яка приймає на вхід 2 стрінги та порівнює їх
print('введіть якусь послідовність символів')
Your_string_1 = str(input())  # отримали "вхідну послідовність_1"
print('введіть ще якусь послідовність символів')
Your_string_2 = str(input())  # отримали "вхідну послідовність_2"
if Your_string_1 == Your_string_2:
    print('Схоже ващі рядки ідентичні')
else:
    print('Ваші рядки відрізняються')
