print('enter the number')
num = int(input())


def is_prime():
    if num >= 1000:
        return False
    elif num <= 1:
        return False
    else:
        return True

if is_prime() is True:
    print(f' {num} is a prime number')
else:
    print(f' {num} isn`t a prime number')
