n = int(input())
x = float(input())

total = 1
exp = 1

for i in range(1, n+1):
    exp *= x
    total += exp

print(total)