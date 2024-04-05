n = 5
m = 6

array = [[z // 2 + 1 if (x + z) % 2 == 0 else 0 for z in range(x * m, x * m + m)]
    for x in range(n)]


for row in array:
    for col in row:
        print(str(col).rjust(2), end=' ')
    print()


