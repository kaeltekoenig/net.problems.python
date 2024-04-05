def triangle(n):
    for i in range(1, n * 2 + 1, 2):
        strn = '*' * i
        print(strn.center(n * 2, ' '))


triangle(7)