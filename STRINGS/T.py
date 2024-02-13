decimal_signs = int(input())
total = int(input())

# for i in range(total):
#     number = float(input())
#     print(f'{number:.{decimal_signs}f}')

list_numbers = []
for i in range(total):
    number = float(input())
    list_numbers.append(number)

for elem in list_numbers:
    print(f'{elem:.{decimal_signs}f}')