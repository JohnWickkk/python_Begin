"""
Implement your own implementation of function max__
Implement your own min function__
"""

numbers = []


def _min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum, maximum


for i in range(3):
    try:
        number = float(input("Enter a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid symbol.")

# Find the minimum and maximum values
min_value, max_value = _min_max(numbers)

# Display the results
print(f"The minimum number is: {min_value}")
print(f"The maximum number is: {max_value}")
"""
Implement your own implementation of function max__
Implement your own min function__
"""

numbers = []


def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum, maximum


for i in range(3):
    try:
        number = float(input("Enter a number: "))
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid symbol.")

# Find the minimum and maximum values
min_value, max_value = find_min_max(numbers)

# Display the results
print(f"The minimum number is: {min_value}")
print(f"The maximum number is: {max_value}")
