synonyms = {}

with open('input.txt', 'r') as f:
    while True:
        s = f.readline().strip()
        if s == '':
            break
        elif ' ' in s:
            k, v = s.split()
            synonyms[k] = v
        else:
            for k, v in synonyms.items():
                if k == s:
                    print(v)
                elif s == v:
                    print(k)

