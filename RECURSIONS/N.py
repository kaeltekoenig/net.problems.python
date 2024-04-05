def read():
    q = int(input())
    if q != 0:
        if q % 2 == 1:
            print(q)
            return
        return read()

read()