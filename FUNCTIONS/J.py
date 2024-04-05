def is_prime(n):
    return 'NO' if any(n % x == 0 for x in range(2, int(n ** 0.5) + 1)) else 'YES'

print(is_prime(int(input())))
