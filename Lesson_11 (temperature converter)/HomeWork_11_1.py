"""
Convert Celsiy to Farengate: Т (° F) = Т (° C) × 9/5 + 32
Convert Farengate to Celsiy: Т (° C) = ( Т (° F) - 32) × 5/9
"""

temp_value = int(input('enter temperature value '))
temp_measure = str(input('enter a measure of temperature C or F'))


def temp_converter(temp_value:int,  temp_measure: str):
    """
    :param temp_value: some int value
    :type temp_measure: object is a C or F
    """
    if temp_measure == 'C':
        return (temp_value * 9/5) + 32
    elif temp_measure == 'F':
        return round(temp_value - 32) * 5/9
    else:
        raise ValueError('wrong parameters. Try again')


# if temp_measure != 0:
#     result = temp_converter(temp_value, temp_measure)
# print('Result convert' is {temp_value}, 'in another measure is', {result})

if temp_converter(temp_value, temp_measure) is not None:
    result = temp_converter(temp_value, temp_measure)
    print(f'Result of converting: {temp_value} degrees {temp_measure.upper()} is equivalent {result} ')
