def is_point_in_area(x, y, x0=-1, y0=1, r=2):
    upper = y - 2 * x >= 2 and x + y >= 0 and r >= ((x0 - x) ** 2 + (y0 - y) ** 2) ** 0.5
    lower = y - 2 * x <= 2 and x + y <= 0 and r <= ((x0 - x) ** 2 + (y0 - y) ** 2) ** 0.5
    return upper or lower


x = float(input())
y = float(input())

if is_point_in_area(x, y):
    print('YES')
else:
    print('NO')