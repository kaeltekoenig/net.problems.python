# ПЕРЕСТАВИТЬ СОСЕДНИЕ [СРЕЗЫ]
array = list(map(int, input().split()))
array[:-1:2], array[1:-1:2] = array[1::2], array[:-1:2]
print(' '.join(map(str, array)))
# в срез [1, 2, 3, 4] через 1 по четным индексам, т.е. [1, 3] заменить на [2, 4] и наоборот