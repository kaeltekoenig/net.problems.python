# ПЕРЕСТАВИТЬ В ОБРАТНОМ ПОРЯДКЕ [ЦИКЛЫ]
array = list(map(int, input().split()))

for i in range(len(array)//2):
    array[i], array[i *-1 -1] = array[i *-1 -1], array[i]

print(' '.join(map(str, array)))

