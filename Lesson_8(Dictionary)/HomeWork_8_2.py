def add_params_to_url(initial_str, params):
  if not params:
    return initial_str

  # Створення рядка для параметрів
  params_str = "&".join(f"{key}={value}" for key, value in params.items())

  # Додавання параметрів до URL-адреси
  return f"{initial_str}?{params_str}"

# Використання функції
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_link = add_params_to_url(initial_str, params)

# Виведення результату
print(result_link)