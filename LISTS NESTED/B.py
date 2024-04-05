n = 5
m = 6
array = []

for i in range(n):
    array.append([i] * m)

for row in array:
    print(' '.join(map(str, row)))
