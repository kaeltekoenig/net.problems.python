# _input = '1 1 1 1 1'
# my_list = list(map(int, _input.split()))

my_list = list(map(int, input().split()))
pairs = 0

for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] == my_list[j]:
            pairs += 1

print(pairs)