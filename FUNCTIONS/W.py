def read(k):
    retseq = []
    prntseq = []   
    seq = list(map(int, input().split()))
    for el in seq:
        retseq.append(el - k)
        prntseq.append(el + k)

    print(*prntseq)
    return retseq

read(7)