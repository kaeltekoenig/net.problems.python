n = int(input())
output = ''

for num in range(1, n+1):
    exp = num ** num
    while num != exp:
        exp //= num
        output += str(num) + ' '
    output += str(num) + ' '

print(output[:n*2]) # умножаем на 2, т.к. считаем пробелы
