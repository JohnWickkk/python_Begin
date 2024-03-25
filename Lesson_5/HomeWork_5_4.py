#Ви маєте список [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]], дістаньте з нього значення
#'Win' та переведіть його у новий список. Результат має бути  ['Win']
List_to_sub = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
List_win = List_to_sub[6][3][0]
List_win = list(str(List_win))
print(List_win)
List_str = ''.join(List_win)
print(List_str)
List_win = [List_str]
print(List_win)