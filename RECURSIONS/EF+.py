from time import time

def fibr(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibr(n-1) + fibr(n-2)
    
def fibw(n):
    fibs = [1, 1]
    i = 2
    while i < n + 1:
        fibs.append(fibs[i-1] + fibs[i-2])
        i += 1

    return fibs[n]
##################
starttime = time()
##################
for _ in range(1000):  
    fibw(20)
##################
endtime = time()
print(f'Программа выполнена. Время работы: {round(endtime - starttime, 5)} сек.')


##################
starttime = time()
##################
for _ in range(1000):  
    fibr(20)
##################
endtime = time()
print(f'Программа выполнена. Время работы: {round(endtime - starttime, 5)} сек.')