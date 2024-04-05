d = {}
mistakes = 0

with open('input.txt', 'r') as f:
    for _ in range(int(f.readline())):
        word = f.readline().strip()
        if word.lower() not in d:
            d[word.lower()] = []
        d[word.lower()].append(word)

    hwork = f.readline().split()

    for hword in hwork:
        if hword.lower() in d:
            if hword not in d[hword.lower()]:
                mistakes += 1
        else:
            curvows = 0
            emphasises = 0
            
            for sym in hword:
                if sym == sym.upper():
                    emphasises += 1

            if emphasises != 1:
                mistakes += 1



print(mistakes)