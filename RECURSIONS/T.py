def unjust(n, s, f):
    t = 6 - s - f
    if n == 1:
        print(n, s, f)
    else:
        unjust(n - 1, s, f)
        print(n, s, t)
        unjust(n - 1, f, s)
        print(n, t, f)
        unjust(n - 1, s, f)


unjust(int(input()), 1, 3)