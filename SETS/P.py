# СОРТИРОВКА: ЗНАЧЕНИЕ ПО УБЫВАНИЮ, ЗАТЕМ КЛЮЧ ПО ВОЗРАСТАНИЮ
words = {}

with open('input.txt', 'r') as f:
    while True:
        s = f.readline().strip().split()

        if not s:
            break

        for ws in s:
            if ws not in words:
                words[ws] = 0
            words[ws] += 1

for le in sorted(words.items(), key=lambda x: (-x[1], x[0])):
    print(le[0])