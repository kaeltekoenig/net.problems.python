# Таблица степеней — 3
# На вход даётся числа d и N. Необходимо вывести таблицу степеней от 1 до d чисел от 0 до N. 
# Числа в таблице должны быть выровнены по правому краю. 
# Ширина каждого столбца должна быть минимальной, но так, чтобы все числа поместились.
d = 4
N = 5

for num in range(N + 1):
    print('|', end='')
    for deg in range(1, d + 1):
        print(f'{num ** deg:>{len(str(N ** deg))}}', end='|')
    print()