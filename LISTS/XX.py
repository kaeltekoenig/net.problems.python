# ЧИСЛА K-БОНАЧЧИ [СРЕЗЫ]
k, n = map(int, input().split())
sequence = [1]*k

for i in range(n):
    sequence.append(sum(sequence[i:]))
print(sequence[n])