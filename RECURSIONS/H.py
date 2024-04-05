def power(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return power(a ** 2, n // 2)
        else:
            return a * power(a, n - 1)
    

print(power(float(input()), float(input())))