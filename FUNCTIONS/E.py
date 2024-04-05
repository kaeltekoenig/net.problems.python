def is_point_in_circle(x, y, xc, yc, r):
    return r >= ((xc - x) ** 2 + (yc - y) ** 2) ** 0.5

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())

if is_point_in_circle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')