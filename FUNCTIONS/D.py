def is_point_in_rhombus(x, y):
    return abs(x) + abs(y) <= 1

a = float(input())
b = float(input())

if is_point_in_rhombus(a, b):
    print('YES')
else:
    print('NO')