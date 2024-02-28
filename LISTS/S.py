_input = '7 0 4 2 5 9'
my_list = list(map(int, _input.split()))


difference = float('inf')

for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        current_dif = abs(my_list[i] - my_list[j])
        if current_dif < difference:
            difference = current_dif
            number_1_i = i
            number_2_i = j


print(number_1_i, number_2_i)