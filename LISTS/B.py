# ЧЕТНЫЕ ЭЛЕМЕНТЫ [ЦИКЛЫ]
my_list = list(map(int, input().split()))

for elem in my_list:
    if elem % 2 == 0:
        print(elem, end=' ')