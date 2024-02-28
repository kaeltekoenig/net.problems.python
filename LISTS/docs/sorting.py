# СОРТИРОВКА ВЫБОРОМ
A = [5, 2, 12, 23, -9, 8]


for j in range(len(A)):                             #   
    minimal = j                                     # ПРИСВАИВАЕМ ПО ПОРЯДКУ МИНИМАЛЬНЫЙ ИНДЕКС ПО УМОЛЧАНИЮ
    for i in range(j, len(A)):
        if A[i] < A[minimal]:
            minimal = i
            A[j], A[minimal] = A[minimal], A[j]

print(A)