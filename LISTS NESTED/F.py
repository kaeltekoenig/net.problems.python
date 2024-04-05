n = 5
m = 6

array = [[x + z for z in range(0, m*5, 5)] for x in range(n-1, -1, -1)]

for row in array:
    for col in row:
        print(col, end=' ')
    print()