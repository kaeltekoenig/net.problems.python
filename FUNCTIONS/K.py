# РАЗЛОЖЕНИЕ НА МНОЖИТЕЛИ
def mindivisor(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return x
    return n


def factor(n):
    divisors = []
    while n > 1:
        mindiv = mindivisor(n)
        n //= mindiv
        divisors.append(mindiv)

    return divisors


print(factor(int(input())))

