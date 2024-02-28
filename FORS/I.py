n = int(input())
result = 0
output = ''

for num in range(1, n):
    result += num * (num + 1)
    output += str(num) + '*'
    output += str(num + 1) + '+'


print(output.strip('+') + f'={result}')