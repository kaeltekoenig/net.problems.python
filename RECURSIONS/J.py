def product(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[len(a) - 1] * product(a[:-1])


print(product(list(map(int, input().split()))))