# Задача 2. Написати програму, яка візьме string і в кожному слові замінить першу літеру на велику.
# string ввести з клавіатури
# Приклад: "This is some test STRING"
# Відповідь: "This Is Some Test String"

print('введіть якусь фразу')
Your_string = str(input())  # отримали "вхідну послідовність"
Your_string_new = Your_string.capitalize()
print('Ваша фраза з заголовними буквами тоді виглядаэ так -->', Your_string_new)