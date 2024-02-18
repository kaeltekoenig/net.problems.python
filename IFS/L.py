x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x2 + y2) - abs(x1 + y1) <= 2:
    print('YES')
else:
    print('NO')