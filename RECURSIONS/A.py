def sum0n(n):
    if n == 1:
        return 1
    else:
        return n + sum0n(n - 1)
    
print(sum0n(int(input())))