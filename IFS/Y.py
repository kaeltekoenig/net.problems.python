a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())


# Больший ноутбук - первый
if a1 * b1 < a2 * b2:
    a1, b1, a2, b2 = a2, b2, a1, b1


if a2 > b2:
    a2, b2 = b2, a2

if a1 * b1 == a2 * b2:
    if (a1 + a2) * b1 > (b1 + a2) * a1:
        print(a1 + a2, b1)
    else:
        print(a1, b1 + a2)
else:
    if (b1 + a2) * a1 < (b1 + b2) * a1:
        print(a1, b1 + a2)
    else:
        print(a1, b1 + b2)