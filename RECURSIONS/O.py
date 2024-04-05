def read():
    q = int(input())
    if q % 2 != 1:
        return read()
    else:
        return q
    
print(read())