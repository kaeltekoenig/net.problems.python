n = 5
m = 6

array = [[x for x in range(m)] for z in range(n)]


for row in array:
    for col in row:
        print(col, end=' ')
    print()
