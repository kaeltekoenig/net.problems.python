# Ищем имеющейся элемент
watermelon_masses = [2, 5, 1, 7, 8, 4, 3]
key = 4

i = 0
while watermelon_masses[i] != key:
    i += 1

print(i)    # Индекс от элемента со значением "4": 5


# Ищем элемент, которого не окажется в списке и получим:
# IndexError: list index out of range
key = 9
i = 0
while watermelon_masses[i] != key:
    i += 1
    if i == len(watermelon_masses):     # ЭТИ СТРОКИ ДОБАВЛЕНЫ,
        break                           # ЧТОБЫ ИЗБЕЖАТЬ ОШИБКИ


# ВАЖНАЯ ЗАВИСИМОСТЬ УСЛОВИЙ: ЕСЛИ ЛЕВОЕ ВЫРАЖЕНИЕ ЛОЖЬ, ПРАВОЕ НЕ ПРОВЕРЯЕТСЯ
key = 9
i = 0
while i < len(watermelon_masses) and watermelon_masses[i] != key:
    i += 1
if i < len(watermelon_masses):
    print('YES')
else:
    print('NO')
# ОШИБКА ИЗ-ЗА ТОГО, ЧТО ПОСЛЕДНЯЯ ИТЕРАЦИЯ WHILE УВЕЛИЧИЛАСЬ НА LEN(LIST)+1 И ВЫШЛА ЗА ДИАПАЗОН
# if watermelon_masses[i] == key:
#     print('YES')
    # IndexError: list index out of range



# В ЭТОМ СЛУЧАЕ PYTHON ИДЕТ ПОСЛЕДОВАТЕЛЬНО: ОН ВЫДАЕТ ОШИБКУ 
# IndexError: list index out of range ВО ВРЕМЯ ЧТЕНИЯ watermelon_masses[i] != key,
# А ДО ВТОРОГО ВЫРАЖЕНИЯ ПРОСТО НЕ ДОШЕЛ!

# while watermelon_masses[i] != key and i < len(watermelon_masses):
    # i += 1
print()


# Способ избежать выхода: еще один
key = 22
watermelon_masses.append(key)
i = 0

while watermelon_masses[i] != key:
    i += 1

print(i)
watermelon_masses.pop()
