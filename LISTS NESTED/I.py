n = 5
m = 5

array = [[min(x, z) for z in range(m)] for x in range(n-1, -1, -1)]

for row in array:
    for col in row:
        print(str(col), end=' ')
    print()