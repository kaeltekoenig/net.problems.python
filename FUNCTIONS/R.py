def triangle(n, spaces):
    for i in range(1, n * 2 + 1, 2):
        strn = '*' * i
        print(strn.center(spaces * 2, ' '))


def fir(a, b):
    for i in range(a, b + 1):
        triangle(i, b)


fir(2, 4)