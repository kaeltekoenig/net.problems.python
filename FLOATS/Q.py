n = int(input())
x = float(input())
sum_ = 0

exp = x
fact = 1
total = 1 + x

for i in range(2, n+2):
    exp *= x
    fact *= i
    # print(f'x в степени = {exp}')
    # print(f'факториал: {fact}')
    sum_ += exp / fact


total += sum_
print(total)
