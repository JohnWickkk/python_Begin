#Ви маєте список ['Tst', 'aBc', 'TEST', 'Hello', 'neW'],
# відсортуйте його, але врахуйте що слова в списку можуть  починатися з великої або малої літери

List_from_Mary = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
List_to_sort = List_from_Mary.copy()
print(type(List_to_sort))
Sorted_List = sorted(List_to_sort, key=str.lower) #I find`ed it on Geminy and not sure thats a correct way
print(Sorted_List)

