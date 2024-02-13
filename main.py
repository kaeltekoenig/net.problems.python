# Диапазон: [a; b)
word = 'Синхрофазотрон'

print(
    f'Все слово: {word[0:len(word)]}\n'
    f'Также все слово: {word[:]}\n'
    f'Без первой буквы: {word[1:]}\n'
    f'Без последней буквы: {word[:-1]}\n'
    f'Без первой и последней буквы: {word[1:-1]}\n'
    f'Без первой и последней буквы: {word[1:-1]}\n'
    f'Оставить только буквы с четным индексом: {word[::2]}\n'
    f'Оставить только буквы с нечетным индексом: {word[1::2]}\n'
    f'В обратном порядке: {word[::-1]}\n'
    f'В обратном порядке через один: {word[::-2]}\n'
    )

changed = word.replace('о', 'о'.upper())
print('Измененное слово с помощью .replace:', changed)



text = 'In the hole in the ground there lived a hobbit'
print()


def find_th_word(strn, wrd_num=1):
    if wrd_num == 0:
        return strn[:strn.find(' ')]
    else:
        rest = strn[strn.find(' ') + 1:]
        return find_th_word(rest, wrd_num-1)

print(find_th_word(text, 4))

def remove_th_word(strn = str, wrd_num=1):
    return strn[:strn.find(find_th_word(strn, wrd_num))] + strn[strn.find(find_th_word(strn, wrd_num)) + 1:]

print(remove_th_word(text, 5))


number = list(map(int, input().zfill(6)))
a = number[:len(number) // 2]
b = number[len(number) // 2:]
if sum(a) == sum(b):
    print('YES')
else:
    print('NO')