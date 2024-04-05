def is_power2(n):
    if n <= 2:
        return n == 2
    else:
        return is_power2(n / 2)
    

print(is_power2(int(input())))