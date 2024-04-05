def read():
    seq = []
    while True:
        n = int(input())
        if n == 0:
            break
        seq.append(n)

    return seq

print(read())