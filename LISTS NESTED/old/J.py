n = 5
m = 5

array = [[(x + z + 1) % 2 for z in range(m)] for x in range(n)]

for row in array:
    for col in row:
        print(str(col), end=' ')
    print()