# ЦИКЛИЧЕСКИЙ СДВИГ ВПРАВО [ЦИКЛЫ]. СПОСОБ 1
array = list(map(int, input().split()))
step = 3

for i in range(step):
    begin = array[0]
    for j in range(len(array)-1):
        array[j] = array[j+1]
    array[-1] = begin


print(*array)