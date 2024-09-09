#my_tuple = (1, 2, 3)
#my_tuple_2 = (4, 5, 6)
#r = my_tuple_2 + my_tuple
#print(r)

a = 10


def mydef(x, a=-5):
    x = x ** 2
    a -= 2
    return x + a
    z = mydef(4)


print(a)

a = 10
b = 2
if a < b:
    print (1)
if b > a:
    print(2)
else:
    print(3)

name = "snow storm"
print("%s" % name[6:8])