n = 5
m = 5

array = [[max(x, z) for z in range(m)] for x in range(n)]
# array = [[x]*x + list(range(x, m)) for x in range(n)]

for row in array:
    for col in row:
        print(col, end=' ')
    print()