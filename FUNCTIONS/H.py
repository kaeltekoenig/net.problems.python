def reversex(n):
    return int(str(n)[::-1])

def next_palindrome(n):
    rev = reversex(n)
    if rev != n:
        return next_palindrome(n + 1)
    return rev

print(next_palindrome(int(input())))