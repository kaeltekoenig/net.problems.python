def hstower(n, s, f):
    t = 6 - s - f
    if n == 1:
        print(n, s, t)
    else:
        if n % 2 == 1:
            hstower(n - 1, s, f)
            print(n, s, t)
        else:
            hstower(n - 1, s, f)
            print(n, s, f)
        

hstower(3, 1, 3)