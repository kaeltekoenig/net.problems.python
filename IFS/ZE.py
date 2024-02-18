x = int(input())
y = int(input())
z = int(input())

max_ = max(x, y, z)
min_ = min(x, y, z)
mid_ = x + y + z - max_ - min_



if (max_ / mid_ == 1.5 and mid_ / min_ == 2 and max_ / min_ == 3) or (
    x == y == z) and (x + y + z == 6):
    print('YES')
else:
    print('NO')