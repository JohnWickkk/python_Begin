# Задача 1. Написати програму, в якій необхідно видалити всі вказані літери з стрінги(string)
# Стрінгу(string) і літеру ввести з клавіатури
print('введіть якусь нерозривну послідовність літер')
Your_string = str(input())  # отримали "вхідна послідовність"
print('введіть літери яку треба прибрати з послідовності')
For_delete = str(input())  # отримали "зайве"
My_String = Your_string.replace(For_delete,"") #буквально: у "вхідна послідовність" замінити "зайве" на нічого
if My_String == Your_string:
    print('Схоже таких літер немає в вашій послідовності')
else:
    print('Ваша очищена стрінга виходить -->','`',My_String,'`')


#Задача 2. Написати програму, яка візьме string і в кожному слові замінить першу літеру на велику.
#string ввести з клавіатури
#Приклад: "This is some test STRING"
#Відповідь: "This Is Some Test String"

#Задача 3. Напишіть програму яка перевертає стрінгу

#Задача 4. Напишіть програму яка приймає на вхід 2 стрінги та порівнює їх

#Задача 5.Напишіть програму яка візьме стрінг та повторить її задану кількість раз. До прикладу#Задача 5.
#Напишіть програму яка візьме стрінг та повторить її задану кількість раз.
#До прикладу ми маємо стрінгу 'abc' та число 3.
#Результатом роботи програми має бути "abcabcabc" ми маємо стрінгу 'abc' та число 3. Результатом роботи програми має бути "abcabcabc"

#Задача 6. Написати програму для підрахунку конвертації валюти: UAH --> USD
#доларів США --> грн
#UAH --> EURLine too long (179 > 88)#Задача 5.
#Напишіть програму яка візьме стрінг та повторить її задану кількість раз.
#До прикладу ми маємо стрінгу 'abc' та число 3.
#Результатом роботи програми має бути "abcabcabc"
#євро --> грн