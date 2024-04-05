def read_greater(x):
    nseq = []
    seq = sorted(map(int, input().split()), reverse=True)
    for num in seq:
        if num > x:
            nseq.append(num)
        else:
            break

    return nseq

print(read_greater(2))