# НАИМЕНЬШИЙ ПОЛОЖИТЕЛЬНЫЙ [ЦИКЛЫ]
my_list = list(map(int, input().split()))

minimal = 1001

for elem in my_list:
    if elem < minimal and elem > 0:
        minimal = elem

print(minimal)
