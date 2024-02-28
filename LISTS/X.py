# ЧИСЛА K-БОНАЧЧИ [ЦИКЛЫ]
k, n = map(int, input().split())
sequence = [1]*k

for j in range(n-2):
    starting_list = sequence.copy()
    for i in range(n-1):
        sequence[i] = sequence[i+1]
    sequence[-1] = sum(starting_list)


print(sequence[-1])