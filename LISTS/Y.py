# КУЗНЕЧИКИ [ЦИКЛЫ]
my_list = list(map(int, input().split()))
t = int(input())

for i in range(t):
    my_list[len(my_list)-1-my_list[-1]], my_list[-1] = my_list[-1], my_list[len(my_list)-1-my_list[-1]]
    for j in range(abs(len(my_list)-1-my_list[-1])):
        my_list[-1-j], my_list[-2-j] = my_list[-2-j], my_list[-1-j]

print(' '.join(map(str, my_list)))

