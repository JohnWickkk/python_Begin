def add_params_to_url(initial_str, params):
  if not params:
    return initial_str

  params_str = "&".join(f"{key}={value}" for key, value in params.items())

  return f"{initial_str}?{params_str}"

# using function
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_link = add_params_to_url(initial_str, params)

print(result_link)