a = int(input())
b = int(input())
c = int(input())

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(x1, x2)
elif discr == 0:
    x = -(b/(2 * a))
    print(x)
else:
    print()