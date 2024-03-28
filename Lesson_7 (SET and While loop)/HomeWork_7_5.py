"""Задача 5. Написати програму, яка порахує суму всіх елементів у списку
Список задати у самій програмі у вигляді: elements  = [1, 5, 68, 0]
У ньому може бути скільки завгодно елементів"""

elements = [-1000, -11, -111000, 1, 5, 68, 0]
start_element = 0
sum_elements = 0
while start_element < len(elements):
  sum_elements = sum_elements + elements[start_element]
  start_element = start_element + 1

print(f"Сума значень в списку = {sum_elements}")
