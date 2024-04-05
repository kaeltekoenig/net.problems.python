n = 7
m = 7

array = [[int(x == z or x+1 + z == n) for z in range(m)] for x in range(n)]


for row in array:
    for col in row:
        print(col, end=' ')
    print()