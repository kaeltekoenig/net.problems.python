def min_divisor(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return x
    return n
        
print(min_divisor(int(input())))