n = 5
m = 6

array = [[x*m + z for z in range(m-1, -1, -1)] for x in range(n-1, -1, -1)]

for row in array:
    for col in row:
        print(str(col).rjust(2), end=' ')
    print()