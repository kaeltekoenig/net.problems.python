n = 5
m = 6

array = [[z+x*m for z in range(m)] for x in range(n)]

for row in array:
    for col in row:
        print(str(col).rjust(2), end=' ')
    print()