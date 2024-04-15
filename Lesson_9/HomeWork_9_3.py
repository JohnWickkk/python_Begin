course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
asking_key = input("Введіть значення ключа")
try:
  value = course[asking_key]
except KeyError:
  # Виведення повідомлення про помилку
  print(f" Errors '{asking_key}' doetn`t exist")
else:
  print(f" For your '{asking_key}' key value is - {value}")