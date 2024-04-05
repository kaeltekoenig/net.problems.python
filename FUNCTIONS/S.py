def read_even():
    nseq = []
    seq = list(map(int, input().split()))
    for num in seq:
        if num % 2 == 0:
            nseq.append(num)

    return nseq


print(read_even())