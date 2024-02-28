_input = '1 2 2 3 3 3'
my_list = list(map(int, _input.split()))

for elem in my_list:
    if my_list.count(elem) == 1:
        print(elem, end=' ')