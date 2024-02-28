_input = '3 2 1 2 3'
my_list = list(map(int, _input.split()))

total = 0

for elem in my_list:
    if my_list.count(elem) == 1:
        total += 1

print(elem)