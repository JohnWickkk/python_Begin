print('Hello World')

print('введіть число')
x = int(input())
print('виберіть дію надрукувавши: plus, minus, add, sub')
act = input()
print('введіть друге число')
y = int(input())
if act == 'plus':
    result = x + y
    print('Результат обчислень', 'дорівнює', result)
elif act == 'minus':
    result = x - y
    print('Результат обчислень', 'дорівнює', result)
elif act == 'add':
    result = x * y
    print('Результат обчислень', 'дорівнює', result)
elif act == 'sub':
    result = x // y
    print('Результат обчислень', 'дорівнює', result)
