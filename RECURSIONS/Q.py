def hanoi(n, s=1, f=3):
    if n == 1:
        print(n, s, f)
    else:
        t = 6 - s - f
        hanoi(n - 1, s, t)
        print(n, s, f)
        hanoi(n - 1, t, f)

hanoi(int(input()))