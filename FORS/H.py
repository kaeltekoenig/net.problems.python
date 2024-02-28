n = int(input())

result = ''
sum_ = 0
for i in range(1, n + 1):
    result += '+' + str(i)
    sum_ += i

print(result.strip('+') + f'={sum_}')
