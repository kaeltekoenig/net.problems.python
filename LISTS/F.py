# НАИБОЛЬШИЙ ЭЛЕМЕНТ [ЦИКЛЫ]
my_list = list(map(int, input().split()))

maximum = float('-inf')

for i, v in enumerate(my_list):
    if v > maximum:
        maximum = v
        index = i

print(maximum, index)