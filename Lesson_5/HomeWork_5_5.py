# Create any list and check if it is sorted correctly
List_to_check = ['only', 'aplle', '2', ' ', 'enjoy']
List_to_check.sort()
# print(List_to_check)
List_to_check =','.join(List_to_check)
# print(List_to_check)
if List_to_check == ' ' ',2,aplle,enjoy,only':
    print('it`s the same')
else:
    print('it`s not')