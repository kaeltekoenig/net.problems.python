def average(A):
    return sum(A) / len(A)

print(average(list(map(float, input().split()))))