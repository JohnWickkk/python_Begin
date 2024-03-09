# 1_задача: Порахувати площу прямокутного трикутника
k1 = 3.5
k2 = 4.2
s = round(1 / 2 * k1 * k2, 2)
print(s)

# 2_задача: n школярів ділять k яблук порівну, залишок, що не ділиться, залишається в кошику
n = 5  # Q-ty of guys#
k = 13  # Q-ty of an apple#

a_1 = k // n  # Integer division (for everyone "variant_1")
print(a_1)

# Another way
a_2 = k % n  # surplus from division
# print(a_2)
a_3 = (k - (a_2)) / n  # (for everyone "variant_2")
print(a_3)


# 3.Написати програму, яка виводить попереднє та наступне число від заданого
# Наприклад: задане число 567, наступне буде 568, попереднє 565
n = 567
Np = n - 2  # previous number
Nn = n + 1  # next number
print('If your number', n, 'previous number', '=', Np)
print('If your number', n, 'next number', '=', Nn)