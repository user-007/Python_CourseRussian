'''
print(), type(), id(), len()....
'''


def print_hi(name):
    print(f'Hi, {name}')

    if __name__ == '__main__':
        print_hi('PyCharm')


def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


print(my_fn(5, 4))
