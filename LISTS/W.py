# _input = '1 2 2 3 3 3'
# my_list = list(map(int, _input.split()))

my_list = list(map(int, input().split()))
maximum = 0

for elem in my_list:
    if my_list.count(elem) > maximum:
        maximum = my_list.count(elem)
        key = elem

print(elem, end=' ')