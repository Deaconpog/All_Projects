def do_something(num):
    difference = 8 - num
    num = num * difference
    return num


def do_something_else(num_c, num_a):
    num1 = num_c * 2
    num2 = do_something(num_a)
    return num1 + num2


a = 5
b = 4
c = -3

print(do_something(b))
print(do_something_else(c, a))
