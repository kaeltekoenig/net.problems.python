# ПЕРЕСТАВИТЬ СОСЕДНИЕ [ЦИКЛЫ]
my_list = list(map(int, input().split()))

for index in range(0, len(my_list), 2):
    if index != len(my_list) - 1:
        my_list[index], my_list[index+1] = my_list[index+1], my_list[index]

print(' '.join(map(str, my_list)))