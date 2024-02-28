_input = '6 1 9 2 3 4 8'
my_list = list(map(int, _input.split()))


number = float('inf')

for i in range(len(my_list)):
    more = 0
    less = 0
    for j in range(len(my_list)):
        if my_list[i] > my_list[j]:
            more += 1
        elif my_list[i] < my_list[j]:
            less += 1
        if abs(more - less) == 0:
            number = my_list[i]
        

print(number)
