""" Задача 4: Написати програму, яка знайде мінімальне значення у списку.
Список задати у самій програмі у вигляді: elements = [1, 5, 68, 0]
У ньому може бути скільки завгодно елементів"""

elements = [-100, 1, 5, 68, 0]
start_element = elements[0]
n = 1
while n < len(elements):
  if elements[n] < start_element:
    start_element = elements[n]
  n = n + 1

# Виведення найменшого елемента
print(f"Найменший елемент: {start_element}")
