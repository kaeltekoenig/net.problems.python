def is_point_in_square(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


a = float(input())
b = float(input())

if is_point_in_square(a, b):
    print('YES')
else:
    print('NO')
