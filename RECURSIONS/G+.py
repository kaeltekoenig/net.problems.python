from time import time

def combination(n, k):
    if k == 1:
        return n
    elif k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return (n / k) * combination(n-1, k-1)
    

def combinationf(n, k):
    if k == 1 and k <= n:
        return n
    elif n == 1 and n < k:
        return 0
    elif k == 0:
        return 1
    else:
        return combinationf(n-1, k-1) + combinationf(n-1, k)


n = 15
k = 10
# 1
##################
starttime = time()
##################
for _ in range(1000):
    combination(n, k)
##################
endtime = time()
print(f'Программа выполнена. Время работы: {round(endtime - starttime, 5)} сек.')

# 2
##################
starttime = time()
##################
for _ in range(1000):
    combinationf(n, k)
##################
endtime = time()
print(f'Программа выполнена. Время работы: {round(endtime - starttime, 5)} сек.')
