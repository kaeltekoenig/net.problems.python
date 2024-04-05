# НЕУПОРЯДОЧЕННЫЕ СОЧЕТАНИЯ (КОМБИНАТОРИКА)
def combination(n, k):
    if k == 1 and k <= n:
        return n
    elif n == 1 and n < k:
        return 0
    elif k == 0:
        return 1
    else:
        return combination(n-1, k-1) + combination(n-1, k)
    
print(combination(int(input()), int(input())))