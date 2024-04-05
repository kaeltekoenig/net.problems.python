# НЕУПОРЯДОЧЕННЫЕ СОЧЕТАНИЯ (КОМБИНАТОРИКА) - 2
def combination(n, k):
    if k == 1:
        return n
    elif k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return (n / k) * combination(n-1, k-1)
    
print(int(combination(int(input()), int(input()))))