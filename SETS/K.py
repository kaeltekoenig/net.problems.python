with open('input.txt', 'r') as f:
    s = f.read().split()

words = {}
wordscnt = []

for word in s:
    if word not in words:
        words[word] = 0

    wordscnt.append(words[word])
    words[word] += 1


print(*wordscnt)

