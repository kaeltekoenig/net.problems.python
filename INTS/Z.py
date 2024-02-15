n = int(input())
m = int(input())

print(
    int(
    n / m == n // m + n % m or
    m / n == m // n + m % n
    )
)