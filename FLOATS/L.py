a = int(input())
b = int(input())
c = int(input())

discr = b ** 2 - 4 * a * c

if a == b == c == 0:
    print(3)
elif discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
    print(2, x1, x2)
elif discr == 0:
    x = -(b/(2 * a))
    print(1, x)
else:
    print(0)