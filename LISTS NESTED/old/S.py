n = 5
m = 6

array = [
    [z + x * m for z in range(m) if x % 2 == 0] + [z + x * m for z in range(m-1, -1, -1) if x % 2 != 0]
    for x in range(n)]


for row in array:
    for col in row:
        print(str(col).rjust(2), end=' ')
    print()


