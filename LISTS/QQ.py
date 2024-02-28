# # ЦИКЛИЧЕСКИЙ СДВИГ ВПРАВО [СРЕЗЫ]. СПОСОБ 1
# array = list(map(int, input().split()))
# print(' '.join(map(str, array[-1:] + array[:-1])))


# # ЦИКЛИЧЕСКИЙ СДВИГ ВПРАВО [СРЕЗЫ]. СПОСОБ 2
# array = list(map(int, input().split()))
# print(*array[-1:] + array[:-1])


# # ЦИКЛИЧЕСКИЙ СДВИГ ВПРАВО [МЕТОДЫ]. СПОСОБ 3
# array = list(map(int, input().split()))

# for i in range(3):
#     array.insert(0, array.pop())

# print(*array)


# ЦИКЛИЧЕСКИЙ СДВИГ ВПРАВО [ФУНКЦИЯ+МЕТОДЫ]. СПОСОБ 4
def shift_list(lst, step):
    if step < 0:
        for el in range(step):
            lst.append(lst.pop())
    else:
        for el in range(step):
            lst.insert(0, lst.pop())
    return lst


array = list(map(int, input().split()))

print(*shift_list(array, 2))