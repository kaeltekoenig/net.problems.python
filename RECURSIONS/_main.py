def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


def powerx(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * power(a, n - 1)
    else:
        return powerx(a, n // 2) ** 2


def hanoimove(n, start, finish):
    '''
    n - количество дисков
    start - стержень, откуда переложить
    finish - стержень, куда переложить
    '''
    if n == 1:
        print('1:', start, finish)
    else:
        tmp = 6 - start - finish
        hanoimove(n-1, start, tmp)
        print(f'{n}:', start, finish)
        hanoimove(n-1, tmp, finish)


hanoimove(2, 1, 3)