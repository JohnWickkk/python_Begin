"""
Implement your own implementation of function max__
Implement your own min function__
"""


def calc_minimum(*args):
    my_minimum = float()
    for i in args:
        if i < my_minimum:
            my_minimum = i
    return my_minimum


def calc_maximum(*args):
    my_maximum = float()
    for i in args:
        if i > my_maximum:
            my_maximum = i
    return my_maximum


"""
For Testing
"""
my_list = [1, 2, -10, 33, 55, -55, 1000, -100000]
minimum = calc_minimum(*my_list)
print(f"Minimum value in the {my_list}: is  {minimum}")
maximum = calc_maximum(*my_list)
print(f"Maximum value in the {my_list}: is {maximum}")