dictionary = {}

with open('input.txt', 'r') as f:
    for _ in range(int(f.readline())):
        eng, latcol = f.readline().strip().split(' - ')
        for lword in latcol.split(', '):
            if lword not in dictionary:
                dictionary[lword] = []
            dictionary[lword].append(eng)

print(len(dictionary))
for k, v in sorted(dictionary.items()):
    # print(f'{k} - {', '.join(v)}')
    print(k, '-', ', '.join(v))
