# Task 6. Write a program to convert currencies:
# UAH --> USD
# USD --> UAH
# UAH --> euro
# euro --> UAH

USD_rate = float(38.50)
euro_rate = float(42.00)
UAH_rate = float(1.00)
print('What currency do you have: USD, UAH, EURO')
Income_currency = (input())  # getting current currency
print('What currency do you WANT to HAVE: USD, UAH, EURO')
Outcome_currency = (input())  # getting wanted currency
print('What q-ty of', {Income_currency}, 'do you have?')
Income_amount = (float(input()))  # getting income amount

if Income_currency == 'UAH' and Outcome_currency == 'USD':
    Outcome_amount = float(Income_amount / USD_rate)
elif Income_currency == 'UAH' and Outcome_currency == 'euro':
    Outcome_amount = float(Income_amount / euro_rate)
elif Income_currency == 'UAH' and Outcome_currency == 'UAH':
    Outcome_amount = float(Income_amount / UAH_rate)
print('Amount of', Outcome_currency, 'after converting is', Outcome_amount)
