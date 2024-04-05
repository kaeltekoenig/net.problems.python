n = 5
m = 6

array = [[int(x != z) + int(x > z) for z in range(m)] for x in range(n)]


for row in array:
    for col in row:
        print(col, end=' ')
    print()