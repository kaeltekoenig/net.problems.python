n = 5
m = 5

array = []

for i in range(n):
    array.append([0] * m)


array = [0] * n

for i in range(n):
    array[i] = [0] * m

###
array_incorrect = [[0] * n] * m
print(array_incorrect)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# Но все элементы списка (row) - это ссылки на один и тот же список
print(array_incorrect[0] is array_incorrect[1]) 
# True
print()


###
array_gen = [2 ** i for i in range(10)]
print(array_gen)
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

array_gen = [[0 for j in range(m)] for i in range(n)]
print(array_gen)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]