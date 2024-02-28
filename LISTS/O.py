# _input = '3 4 5 2 1'
# my_list = list(map(int, _input.split()))

my_list = list(map(int, input().split()))

maximum = my_list.index(max(my_list))
minimum = my_list.index(min(my_list))

my_list[maximum], my_list[minimum] = min(my_list), max(my_list)

print(' '.join(map(str, my_list)))