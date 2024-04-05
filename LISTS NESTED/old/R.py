n = 8
m = 8

array = [[ 
    int(x < z and (x + 1 + z < n)) +
    int(x < z and (x + 1 + z > n)) * 2 +
    int(x > z and (x + 1 + z > n)) * 3 +
    int(x > z and (x + 1 + z < n)) * 4
    for z in range(m)] 
    for x in range(n)]


for row in array:
    for col in row:
        print(col, end=' ')
    print()