print('enter the first number')
number_1 = int(input())
print('enter second number')
number_2 = int(input())
print('choose an action: plus,minus,sub,add')
diya = input()

def plus(number_1, number_2):
    return number_1 + number_2

def minus(number_1, number_2):
    return number_1 - number_2

def divide(number_1, number_2):
    if number_2 == 0:
        print("Error: Division by zero")
        return None  # Indicate error or handle appropriately
    else:
        return number_1 / number_2

if diya == 'plus':
    result = plus(number_1, number_2)
elif diya == 'minus':
    result = minus(number_1, number_2)
elif diya == 'add':
    result = plus(number_1, number_2)  # Use the corrected plus function
elif diya == 'divide':
    result = divide(number_1, number_2)

print(f"{number_1} {diya} {number_2} = {result}")
