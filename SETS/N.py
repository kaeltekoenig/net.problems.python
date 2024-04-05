words = {}

with open('input.txt', 'r') as f:
    a = f.readline().split()
    for el in a:
        if el not in words:
            words[el] = 0
        words[el] += 1


maxcount = 0
maxword = ''

for k, v in words.items():
    if v > maxcount or (v == maxcount and k < maxword):
        maxcount = v
        maxword = k

print(maxword)