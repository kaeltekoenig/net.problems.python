def minx(a, b):
    return a if a < b else b

def factorialx(n):
    f = 1
    for i in range(2, n + 1):
        f *= i

    return f


def findcombcount(n, k):
    return factorialx(n) // (factorialx(k) * factorialx (n - k))


def islatinalpha(s):
    return 'A' <= s <= 'Z' or 'a' <= s <= 'z'


def toupper(sym):
    return chr(ord(sym) - 32) if 'a' <= sym <= 'z' else sym


