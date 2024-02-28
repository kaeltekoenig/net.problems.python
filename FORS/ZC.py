N = int(input())
variations = 0
addendums_same_3 = 0
addendums_same_2 = 0
addendums_same_1 = 0
addendums = 0

# print(f'Список слагаемых: ')
for i in range(0, 10):
    for j in range(0, 10):
        for z in range(0, 10):
            if i + j + z == N:
                # print(f'{i, j, z}')
                addendums += 1
                if i == j == z:
                    addendums_same_3 += 1
                elif i == j or j == z or i == z:
                    addendums_same_2 += 1
                else:
                    addendums_same_1 += 1

# print(f'Всего вариантов со слагаемыми: {addendums}')
# print(f'Все три одинаковые: {addendums_same_3}')
# print(f'Два из трех одинаковые: {addendums_same_2}')
# print(f'Все разные: {addendums_same_1}')



variations = addendums_same_3 + addendums_same_2 * 2 + 6 * addendums_same_1

# print(f'Итого вариаций магического квадрата: {variations}')
print(variations)